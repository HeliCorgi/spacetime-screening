#!/usr/bin/env python3
"""Select PR checks conservatively; run unchanged research assertions.

Only the standard library is required for planning, doc checks and self-tests.
Research dependencies are installed by the workflow before the run command.
See docs/ci-policy.md for the selection contract and its limitations.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
from urllib.parse import unquote, urlsplit

RESEARCH_DIRS = {'src/symbolic', 'src/numerical'}
CONTROL_PREFIX = ('scripts/ci/', '.github/actions/')
PY_CONFIG = {'requirements.txt', 'pyproject.toml', 'setup.py', 'setup.cfg',
             'Pipfile', 'Pipfile.lock', 'uv.lock', 'poetry.lock', 'tox.ini'}
LEAN_CONFIG = {'lean-toolchain', 'lakefile.lean', 'lakefile.toml', 'lake-manifest.json'}
FULL_WORKFLOWS = {'.github/workflows/pr-checks.yml', '.github/workflows/symbolic-ci.yml'}
LEAN_WORKFLOW = '.github/workflows/chronology-six-gate.yml'


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(['git', '-C', str(root), *args], text=True,
                                   encoding='utf-8', errors='strict')


def tracked(root: Path, ref: str | None = None) -> list[str]:
    args = ('ls-tree', '-r', '--name-only', '-z', ref) if ref else ('ls-files', '-z')
    return [p for p in git(root, *args).split('\0') if p]


def entrypoint(p: str) -> bool:
    q = Path(p)
    return q.parent.as_posix() in RESEARCH_DIRS and q.suffix == '.py' and q.name != '__init__.py'


def documentation(p: str) -> bool:
    return Path(p).suffix.lower() in {'.md', '.rst', '.txt'} or Path(p).name in {
        'LICENSE', 'LICENSE-DOCS', 'NOTICE', 'CITATION.cff', '.gitignore', '.gitattributes'}


def lean_related(p: str) -> bool:
    return p.startswith('src/lean/') or p in LEAN_CONFIG or p == LEAN_WORKFLOW


def inspect_consumers(root: Path, refs: list[str | None], changed: set[str]) -> list[str]:
    """Use BOTH trees so removed imports cannot hide a dependency.

A local import or a literal reference to a changed script triggers the full
suite, not a guess about which consumers to omit. Dynamic loading / directory
execution is also conservative. This is not a complete Python dependency
prover: unanalysable/shared dependencies must use the full-suite override.
"""
    names = {Path(p).stem for p in changed}
    basenames = {Path(p).name for p in changed}
    reasons: set[str] = set()
    dynamic = {'__import__', 'exec', 'eval', 'import_module', 'run_module',
               'run_path', 'glob', 'rglob', 'iterdir', 'listdir', 'walk',
               'system', 'Popen'}
    for ref in refs:
        for p in tracked(root, ref):
            if not p.endswith('.py') or not p.startswith('src/'):
                continue
            try:
                text = git(root, 'show', f'{ref}:{p}') if ref else (root / p).read_text(encoding='utf-8-sig')
                tree = ast.parse(text, filename=p)
            except (SyntaxError, UnicodeError, OSError, subprocess.CalledProcessError):
                reasons.add(f'unanalysable Python source: {p}')
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    func = node.func
                    name = func.id if isinstance(func, ast.Name) else getattr(func, 'attr', '')
                    # Dynamic discovery in any source may consume an added file.
                    if name in dynamic:
                        reasons.add(f'dynamic execution/discovery in {p}')
                if p in changed:
                    continue
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    parts = set()
                    for alias in node.names:
                        parts.update(alias.name.split('.'))
                    parts.update((getattr(node, 'module', '') or '').split('.'))
                    if '*' in parts or names & parts:
                        reasons.add(f'possible shared-code consumer: {p}')
                if isinstance(node, ast.Constant) and isinstance(node.value, str):
                    if any(n in node.value for n in basenames):
                        reasons.add(f'literal script reference in {p}')
    return sorted(reasons)


def make_plan(root: Path, base: str | None = None, head: str = 'HEAD',
              full: bool = False) -> dict:
    current = tracked(root)
    all_scripts = sorted(p for p in current if entrypoint(p))
    if not all_scripts:
        raise ValueError('No research entrypoints found; refusing a vacuous full-suite PASS')
    changed: list[str] = []
    removed: list[str] = []
    reasons: list[str] = []
    ancestor = None
    fallback = False
    if full:
        reasons.append('explicit full-reproducibility run')
    else:
        try:
            if not base:
                raise ValueError('--base is required for PR selection')
            ancestor = git(root, 'merge-base', base, head).strip()
            changed = [p for p in git(root, 'diff', '--no-renames', '--name-only', '-z',
                                      ancestor, head, '--').split('\0') if p]
            removed = [p for p in changed if p not in current]
        except (ValueError, subprocess.CalledProcessError):
            fallback = True
            reasons.append('diff/base unavailable: fail-safe full suite plus Lean')
    lean = full or fallback or any(lean_related(p) for p in changed)
    for p in changed:
        if lean_related(p):
            continue
        if (p in PY_CONFIG or Path(p).name.startswith('requirements')
                or p.startswith(CONTROL_PREFIX) or p in FULL_WORKFLOWS):
            reasons.append(f'CI/shared dependency changed: {p}')
            fallback = True
        elif p.startswith(('data/', 'notes/data/')):
            reasons.append(f'input/reference data changed: {p}')
            fallback = True
        elif entrypoint(p):
            pass
        elif not documentation(p):
            reasons.append(f'unknown/shared impact: {p}')
            fallback = True
    source_changes = {p for p in changed if entrypoint(p)}
    if source_changes and not (full or fallback):
        extra = inspect_consumers(root, [None, ancestor], source_changes)
        if extra:
            reasons.extend(extra)
            fallback = True
    selected = all_scripts if full or fallback else sorted(source_changes & set(all_scripts))
    if not reasons:
        reasons.append('changed independent entrypoints' if selected else 'no affected Python entrypoints')
    # Removal/rename may break links in otherwise unchanged documents.
    docs = sorted(p for p in current if p.endswith('.md') and (removed or p in changed))
    if full:
        docs = []  # Full run reproduces calculations, not historical-link linting.
    mode = 'full' if full else ('full-fallback' if fallback else ('targeted' if selected else 'docs-or-lean-only'))
    shards = 4 if len(selected) >= 16 else 1
    versions = ['3.11', '3.12'] if full else ['3.12']
    matrix = {'include': [{'python': v, 'shard': i, 'shards': shards}
                          for v in versions for i in range(shards)]}
    return {'mode': mode, 'base': base, 'merge_base': ancestor, 'head': head,
            'checkout_sha': git(root, 'rev-parse', 'HEAD').strip(),
            'changed': changed, 'removed': removed, 'selected': selected,
            'all_script_count': len(all_scripts), 'docs': docs,
            'lean': lean, 'python_required': bool(selected),
            'reasons': sorted(set(reasons)), 'matrix': matrix}


def check_docs(root: Path, plan: dict) -> None:
    """Check local Markdown file targets, not external URLs or heading anchors.

When a file is deleted, unchanged docs are checked only for references to
that removed path, so historical unrelated broken links do not block a PR.
"""
    errors = []
    removed = plan['removed']
    for p in plan['docs']:
        text = (root / p).read_text(encoding='utf-8')
        text = re.sub(r'^\s*(`{3,}|~{3,}).*?^\s*\1\s*$', '', text, flags=re.M | re.S)
        targets = re.findall(r'\]\(\s*(<[^>]+>|[^\s)]+)', text)
        targets += re.findall(r'^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)', text, flags=re.M)
        for raw in targets:
            target = raw.strip('<>')
            if target.startswith(('#', '//')) or urlsplit(target).scheme or '`' in target:
                continue
            path = unquote(urlsplit(target).path)
            if not path:
                continue
            dest = (root / path.lstrip('/')) if path.startswith('/') else (root / p).parent / path
            dest = dest.resolve()
            try:
                rel = dest.relative_to(root.resolve()).as_posix()
            except ValueError:
                errors.append(f'{p}: target escapes repository: {raw}')
                continue
            affected_deletion = any(rel == q or rel.startswith(q + '/') for q in removed)
            if p not in plan['changed'] and not affected_deletion:
                continue
            if not dest.exists():
                errors.append(f'{p}: missing local link target: {raw}')
    if errors:
        raise ValueError('\n'.join(errors))
    print(f'PASS local file links: {len(plan["docs"])} Markdown file(s); external URLs/anchors not tested')


def run_selected(root: Path, plan: dict, shard: int, shards: int, timeout: int) -> int:
    if shards < 1 or not 0 <= shard < shards:
        raise ValueError('Invalid shard index/count')
    selected = plan['selected'][shard::shards]
    status = 0
    lines = ['### Research check timings', '', '| Script | Seconds | Result |', '|---|---:|---|']
    for p in selected:
        if not entrypoint(p) or not (root / p).is_file():
            raise ValueError(f'Invalid or missing entrypoint: {p}')
        print(f'::group::{p}', flush=True)
        started = time.monotonic()
        # Compile without creating tracked output; assertions run normally, never with -O.
        compile((root / p).read_bytes(), p, 'exec')
        try:
            result = subprocess.run([sys.executable, '-u', p], cwd=root, timeout=timeout,
                                    check=False)
            code = result.returncode
        except subprocess.TimeoutExpired:
            code = 124
        elapsed = time.monotonic() - started
        if code:
            status = 1
            print(f'::error file={p}::Research check failed (exit {code})', flush=True)
        lines.append(f'| `{p}` | {elapsed:.2f} | {"PASS" if not code else "FAIL"} |')
        print(f'::endgroup::\n{p}: {elapsed:.2f}s, exit={code}', flush=True)
    if not selected:
        print('No entrypoints on this shard (no research PASS inferred).')
    if os.getenv('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')
    return status


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('command', choices=['plan', 'docs', 'run'])
    ap.add_argument('--root', type=Path, default=Path.cwd())
    ap.add_argument('--base')
    ap.add_argument('--head', default='HEAD')
    ap.add_argument('--full', action='store_true')
    ap.add_argument('--plan', type=Path, default=Path('ci-plan.json'))
    ap.add_argument('--shard', type=int, default=0)
    ap.add_argument('--shards', type=int, default=1)
    ap.add_argument('--timeout', type=int, default=900)
    args = ap.parse_args()
    root = args.root.resolve()
    if args.command == 'plan':
        plan = make_plan(root, args.base, args.head, args.full)
        args.plan.parent.mkdir(parents=True, exist_ok=True)
        args.plan.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(plan, ensure_ascii=False, indent=2))
        if os.getenv('GITHUB_OUTPUT'):
            with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as out:
                for k in ('python_required', 'lean', 'matrix'):
                    out.write(f'{k}={json.dumps(plan[k], separators=(",", ":"))}\n')
        if os.getenv('GITHUB_STEP_SUMMARY'):
            with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as out:
                out.write('### Check selection\n\n```json\n' + json.dumps(plan, ensure_ascii=False, indent=2) + '\n```\n')
        return 0
    plan = json.loads(args.plan.read_text(encoding='utf-8'))
    if args.command == 'docs':
        check_docs(root, plan)
        return 0
    return run_selected(root, plan, args.shard, args.shards, args.timeout)


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f'CI error: {exc}', file=sys.stderr)
        raise SystemExit(1)

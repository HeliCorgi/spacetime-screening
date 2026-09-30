#!/usr/bin/env python3
"""Negative selector controls for R4's new dependencies and stored evidence.

Runs against the repository's actual CI selector. It never imports numerical
research code. Reference JSON must not be treated as a documentation-only PR.
"""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile


def main():
    root = Path(__file__).resolve().parents[2]
    spec = importlib.util.spec_from_file_location('r4_ci_selector', root/'scripts/ci/checks.py')
    checks = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checks)
    rows = []
    for changed, content in (
        ('requirements.txt', 'sympy>=1.12,<2\nnumpy>=1.26,<3\nscipy>=1.14,<2\n'),
        ('research/relational_qg_R4/results.json', '{"implemented_checks_passed": false}\n'),
    ):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory)
            def git(*args):
                return subprocess.check_output(['git','-C',str(p),*args],text=True).strip()
            git('init','-q')
            git('config','user.name','CI fixture')
            git('config','user.email','ci-test@example.invalid')
            for name in ('src/symbolic/a.py','src/numerical/b.py'):
                dst=p/name
                dst.parent.mkdir(parents=True,exist_ok=True)
                dst.write_text('assert True\n')
            git('add','.')
            git('commit','-qm','base')
            base=git('rev-parse','HEAD')
            dst=p/changed
            dst.parent.mkdir(parents=True,exist_ok=True)
            dst.write_text(content)
            git('add','.')
            git('commit','-qm','dependency or evidence change')
            plan=checks.make_plan(p,base)
            if plan['mode']!='full-fallback' or len(plan['selected'])!=2:
                raise AssertionError('dependency/evidence change was incorrectly skipped')
            rows.append(dict(changed=changed,mode=plan['mode'],selected=plan['selected']))
    print(json.dumps(dict(passed=True,negative_selection_controls=rows)))


if __name__=='__main__':
    main()

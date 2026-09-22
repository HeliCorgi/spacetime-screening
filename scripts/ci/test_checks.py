#!/usr/bin/env python3
"""Negative controls for CI selection; no research dependencies required."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('ci_checks', Path(__file__).with_name('checks.py'))
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class SelectionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git('init', '-q')
        self.git('config', 'user.email', 'ci-test@example.invalid')
        self.git('config', 'user.name', 'CI tests')
        self.write('src/symbolic/a.py', 'assert 1 + 1 == 2\n')
        self.write('src/symbolic/b.py', 'assert 2 + 2 == 4\n')
        self.write('src/numerical/c.py', 'assert True\n')
        self.write('README.md', '[note](notes/n.md)\n')
        self.write('notes/n.md', '# Note\n')
        self.base = self.commit()

    def git(self, *args):
        return checks.git(self.root, *args).strip()

    def write(self, p, content):
        dst = self.root / p
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(content, encoding='utf-8')

    def commit(self):
        self.git('add', '.')
        self.git('commit', '-qm', 'fixture')
        return self.git('rev-parse', 'HEAD')

    def plan(self):
        return checks.make_plan(self.root, self.base)

    def test_docs_only(self):
        self.write('README.md', '[note](notes/n.md)\nnew text\n')
        self.commit()
        p = self.plan()
        self.assertEqual(p['selected'], [])
        self.assertFalse(p['lean'])
        checks.check_docs(self.root, p)

    def test_new_independent_script(self):
        self.write('src/symbolic/new.py', 'import json\nassert 3 == 3\n')
        self.commit()
        self.assertEqual(self.plan()['selected'], ['src/symbolic/new.py'])

    def test_pr_cumulative_not_last_commit(self):
        self.write('src/symbolic/a.py', 'assert 1 == 1\n')
        self.commit()
        self.write('README.md', '# docs-only final commit\n')
        self.commit()
        self.assertEqual(self.plan()['selected'], ['src/symbolic/a.py'])

    def test_modified_script(self):
        self.write('src/symbolic/a.py', 'assert 5 == 5\n')
        self.commit()
        self.assertEqual(self.plan()['matrix']['include'], [{'python': '3.12', 'shard': 0, 'shards': 1}])

    def test_shared_import_is_full(self):
        self.write('src/symbolic/b.py', 'from a import thing\n')
        self.base = self.commit()
        self.write('src/symbolic/a.py', 'thing = 2\n')
        self.commit()
        self.assertEqual(self.plan()['mode'], 'full-fallback')
        self.assertEqual(len(self.plan()['selected']), 3)

    def test_deleted_import_found_in_old_tree(self):
        self.write('src/symbolic/b.py', 'import a\n')
        self.base = self.commit()
        (self.root / 'src/symbolic/a.py').unlink()
        self.write('src/symbolic/b.py', 'assert True\n')
        self.commit()
        # Both changed files remove the consumer; nothing still imports a.
        # b is still executed and the deleted a is never executed.
        self.assertEqual(self.plan()['selected'], ['src/symbolic/b.py'])

    def test_deleted_dependency_with_consumer_is_full(self):
        self.write('src/symbolic/b.py', 'import a\n')
        self.base = self.commit()
        (self.root / 'src/symbolic/a.py').unlink()
        self.commit()
        self.assertEqual(self.plan()['mode'], 'full-fallback')

    def test_rename_is_delete_plus_add(self):
        (self.root / 'src/symbolic/a.py').rename(self.root / 'src/symbolic/new.py')
        self.commit()
        self.assertEqual(self.plan()['selected'], ['src/symbolic/new.py'])
        self.assertIn('src/symbolic/a.py', self.plan()['removed'])

    def test_inputs_dependencies_unknown_and_infra_are_full(self):
        for path in ('data/input.csv', 'notes/data/reference.json', 'requirements.txt',
                     'src/lib/helper.py', 'strange.bin', 'scripts/ci/control.py'):
            with self.subTest(path=path):
                self.write(path, '{}\n')
                self.commit()
                self.assertEqual(self.plan()['mode'], 'full-fallback')

    def test_dynamic_discovery_is_full(self):
        self.write('src/numerical/c.py', 'from pathlib import Path\nxs = Path(".").glob("*.py")\n')
        self.base = self.commit()
        self.write('src/symbolic/a.py', 'assert 9 == 9\n')
        self.commit()
        self.assertEqual(self.plan()['mode'], 'full-fallback')

    def test_syntax_error_cannot_disappear(self):
        self.write('src/symbolic/a.py', 'this is not valid: !\n')
        self.commit()
        self.assertEqual(self.plan()['mode'], 'full-fallback')
        with self.assertRaises(SyntaxError):
            checks.run_selected(self.root, self.plan(), 0, 1, 5)

    def test_lean_only(self):
        self.write('src/lean/Test.lean', '#check Nat\n')
        self.commit()
        p = self.plan()
        self.assertTrue(p['lean'])
        self.assertEqual(p['selected'], [])

    def test_python_only_does_not_run_lean(self):
        self.write('src/symbolic/a.py', 'assert 7 == 7\n')
        self.commit()
        self.assertFalse(self.plan()['lean'])

    def test_missing_base_fails_safe(self):
        p = checks.make_plan(self.root, None)
        self.assertEqual(p['mode'], 'full-fallback')
        self.assertTrue(p['lean'])
        self.assertEqual(len(p['selected']), 3)

    def test_full_matrix_and_no_duplicates(self):
        p = checks.make_plan(self.root, full=True)
        self.assertEqual({v['python'] for v in p['matrix']['include']}, {'3.11', '3.12'})
        self.assertEqual(len(p['selected']), 3)
        for i in range(18):
            self.write(f'src/symbolic/test{i}.py', 'assert True\n')
        self.commit()
        p = checks.make_plan(self.root, full=True)
        self.assertEqual(len(p['matrix']['include']), 8)
        flat = [f for i in range(4) for f in p['selected'][i::4]]
        self.assertCountEqual(flat, p['selected'])
        self.assertEqual(len(flat), len(set(flat)))

    def test_deleted_link_detected(self):
        (self.root / 'notes/n.md').unlink()
        self.commit()
        with self.assertRaisesRegex(ValueError, 'missing local link'):
            checks.check_docs(self.root, self.plan())

    def test_external_anchor_and_code_links_are_not_fetched(self):
        self.write('README.md', '[a](#anchor) [b](https://example.invalid)\n```md\n[x](absent)\n```\n')
        self.commit()
        checks.check_docs(self.root, self.plan())

    def test_failure_not_relabelled_pass(self):
        self.write('src/symbolic/a.py', 'raise AssertionError("expected test failure")\n')
        self.commit()
        self.assertEqual(checks.run_selected(self.root, self.plan(), 0, 1, 5), 1)

    def test_timeout_is_failure(self):
        self.write('src/symbolic/a.py', 'import time\ntime.sleep(10)\n')
        self.commit()
        self.assertEqual(checks.run_selected(self.root, self.plan(), 0, 1, 1), 1)

    def test_no_entrypoints_not_success(self):
        for p in self.root.glob('src/*/*.py'):
            p.unlink()
        self.commit()
        with self.assertRaises(ValueError):
            checks.make_plan(self.root, full=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)

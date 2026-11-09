"""Offline tests for the trusted translation patch boundary."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import translation_guard as guard


class TranslationGuardTests(unittest.TestCase):
    def test_scope(self):
        for path in ('docs/de/docs/new.md', 'docs/ja/mkdocs.yml', '.translation-cache.json'):
            self.assertTrue(guard.allowed_path(path), path)
        for path in ('docs/en/docs/new.md', 'scripts/anchors.py', '../docs/de/a.md',
                     '/docs/de/a.md', 'docs/de/../../scripts/a.py',
                     'docs/de/docs/regulatory_statement.md', 'docs/uk/mkdocs.yml',
                     'docs/de/site/index.html', 'docs/de/a\nb.md'):
            self.assertFalse(guard.allowed_path(path), path)

    def test_protected_sections(self):
        text = '# Page {#page}\n\n## Safety {#safety-information}\nApproved.\n\n## Setup {#setup}\nNormal.\n'
        self.assertEqual(guard.protected_sections(text), ['## Safety {#safety-information}\nApproved.\n\n'])
        self.assertEqual(guard.protected_sections('## Setup {#setup}\nText.\n'), [])

    def test_protected_section_may_not_move(self):
        legal = '## Safety {#safety-information}\nApproved.\n\n'
        setup = '## Setup {#setup}\nInstructions.\n\n'
        before = '# Page {#page}\n\n' + legal + setup
        after = '# Page {#page}\n\n' + setup + legal
        self.assertEqual(guard.protected_sections(before), guard.protected_sections(after))
        with self.assertRaisesRegex(ValueError, 'placement'):
            guard.check_content('docs/de/docs/page.md', before, after)

    def test_regulatory_nav_and_links_are_rejected(self):
        for path, content in (
            ('docs/de/mkdocs.yml', 'nav:\n  - Legal: user_guide/gl-rm1/regulatory_statement.md\n'),
            ('docs/de/docs/index.md', '[Legal](https://docs.example/en/regulatory_statement/)'),
            ('docs/fr/mkdocs.yml', 'redirect_maps:\n  fcc_ic_compliance_statements: legal\n'),
        ):
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, 'regulatory reference'):
                guard.check_content(path, '', content)
            guard.check_content(path, content, content)  # No unrelated pre-existing cleanup.

    def test_report(self):
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / 'report.json'
            for status, passed, accepted in (('completed', True, True), ('blocked', True, False),
                                              ('completed', False, False), ('no_changes', True, False)):
                report.write_text(json.dumps({'status': status, 'validation': {'passed': passed}}))
                if accepted:
                    guard.validate_report(report)
                else:
                    with self.assertRaises(ValueError):
                        guard.validate_report(report)

    def test_staged_patch_and_legal_protection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.DEVNULL)
            git('init')
            git('config', 'user.email', 'test@example.com')
            git('config', 'user.name', 'Test')
            page = root / 'docs/de/docs/test.md'
            page.parent.mkdir(parents=True)
            original = '# Page {#page}\nText.\n\n## Safety {#safety-information}\nApproved.\n'
            page.write_text(original, encoding='utf-8')
            git('add', '.')
            git('commit', '-m', 'initial')
            previous = Path.cwd()
            try:
                os.chdir(root)
                page.write_text(original.replace('Text.', 'Updated.'), encoding='utf-8')
                git('add', '.')
                self.assertEqual(guard.check_patch(), ['docs/de/docs/test.md'])
                page.write_text(original.replace('Approved.', 'Altered.'), encoding='utf-8')
                git('add', '.')
                with self.assertRaisesRegex(ValueError, 'approved legal'):
                    guard.check_patch()
                git('reset', '--hard', 'HEAD')
                script = root / 'scripts/evil.py'
                script.parent.mkdir()
                script.write_text('print(1)')
                git('add', '.')
                with self.assertRaisesRegex(ValueError, 'forbidden path'):
                    guard.check_patch()
            finally:
                os.chdir(previous)

    def test_symlink_mode_is_rejected(self):
        responses = [b'docs/de/docs/a.md\0', b'120000 abc 0\tdocs/de/docs/a.md\n']
        with patch.object(guard, 'git', side_effect=responses):
            with self.assertRaisesRegex(ValueError, 'non-regular'):
                guard.check_patch()


if __name__ == '__main__':
    unittest.main()

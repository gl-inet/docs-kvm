"""Static regression checks for scheduled translation workflow wiring."""
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]


class TranslationWorkflowTests(unittest.TestCase):
    def test_time_languages_and_revision(self):
        workflow = yaml.load(
            (ROOT / '.github/workflows/translation.yml').read_text(encoding='utf-8'),
            Loader=yaml.BaseLoader,
        )
        self.assertEqual(workflow['on']['schedule'][0]['cron'], '43 23 * * 0-4')
        self.assertIn('workflow_dispatch', workflow['on'])
        self.assertEqual(workflow['permissions'], {'contents': 'read'})
        for job in ('translate', 'validate', 'publish'):
            checkout = workflow['jobs'][job]['steps'][0]
            self.assertEqual(checkout['with']['ref'], '${{ needs.prepare.outputs.source_sha }}')
        commands = '\n'.join(s.get('run', '') for s in workflow['jobs']['validate']['steps'])
        self.assertIn('translation_guard.py', commands)
        self.assertIn('list --fail-on-delta', commands)
        self.assertIn('for lang in de es fr it ja nl pl sv;', commands)
        self.assertNotIn(' sv uk', commands)
        commands = '\n'.join(s.get('run', '') for s in workflow['jobs']['publish']['steps'])
        self.assertIn('Assisted-by: Cindy (https://cindy.app)', commands)
        self.assertIn('core.hooksPath=/dev/null', commands)
        self.assertNotIn('gh pr merge', commands)

    def test_prompt_uses_per_language_cache(self):
        prompt = (ROOT / '.github/codex/prompts/translation.md').read_text(encoding='utf-8')
        self.assertIn('objects with path and langs', prompt)
        self.assertIn('translation_delta.py diff', prompt)
        self.assertIn('translation_delta.py mark', prompt)
        self.assertIn('translation_delta.py prune', prompt)
        self.assertNotIn('translation_delta.py update', prompt)
        self.assertNotIn('SINGLE source_hash', prompt)
        self.assertNotIn('docs4.x', prompt)
        self.assertNotIn('router-specific', prompt)
        skill = (ROOT / '.agents/skills/glinet-docs-translation/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('source_blob', skill)
        self.assertIn('target_hash', skill)
        self.assertNotIn('translation_delta.py update', skill)


if __name__ == '__main__':
    unittest.main()

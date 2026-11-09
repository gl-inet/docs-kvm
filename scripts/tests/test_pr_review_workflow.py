"""Static checks for trusted PR-review workflow wiring."""
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]


class ReviewWorkflowTests(unittest.TestCase):
    def test_trusted_executables_and_policy(self):
        workflow = yaml.load(
            (ROOT / '.github/workflows/pr-review.yml').read_text(encoding='utf-8'),
            Loader=yaml.BaseLoader,
        )
        self.assertEqual(workflow['permissions'], {'contents': 'read'})
        self.assertEqual(workflow['on']['pull_request']['branches'], ['master'])
        self.assertEqual(workflow['on']['pull_request']['paths'], ['docs/**'])
        review = workflow['jobs']['review']
        self.assertIn('!github.event.pull_request.draft', review['if'])
        self.assertIn('head.repo.full_name == github.repository', review['if'])
        for name in ('review', 'publish'):
            steps = workflow['jobs'][name]['steps']
            self.assertEqual(steps[0]['with']['ref'], '${{ github.event.pull_request.base.sha }}')
            for step in steps:
                command = step.get('run', '')
                self.assertNotIn('pip install', command)
                self.assertNotIn('pr-data/scripts', command)
                if 'codex_review.py' in command:
                    self.assertIn('python3 -I trusted/scripts/codex_review.py', command)
        action = next(s for s in review['steps'] if s.get('uses', '').startswith('openai/codex-action@'))
        self.assertEqual(action['with']['permission-profile'], ':read-only')
        self.assertEqual(action['with']['working-directory'], '${{ github.workspace }}/trusted')
        self.assertNotIn('permissions', review)
        self.assertEqual(workflow['jobs']['publish']['permissions']['pull-requests'], 'write')


if __name__ == '__main__':
    unittest.main()

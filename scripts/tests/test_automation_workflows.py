"""Regression checks for shared Codex client and streaming preflight wiring."""
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]


class CodexWorkflowTests(unittest.TestCase):
    def test_codex_client_and_streaming_preflight(self):
        for name, job, command in (
            ('translation.yml', 'translate', 'python -I scripts/codex_preflight.py'),
            ('pr-review.yml', 'review', 'python3 -I trusted/scripts/codex_preflight.py'),
        ):
            with self.subTest(workflow=name):
                workflow = yaml.load(
                    (ROOT / '.github/workflows' / name).read_text(encoding='utf-8'),
                    Loader=yaml.BaseLoader,
                )
                steps = workflow['jobs'][job]['steps']
                action = next(s for s in steps if s.get('uses', '').startswith('openai/codex-action@'))
                self.assertEqual(action['with']['codex-version'], '0.166.0')
                self.assertEqual(action['with']['model'], "${{ vars.CODEX_MODEL || 'gpt-6.1-sol' }}")
                preflight = next(s for s in steps if s.get('run') == command)
                self.assertLess(steps.index(preflight), steps.index(action))
                self.assertEqual(preflight['env']['CODEX_MODEL'], action['with']['model'])
                self.assertEqual(preflight['env']['CODEX_RESPONSES_API_ENDPOINT'], action['with']['responses-api-endpoint'])
                self.assertNotIn('continue-on-error', preflight)
                self.assertNotIn('continue-on-error', action)


if __name__ == '__main__':
    unittest.main()

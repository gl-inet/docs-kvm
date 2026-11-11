"""Reporting wiring checks; no network or AI calls required."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]


class StatsWorkflowTests(unittest.TestCase):
    def test_review_report_is_read_only_and_uses_trusted_base(self):
        source = (ROOT / '.github/workflows/pr-review.yml').read_text()
        report = source.split('\n  report:\n', 1)[1]
        for expected in ["needs: [review, publish]", "if: always() && needs.review.result != 'skipped'", 'continue-on-error: true', 'ref: ${{ github.event.pull_request.base.sha }}', 'persist-credentials: false', 'contents: read', 'actions: read', 'ai-agent-stats-review-attempt-${{ github.run_attempt }}', 'stats/review-run.json', 'retention-days: 30', 'codex-review-added-lines', 'path: review/.codex-run']:
            self.assertIn(expected, report)
        self.assertNotIn('secrets.', report)
        self.assertNotIn('write', report)
        self.assertIn('path: trusted/.codex-run/added-lines.json', source)

    def test_translation_always_reports_from_workflow_revision(self):
        source = (ROOT / '.github/workflows/translation.yml').read_text()
        report = source.split('\n  report:\n', 1)[1]
        for expected in ['needs: [prepare, translate, validate, publish]', 'if: always()', 'continue-on-error: true', 'ref: ${{ github.sha }}', 'persist-credentials: false', 'contents: read', 'ai-agent-stats-translation-attempt-${{ github.run_attempt }}', 'stats/translation-run.json', 'retention-days: 30']:
            self.assertIn(expected, report)
        self.assertNotIn('secrets.', report)
        self.assertNotIn('write', report)


if __name__ == '__main__':
    unittest.main()

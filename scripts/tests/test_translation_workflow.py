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
        self.assertIn('`regulatory_statement.md` pages and redirects from the legacy', prompt)
        self.assertIn('`fcc_ic_compliance_statements.md` paths exist only in the English docs.', prompt)
        self.assertIn('legacy paths are redirects, not current Markdown files', prompt)
        skill = (ROOT / '.agents/skills/glinet-docs-translation/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('source_blob', skill)
        self.assertIn('target_hash', skill)
        self.assertNotIn('translation_delta.py update', skill)

    def test_heading_ids_follow_titles_without_separate_approval(self):
        guidance = ' '.join((ROOT / 'AGENTS.md').read_text(encoding='utf-8').split())
        self.assertIn('Heading IDs follow the current English heading text.', guidance)
        self.assertIn('needs no separate migration approval', guidance)
        self.assertIn('all in-repository anchor links and redirects', guidance)
        self.assertIn('Do not derive shared IDs from localized titles', guidance)
        self.assertNotIn('Do not change an existing ID when heading wording changes', guidance)
        self.assertFalse((ROOT / '.github/codex/approved-heading-migrations.json').exists())
        review = ' '.join((ROOT / '.github/codex/prompts/pr-review.md').read_text(encoding='utf-8').split())
        self.assertIn('Do not flag a title-driven ID change solely', review)
        self.assertNotIn('changed stable IDs', review)

    def test_prompt_syncs_title_ids_and_keeps_validation(self):
        prompt = ' '.join((ROOT / '.github/codex/prompts/translation.md').read_text(encoding='utf-8').split())
        for rule in (
            'The cache is a translation baseline, not a source-correctness authority.',
            'no separate approval or migration list',
            'Dimension -> Appearance may change dimension -> appearance',
            'never derive shared IDs from localized titles',
            'including files outside the initial cache delta',
            'Never use a blanket replacement',
            'Do not preserve old IDs or add aliases solely for external bookmarks',
            'Protected localized legal sections keep their wording and IDs.',
            'report that specific source issue rather than editing English',
            'Unresolved broken links prevent completion.',
            'An already-aligned localized ID does not mean its pending prose is synchronized.',
        ):
            self.assertIn(rule, prompt)
        self.assertNotIn('approved-heading-migrations.json', prompt)
        self.assertIn('Initial validation failures', prompt)
        self.assertIn('not reasons to stop before editing', prompt)
        self.assertIn('then rerun validation', prompt)
        self.assertIn('it still prevents completed status if final checks fail', prompt)
        self.assertIn('Do not edit English sources, scripts, workflows, skills, requirements,', prompt)
        self.assertIn('ALL checks/builds pass', prompt)
        self.assertIn('never bypass validation or edit the cache manually', prompt)
        skill = ' '.join((ROOT / '.agents/skills/glinet-docs-translation/SKILL.md').read_text(encoding='utf-8').split())
        self.assertIn('needs no separate approval or migration list', skill)
        self.assertIn('Protected localized-only legal sections retain their wording, placement and IDs.', skill)
        self.assertNotIn('approved-heading-migrations.json', skill)
        # Existing workflow gates and edit scope remain independent of model policy.
        workflow = yaml.load(
            (ROOT / '.github/workflows/translation.yml').read_text(encoding='utf-8'),
            Loader=yaml.BaseLoader,
        )
        commands = '\n'.join(s.get('run', '') for s in workflow['jobs']['validate']['steps'])
        for command in ('python scripts/i18n_check.py', 'python scripts/anchors.py check',
                        'list --fail-on-delta', '--strict'):
            self.assertIn(command, commands)


if __name__ == '__main__':
    unittest.main()

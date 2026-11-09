# Scheduled documentation translation {#scheduled-documentation-translation}

`.github/workflows/translation.yml` runs incremental Codex translation in
GitHub Actions, **Monday–Friday at 07:43 Asia/Shanghai**, with manual dispatch.
Its UTC cron is `43 23 * * 0-4` (Sunday–Thursday at 23:43 UTC). GitHub schedules
can be delayed. This change does not add PR review or alter deployment.

## Pipeline and cache {#pipeline-and-cache}

Preparation checks the per-language cache delta; no model call is made when
there is no delta. A source revision is pinned across all jobs. Codex edits
localized files and the cache with a read-only repository token, not a
publishing token. A separate clean job applies the patch and checks scope,
approved legal wording/placement, i18n structure, anchors, zero cache delta and
strict MkDocs builds for all eight languages: `de`, `es`, `fr`, `it`, `ja`,
`nl`, `pl`, `sv`. The `regulatory_statement.md` pages and redirects from legacy
`fcc_ic_compliance_statements.md` paths remain in English docs only. The legacy
paths are redirects, not current Markdown files; their pages, navigation,
redirects and index links are not copied into localized docs.

After validation, publishing rechecks scope and legal wording, refuses an
outdated source revision and creates a unique branch and PR. It **never merges**
that PR. English source issues appear in the PR report, or in a GitHub issue
when no PR is created. Reports and patches remain workflow artifacts.
Partial/blocked work is not published; existing validation backlog must be
resolved rather than bypassed with allowlists or cache updates.

The translation skill describes per-language `mark`, `diff` and `prune` usage.
Only the coordinating agent writes the cache. Unknown snapshots require full
page comparison; a language's sync does not advance other languages. The old
bulk `update` command must not be used.

## GitHub setup {#github-setup}

1. Create or reuse the `OpenAI` environment in `gl-inet/docs-kvm`.
2. Enter `OPENAI_API_KEY` and `CODEX_RESPONSES_API_ENDPOINT` as environment
   secrets directly in GitHub. Use a full Responses API endpoint, including
   `/v1/responses` when required by the provider.
3. Allow the environment on `master`. Required environment reviewers add
   manual approval before each protected run.
4. Under **Settings → Actions → General**, allow the required actions and
   enable **Allow GitHub Actions to create and approve pull requests**.
   Each job declares its own permissions; no PAT or new deployment key is needed.

Use a narrowly scoped, budget-limited API key and no unrelated secrets. The
model's workspace permission profile is not a network-exfiltration guarantee.
No secrets or statistics-service configuration are stored in this repository.

## Verification and first run {#verification-and-first-run}

```powershell
python -m unittest discover -s scripts/tests -p test_translation_guard.py -v
python -m unittest discover -s scripts/tests -p test_translation_workflow.py -v
python scripts/translation_delta.py list --json
python scripts/anchors.py check
python scripts/i18n_check.py
```

The schedule becomes active when merged into the default branch (`master`).
To stage configuration without activating the schedule, temporarily retain
only `workflow_dispatch`. After configuring secrets and merging, select
**Actions → Incremental documentation translation → Run workflow** on `master`.
Inspect reports, all checks/builds, legal wording and the resulting cache diff.
Do not weaken validation to publish a partial sync.

PRs created with `GITHUB_TOKEN` do not normally trigger another `pull_request`
workflow. A separately added Codex PR review will therefore not automatically
review generated translation PRs. This pipeline already validates changes
before creating the PR; no PAT, GitHub App or auto-merge is introduced.

## Operate and pause {#operate-and-pause}

Monitor API budget and Actions logs after the first scheduled run. Disable
**Incremental documentation translation** in Actions to pause it, not deployment.
Review or close older translation PRs before merging a newer one: an unmerged
PR does not advance `master`'s cache, so later runs can propose the same changes.
AI-assisted translation commits and PRs include
`Assisted-by: Cindy (https://cindy.app)`.

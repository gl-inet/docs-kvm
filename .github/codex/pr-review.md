# Codex PR review {#codex-pr-review}

`.github/workflows/pr-review.yml` runs report-only Codex reviews in GitHub
Actions. It does not add scheduled translation or change deployment.

## Trigger and trust boundaries {#trigger-and-trust-boundaries}

The workflow reviews non-draft, same-repository PRs targeting `master` that
change `docs/**`. It runs on opened, synchronize, reopened and ready_for_review;
a new push cancels the older review. Fork PRs are skipped.

Policy, prompt, schema and executable helpers come from the trusted base SHA.
The PR head is a separate data-only checkout: no PR-controlled dependency
installation or script execution occurs with review API secrets or the
publisher's write token. Codex uses a read-only permission profile. Review
output is independently validated, added lines are recomputed, and the current
PR head/eligibility is checked before comments are published. Findings on added
lines receive inline comments, with single-line suggestions where applicable;
other findings appear in an updated summary. Review never approves, merges or
blocks a PR. Older inline comments may remain visible after subsequent runs.

## GitHub setup {#github-setup}

1. Create the `OpenAI` environment in `gl-inet/docs-kvm`.
2. Enter `OPENAI_API_KEY` and `CODEX_RESPONSES_API_ENDPOINT` as environment
   secrets directly in GitHub. The latter is the full Responses API endpoint,
   including `/v1/responses` when required by the provider.
3. Allow the environment on intended PR branches, not only `master`. Required
   environment reviewers cause a manual approval before each protected run.
4. Allow the required actions under repository/organization Actions policy.
   The publisher declares issue/PR write permissions; no PAT is needed.

Use a narrowly scoped, budget-limited API key. Do not place unrelated secrets
in these jobs. No credentials are stored in this repository.

## Test and operate {#test-and-operate}

```powershell
python -m unittest discover -s scripts/tests -p test_codex_review.py -v
python -m unittest discover -s scripts/tests -p test_github_api.py -v
python -m unittest discover -s scripts/tests -p test_pr_review_workflow.py -v
```

After the tooling reaches `master`, open a small same-repository non-draft
`docs/**` PR. Verify inline findings and the summary, push a follow-up commit
and confirm stale results are not published. Confirm draft/fork PRs are skipped.
The initial tooling PR does not modify `docs/**`, so it does not review itself.
Do not configure review as a required branch-protection check unless desired.
Disable **Codex PR review** in Actions to pause it; leave deployment enabled.

PRs created with `GITHUB_TOKEN` do not normally trigger another `pull_request`
workflow. If translation automation is added separately, its generated PRs will
not automatically invoke this review; a human push or separately authorized
integration is needed. No statistics service or auto-merge is included.

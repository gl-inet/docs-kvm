---
name: glinet-docs-translation
description: Translate, sync, or review GL.iNet KVM documentation between English source files and localized docs. Use when asked to translate English KVM docs into German, Japanese, Spanish, French, Italian, Polish, Dutch, or Swedish; update localized docs after changes under docs/en/**; fix differences reported by scripts/i18n_check.py; improve machine-translated localized pages; or check localized terminology, UI labels, Markdown structure, links, and technical accuracy.
---

# GL.iNet KVM Docs Translation

Use this skill for translation-specific work only. For ordinary documentation edits that do not translate, sync, or review localized content, follow the repository instructions.

## References

Read the target-language reference before editing that language:

- German: `references/german.md`
- Japanese: `references/japanese.md`
- Spanish: `references/spanish.md`
- French: `references/french.md`
- Italian: `references/italian.md`
- Polish: `references/polish.md`
- Dutch: `references/dutch.md`
- Swedish: `references/swedish.md`

If a task touches several languages, read each of their references before editing.

## Common Translation Rules

- Treat `docs/en/` as the English source root, including `mkdocs.yml`, homepage overrides, and page content under `docs/en/docs/`.
- Keep translated docs functionally equivalent to English. Preserve user workflows, warnings, limits, technical behavior, and access restrictions.
- Produce publishable technical documentation, not literal sentence-by-sentence translation.
- Keep product names, model names, protocol names, brand names, standards, firmware versions, IP addresses, URLs, port numbers, file names, and technical values unchanged unless the target language has an official localized form.
- Preserve actual product UI labels when they appear in screenshots or navigation paths. Do not invent localized UI labels that are not shown in the product.
- Preserve Markdown structure: headings, admonitions, numbered steps, bullet lists, tables, images, links, custom anchors, and separators.
- Every heading in every language carries an explicit ID, for example `## Local Access {#local-access}`. Localized headings use the ID of the matching English heading: translate the heading text, never the ID. After adding or editing headings or anchor links, run `python scripts/anchors.py check`.
- Keep image URLs unchanged. Keep relative links unchanged unless the localized target path intentionally differs.
- Remove machine-translation artifacts and unintended source-language fragments from localized prose.
- Check technical words such as `all`, `only`, `must`, `default`, `enabled`, `disabled`, `remote`, `local`, `client`, `host`, and `does not` carefully because they often change device behavior.
- Treat KVM regulatory and compliance statement pages as English-only unless the user explicitly asks to localize them. This includes pages such as `regulatory_statement.md` and legacy `fcc_ic_compliance_statements.md`, plus their corresponding nav entries, redirects, and index links.

## Heading IDs Follow English Titles {#heading-ids-follow-english-titles}

When an English heading changes, its ID follows the current English title in
lowercase ASCII kebab-case, unique within the page. Synchronizing that change
is normal translation work and needs no separate approval or migration list.
The cache is a translation baseline, not an authority for restoring old IDs.
An ID change relative to the cache alone is not a blocking source issue.

Copy the current English ID to matching localized headings; never derive shared
IDs from localized titles. Update inbound anchor links and redirects to the
affected page across all languages, including files outside the initial cache
delta. Use the old/current pages and surrounding content to match sections; do
not replace identical IDs on unrelated pages. Do not preserve old IDs or add
aliases solely for external bookmarks. Do not bulk-rewrite unchanged headings.
Protected localized-only legal sections retain their wording, placement and IDs.

If the English ID does not follow its changed title, the section mapping is
ambiguous, or an English link needs correction, report the specific source
problem instead of editing English outside the task's scope. Unresolved broken
links still prevent completion. An already-aligned localized ID does not clear
pending prose changes.

Missing localized pages, sections, links and updated images reported before a
sync are normally pending translation work when covered by the source set, not
an automatic reason to stop before editing. Fix them through translation, then
rerun all required checks. Unrelated backlog or genuine source ambiguity must
still be reported; do not bypass validation, add allowlist exceptions or advance
the cache to conceal unresolved errors.

## Translation Cache

When `.translation-cache.json` exists, use `scripts/translation_delta.py` to build the incremental English change list and to update the cache after syncing.

```powershell
python scripts/translation_delta.py list
python scripts/translation_delta.py diff docs/en/docs/faq/index.md --lang de
python scripts/translation_delta.py mark docs/en/docs/faq/index.md --lang de --model manual-sync
```

Each English source path has a `targets` object; each language records its own
`source_hash`,
`source_blob` (when recoverable), `target_hash` (when the target baseline is
known), `model`, and `updated_at`. There is no shared top-level `source_hash`.

- `source_hash` identifies the English version synced for that language.
- `source_blob` identifies that English file's Git blob, used by `diff`. A
  historical blob must be available in the clone; if not, compare full pages.
  Only source versions found in committed history reachable from `HEAD` get
  a blob. An uncommitted version without a matching reachable snapshot is
  recorded without `source_blob`; `diff` then requires full-page comparison.
  Commit English source changes before syncing for portable history.
- `target_hash` identifies the localized file after its recorded sync.
- `mark` updates only the explicitly named files and languages after validation.
  Failed languages remain out of date; they cannot be hidden by another
  language's sync. Never edit the cache manually or bulk-refresh it.
- Run `python scripts/translation_delta.py migrate` once for a legacy cache.
  Migration preserves existing hashes and metadata, does not translate files
  or mark pending work complete, and does not invent missing language records.

Hashing and source selection:

- For text files, calculate `source_hash` as SHA-256 over UTF-8 text after normalizing line endings to LF (`\n`). Do not use raw file-byte hashes on Windows, because CRLF checkout conversion produces false mismatches.
- Treat these extensions as text: `.md`, `.yml`, `.yaml`, `.html`, `.css`, `.js`, `.svg`, `.txt`, `.json`.
- For binary files, calculate SHA-256 over raw bytes.
- Scan all current files under `docs/en/**`; report missing cache entries and hash mismatches per language. JSON `cache_missing` and `hash_mismatch` entries contain `path` and `langs`; `target_missing` entries contain `path` and `missing_targets`.
- Include cached `docs/en/**` entries whose source file no longer exists as deleted.
- Treat KVM regulatory and compliance statement pages as English-only unless explicitly requested.

## Incremental Sync Workflow

Use this workflow when syncing English changes into localized docs, especially after a commit.

1. Report the current branch and working tree status before building the change set.
2. Establish the English change set:
   - If the user gives a commit, diff `commit..HEAD`.
   - If `.translation-cache.json` and `scripts/translation_delta.py` exist, run the script and prefer its cache-based change list for incremental sync.
   - If no baseline is available, ask for the intended commit range before doing broad translation work.
3. Build an English change list covering modified, added, deleted, and renamed files under `docs/en/`, plus changes to `docs/en/mkdocs.yml`, nav, redirects, plugins, and path references.
4. Handle structure before prose:
   - Filter out English-only regulatory and compliance statement changes. Do not create, rename, delete, translate, or add localized nav/redirect/index entries for these pages unless explicitly requested.
   - Mirror English renames and deletions in every localized language root, and delete localized pages whose English page was deleted.
   - Create matching localized pages when English adds pages and the user asks to add that target language.
   - Sync localized `mkdocs.yml` changes when English changes nav, redirects, plugins, or path references.
5. Translate only the changed English portions. Do not retranslate whole pages unless the English page is new or the localized page is unusable and the user agrees.
6. Work by topic or small batches for large change sets. Avoid one huge patch across unrelated topics. Use `python scripts/translation_delta.py diff <en-file> --lang <lang>` to inspect the English changes since each language's last sync; when no snapshot is available, compare the full English and localized files.
7. Inspect diffs for unrelated translation churn, accidental mixed-language fragments, broken anchors, malformed Markdown, and missing matching localized files. After validating a batch, record only that batch with `python scripts/translation_delta.py mark <en-file> ... --lang <langs> --model <model>`. Only the coordinating agent writes the cache. Use `--no-target-change` only for reviewed English edits requiring no localized change, with languages listed explicitly. Never use it just to bypass a failure. For deleted source files, remove their localized counterparts first, then use `prune` to remove stale cache records; do not remove approved localized-only legal pages.
8. If you notice an obvious issue in the English source while syncing, fix it only when the user requested source fixes or the correction is clearly in scope; otherwise mention it in the final summary with the file path and suggested correction.

## Single-File Translation Workflow

1. Identify the English source file and the target localized file.
2. Read the full English source before translating or syncing.
3. Read the existing localized file when it exists, including nearby sections that establish terminology.
4. Preserve the English source structure unless the localized docs intentionally differ.
5. Translate or update the localized prose with natural, professional target-language wording.
6. Preserve UI labels, product names, technical values, links, images, tables, admonitions, and custom anchors.
7. Remove machine-translation artifacts and unintended source-language fragments.
8. Check that technical behavior, warnings, limits, routing logic, security notes, and default states still match English.

## Path Conventions

- English source docs live under `docs/en/`.
- Localized docs live under `docs/de/`, `docs/ja/`, `docs/es/`, `docs/fr/`, `docs/it/`, `docs/pl/`, `docs/nl/`, and `docs/sv/`.
- Page content lives under each language root's `docs/` subdirectory, for example `docs/en/docs/faq/index.md` -> `docs/de/docs/faq/index.md`.
- Language-level files such as `mkdocs.yml` and `overrides/` belong directly under each language root.

## Validation

Use the parent virtual environment for MkDocs in this repository. Do not install dependencies unless the environment is missing required packages.

Run the structure and language checks for every touched language, and fix the translation instead of allowlisting:

```powershell
python scripts/i18n_check.py --lang de ja
python scripts/anchors.py check
```

`i18n_check.py` reports sections, images, admonitions, code blocks, tables, links, and values that differ from English, orphan or missing pages, redirect mismatches, untranslated English, and language rules (for Japanese: full-width `（） ？ ！` next to Japanese text and half-width letters and digits). Add an entry to `scripts/i18n_allowlist.yml` only for an intentional difference, with a reason.

The pre-commit hook in `.githooks/` runs these checks on staged files when enabled with `git config core.hooksPath .githooks`.

For translation work, build every touched language that has a `mkdocs.yml`. Also build English if source structure, nav, redirects, shared assets, or overrides changed.

```powershell
$mkdocs="..\Scripts\mkdocs.exe"
& $mkdocs build -f "docs/en/mkdocs.yml" --strict --site-dir "$env:TEMP\docs-kvm-site-en"
& $mkdocs build -f "docs/de/mkdocs.yml" --strict --site-dir "$env:TEMP\docs-kvm-site-de"
& $mkdocs build -f "docs/ja/mkdocs.yml" --strict --site-dir "$env:TEMP\docs-kvm-site-ja"
```

Skip a localized build only when that language root does not exist yet, and state that clearly in the final response.

MkDocs may report existing pages not included in nav and plugin deprecation notices. Treat these as informational unless they are new errors or `--strict` fails.

## Final Check

Before finishing a translation task, verify:

- The target-language text reads naturally from start to finish.
- No unintended source-language artifacts remain in prose.
- UI labels, links, images, Markdown formatting, and admonitions are preserved correctly.
- Technical behavior and security notes still match English.
- Terminology is consistent within the file and with nearby localized docs.
- Build output succeeds for touched languages that exist.

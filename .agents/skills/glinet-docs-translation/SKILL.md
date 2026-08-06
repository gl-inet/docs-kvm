---
name: glinet-docs-translation
description: Translate, sync, or review GL.iNet KVM documentation between English source files and localized docs. Use when Codex is asked to translate English KVM docs into German or Japanese; add or update docs/de/** or docs/jp/** after changes under docs/en/**; improve machine-translated localized pages; or check localized terminology, UI labels, Markdown structure, links, and technical accuracy.
---

# GL.iNet KVM Docs Translation

Use this skill for translation-specific work only. For ordinary documentation edits that do not translate, sync, or review localized content, follow the repository instructions.

## References

Read the target-language reference before editing that language:

- German: `references/german.md`
- Japanese: `references/japanese.md`

If a task touches both languages, read both references before editing.

## Common Translation Rules

- Treat `docs/en/` as the English source root, including `mkdocs.yml`, homepage overrides, and page content under `docs/en/docs/`.
- Keep translated docs functionally equivalent to English. Preserve user workflows, warnings, limits, technical behavior, and access restrictions.
- Produce publishable technical documentation, not literal sentence-by-sentence translation.
- Keep product names, model names, protocol names, brand names, standards, firmware versions, IP addresses, URLs, port numbers, file names, and technical values unchanged unless the target language has an official localized form.
- Preserve actual product UI labels when they appear in screenshots or navigation paths. Do not invent localized UI labels that are not shown in the product.
- Preserve Markdown structure: headings, admonitions, numbered steps, bullet lists, tables, images, links, custom anchors, and separators.
- Keep image URLs unchanged. Keep relative links unchanged unless the localized target path intentionally differs.
- Remove machine-translation artifacts and unintended source-language fragments from localized prose.
- Check technical words such as `all`, `only`, `must`, `default`, `enabled`, `disabled`, `remote`, `local`, `client`, `host`, and `does not` carefully because they often change device behavior.
- Treat KVM regulatory and compliance statement pages as English-only unless the user explicitly asks to localize them. This includes pages such as `regulatory_statement.md` and legacy `fcc_ic_compliance_statements.md`, plus their corresponding nav entries, redirects, and index links.

## Translation Cache

When `.translation-cache.json` exists, use `scripts/translation_delta.py` to build the incremental English change list and to update the cache after syncing.

```powershell
python scripts/translation_delta.py list
python scripts/translation_delta.py update --target de
```

The cache stores `source_hash` values for files under `docs/en/**`.

- For text files, calculate `source_hash` as SHA-256 over UTF-8 text after normalizing line endings to LF (`\n`). Do not use raw file-byte hashes on Windows, because CRLF checkout conversion produces false mismatches.
- Treat these extensions as text: `.md`, `.yml`, `.yaml`, `.html`, `.css`, `.js`, `.svg`, `.txt`, `.json`.
- For binary files, calculate SHA-256 over raw bytes.
- Scan all current files under `docs/en/**`; include missing cache entries and hash mismatches in the English change list.
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
   - Mirror English renames in `docs/de/` and `docs/jp/` when those language roots exist.
   - Create matching localized pages when English adds pages and the user asks to add that target language.
   - Sync localized `mkdocs.yml` changes when English changes nav, redirects, plugins, or path references.
5. Translate only the changed English portions. Do not retranslate whole pages unless the English page is new or the localized page is unusable and the user agrees.
6. Work by topic or small batches for large change sets. Avoid one huge patch across unrelated topics.
7. Inspect diffs for unrelated translation churn, accidental mixed-language fragments, broken anchors, malformed Markdown, and missing matching localized files.
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
- German docs should live under `docs/de/`.
- Japanese docs should live under `docs/jp/`.
- Page content lives under each language root's `docs/` subdirectory, for example `docs/en/docs/faq/index.md` -> `docs/de/docs/faq/index.md`.
- Language-level files such as `mkdocs.yml` and `overrides/` belong directly under each language root.

## Validation

Use the parent virtual environment for MkDocs in this repository. Do not install dependencies unless the environment is missing required packages.

For translation work, build every touched language that has a `mkdocs.yml`. Also build English if source structure, nav, redirects, shared assets, or overrides changed.

```powershell
$mkdocs="..\Scripts\mkdocs.exe"
& $mkdocs build -f "docs/en/mkdocs.yml" --strict --site-dir "$env:TEMP\docs-kvm-site-en"
& $mkdocs build -f "docs/de/mkdocs.yml" --strict --site-dir "$env:TEMP\docs-kvm-site-de"
& $mkdocs build -f "docs/jp/mkdocs.yml" --strict --site-dir "$env:TEMP\docs-kvm-site-jp"
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

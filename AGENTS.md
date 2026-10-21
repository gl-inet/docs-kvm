# Agent Instructions for GL.iNet KVM Documentation

This repository contains GL.iNet KVM documentation built with MkDocs. These rules apply to general documentation editing, whether the change is for English source docs, localized docs, navigation, images, or supporting scripts.

## Repository Expectations

- Produce publishable technical support documentation.
- Keep product behavior, security notes, warnings, limits, and setup workflows technically accurate.
- Do not add product claims, troubleshooting advice, compatibility statements, or behavioral explanations unless they are supported by the source material or nearby documentation.
- Prefer concise, neutral, instructional wording over conversational or marketing-heavy language.
- Preserve exact product names, model names, firmware versions, IP addresses, URLs, port numbers, file names, protocol names, and option values.

## Markdown and Structure

- Preserve Markdown structure unless the requested change requires otherwise.
- Keep headings, callouts, numbered steps, bullet lists, tables, image references, links, and separators coherent with nearby pages.
- Preserve admonition blocks such as `!!! Note` and keep their content complete.
- Keep image URLs and relative links unchanged unless the target file or path intentionally changes.
- Leave a blank line before a `---` separator; directly below a paragraph or code fence it turns into a heading.

## Heading IDs and Anchor Links

- Every Markdown heading in every language, including English, carries an explicit ID, for example `## Local Access {#local-access}`. Always include the `#`; `{local-access}` without `#` does not set an ID.
- English is the source of heading IDs. A localized heading uses the same ID as the matching English heading: translate the heading text, never the ID.
- IDs are lowercase ASCII kebab-case and unique within the page. For a new heading, derive the ID from the English heading text. For a heading that exists only in a localized page, derive the ID from an English rendering of that heading, for example `{#safety-information}` for the German safety information.
- Do not change an existing ID when heading wording changes, because links and bookmarks depend on it. If an ID must change, update it in every language and update every link that uses it.
- Anchor links use the shared ID in every language, for example `[Lokaler Zugriff](quick_setup_guide.md#local-access)`. Do not add `<a id>` or `<span id>` placeholders for headings.
- After adding or editing headings or anchor links, run `python scripts/anchors.py check`.

## UI Labels and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- Keep console navigation paths aligned with the product UI, for example: `**Settings** -> **Video**`.
- If a button or menu label is visibly English in the UI, it is acceptable to keep the label in English in localized docs.
- Do not invent localized UI labels that are not shown in the product.
- Distinguish between explanatory prose and literal UI labels.

## Regulatory and Legal Pages

- Regulatory statement pages (`regulatory_statement.md` and the legacy `fcc_ic_compliance_statements.md` redirects) are English-only. Do not create localized copies, nav entries, redirects, or index links for them unless explicitly asked.
- The German safety information pages and sections exist only in German and keep their approved wording.

## Editing Workflow

- Read enough surrounding context before editing a page.
- Prefer updating the existing matching page instead of creating a different structure unless a new page is required.
- Keep related localized and English documentation structures compatible when the change naturally affects multiple languages.
- When editing shared scripts or automation, update hard-coded documentation paths that depend on moved files.
- Before finishing, scan for broken links, malformed Markdown, missing images, and accidental mixed-language fragments when those risks are relevant.

## Translation Work

Use the `glinet-docs-translation` skill for translation-specific tasks, including translating English docs into localized docs, syncing English changes into localized files, or reviewing localized translation quality. Keep detailed translation workflow and language terminology rules in that skill, not in this default repository guidance.

After adding, renaming, or deleting pages, editing `redirect_maps`, or changing localized pages, run `python scripts/i18n_check.py`. It compares each localized page with the English page section by section (images, admonitions, code blocks, tables, links, IP addresses, and version numbers) and reports orphan pages and broken redirects. It also flags untranslated English and language rules such as Italian accents, French spaces before `: ; ? !`, and full-width `（） ？ ！` next to Japanese text. Fix the translation; add an entry to `scripts/i18n_allowlist.yml` only for intentional differences, with a reason.

The pre-commit hook in `.githooks/` runs these checks on staged files; enable it with `git config core.hooksPath .githooks`.

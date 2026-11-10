# GL.iNet Documentation

This repository contains the source files for GL.iNet KVM documentation.

It is structured as a multilingual documentation repository. The current language sites are:

- English: `docs/en/`
- German: `docs/de/`
- Japanese: `docs/ja/`
- Spanish: `docs/es/`
- French: `docs/fr/`
- Italian: `docs/it/`
- Polish: `docs/pl/`
- Dutch: `docs/nl/`
- Swedish: `docs/sv/`

Each language has its own `mkdocs.yml`, `docs/`, and `overrides/` directory.

## Environment 

The documentation is built with [MkDocs](https://www.mkdocs.org/) 1.5.3 and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme 9.4.6.

## Installation

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

You can also install Material for MkDocs directly:

```bash
pip install mkdocs-material
```

Refer: [https://squidfunk.github.io/mkdocs-material/getting-started/#with-pip](https://squidfunk.github.io/mkdocs-material/getting-started/#with-pip)

## Repository Structure

The root `docs/` folder contains one MkDocs project per language:

```text
docs/
  en/
  de/
  ja/
  es/
  fr/
  it/
  pl/
  nl/
  sv/
```

Each language directory contains `mkdocs.yml`, `mkdocs.fast.yml`, `docs/`, and `overrides/`.

In most cases, localized pages should mirror the corresponding English page path under `docs/en/docs/`.

English is the source for translations. Regulatory and compliance statements remain English-only and are omitted from localized navigation.

## Local Preview

Run MkDocs against the language you want to preview.

```bash
mkdocs serve -f docs/en/mkdocs.yml
```

For faster local editing, use:

```bash
mkdocs serve -f docs/en/mkdocs.fast.yml --dirty
```

To preview the Spanish site, use `mkdocs serve -f docs/es/mkdocs.fast.yml --dirty`.
To preview the French site, use `mkdocs serve -f docs/fr/mkdocs.fast.yml --dirty`.
To preview the Italian site, use `mkdocs serve -f docs/it/mkdocs.fast.yml --dirty`.
To preview the Polish site, use `mkdocs serve -f docs/pl/mkdocs.fast.yml --dirty`.
To preview the Dutch site, use `mkdocs serve -f docs/nl/mkdocs.fast.yml --dirty`.
To preview the Swedish site, use `mkdocs serve -f docs/sv/mkdocs.fast.yml --dirty`.

## Checks Before Committing

Enable the repository's pre-commit hook once per clone:

```bash
git config core.hooksPath .githooks
```

For fully staged English pages, the hook first adds missing explicit heading IDs using the IDs MkDocs already generates, then stages the fixes. Existing IDs are preserved. Pages with unstaged changes are left untouched; add their missing IDs manually or stage the complete page before committing.

The hook selects checks from the staged changes:

- Heading IDs and anchor links (`scripts/anchors.py`), including broken anchor links elsewhere in each touched language.
- Localized pages: structure compared with the English page, untranslated English, and language rules such as Japanese full-width punctuation (`scripts/i18n_check.py`).
- Approved localized legal sections and standalone legal pages: compare `HEAD` with the staged content and reject wording changes or removals, including deleted pages. Renames within the same language are compared with the original file. Unstaged edits cannot hide staged legal changes, and translation allowlist entries do not bypass this protection.
- Changed localized files with a matching English source: independent per-language cache records must match the staged English and localized content. This includes Markdown, configuration, overrides, text assets and binary files. Both the localized file and `.translation-cache.json` must be staged; an unstaged cache update cannot satisfy the check. Other languages may remain pending. English-only regulatory sources and localized-only legal pages have no translation-cache requirement.
- `mkdocs.yml` changes and added, renamed, or deleted pages: orphan pages and redirect problems.

English-only commits do not require translations to be updated in the same commit, but heading and anchor errors still block the commit. To bypass the hook in an emergency, use `git commit --no-verify`.

If no Python interpreter with the documentation dependencies is available, the hook prints a warning and skips its checks. Install `requirements.txt` in the documentation virtual environment to enable them.

### Pull Request Checks

The `Documentation PR checks` workflow runs for pull requests to `master` that change documentation, checking scripts, dependencies, `.translation-cache.json`, hook or documentation policy files, or the workflow itself. It runs separately from AI review and does not change deployment behavior.

- **Structure:** checking-script regression tests, followed by the same heading, anchor, localized structure, legal protection and `.translation-cache.json` checks as the local hook, selected by the committed PR diff. English-only changes may leave translations pending.
- **Build:** strict MkDocs builds for the changed languages; changes outside language directories still build English.
- **Content:** codespell checks added English lines; newly added remote image URLs returning HTTP 404 or 410 fail the check. Grammar, removed heading IDs, suspicious image alt text and repeated Official Website links are warnings. Other image network errors are warnings. LanguageTool unavailability skips grammar checking, not the other content checks.

PR jobs use read-only repository permissions and do not receive publishing tokens or API secrets. Missing heading IDs are reported for manual correction; the workflow does not post one-click suggestions or edit PR files.

To reproduce the structure check locally after committing your changes:

```bash
git fetch origin master
python scripts/precommit.py --base origin/master
```

Unlike local hook mode, `--base` never adds heading IDs or stages changes. It checks committed `HEAD`, including related documentation pages, configuration and the allowlist, regardless of changes in the index or working directory. Legal text is compared with the merge base. A failed check returns a nonzero exit code.

To run the content checks locally:

```bash
python -m pip install codespell==2.4.1
python scripts/pr_check.py --base origin/master
# Optional grammar check against a running LanguageTool server:
python scripts/pr_check.py --base origin/master --languagetool http://localhost:8081
```

The content check also reads committed `HEAD`, not uncommitted documentation edits. These workflows do not configure GitHub rulesets or required status checks. Repository administrators must configure required checks separately if failures should prevent merging.

### Translation cache

The cache records each language separately under `targets.<lang>`: `source_hash` identifies its synchronized English version, `target_hash` identifies the localized content, and `source_blob` stores a reachable English Git snapshot when available. Syncing one language does not mark other languages complete.

For a legacy checkout, migrate once without advancing translation baselines:

```bash
python scripts/translation_delta.py migrate
```

Migration is idempotent and does not invent missing language records. The current repository cache is already migrated. Do not bulk-refresh it to hide pending translation work.

After translating and validating a file, record only the files and languages actually reviewed, then stage the corresponding localized files and cache:

```bash
python scripts/translation_delta.py diff docs/en/docs/faq/index.md --lang de
python scripts/translation_delta.py mark docs/en/docs/faq/index.md --lang de --model manual-sync
git add docs/de/docs/faq/index.md .translation-cache.json
```

Use `--no-target-change` with explicitly named languages only after reviewing an English change that requires no localized edit. It does not bypass validation. When a staged source or target differs from the working-tree version used by `mark`, stage the matching versions or mark the intended versions again before committing. For deleted sources, remove their localized counterparts and use `prune`; never remove approved localized-only legal pages.

## Online View

- English: [https://docs.gl-inet.com/kvm/en/](https://docs.gl-inet.com/kvm/en/)
- German: [https://docs.gl-inet.com/kvm/de/](https://docs.gl-inet.com/kvm/de/)
- Japanese: [https://docs.gl-inet.com/kvm/ja/](https://docs.gl-inet.com/kvm/ja/)
- Spanish: [https://docs.gl-inet.com/kvm/es/](https://docs.gl-inet.com/kvm/es/)
- French: [https://docs.gl-inet.com/kvm/fr/](https://docs.gl-inet.com/kvm/fr/)
- Italian: [https://docs.gl-inet.com/kvm/it/](https://docs.gl-inet.com/kvm/it/)
- Polish: [https://docs.gl-inet.com/kvm/pl/](https://docs.gl-inet.com/kvm/pl/)
- Dutch: [https://docs.gl-inet.com/kvm/nl/](https://docs.gl-inet.com/kvm/nl/)
- Swedish: [https://docs.gl-inet.com/kvm/sv/](https://docs.gl-inet.com/kvm/sv/)

## Guide

### Markdown syntax

Each page use markdown, please check out this basic syntax of markdown [here](https://www.markdownguide.org/basic-syntax/).

### Open in new tab

If you wanna a link to open in new tab, add `{target="_blank"}` at the end of link block.

### Image file type

Prefer to use png.

### Image lightbox

If the size of image is too big, please use the PhotoSwipe, check out [here](#about-plugin-photoswipe).

### Image size

Use `gl-50-desktop`, `gl-60-desktop`, `gl-70-desktop`,`gl-80-desktop`, `gl-90-desktop` to set the percentage of the image width on desktop browser.

Example:

`![gl.inet enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="gl-50-desktop"}`

### Image shadow effect

Use `{class="glboxshadow"}` to add shadow effect to the image.

Example:

`![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}`

### Image captions

```html
<figure>
  <img src="https://dummyimage.com/600x400/eee/aaa" width="300" />
  <figcaption>Image caption</figcaption>
</figure>
```

### Heading IDs

Every heading in every language carries an explicit ID, for example `## Local Access {#local-access}`. Always include the `#`; `{local-access}` does not set an ID.

English defines the IDs. A localized heading uses the same ID as the matching English heading, so anchor links such as `quick_setup_guide.md#local-access` work in every language.

```bash
python scripts/anchors.py check                      # report missing IDs and broken anchor links
python scripts/anchors.py add --lang en              # turn generated English IDs into explicit IDs
python scripts/anchors.py add --lang de [pages ...]  # copy IDs from the matching English headings
```

### Localized page checks

After adding, renaming, or deleting pages, editing `redirect_maps`, or changing localized pages, run:

```bash
python scripts/i18n_check.py [--lang de ja ...] [pages ...]
```

It compares each localized page with the English page section by section (images, admonitions, code blocks, tables, links, IP addresses, and version numbers) and reports orphan pages, missing pages, and broken redirects. It also flags untranslated English and language rules, such as Italian accents, French spaces before `: ; ? !`, and full-width `（） ？ ！` next to Japanese text.

English-only regulatory pages and German-only safety information are not compared. Fix the translation for everything else; add an entry to `scripts/i18n_allowlist.yml` only for intentional differences, with a reason.

### Use relative path to link internal content

```
[easytethering](../../../tutorials/tether)
```

## About plugin PhotoSwipe

Using the v4 version, v5 version looks better, but need to load js module. Don't know how to work it out in mkdocs.

Suggest to use PhotoSwipe when the width of image is large than 1021px.

```
<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/3/setup/gl-b2200/hardware/hardware_1.jpg" itemprop="contentUrl" data-size="3167x2480">
      <img src="https://static.gl-inet.com/docs/router/en/3/setup/gl-b2200/hardware/hardware_1.jpg" itemprop="thumbnail" alt="gl-b2200 pcb pinout" />
    </a>
  </figure>
</div>
```

Reference:

[https://photoswipe.com/documentation/getting-started.html](https://photoswipe.com/documentation/getting-started.html)

[https://codepen.io/dimsemenov/pen/ZYbPJM](https://codepen.io/dimsemenov/pen/ZYbPJM)

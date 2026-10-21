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

## Online View

- English: [https://docs.gl-inet.com/kvm/en/](https://docs.gl-inet.com/kvm/en/)
- German: [https://docs.gl-inet.com/kvm/de/](https://docs.gl-inet.com/kvm/de/)
- Japanese: [https://docs.gl-inet.com/kvm/ja/](https://docs.gl-inet.com/kvm/ja/)
- Spanish: [https://docs.gl-inet.com/kvm/es/](https://docs.gl-inet.com/kvm/es/)
- French: [https://docs.gl-inet.com/kvm/fr/](https://docs.gl-inet.com/kvm/fr/)
- Italian: [https://docs.gl-inet.com/kvm/it/](https://docs.gl-inet.com/kvm/it/)
- Polish: [https://docs.gl-inet.com/kvm/pl/](https://docs.gl-inet.com/kvm/pl/)

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

"""Build page-aware links for the Material language selector.

Material normally renders ``extra.alternate`` as fixed links to each
language's home page. For every content page, this hook checks whether the
same source file exists in a sibling language project (``docs/<lang>/docs``)
and points the selector at that equivalent page when it does. If a translation
does not exist, the configured home-page link is retained to avoid a 404.
"""

import os
import posixpath


def _lang_dir(link):
    """Return the language directory from a link such as ``/kvm/ja/``."""
    parts = [part for part in link.split("/") if part]
    return parts[1] if len(parts) > 1 else None


def on_page_context(context, page, config, nav):
    alternates = (config.get("extra") or {}).get("alternate") or []
    if not alternates:
        return context

    # docs/<lang>/docs -> docs/
    langs_root = os.path.dirname(os.path.dirname(os.path.abspath(config["docs_dir"])))
    src_parts = page.file.src_path.replace(os.sep, "/").split("/")

    resolved = []
    for alt in alternates:
        link = alt.get("link", "")
        lang_dir = _lang_dir(link)
        if lang_dir and os.path.isfile(
            os.path.join(langs_root, lang_dir, "docs", *src_parts)
        ):
            # page.url is '' on the home page and 'faq/example/' elsewhere.
            link = posixpath.join(link, page.url)
        resolved.append({**alt, "link": link})

    context["alternate_links"] = resolved
    return context

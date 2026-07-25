# Directory prose source-of-truth

## Trigger
Use this when an Acadie.sol directory card shows a shortened intention, inferred taxonomy, or tag-like rendering instead of the steward's authored `entry.md` wording.

## Verified pipeline rule
The canonical path is:

```text
acadie_sol_directory/entries/<slug>/entry.md + meta.json
  -> scripts/export_to_site.py:parse_entry()
  -> assets/directory-data.json
  -> directory.html / entry.html
```

In `parse_entry()`, the Markdown preamble must win over metadata prose:

```python
markdown_description = clean_text(
    " ".join(line for line in sections.get("preamble", []) if line.strip())
)
metadata_description = display_text(meta.get("summary") or meta.get("short_description"))
description = markdown_description or metadata_description
```

`category` and `tags` remain explicit structured metadata. Never derive or display them as substitutes for the prose. Public-note bullets may be normalized into `note_points` for list rendering, but do not treat those points as taxonomy.

## Manila comparison
Manila uses the same exporter contract but its card renderer separates the first description segment from the expandable remainder. Compare `manila/edm/directory.html` before changing Acadie card composition; copy the rendering pattern, not the metadata precedence bug.

## Regression test
Create a temporary official entry whose Markdown preamble intentionally differs from `meta.json.short_description`. Assert:

- exported `description` equals the Markdown preamble;
- explicit `category` and `tags` are unchanged;
- Markdown note bullets remain in `note_points`.

## Deployment verification
After export and Pages deployment:

1. Check the live `assets/directory-data.json` with a cache-busting query and verify the exact authored sentence.
2. Use headless Chrome or browser DOM inspection on `directory.html#browse` and `entry.html#<slug>`.
3. Confirm prose is visible, tag/category chips are not being used as the headline copy, and the full-entry back link is `directory.html#browse`.
4. Run the directory tests and `git diff --check` before commit/push.

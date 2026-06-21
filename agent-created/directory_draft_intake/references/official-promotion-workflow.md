# Draft → Official Entry Promotion Workflow

Use this when Acadie.sol directory work shifts from low-friction inbox capture to publishing a proper official entry.

## Core principle

Capture stays permissive; promotion is where canonical decisions happen.

```text
Telegram/live intake → inbox/*.md draft
manual cleanup → entries/<slug>/entry.md + meta.json
export_to_site.py → acadie_sol/assets/directory-data.json
site repo commit/push → GitHub Pages review
```

## MVP public-card threshold

A draft is promotable when the quick public card has enough stable public value:

- canonical display name
- slug
- category
- public area
- one-line summary
- at least one useful public detail, usually address, phone, hours, or strong local context
- public-safe notes with admin-only uncertainty removed

Not required for MVP promotion:

- full official website
- email
- photos
- rich review text
- accessibility/payment/menu details
- complete source history
- full page-level cultural context

Those can wait for future detail pages.

## Promotion steps

1. Read the draft and identify what is missing for the public card vs what is merely detail-page enrichment.
2. Create `entries/<slug>/entry.md` from the official entry template.
3. Create `entries/<slug>/meta.json` from the official meta template.
4. Move stable public prose into `entry.md`.
5. Move canonical machine fields into `meta.json`:
   - `name`, `slug`, `status`, `category`, `short_description`
   - `location.public_area`
   - `tags`
   - `contact`
   - `aliases`, `brand_name`, `branch_name` when useful
6. Preserve relationship hints in `related` / `Related places` when known.
7. Remove or move the old inbox draft once the official entry represents the same record.
8. Run tests and exporter verification before committing.
9. Run `scripts/export_to_site.py` from the directory repo.
10. Commit and push the directory repo first.
11. Commit and push the generated site payload in the site repo.
12. Verify the live GitHub Pages payload, not just the raw GitHub file.

## Verification pattern

Minimum checks used successfully:

```bash
python3 -m pytest -q
python3 scripts/export_to_site.py --stdout >/tmp/acadie_payload.json
python3 scripts/export_to_site.py
```

Then verify the site payload contains the promoted entry with:

- expected `entry_count`
- draft count decreased by 1 if the inbox draft was removed
- `published_count` increased by 1
- promoted item has `status: published` and `draft: false`

## Review note

Tell the user what was missing separately for:

- MVP card readiness
- future full-page richness

This avoids making incomplete-but-useful local entries feel blocked by full CMS-level completeness.

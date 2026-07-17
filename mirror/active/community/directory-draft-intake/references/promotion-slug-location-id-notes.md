# Promotion Slug / Location-ID Notes

Session-derived guardrails for promoting inbox drafts into official entries.

## What is canonical

- `entries/<slug>/` is the canonical entry identity on disk.
- `meta.json.slug` should match the folder name.
- The exporter’s payload items are keyed by `slug` in legacy output scans.
- `location_id` is a reference to a location record, not a renameable display label.

## What to do during promotion

- Keep `entry.md` as the public prose surface.
- Keep `meta.json` as the structured contract.
- Remove or move the inbox draft once the official entry replaces it.
- Verify the exported payload by checking the new `slug` values, not by assuming an `id` field.

## Pitfall

Renaming `location_id` because the wording feels better is usually the wrong move. If the location record already exists, preserve the ID and update the linked record only when the whole location entity is being renamed intentionally.

## Useful verification

- `python3 scripts/export_to_site.py --stdout`
- confirm promoted slugs appear in `items[*].slug`
- confirm draft counts go down only when the source inbox drafts were removed

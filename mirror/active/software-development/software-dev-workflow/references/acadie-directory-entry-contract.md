# Acadie.sol Directory Entry Contract

Use this when working in `acadie_sol_directory` / `acadie_sol` data-export flows.

## Core split
- `entry.md` is *not* dev-only. It is the human-readable source for public prose, notes, sources, and related-place context.
- `meta.json` is the structured contract: IDs, categories, location, contacts, tags, verification, timestamps.
- Exporters consume both; official entries typically prefer `summary` for the public description and fall back to `short_description` when needed.

## Practical rules
- Keep `short_description` a plain string for reliable card rendering.
- Put multilingual/public prose in `summary`.
- Treat `slug` as the entry folder identity.
- Treat `location_id` as a foreign key to a location record; don’t rename it casually.
- If you rename a location ID, update the related location/event records in the same pass.
- `category` is the coarse bucket; `tags` are the richer search/discovery labels.

## Verified behavior from exporter
- Public card description resolution: `summary` → `short_description` → markdown preamble.
- Entry cards use the entry slug in URLs and search indexing.
- Location/public-area values may be normalized by exporter logic, so keep schema and template aligned with any new fields.

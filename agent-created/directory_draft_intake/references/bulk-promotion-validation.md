# Bulk inbox promotion validation notes

Use this when a large `acadie_sol_directory/inbox/*.md` set needs to become proper `entries/*` records.

## Promotion shape

- Promote by **moving**, not copying. If an inbox draft remains beside the new entry, `export_to_site.py` exports both and creates duplicate slugs/anchors.
- Create exactly:
  - `entries/<slug>/entry.md`
  - `entries/<slug>/meta.json`
- Use the inbox filename stem as the slug unless there is a deliberate canonical correction.
- Ensure `meta.slug` matches the folder name exactly.
- Strip `Draft:` from all names and headings.
- Keep `short_description` as a plain schema-compatible string, max 160 chars.
- Add localized summaries in exporter-supported metadata:
  - `summary.en`
  - `summary.fr`
  - `summary.shiac`
- If a French copy should be human-visible in source, add an `## Résumé français` section to `entry.md` as well.

## Category normalization

The schema category list is narrower than the inbox layer. Normalize common draft categories during promotion:

- `entertainment` → `venue`
- `outdoor` → `venue` or `civic`
- `personal care` → `business`
- `music` → `musician` or `artist`
- `retail` → `business`
- `grocery` → `business` or `food`

## Verification status

Do not copy older `steward-reviewed` values into new entries. The schema-safe values are:

- `unverified`
- `steward-verified`
- `community-confirmed`
- `on-chain`

For user/steward-reviewed local entries, prefer `steward-verified`.

## Chain and branch records

For chains or repeated brands, preserve branch specificity:

```json
{
  "name": "Pizza Delight — Bathurst",
  "brand_name": "Pizza Delight",
  "branch_name": "Bathurst",
  "aliases": ["Pizza Delight Bathurst"]
}
```

## Post-promotion checks

Run export to stdout before writing the site payload:

```bash
python3 scripts/export_to_site.py --stdout > /tmp/acadie_export.json
python3 - <<'PY'
import json
from collections import Counter

d=json.load(open('/tmp/acadie_export.json'))
items=d['items']
print('entry_count', d['entry_count'])
print('published_count', d['published_count'])
print('draft_count', d['draft_count'])
print('duplicate_slugs', [k for k,v in Counter(i['slug'] for i in items).items() if v>1])
print('draft_titles', sum(1 for i in items if i['title'].startswith('Draft:')))
print('missing_fr', sum(1 for i in items if not i.get('description_localized',{}).get('fr')))
PY
```

Expected for a complete inbox promotion:

- `draft_count` is `0`
- no duplicate slugs
- no titles beginning with `Draft:`
- no missing `description_localized.fr`

Only after that, run the real export:

```bash
python3 scripts/export_to_site.py --all --site ~/ExoCortex/websites/projects/acadie_sol
```

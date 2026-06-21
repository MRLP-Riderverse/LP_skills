# Directory promotion + Sol.site notes

## Draft → official entry promotion
- Drafts live in `inbox/*.md` and are intentionally loose.
- Official entries live in `entries/<slug>/` and must contain both `entry.md` and `meta.json`.
- After promotion, run the site export so the website payload reflects the new official entry.
- Important pitfall: `scripts/export_to_site.py` exports **both** `inbox/*.md` drafts and `entries/*/entry.md` official entries. If the promoted draft is left in `inbox/`, it will appear as a duplicate draft card in the site payload.

## Verified export behavior
- `python3 scripts/export_to_site.py --stdout` prints the JSON payload for inspection.
- `python3 scripts/export_to_site.py` writes to `../acadie_sol/assets/directory-data.json` by default.
- Current payload shape includes `entry_count`, `draft_count`, `published_count`, and `items`.

## Sol.site / GitHub Pages
- Sol.site docs state that `.sol` domains can point to web2 hosting providers, including GitHub Pages, via a **CNAME** to the provider hostname.
- The custom domain should be the hostname only (`acadie.sol.site`), not a full GitHub Pages path.
- For GitHub Pages, the target value should be the Pages hostname (e.g. `mrlp-riderverse.github.io`), with TXT only if the host requires verification.

## Copy/paste reminders
- Promotion sequence: write official files → validate metadata → export site payload → verify the public payload → remove or archive the inbox draft if you do not want duplication.
- Domain sequence: set the GitHub Pages custom domain to `acadie.sol.site` → configure Sol.site CNAME to the Pages hostname → verify after propagation.

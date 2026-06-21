# Directory ↔ Site Sync

This repo pair uses a **static export pipeline**, not live filesystem coupling at page-load time.

## Roles
- `acadie_sol_directory` = canonical source of truth for listings
- `acadie_sol` = static presentation repo

## Manual sync flow
1. Edit or add drafts in `acadie_sol_directory/inbox/*.md`.
2. Run the export script from the directory repo:
   ```bash
   cd /home/midnight/ExoCortex/websites/projects/acadie_sol_directory
   python3 scripts/export_to_site.py
   ```
3. The script writes `../acadie_sol/assets/directory-data.json` by default.
4. Commit/push the website repo so the public site reflects the new snapshot.

## Useful flags
- `--stdout` prints the JSON payload without writing it.
- `--directory <path>` overrides the directory repo root.
- `--site <path>` overrides the website repo root.

## Safety notes
- Keep admin notes out of the public JSON payload.
- Mark drafts visibly in the rendered site (`DRAFT` badge / preview language).
- Do not assume a push to the directory repo updates the website automatically unless CI/hook automation has been added.

## Verification
- Check the exported JSON file exists and loads.
- Check the website page renders the JSON snapshot.
- If using live preview, keep the page labeled as draft/preview so users understand it is not final.
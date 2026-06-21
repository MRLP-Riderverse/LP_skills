# Directory export workflow

Use this when the user asks to keep the website synced with the directory or wants a live-ish preview of drafts.

## Trigger phrase
- Treat **"export to site"** as the manual sync trigger.

## Manual flow
1. Update listings in `acadie_sol_directory`.
2. Run:
   ```bash
   cd /home/midnight/ExoCortex/websites/projects/acadie_sol_directory
   python3 scripts/export_to_site.py
   ```
3. Confirm `acadie_sol/assets/directory-data.json` was written.
4. Commit/push the website repo when the snapshot should go public.

## Local preview / review
- Serve the site repo locally and open `directory.html`.
- Use a headless browser screenshot for Telegram review when the user wants visual proof.
- Keep draft pages visibly labeled so the preview stays honest.

## Safety
- The export is a snapshot, not a live DB link.
- A directory push alone does not update the site unless the export/deploy path is wired up.
- Keep admin notes out of the exported payload.

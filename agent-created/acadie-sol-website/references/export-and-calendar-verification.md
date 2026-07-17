# Export and Calendar Verification

Use this when a directory-repo change must land in the `acadie_sol` site repo.

## Export order
1. Commit the source data repo change first.
2. Run the export from the directory repo:
   ```bash
   python3 scripts/export_to_site.py --all --site /home/midnight/ExoCortex/websites/projects/acadie_sol
   ```
3. Commit/push the site repo payloads.

## Verify these site payloads
- `assets/directory-data.json`
- `assets/events-data.json`
- `assets/locations-data.json`
- `assets/search-index.json`
- `assets/site-meta.json`
- `assets/calendar/*.ics`

## Calendar-file pitfall
- If `git diff --check` flags generated `.ics` files after export, inspect the file contents for line-ending churn first.
- The exported ICS files should be LF-only in the repo; CRLF-only bodies can show up as trailing-whitespace noise.
- Normalize the `.ics` files and rerun the export before committing if that shows up.

## Quick verification commands
```bash
git diff --check
git status --short
python3 - <<'PY'
import json, pathlib
site = pathlib.Path('/home/midnight/ExoCortex/websites/projects/acadie_sol/assets')
for name in ['directory-data.json','events-data.json','locations-data.json','search-index.json','site-meta.json']:
    data = json.loads((site / name).read_text())
    print(name, 'ok')
PY
```

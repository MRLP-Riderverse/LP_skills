# Directory batch sync: commit → push → export → commit site → push site

Use this sequence when the user says things like "commit X, push, export to site" after staging new directory drafts.

## Repeatable order
1. Commit the new inbox drafts in `acadie_sol_directory`.
2. Push the directory repo to `origin/main`.
3. Run `python3 scripts/export_to_site.py` in `acadie_sol_directory`.
4. Commit the changed `acadie_sol/assets/directory-data.json` in `acadie_sol`.
5. Push the site repo to `origin/main`.
6. Verify the exported payload changed, ideally by checking the live Pages asset URL.

## Verification pattern
- The export script should report counts like `Entries: N Drafts: N Published: 0`.
- After pushing the site repo, check the served `assets/directory-data.json` or the relevant page for the new entry title.
- If the user only asked for the directory repo commit, do not silently export the site; follow the requested scope.

## Pitfalls
- Do not assume local changes are visible on Pages before the site repo is committed and pushed.
- Do not skip the site commit after export; the export only changes the working tree until it is committed.
- Keep the directory repo and site repo as separate pushes even when the change originated from one user request.

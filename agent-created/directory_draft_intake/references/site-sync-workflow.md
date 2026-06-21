# Site sync workflow notes

Use this when the user says things like:
- commit
- push
- export to site
- publish the new entries

## Canonical flow
1. Commit the new `acadie_sol_directory/inbox/*.md` drafts in the directory repo.
2. Push `acadie_sol_directory` to `origin/main`.
3. Run `scripts/export_to_site.py` from `acadie_sol_directory` to regenerate `acadie_sol/assets/directory-data.json`.
4. Commit the updated site payload in `acadie_sol`.
5. Push `acadie_sol` to `origin/main`.

## Notes
- The directory repo is the source of truth; the site repo is a generated/public mirror.
- If the user asks for a batch action, do not stop after drafting. Finish the export and push sequence.
- Preserve the inbox drafts even when the final public site is still draft-only.
- If a name is clearly a separate physical business in the same building/cluster, keep a separate inbox draft rather than collapsing it into one record.

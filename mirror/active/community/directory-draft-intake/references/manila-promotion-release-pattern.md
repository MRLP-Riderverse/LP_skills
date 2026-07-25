# Manila-style derivative promotion and release

This reference records the verified promotion pattern for an English-first derivative directory with a separate local source repo and GitHub Pages site repo.

## Source transformation

For each stable inbox draft:

- Move it into `entries/<slug>/entry.md`.
- Add `entries/<slug>/meta.json` with `status: published`, an allowed canonical `category`, stable slug, location, contact fields, tags, and provenance.
- Keep `short_description` concise and schema-safe (160 characters or fewer); keep richer scene language and contextual notes in `entry.md`.
- Do not leave the old inbox draft after its canonical replacement exists.
- If relationships are declared in `meta.json.related`, omit the duplicate `## Related places` section from `entry.md`; the exporter combines both sources.
- Keep future/upcoming event mentions out of the quick directory card. They may remain in full-entry notes until a structured events layer exists.

## Deterministic pre-release checks

Run from the source repo's group directory:

```bash
python3 scripts/export_to_site.py --stdout
python3 -m pytest -q
python3 scripts/export_to_site.py --site ../../manila/edm
git diff --check
```

Inspect or assert the generated directory payload:

- expected `entry_count`
- `draft_count == 0` for a full publication batch
- expected `published_count`
- unique slugs for every item
- every promoted item has `status == "published"` and `draft == false`
- each card description is within the schema length limit

## Two-repository release order

1. Review and commit the source transformation in `manila-directory`.
2. Push the source repo and verify local `HEAD` equals `origin/main`.
3. Export the generated payload into `manila-site`.
4. Selectively stage only the intended generated payload changes; do not broad-stage unrelated local artifacts.
5. Commit and push the site repo; verify its local/remote SHA.
6. Wait for the GitHub Pages workflow to complete successfully.
7. Fetch the deployed `assets/directory-data.json` using a cache-busting query and validate the live counts and slugs.
8. Check the key public HTML routes return HTTP 200 before handing the live URL to the user.

A pushed commit is not deployment proof. The deployed payload is the final source-to-render verification boundary.

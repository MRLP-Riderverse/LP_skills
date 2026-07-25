# Manila intake routing reference

Use this for the derivative Manila directory when a user asks to add a submission to the inbox and then turn it into a clean public entry.

## Reliable sequence

1. Check both `manila-directory` and `manila-site` repositories for existing work and duplicate names/aliases.
2. Write the raw submission to the source repository's top-level inbox:
   `manila-directory/inbox/<slug>.md`
3. Include `Group: edm` when the submission belongs to the EDM directory.
4. Run the router with the repository root explicitly:

   ```bash
   python3 scripts/route_inbox.py --root /absolute/path/to/manila-directory
   ```

   Do not rely on the script's implicit default when working from the project tree; the current default can resolve the parent projects directory rather than the Manila repository.
5. Read the routed draft under `edm/inbox/` and use it as the raw capture source.
6. For a clean entry, create both:
   - `edm/entries/<canonical-slug>/entry.md`
   - `edm/entries/<canonical-slug>/meta.json`
7. Normalize draft-only categories to the schema's allowed canonical category values. For creator/steward/cultural-infrastructure records, prefer `project` or `community` over inventing a slash-combined category.
8. Preserve supplied identities as `aliases` and keep public social/profile URLs in the human-facing entry. Use `contact.website` for the primary public destination the renderer supports; keep additional social URLs in `links.social` when the schema allows them.
9. Add explicit relationships in `meta.json.related` using existing canonical slugs. Do not invent new venue records for related-scene context.
10. Remove the routed inbox draft only after the canonical entry files exist, preventing duplicate draft + published records.
11. Run the source tests, `git diff --check`, and `python3 scripts/export_to_site.py --stdout` before committing.
12. Export to the sibling site repository:

   ```bash
   python3 scripts/export_to_site.py --site ../../manila/edm
   ```

13. Verify the generated site payload contains the exact slug, name, aliases, category, public area, primary website, tags, and related slugs. Stage only the intended generated payload.
14. Commit and push the source repository first, then commit and push the site repository. If the user supplies an exact commit message, use it verbatim in both repositories.
15. Verify local `HEAD` equals `origin/main` in both repositories. For GitHub Pages, resolve the Pages URL and fetch the live JSON with a cache-busting query; confirm HTTP 200 and the new slug marker before reporting publication.

## Canonical identity example

For a self-submitted creator using a project identity, keep the person as the display name and the project identity as an alias. Example shape:

```json
{
  "name": "Joshua Den Ouden",
  "aliases": ["JoshShoot.sol", "JoshShoot"],
  "category": "project",
  "contact": {"website": "https://linktr.ee/joshshoot.sol"},
  "links": {
    "social": [
      {"platform": "instagram", "url": "https://www.instagram.com/joshuadenouden"},
      {"platform": "soundcloud", "url": "https://soundcloud.com/joshua-den-ouden"}
    ]
  }
}
```

Keep the exact supplied public handle and URL visible in `entry.md`; structured links are for renderer/search support and future full-page use.

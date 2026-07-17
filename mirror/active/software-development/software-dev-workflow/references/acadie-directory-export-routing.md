# Acadie directory export + routing verification

Use this when a static site page consumes generated JSON from the directory repo and the user reports missing entries or "ghost" transitions.

## What happened
- The public website repo (`acadie_sol`) was rendered from exported assets generated out of `acadie_sol_directory`.
- Missing search results were not a live render bug; they were fixed by adding/refreshing the source records and re-running the exporter.
- The events page differed between `all` and `upcoming` by design: `computed_status` / time filtering split the payload.
- A route-pending cloak (`html.route-pending`) removed intermediate page flashes while data loaded.

## Reliable verification sequence
1. Check source records in the directory repo first:
   - `entries/**/entry.md` + `meta.json`
   - `events/**/event.md` + `meta.json`
2. Search the source repo for the exact title/alias the user expects.
3. Re-export the public payloads into the website repo.
4. Confirm the generated assets contain the new item/title.
5. Confirm the rendered page has the expected search anchors and no redundant chrome.
6. If page transitions flash intermediate states, add a route-pending cloak to hide splash/shell until `loadData()` resolves, then remove the cloak in both success and catch paths.

## Search/UI checks
- Prefer one compact search affordance; if the page already auto-searches on typing and Enter, do not keep a separate visible `Search` label or submit button.
- Put utility pills like `View all` and `Filters` *above* the main search container if they need to read as global mode switches.
- Keep the clear affordance inline as a small `×` at the right edge of the input.
- If the user says the pills are "big" or "stacked," tighten the control grid before changing data.

## Common failure modes
- Source record exists, but exporter was not run, so the public repo is stale.
- Search index contains the entry title, but the main payload still lacks the item, so the page never renders it.
- Events appear inconsistent across tabs because the page splits `all` vs `upcoming` using computed time status, not because routing is broken.
- Route transitions flash because shell visibility is not gated while data is loading.

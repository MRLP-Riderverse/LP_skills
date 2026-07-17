# Session notes: directory intake batching and chain locations

Compact lessons from the Four Rivers + Bathurst batch intake session.

## What worked

- Batch requests can be staged as one inbox draft per distinct physical location.
- For chains with multiple local branches, the title should disambiguate the branch or street address.
- If the user says a place has 2 locations, do not merge them into one draft.
- If a web search returns conflicting address variants, keep the uncertainty in `## Notes` rather than forcing a single normalized field.
- Public-source URLs belong in `## Public source`; location summaries can stay in `## Notes` until cleanup.

## Useful web lookup pattern

- Official site pages are the best anchor when available.
- Search-result snippets can be enough to identify candidate addresses before draft creation.
- For small local-business lookups, lightweight web search plus map/geocoder confirmation is often faster than trying to derive structure from the first hit.

## Examples from this session

- McDonald's Bathurst split cleanly into:
  - 620 St. Peter Ave
  - 900 St. Anne St (Walmart)
- CCNB Bathurst split cleanly into:
  - 725 College St
  - 75 Youghall Dr
- Subway in Bathurst and Beresford/Belle-Baie should remain separate drafts.
- Waterfront cluster businesses (Librairie Pélagie, Monty's Pretzelria) are useful to keep as distinct drafts even when they share a corridor / venue cluster.

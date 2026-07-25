---
name: community-event-directory-linking
description: Keep community directory entries, locations, events, search index, and calendar artifacts synchronized when adding or updating public-facing local listings.
---

# Community Event / Directory Linking

Use this skill when a request touches any combination of:
- a community business/venue/organization entry
- a location record
- an event record
- the search index
- a calendar/ICS artifact
- cross-linking between hosts, venues, and nearby organizers

## Source-link access rule
- A public Discord invite with an `event=<scheduled_event_id>` parameter is only a candidate source. Verify whether the fetched page exposes event-level fields; it may expose only generic server-level metadata. If event fields are gated behind authentication, request a screenshot or copied event details and never infer title, time, location, or description. See `references/discord-event-link-parsing.md`.

## Default workflow
1. Identify the source of truth for each object type.
   - Directory entry: human-facing business/org record.
   - Location record: physical place / routing anchor.
   - Event record: time-based occurrence.
   - Search index: derived discovery layer.
   - Calendar file: user-facing shareable schedule artifact.
2. Resolve the minimum viable identifiers first.
   - Title / slug / location_id / start time / address.
3. Add or update the directory entry before the event when the event depends on a host or organizer.
4. Add or update the location record if the event needs a new physical anchor.
5. Link the event to the location and host entry IDs.
6. Refresh the derived site payloads so the new objects are discoverable immediately. For the Acadie.sol exporter, use the full export mode with the resolved site target (`python3 scripts/export_to_site.py --all --site ~/ExoCortex/websites/projects/acadie_sol`); the legacy default command writes only `directory-data.json` and silently leaves event/location/search/calendar payloads stale.
7. If the project uses ICS/calendar exports, generate or update the matching calendar artifact.
8. Verify the full chain by reading back the modified JSON and checking the *actual runtime search payload* (which may be directory data rather than a separate search-index file). Read the generated event/location payloads and the matching `.ics` file, not just the source records.
9. When publishing a two-repository source/site pair, commit and push the source records first, then export, verify the generated site payload, and commit/push the site repository second. Stage only intended source and generated paths; exclude test caches and unrelated local files. If the user supplies an exact commit message, use it verbatim in both repository commits.
10. After the Pages workflow completes, fetch the live generated event JSON and matching ICS URL with a cache-busting query. Confirm HTTP 200, expected content type, and a unique event ID/title marker before calling the site published.

## Data-shape notes
- Prefer one canonical record per real-world entity.
- If a business is also an organizer and venue hub, model it once and reuse that entry across related events.
- Keep public contact data limited to what is publicly available.
- Use stable slugs/IDs that reflect the actual entity and avoid ephemeral wording.
- Event titles can be user-facing; IDs should stay machine-stable and descriptive.

## Pitfalls
- Do not update only the event and forget the search index; discovery then lags behind the data.
- Do not add a new organizer/venue without checking whether the same entity already exists under a slightly different title or slug.
- Do not over-structure intake fields at the draft layer; capture the minimum required identity and keep extra context in a notes block for later normalization.
- Do not misclassify a steward, builder, or project contact as a local artist merely because the directory began with an artist-focused group. Use the closest supported project/community category and a truthful public area.
- Preserve explicit public social handles in a public-data/contact field; when the renderer supports it, convert only clearly labeled Instagram/X handles into platform links. Never complete a truncated handle or infer an account.
- Include public-data fields in the runtime search haystack. A generated `search-index.json` may be empty or auxiliary while the browser searches `directory-data.json` directly.
- When an exporter has a configurable site target, verify the resolved target path before writing derived files; do not alter canonical source data to compensate for a stale example path.

## Verification
- Read the canonical entry/meta files back after edits.
- Run the repository's exporter/tests and inspect the rendered payload for the exact name, category, area, description, tags, and public data.
- Confirm the new entry is discoverable through the browser's real search source, including searches for supplied social handles and tags.
- Confirm IDs are referenced consistently across files.
- If a calendar file was created, confirm its UID, DTSTART, SUMMARY, and LOCATION align with the event record.

## Reference
- `references/event-linking-workflow.md` — session-specific example and compact checklist.

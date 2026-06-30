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
6. Refresh the search index so the new objects are discoverable immediately.
7. If the project uses ICS/calendar exports, generate or update the matching calendar artifact.
8. Verify the full chain by reading back the modified JSON and checking the search index inclusion.

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
- Do not invent contact details or social handles; only promote what is publicly stated.

## Verification
- Read the JSON back after edits.
- Confirm the new entry/event/location appears in the search index.
- Confirm IDs are referenced consistently across files.
- If a calendar file was created, confirm its UID, DTSTART, SUMMARY, and LOCATION align with the event record.

## Reference
- `references/event-linking-workflow.md` — session-specific example and compact checklist.

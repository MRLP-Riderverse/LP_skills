# Discord event link parsing

Discord invite URLs may contain an `event=<scheduled_event_id>` query parameter, but the publicly retrievable invite page can still expose only server-level Open Graph metadata (server name, member count, generic invite description). Do not treat the presence of an event ID as proof that event-specific title, timing, location, or description is available.

## Intake rule
1. Fetch the invite URL and inspect the final URL plus public metadata.
2. Distinguish server-level metadata from event-level metadata.
3. If the event fields are not present publicly, ask for a screenshot or copied event details from an authenticated Discord view.
4. Preserve the Discord URL as a public source/join link, but do not invent missing event fields.
5. Once the fields are supplied, create the canonical site event record and include the Discord URL in its public links.

## Minimum fields to request when Discord metadata is gated
- title
- date
- start/end time and timezone
- online or physical location
- description
- host/organizer
- joining or registration link
- bring/participation notes

## Verification language
Say that the Discord link was verified as resolving to the intended server/invite when that is what the fetch proves. Say separately that event-specific details were unavailable if only server-level metadata was exposed. Never claim to have copied the event from the URL unless the event fields were actually read.

# Acadie.sol events + locations V1 architecture

Session-derived guidance for maturing Acadie.sol from directory preview into a lightweight event/discovery layer while preserving the existing source-of-truth split.

## Core decision

Keep events inside the **data repo** for V1:

```text
acadie_sol_directory/
  entries/
  events/
  locations/
  offers/
  regions/
  archive/
  schemas/
  scripts/
```

Do **not** create a separate events repo yet. Bundling is easier to inspect, export, fork, and reason about while the project is still pre-public/V1. Split later only if event volume, permissions, or regional stewardship demands it.

The site repo remains rendering-only:

```text
acadie_sol/
  assets/
    directory-data.json
    events-data.json
    locations-data.json
    regions-data.json
    search-index.json
    site-meta.json
    calendar/*.ics
```

## Do not embed events inside venue entries

Events should be first-class records, not nested lists inside a venue/contact entry.

Bad long-term shape:

```json
{
  "entry": "La Louga",
  "events": [{ "title": "EDM Night" }]
}
```

Why not: the event becomes owned by one venue page, but real events may need to render on a venue page, artist page, region page, all-events page, search results, suggested route, archive article, sponsor page, and calendar file.

Preferred shape:

```json
{
  "id": "louga-edm-night-placeholder",
  "status": "placeholder",
  "title": {
    "en": "EDM Neon Night",
    "fr": "Soirée EDM néon",
    "shiac": "Neon night au Louga là 🔥"
  },
  "host_entry_ids": ["la-louga-night-bar-resto"],
  "location_id": "la-louga-main-st",
  "starts_at": "",
  "ends_at": "",
  "timezone": "America/Moncton"
}
```

Then venue pages render chronological events by relationship:

```js
relatedEvents = events.filter(event =>
  event.host_entry_ids.includes(entry.slug) ||
  event.performer_entry_ids.includes(entry.slug) ||
  event.sponsor_entry_ids.includes(entry.slug) ||
  entry.location_ids?.includes(event.location_id)
)
```

## Data responsibilities

- `entries/` = who/what exists long-term: venues, artists, businesses, organizations, sponsors, hosts.
- `events/` = time-based happenings: concerts, walks, meetups, markets, fundraisers.
- `locations/` = physical places/corridors/trailheads/buildings where things happen.
- `regions/` = cultural/geographic grouping: Acadie-Bathurst, Belle-Baie, Caraquet, etc.
- `offers/` = temporary opportunities/promos/open calls.
- `archive/` = after-the-fact recap/preservation articles and external links.

## Why locations are first-class

Locations should not only be static fields on entries because:

1. One entry can have multiple physical contexts, branches, campuses, trailheads, or event grounds.
2. Multiple entries/events can share one location or corridor.
3. Wayfinding, parking, accessibility, map/day-trip logic, and weather-sensitive notes belong to places, not always to business identity.
4. Future route/day-trip/search behavior needs reusable physical nodes.
5. Archive/recap records can link to where something happened without polluting the venue profile.

Location records may stay minimal in V1; the important part is having stable IDs.

### Related-business handling via location graph

Do **not** hand-maintain every adjacent-business relationship pair-by-pair. Prefer a relation graph that can be derived:

- `entry.location_id` links a business/venue identity to a reusable place.
- `entry.street_id` or `location.street_id` links places on a corridor such as `main-st-bathurst` or `st-peter-ave-bathurst`.
- `locations/<corridor>/` can represent known sub-communities/corridors/districts even when no single owner exists.
- `nearby_location_ids` captures explicit known adjacency only where human judgment matters.
- Future coordinate/radius fields can be added later; do not block V1 on geocoding.

Example V1 pilot mapping:

```text
la-louga-night-bar-resto → la-louga-main-st → main-st-bathurst
big-d-drive-in           → big-d-st-peter   → st-peter-ave-bathurst
```

This lets directory cards, venue pages, event pages, and day-trip routes infer related places by `location_id`, `street_id`, corridor membership, and later radius — instead of stuffing every related business into every entry.

## Language fields

For clean/published records, prefer nested language objects:

```json
"title": {
  "en": "",
  "fr": "",
  "shiac": ""
},
"description": {
  "en": "",
  "fr": "",
  "shiac": ""
}
```

The user wants a third manual tier for **Acadian/Shiac** meme/local voice. Do not force this on raw inbox drafts; drafts remain low-friction and can be normalized later.

## Placeholder / demo events

Example events discussed during design are not true public events. Default to marking demo/seed records clearly:

```json
"status": "placeholder"
```

or keep them out of public rendering until intentionally exposed as demos.

If the user explicitly asks to test the public/mobile site with the placeholders visible, it is acceptable to temporarily set those demo records to:

```json
"status": "published"
```

Keep the event IDs/titles obviously placeholder-like unless the user supplies real event details. This lets the public UI, event filters, venue feeds, and `.ics` generation be tested without pretending the examples are confirmed community events.

## Event lifecycle and archive automation

Keep two layers distinct:

1. **Rendered/computed state** — the exporter may compute `computed_status: archived` once `expires_at`/`ends_at` has passed so stale events disappear from active UI even before source files are patched.
2. **Durable source state** — an explicit script/cron can later patch `events/*/meta.json` from `active`/`published` to `archived` when expired.

Recommended source fields:

```json
{
  "status": "active",
  "starts_at": "2026-07-12T21:00:00-03:00",
  "ends_at": "2026-07-13T01:00:00-03:00",
  "expires_at": "2026-07-13T01:00:00-03:00"
}
```

Use a dry-run-first archive script pattern:

```bash
python3 scripts/archive_expired_events.py          # report only
python3 scripts/archive_expired_events.py --apply  # patch source meta.json files
```

Do not auto-archive `placeholder` records unless explicitly requested; placeholders are UI/test records and should not be treated as confirmed public activity.

## Calendar feature

Add-to-calendar is a high-value pre-PWA feature. Generate static `.ics` files during export:

```text
acadie_sol/assets/calendar/<event-id>.ics
```

Render:

```html
<a href="assets/calendar/<event-id>.ics" download>Add to calendar</a>
```

This works with iPhone Calendar, Google Calendar, Outlook, and most native mobile calendar apps without accounts or tracking.

## Search / browse UX

Quick search should expose critical curiosity signals while users browse:

- events within next 7 days
- next event for venue
- event type badge
- location/region badge

Venue cards/pages should show chronological event feeds. Once venue-profile event rendering works, the global all-events page is straightforward.

## Site metadata without tracking

Avoid privacy-invasive visitor analytics. For friendly proof-of-life, prefer build/export metadata:

- `latest_source_modified_at`
- `latest_source_modified_ts`
- `snapshot_refresh_count`
- directory/event/location counts
- `activity_led`

A true global page-refresh or visitor counter requires writable backend infrastructure and should not be added for V1.

The preferred Acadie.sol V1 homepage pulse is a small unexplained LED/easter egg derived from recent source modification/commit activity:

```text
green  = modified within 14 days
yellow = 15–30 days
red    = 30+ days
```

Prefer a static `snapshot_refresh_count` that increments on export/build, not human visits. This gives proof-of-life without IPs, cookies, identity, or analytics.

## Implementation notes from V1 pass

When implementing this class of change:

- Keep source data in `acadie_sol_directory`; write generated payloads only into `acadie_sol/assets/`.
- Preserve existing tests and legacy exporter behavior while adding `--all` or equivalent multi-payload export mode.
- Generate `.ics` files during export rather than client-side when possible.
- Add comments in larger code blocks explaining each block’s relation and modularity. The user specifically values code comments that make future handoff/dev-worker review easier.
- Add repo-local continuity notes under `acadie_sol/todo/` for project-handoff details that should travel with the site repo; do not put secrets or private escalation channels there.
- Verify with: Python compile, test suite, export run, JSON count inspection, JS syntax checks for inline scripts, and static HTTP fetches for changed pages/assets.
- If browser screenshot tooling is unavailable, do not claim visual QA; report that static serving/script checks passed and visual review remains manual/pending.

## Contact boundary

Defer public contact/report flows until the user decides channels. Intended split:

- low urgency → low-agency channel such as email/form
- high urgency venue/event coordination → higher-agency channel such as Telegram/Signal/Discord

Do not hardcode contact mechanics prematurely.

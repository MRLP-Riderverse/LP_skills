# Events + contrast lessons from Acadie.sol site work

Use this as a compact checklist when changing `events.html` or exporting event records from `acadie_sol_directory`.

## Proper event-add flow

1. Add the event to the source-of-truth data repo, not directly to site assets:
   - `~/ExoCortex/websites/projects/acadie_sol_directory/events/<event-id>/event.md`
   - `~/ExoCortex/websites/projects/acadie_sol_directory/events/<event-id>/meta.json`
2. If the venue is not yet a polished directory entry, add a reusable location record instead of blocking on entry polish:
   - `locations/<location-id>/location.md`
   - `locations/<location-id>/meta.json`
3. Export to the site with the script's actual flag names:
   ```bash
   cd ~/ExoCortex/websites/projects/acadie_sol_directory
   python3 scripts/export_to_site.py --all --site ~/ExoCortex/websites/projects/acadie_sol
   ```
4. Verify generated site artifacts:
   - `assets/events-data.json` contains the new event
   - `assets/locations-data.json` contains the location
   - `assets/search-index.json` contains the event/location search rows
   - `assets/calendar/<event-id>.ics` exists when `calendar.ics_enabled` is true
5. Commit/push both repos when both source and static export are correct:
   - directory repo commit for source records
   - website repo commit for generated assets + any rendering changes

## Event notes rendering

If an event has practical details, keep them in event metadata and render them from data:

- `bring.en`: audience-facing "bring / entry" detail
- `wayfinding.en`: location/access note

In `events.html`, render these as optional `.event-notes` below `.description`, not as hardcoded copy in the page. This keeps public text tied to the source event record and lets future events reuse the same card structure.

## Host + venue link routing

For published venues, create/promote a full directory entry and link the relationship fields together:

- `event.host_entry_ids`: include the published entry slug
- `location.entry_ids`: include the same published entry slug

Public event links should route to the full page, not the quick-card stack:

```js
function fullEntryHref(slug) { return `entry.html#${encodeURIComponent(slug)}`; }
```

Use `entry.html#<slug>` for “Hosted by”, “At <venue>”, and “View host” when the slug is a published entry. Reserve `directory.html#entry-<slug>` for directory-internal expansion or drafts that intentionally do not have full pages.

When promoting an inbox draft into a published entry, remove the old `inbox/<slug>.md` before export. Otherwise the generated `assets/directory-data.json` can contain duplicate slugs and hash/full-page routing becomes ambiguous.

## Responsive expandable cards

When cards sit side-by-side in CSS Grid and use `<details>`, do not let closed neighbours stretch to match the opened card’s row height. The pattern is:

```css
.results-grid,
.time-group {
  align-items: start;
}
```

Also avoid desktop/tablet card rules like `min-height: 100%` on the expandable card. Verify by opening one card in a two-column viewport and measuring that the neighbour remains at its natural collapsed height.

## Dark-mode contrast audit for events

When the user says text is still hard to read, do not rely on visual intuition alone. Check for all of these:

- dangling or duplicate `[data-theme="dark"]` blocks near the end of `<style>`
- hardcoded light surfaces such as `background: rgba(255,250,242,...)` on cards/dock/drawer/empty states
- `a { color: inherit; }`, `color: #fff`, `color: rgba(...)`, and stale `--text` tokens
- secondary text (`--muted`, `--soft`) that is too dim on charcoal cards

Use browser computed styles to verify actual rendered values. For event cards in dark mode, acceptable target values are roughly:

- event title: near `#fff8ec` / `rgb(255,248,236)`
- description/body: near `#f2eadf` / `rgb(242,234,223)`
- notes/subline: near `#d1c2ad` / `rgb(209,194,173)`
- card surface: charcoal paper token near `#2a2520`

## Date badge styling (always-dark standard)

Event date badges (`month/day` chips on `<details>` cards) use a fixed dark-glass look **regardless of light/dark mode** — declared as a visual standard, not a theme toggle:

```css
.date-badge {
  color: #f3c85b;                        /* fixed acadian-yellow, not var() */
  background: rgba(10, 43, 87, 0.68);   /* fixed dark-blue glass, not var(--glass) */
  border: 1px solid var(--red);           /* red border stays token-driven for light/dark red */
  backdrop-filter: blur(20px) saturate(1.45);
  -webkit-backdrop-filter: blur(20px) saturate(1.45);
}
```

Using `var(--acadian-yellow)` and `var(--glass)` caused light-mode mismatches because those tokens shift between themes. Hard-coding `#f3c85b` and `rgba(10, 43, 87, 0.68)` keeps the badge consistent. The red `border` via `var(--red)` is the only theme-sensitive property (`#bf4a4f` light, `#ff7f86` dark).

## Events hero section (removed)

The "Community calendar" hero card (`<section class="hero">`) was removed from `events.html` — filter pills and event list are self-explanatory. Page structure is now: `<header>` → `<div class="filters">` → `<main id="events">`. `setText()` calls for removed hero IDs safely no-op (guard: `if (el) el.textContent = value`).

## Archiving placeholder events

To remove placeholder/test events from the active calendar without losing the record:

1. In `events-data.json`, set `"status": "archived"` and `"computed_status": "archived"` on the event object.
2. Update top-of-file counts: `active_count` decrements, `archived_count` increments, `event_count` stays the same.
3. The `isArchived()` function in `events.html` matches either field.
4. The "Upcoming" filter excludes archived events; the "Archive" filter shows them.
5. Archived events remain in the source JSON for admin/GitHub access.
6. **TODO: at scale, build a dedicated `archive.json` endpoint or API for systematic preservation queries.** Current approach (flagged status in main data) works for small datasets but will need a separate archive system as records grow.

## Marking events as placeholder/preview

`events.html` uses two functions to detect and mask placeholder events:

```js
function publicTitle(event) {
  return String(text(event.title) || event.name || '').replace(/\s+Placeholder\b/i, ' Preview');
}

function publicSummary(event) {
  const raw = String(text(event.summary) || copy().detailsSoon);
  return /placeholder|non-public/i.test(raw) ? copy().previewSummary : raw;
}
```

- If the word "Placeholder" appears in the title, it's replaced with "Preview".
- If the summary matches `/placeholder|non-public/i`, the entire summary is replaced with `copy().previewSummary` ("Preview listing while the public calendar format is being shaped.").
- To mark a real event as placeholder: seed the word "placeholder" into the summary text. The event data stays — only the public rendering changes.

## Style preference reinforced

For this user, readability is literal: dark text on offwhite in light mode, light text on charcoal in dark mode. Links must be explicit token colors in both modes; inherited link colors are not acceptable for public pages.
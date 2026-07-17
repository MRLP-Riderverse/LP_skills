# Homepage live carousel + home-feed pattern

Use this when the user wants Acadie.sol Home to behave like a calm launcher with one live progress surface.

## Pattern
- Keep Home to three stacked layers only:
  1. centered welcome/identity banner
  2. one action container
  3. one live container
- For the action container, default to a 2×2 grid when the user asks for “4 quick ways in.”
- For the live container, show only the newest 3 items and auto-cycle every 4 seconds.
- Clicking a live slide should open a dedicated archive page (`home-feed.html`), not expand Home into a long feed.

## Data sources
Prefer existing exported payloads over inventing a new feed source.
- `assets/directory-data.json`
- `assets/events-data.json`
- `assets/site-meta.json` for latest-source timestamp only when available

## Normalization rules
Merge entries/drafts/events into one common shape, then sort descending by source freshness.

Suggested fields:
- `type`: `draft` | `entry` | `event`
- `id`
- `anchorId`: stable fragment for Home-feed deep links
- `title`
- `summary`
- `href`: homepage slide target, usually `home-feed.html#activity-...`
- `detailHref`: destination page for the archive card CTA
- `badge`
- `statusLabel`
- `whenLabel` for events
- `category`
- `area`
- `source_modified_ts`

Use `source_modified_ts` when present; otherwise parse `source_modified_at`.

## Routing rules
- Homepage slide click → `home-feed.html#activity-...`
- Published entry CTA → `entry.html#<slug>`
- Event CTA → `events.html#event-<id>`
- Draft CTA can point to the directory quick-card hash when the record is not yet a full published entry.

## i18n rule that matters
Do **not** cache already-localized card content and then merely repaint the shell on `acadie:languagechange`.

Instead:
- reload/re-normalize from source JSON on language change, or
- store raw multilingual fields and derive localized strings during each render.

Otherwise the page chrome flips EN/FR while titles, summaries, badges, and status/context strings stay in the previous language until full reload.

## Resilience rule
`site-meta.json` is optional enhancement, not required truth.

Good behavior:
- hard-require `directory-data.json` and `events-data.json`
- soft-load `site-meta.json`
- if meta is missing, still render the live carousel/feed and fall back to the newest item timestamp or omit the “latest update” stamp

Bad behavior:
- throwing the whole Home/feed module into an empty state just because meta was unavailable

## Verification pattern
After edits:
1. `python3 -m http.server 8777`
2. run JS syntax checks across inline scripts
3. use headless Chrome DOM dumps to confirm rendered structures exist after runtime fetches:
   - homepage action grid
   - carousel slides
   - `home-feed.html` cards
   - entry + event anchors/links
4. capture screenshots for a quick mobile sanity pass if needed

Useful checks:
- `google-chrome --headless --dump-dom http://127.0.0.1:8777/index.html`
- `google-chrome --headless --dump-dom http://127.0.0.1:8777/home-feed.html`

Look for:
- exactly one live module on Home
- max 3 slides on Home
- archive page contains mixed event + entry items
- no null-element/runtime regressions from removed homepage IDs

## Implementation notes
- Guard DOM writes with small helpers (`setText`, `setHtml`, etc.) so homepage IA changes do not leave null-element errors behind.
- Localize accessibility strings too (for example carousel dot `aria-label`s).
- If the carousel binds hover/focus listeners on re-render, ensure listeners are attached only once.
- For Home, prefer the copy stance “launcher + progress signal,” not “full explainer + dashboard + feed.”

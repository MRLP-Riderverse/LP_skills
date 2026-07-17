# Public mobile site preview workflow — Acadie.sol

Use when the user wants to make the Acadie.sol public site viewable on mobile after a design/export pass, especially after sending mobile screenshots as steering.

## Intent

The user usually means the full public snapshot path, not only a local commit:

1. make the requested public/UI changes,
2. export directory payloads into the site repo,
3. commit/push whichever repos changed,
4. wait for GitHub Pages to build,
5. verify deployed URLs and browser-rendered mobile text/console.

The user may call this the **commit combo**.

## Two-repo sequence

- Source/data repo: `acadie_sol_directory`
- Public site repo: `acadie_sol`

Recommended order:

1. If source data changed, commit/push `acadie_sol_directory` first.
2. Run exporter from the source repo: `python3 scripts/export_to_site.py --all`.
3. In the site repo, include changed payload files such as:
   - `assets/directory-data.json`
   - `assets/events-data.json`
   - `assets/locations-data.json`
   - `assets/site-meta.json`
   - `assets/calendar/*.ics`
4. Commit/push the site repo.
5. Poll GitHub Pages until status is `built`.
6. Verify live routes with HTTP 200 and a headless mobile render pass.

## Mobile render verification

Use a local HTTP server or deployed URL; avoid `file://` for pages that fetch JSON because browser CORS will produce false failures.

Minimum checks:

- JS syntax: extract inline scripts and run `node --check`.
- Browser render: Puppeteer/Chrome at ~390×844 mobile viewport.
- Capture/inspect:
  - console warnings/errors
  - `h1`
  - first body text chunk
  - scroll height
- Verify deployed URLs:
  - `/`
  - `/directory.html`
  - `/events.html`
  - main JSON payloads

## Screenshot steering workaround

If direct `vision_analyze` on several uploaded screenshots times out:

1. Inspect images locally to confirm paths, dimensions, and sizes.
2. Build a compressed contact sheet or smaller thumbnails.
3. Run vision analysis once on the contact sheet with a concise, design-specific prompt.
4. Treat the resulting design direction as valid steering, but tell the user the first direct image calls timed out and the contact-sheet workaround succeeded.

This avoids falsely saying images were invisible when the files existed.

## Public UX corrections from June 2026 pass

- Home should feel like a warm local landing page, not a dashboard.
- Remove public submission/suggestion CTAs until the user explicitly wants them back.
- Collapse “discover / search / explore” into one public intent: **Find local places**.
- Avoid public admin/source-model language such as `placeholder`, `published`, `active`, `static layer`, `renderer`, or `source repo` in primary UI copy.
- If demo/placeholder events are made public for testing, soften their public rendering:
  - title: `... Event Preview`
  - summary: `Preview listing while the public calendar format is being shaped.`
- Event cards should look like community bulletin cards:
  - date badge
  - event title
  - time
  - host
  - location
  - short summary
  - add-to-calendar / view-host actions
- Related places must not duplicate. Pick **one** representation per page:
  - default for the events index: keep host/location as simple sub-info inside each event card plus `View host`; do **not** also render a bottom related-places panel.
  - only use a bottom `Related places` section when the page is primarily about a place/location cluster, not when event cards already show host/location context.
- If the user says the site is ugly/out of proportion, immediately tighten rather than defending the pass:
  - remove full-viewport hero/card treatments unless the user explicitly wants a splash page,
  - reduce heading, card, pill, badge, shadow, border-radius, and padding scales together,
  - avoid oversized novelty fonts for primary mobile headings,
  - verify that the first mobile viewport is calm and proportionate at ~390×844.

## Visual direction from user screenshots

- Dark charcoal base.
- Deep Acadian/navy blue rounded cards.
- Restrained gold/yellow accents for active/primary states.
- Mobile-first single column with visible pill navigation.
- Small uppercase section labels.
- Civic/community-board feel: local, practical, culturally grounded.
- Avoid sterile white app UI, over-polished marketplace language, or generic social-network framing.

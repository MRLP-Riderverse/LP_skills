# Homepage simplification and export verification notes

Use this when Acadie.sol Home starts feeling crowded or when directory/event widgets duplicate routes already present in the bottom dock.

## Product rule

If the bottom dock already owns the primary navigation route, avoid restating that same route as a large homepage widget.

Good Home shape:

- hero/poster surface
- one calm welcome/explanation card
- one forward-looking CTA or placeholder, such as calendar/gallery/community feature space
- persistent dock for Home / Events / Search / Menu

Avoid:

- a directory launch banner plus a dock Search/Directory route
- an event preview stack plus a dock Events route
- home-level JSON fetches for widgets that are only duplicating navigation
- multiple competing first-screen choices that make the page feel like a dashboard

## Minimal implementation pattern

- Remove the homepage `directory-banner` block when the dock Search item already routes to `directory.html`.
- Remove the homepage event preview list when the dock Events item already routes to `events.html`.
- Replace both with:
  - `.welcome-card` for purpose and tone
  - `.calendar-teaser` or equivalent low-pressure future-space CTA
- Keep bilingual copy in the same `HOME_COPY` structure.
- Use small DOM helpers for iterative pruning:

```js
function setText(id, value) { const el = document.getElementById(id); if (el) el.textContent = value; }
function setHtml(id, value) { const el = document.getElementById(id); if (el) el.innerHTML = value; }
```

This prevents `null.textContent` errors when removing old sections.

## Verification pattern

After editing `index.html`:

```bash
python3 -m http.server 8777
```

Then verify mechanically:

```bash
curl -fsS http://localhost:8777/index.html >/tmp/acadie_index.html
python3 - <<'PY'
from pathlib import Path
html=Path('/tmp/acadie_index.html').read_text()
checks={
  'directory banner removed':'directory-banner' not in html,
  'event preview removed':'event-preview-list' not in html,
  'welcome card exists':'welcome-card' in html,
  'calendar teaser exists':'calendar-teaser' in html,
  'no fetch on home':'fetch(' not in html,
}
for k,v in checks.items(): print(k, v)
if not all(checks.values()): raise SystemExit(1)
PY
```

If Puppeteer is available, also load mobile and check console/page errors:

```js
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({headless: 'new', executablePath: '/usr/bin/google-chrome', args: ['--no-sandbox']});
  const page = await browser.newPage();
  const messages=[];
  page.on('console', msg => messages.push(`${msg.type()}: ${msg.text()}`));
  page.on('pageerror', err => messages.push(`pageerror: ${err.message}`));
  await page.setViewport({width: 390, height: 844, deviceScaleFactor: 2, isMobile: true});
  await page.goto('http://localhost:8777/index.html', {waitUntil: 'networkidle0'});
  await page.screenshot({path: '/tmp/acadie_home_mobile.png', fullPage: true});
  const summary = await page.evaluate(() => ({
    hasWelcome: !!document.querySelector('.welcome-card'),
    hasCalendar: !!document.querySelector('.calendar-teaser'),
    hasDirectoryBanner: !!document.querySelector('.directory-banner'),
    hasEventList: !!document.querySelector('.event-preview-list'),
  }));
  console.log(JSON.stringify({summary, messages}, null, 2));
  await browser.close();
})();
```

## Export diff pitfall

`export_to_site.py --all` may rewrite `.ics` calendar files with timestamp-only changes. Those can trigger `git diff --check` trailing-whitespace warnings because ICS files use CRLF-style line endings.

If no event source data changed and the `.ics` files only churned from export timestamps, revert those generated calendar files before committing the site repo:

```bash
git checkout -- assets/calendar
```

Then commit the meaningful payload/design files.

## Live verification

After pushing the site repo, wait for the GitHub Pages run and verify both page and payload:

```bash
gh run list --limit 5 --json databaseId,status,conclusion,name,headSha,url
gh run watch <run-id> --exit-status
curl -L -H 'Cache-Control: no-cache' 'https://mrlp-riderverse.github.io/acadie.sol/?v=<sha>' -o /tmp/live.html
curl -L -H 'Cache-Control: no-cache' 'https://mrlp-riderverse.github.io/acadie.sol/assets/directory-data.json?v=<sha>' -o /tmp/live-directory.json
```

Verify the live HTML contains the new Home affordances and not the removed widgets; verify the live JSON has expected counts, no duplicate slugs, and no missing French summaries.


## Homepage layout tweaks (2026-06-21)

- **Community OS pill spacing**: Added `top: 12px` to `.welcome-label-pill` to create 12px of space between the pill and the global header, matching the stacked UI gap used elsewhere (e.g., `.phone-shell` gap).
- **Global header font size**: Reduced `.site-header` font size from `.82rem` to `.70rem` to ensure the header text (e.g., “## Entries - Vive l'Acadie! - ## Events”) fits comfortably within mobile viewports without wrapping or overflow.
- **Welcome card typography**:
  - Reduced `.welcome-title-prefix` font size from `.76rem` to `.68rem`.
  - Adjusted `.welcome-card h1` clamp range from `clamp(1.08rem, 5.8vw, 1.48rem)` to `clamp(0.94rem, 5.2vw, 1.28rem)`.
  - Removed underline, underline thickness, and underline offset from `.welcome-card h1`.
- **Section divider line**: Added a `.section-divider-line` (1px height, `--line` at 50% opacity, `margin: 6px 0 0`) below the ornament in the divider between the 2×2 action grid and the updates feed to provide a clear visual separation.

These changes were made to improve spacing, readability, and visual hierarchy on the homepage while maintaining low-friction, raw-preserving drafts and clear modular code.

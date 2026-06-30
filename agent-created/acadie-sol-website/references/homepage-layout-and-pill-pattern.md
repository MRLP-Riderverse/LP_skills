# Homepage Layout Patterns — June 2026

Session-captured patterns for the launcher-style homepage after the welcome-card + 2×2 grid + gallery + updates feed IA.

## Layout Order (top to bottom)

1. **Global header** — fixed, `font-family: monospace` (NOT pixel font), `.74rem` max
2. **Welcome card** (`surface`) — centered identity block, no underline on title
3. **"Community OS" pill** — straddles the *bottom* border of the welcome card (`position:absolute; bottom:0; left:50%; transform:translate(-50%,50%)`)
4. **Media gallery** — swipeable carousel, needs `margin-top:6px` on `.media-gallery-section` to clear the pill
5. **2×2 action grid** — 4 tiles (View Everyone, Events, Support, About Us)
6. **Section divider** — subtitle text + `✧❅✦❅✧` ornament + 1px divider line
7. **Updates feed** — top-10 recent items, "View Updates" pill top-right, relative timestamps stepping through `min / h / d / w`

## Pill Positioning

The "Community OS" / "Système Communautaire" pill uses:
```css
.welcome-label-pill {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translate(-50%, 50%);
  /* pill center sits exactly on the container's bottom border */
}
```

Dark mode keeps the pill styled with `--button-bg` / `--button-fg` / `--button-border`.

## Update-time Formatter

The updates feed must step through reasonable units instead of dumping huge hour counts:

```js
function relativeTimeBreakdown(minutes) {
  if (minutes < 60)  return { value: minutes, unit: 'min' };
  const hours = Math.round(minutes / 60);
  if (hours < 48)    return { value: hours, unit: 'h' };   // up to 2 days
  const days  = Math.round(hours / 24);
  if (days  < 14)    return { value: days,  unit: 'd' };   // up to 2 weeks
  const weeks = Math.round(days / 7);
  return { value: weeks, unit: 'w' };
}
```

Thresholds: **min → h (under 48h) → d (under 14d) → w**. Strings live in `HOME_COPY`:

| Unit | EN | FR |
|------|----|----|
| min  | `5 min ago`         | `Il y a 5 min` |
| h    | `3 h ago`           | `Il y a 3 h` |
| d    | `3 d ago`           | `Il y a 3 j` (jours) |
| w    | `4 w ago`           | `Il y a 4 sem` (semaines) |

The breakdown function is a regular function declaration living **outside** `HOME_COPY` (hoisted) so both `en.updatedAgo` and `fr.updatedAgo` can call it. `71h ago` becomes `3 d ago` / `Il y a 3 j`. Verify boundary rounding (`2880 min → 2 d`, `20160 min → 2 w`) before pushing.

## Header Layout Pitfalls

- **Do not split the header's `height` and `padding` to add 12px clearance.** An attempted fix using `height: auto; min-height: calc(30px + env(safe-area-inset-top)); padding: env(...) 0 12px; box-sizing: border-box` **loaded the home page offset/cropped**, especially in FR mode. Reverted via `git revert 2386995`. The working combination is the safe-area-aware `calc(30px + env(...))` header height + matching body padding-top.
- When the welcome card slips under the header on hard refresh, suspect paint-timing first. The body padding-top is the only thing keeping content below the fixed header before first paint. Mutating safe-area math mid-render is a likely culprit, not the CSS primitives.

## Key Lessons

- Pixel font (Pokemon GB) is too wide for constrained horizontal chrome like the global header. Use `monospace` instead.
- When a pill overflows a container's border, the grid gap doesn't account for the overflow — next siblings need explicit margin to avoid collision.
- Title underline was removed per user preference — cleaner look for the `⁜ Acadie.sol ⁜` wordmark.
- The `⁜` (U+205C, four asterisk) symbol is used both as the title flanking mark and as the About Us action-tile icon.

## FR Localization for Homepage

| Element | EN | FR |
|---|---|---|
| Label pill | Community OS | Système Communautaire |
| Title prefix | Welcome to | Bienvenue à |
| Title | ⁜ Acadie.sol ⁜ | ⁜ Acadie.sol ⁜ |
| Subtitle (on divider) | For Acadians, By Acadians. | Pour les Acadiens, par les Acadiens. |
| Update ago (just-now) | Updated just now | Mis à jour à l'instant |
| Update ago (min/h/d/w) | `5 min ago` / `3 h ago` / `3 d ago` / `4 w ago` | `Il y a 5 min` / `Il y a 3 h` / `Il y a 3 j` / `Il y a 4 sem` |

## Spacing Standards

- Global header height: `calc(30px + env(safe-area-inset-top))`
- Body padding-top: `calc(42px + env(safe-area-inset-top))` — header + 12px clearance
- Phone-shell grid gap: 12px
- Media gallery margin-top: 6px (pill clearance)

## Date Badge System (events.html) — June 2026

The calendar month/day chip on event cards has been moved *off* a hard red `var(--calendar-red-top)` background and onto the shared menu/overlay surface system. Result: dark mode reads clean; user noted "sick" — light mode still on-deck.

**Adopted treatment** (declared as a cross-theme standard — no light/dark toggle):

```css
.date-badge {
  background: var(--glass, rgba(10, 43, 87, 0.68));
  border: 1px solid var(--red);
  color: var(--acadian-yellow);
  backdrop-filter: blur(20px) saturate(1.45);
  -webkit-backdrop-filter: blur(20px) saturate(1.45);
  box-shadow: 0 14px 38px var(--shadow);
}
```

Rationale: matches the floating menu overlay (`var(--glass)` blue + backdrop blur), so calendar chips read as part of the same product surface instead of another red surface competing with `--red`. Yellow `--acadian-yellow` stays readable on the glass blue. The thin `--red` border keeps the calendar identity (calendar = red) without flooding the layout with red.

**Do not** bring back `--calendar-red-top` / `--calendar-red-bottom` as the chip background — too much red on the page. The tokens can stay defined for the day/calendar pill button if/when one is reintroduced, but the badge itself rides the glass system. Future tasks should treat the badge as a stable standard, not a toggle, and verify on the live build before any further tweaks.

## Verification Snippets

Inline Node test for the formatter boundaries:

```bash
node -e 'function r(m){if(m<60)return{v:m,u:"min"};const h=Math.round(m/60);if(h<48)return{v:h,u:"h"};const d=Math.round(h/24);if(d<14)return{v:d,u:"d"};return{v:Math.round(d/7),u:"w"}}console.log(r(71*60),r(20160),r(2880))'
```

Index.html script syntax check (since `node --check` doesn't accept `.html`):

```bash
awk '/<script>/,/<\\/script>/' index.html | sed 's|<script>||;s|</script>||' > /tmp/check.js && node --check /tmp/check.js
```

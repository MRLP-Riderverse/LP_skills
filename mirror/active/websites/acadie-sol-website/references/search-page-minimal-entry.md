# Search Page Minimal Entry Pattern

Session lesson: when the user asks for a dedicated Acadie.sol search surface, do not let it become a floating directory or branded landing page.

## Product intent
- Fresh `search.html` should be non-influential: no preloaded result cards, no empty-state card, no "try this" suggestions, no instructional paragraph.
- Prefer universal/minimal placeholder language. In this session, `?` was preferred over `Search`.
- Put operation controls above the input in flow order: `View All` / `Filters`, then the input.
- Keep filters hidden behind a compact `Filters` control until requested; visible tag/chip rows read as suggestions and can influence the user.
- Anchor the input low on mobile near the bottom dock/finger zone using `position: fixed` on a `.search-controls` wrapper, rather than flow-centering it like a hero landing page.
- Results should appear above the controls/input so the lower interaction zone stays stable when results populate.

## Visual treatment
- Avoid container-card vibes for the initial search state: no large card wrapper, no glass panel, no shadowed searchbar cage.
- Prefer a freed input line: transparent background, no border-radius, no top/side border, one subtle underline (`border-bottom`), focus changes underline color.
- Keep page background tied to the global token (`background: var(--page-bg)`) unless the user explicitly asks for a special surface. Do not add page-local gradients after a global color constant has been established.

## Font sizing
- Search input text should be compact (~50% of hero-sized defaults). Use `clamp(1rem, 3.4vw, 1.15rem)` — the floor is 16px to prevent iOS auto-zoom on focus. Font-weight ~700-750 keeps it purposeful without being loud.
- Button/pill text should be reduced ~10% from standard: `.79rem` with `font-weight: 900` for legibility at small sizes.
- Glyph (search icon) scales down proportionally: `1rem` at the reduced input size.

## Safari-style scroll chrome (auto-hide on scroll-down, restore on scroll-up)
- Wrap actions + input in a `.search-controls` container with `position: fixed; bottom: calc(86px + env(safe-area-inset-bottom))` (adjust bottom value so the controls sit just above the dock with a ~8px gap).
- On mobile (< 680px), move controls closer: `bottom: calc(92px + env(safe-area-inset-bottom))`.
- Use `will-change: transform, opacity` and `transition: transform .24s ease, opacity .2s ease` for smooth hide/show.
- Hidden state: `body.search-chrome-hidden .search-controls { opacity: 0; pointer-events: none; transform: translate(-50%, calc(100% + 110px)); }` — slides down behind the dock.
- JS scroll direction detection: track `lastScrollY`, on `scroll` (passive, rAF-throttled) compute delta. If `delta > 12` and `scrollY > 24`, add `search-chrome-hidden` class. If `delta < -12` or `scrollY <= 8`, remove it.
- Input `focus` always restores chrome (`setChromeHidden(false)`).
- If the filter `<details>` is open, do not hide chrome even on scroll-down.
- Main `.wrap` needs extra `padding-bottom` (~188px) so scroll content isn't occluded by the fixed controls.

### Key constants
| Context | Fixed bottom | Typical gap to dock top |
|---------|-------------|------------------------|
| Desktop default | `calc(86px + safe-area)` | ~14px |
| Mobile ≤680px | `calc(92px + safe-area)` | ~8px |

## Verification probes
- Fresh load: `document.querySelectorAll('.result-card').length === 0`.
- Fresh load: no `.empty` result state is visible.
- Fresh load: filters/chips are hidden until the filter control opens.
- Computed body background image should be `none` when relying on the global background token.
- Search input font size ≤ 16px on mobile viewport (confirms no iOS zoom trigger).
- Button/pill font size ~12.6px on mobile (confirms ~10% reduction).
- Scroll down after results: `document.body.classList.contains('search-chrome-hidden') === true`, controls opacity ~0.
- Scroll up: chrome restores, opacity 1.
- Input focus while hidden: chrome restores.
- Filter menu open while scrolling: chrome stays visible.
- Gap between controls bottom and dock top: 4–24px (no overlap, no dead space).

## Mobile keyboard / focus conflict (critical pitfall)

iOS/Android soft keyboards and `position: fixed` inputs create a vicious focus cycle
if you are not careful. The user reported "clicking the search input opens and closes
the keyboard before I have time to type anything" — this section documents the root
causes and fixes.

### Root causes
1. **Scroll-triggered blur on every scroll event.** A `window.addEventListener('scroll', () => { if (document.activeElement === input) input.blur(); })` fires immediately when the keyboard opens because the visual viewport resize triggers a scroll event. The blur closes the keyboard before the user can type.
2. **`visualViewport.scroll` listener.** Fires erratically on iOS when the keyboard opens/closes, calling `detectKeyboard()` which toggles `keyboard-open` class → layout transition → another scroll event → blur loop.
3. **Forced `input.focus()` after filter selection.** Selecting a filter chip programmatically focuses the input, which on mobile reopens the keyboard even though the user was just tapping a pill, not asking to type.
4. **Scroll-to-input on focus.** When `setChromeHidden(false)` triggers a layout shift (e.g., the search controls animating back to visible), the browser may scroll to keep the focused input in view. On mobile this creates a jarring page jump.

### Fixes
- **Remove `input.blur()` from the general scroll handler.** Only blur on deliberate downward scroll through results: `if (delta > 32 && document.activeElement?.id === 'search-input' && !focusGuard) input.blur()`.
- **Remove `visualViewport.scroll` listener.** Only listen to `visualViewport` `resize` for keyboard detection. The `scroll` event on visualViewport fires unreliably when the keyboard animates.
- **Debounce `detectKeyboard()`.** Use a `setTimeout` (80ms) to prevent rapid toggle flicker during the keyboard open/close animation.
- **Do not call `input.focus()` after filter chip selection.** The filter state change is enough; the user will tap the input themselves if they want to continue typing.
- **Use a `focusGuard` flag.** Set `focusGuard = true` on input `focus`, clear it after 150ms. This prevents the scroll-handler blur from firing in the window immediately after focus (when the keyboard animation triggers scroll events).
- **Enter key blur is safe.** `input.addEventListener('keydown', e => { if (e.key === 'Enter') input.blur(); })` is explicit user intent and does not conflict.

### Verification
- On mobile: tap the search input → keyboard opens and *stays open* for typing.
- Type a query → results appear.
- Scroll down through results → keyboard dismisses, chrome hides.
- Scroll up → chrome restores.
- Tap a filter chip → filter applies, keyboard does *not* reopen.
- Press Enter → keyboard dismisses.

## Pill-shaped search chrome visual treatment

The search-controls container should feel like a floating "flash card" / pill:

```css
.search-controls {
  position: fixed;
  z-index: 35;
  left: 50%;
  bottom: calc(98px + env(safe-area-inset-bottom));
  width: min(620px, calc(100vw - 28px));
  display: grid;
  gap: 8px;
  padding: 10px 12px 12px;
  background: var(--page-bg);
  border: 1px solid color-mix(in srgb, #000 32%, transparent);
  border-radius: 18px;
  box-shadow: 0 -6px 22px -4px var(--shadow);
  transform: translateX(-50%);
  transition: transform .24s ease, opacity .2s ease;
  will-change: transform, opacity;
}
```

Key properties:
- **`border-radius: 18px`** — fully rounded pill on all corners.
- **`border: 1px solid color-mix(in srgb, #000 32%, transparent)`** — very thin black border at 32% opacity. Subtle on light/dark modes.
- **`background: var(--page-bg)`** — matches page so results scroll behind it cleanly (parallax/layered feel).
- **`box-shadow`** — upward shadow to lift it above the scroll content.

## Filter menu positioning (above the pill, centered page-horizontal)

The filter options dropdown must appear **above** the search chrome pill, centered
relative to the viewport (not offset from the toggle button).

```css
.filter-menu[open] .chips {
  position: fixed;
  bottom: calc(140px + env(safe-area-inset-bottom));
  left: 50%;
  transform: translateX(-50%);
  width: min(390px, calc(100vw - 32px));
  z-index: 40;
  /* inherit visual treatment from base .chips */
}
```

Key properties:
- **`position: fixed`** — breaks out of the `<details>` flow context entirely.
- **`bottom`** — set so the chips sit ~16px above the search-controls top edge.
- **`left: 50%; transform: translateX(-50%)`** — true viewport center, not relative to the toggle button.
- **`z-index: 40`** — above the search-controls (z-index 35) and above the dock.

### Pitfall: inherited `top` leaks into fixed positioning
The base `.chips` class inherits `top: calc(100% + 8px)` from its absolute-positioned default.
When overriding to fixed positioning for the open state, you MUST add `top: auto` or the
inherited `top` will override `bottom` and push the chips below the viewport (below the dock).
This was the bug causing "filter options show below the dock."

## Result rendering preferences
- **Divider lines**, not container cards. Use `border-bottom: 1px solid color-mix(in srgb, var(--line) 55%, transparent)` on each result. Last result has no border.
- **Bottom-up order.** `.results` container uses `flex-direction: column-reverse` so the best/first result sits nearest the user's thumb (just above the search chrome).
- **No container wrapping.** No card borders, no rounded boxes, no background on individual results.

## Keyboard open/close: dock hiding and chrome repositioning

When the soft keyboard is open:
- The dock should slide away (hidden below keyboard), NOT stack above the keyboard.
- The search chrome should reposition to sit just above the keyboard.
- Detect keyboard via `visualViewport` resize (debounced 80ms): if `vv.height < window.innerHeight - 80`, add `keyboard-open` class.
- CSS:
  ```css
  body.keyboard-open .site-dock {
    transform: translateX(-50%) translateY(200px);
    opacity: 0;
    pointer-events: none;
    transition: transform .22s ease, opacity .18s ease;
  }
  body.keyboard-open .search-controls {
    bottom: calc(14px + env(safe-area-inset-bottom));
  }
  ```
- When keyboard closes, restore `setChromeHidden(false)` so controls reappear.

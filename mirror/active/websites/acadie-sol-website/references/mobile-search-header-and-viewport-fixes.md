# Mobile search header and viewport fixes

Session note: the directory search surface still had two recurring issues on touch devices:

1. **Residual top dead space above search**
   - Tightened the `body-search` / `control-panel` spacing instead of only shrinking inner controls.
   - If pills sit above the search box, reduce the outer section margin first; inner padding changes alone can leave a visible gap.

2. **iOS auto-zoom cascading into dock/layout jitter**
   - Keep search inputs/selects at `font-size: 16px` minimum on mobile.
   - `-webkit-text-size-adjust: 100%` belongs on `html`, but it does not replace the 16px control threshold.
   - The zoom side effect can reflow the fixed dock and make its position look broken until the user zooms out again.

3. **Desktop header chrome leaking onto iPad/touch**
   - If top-right nav controls are no longer part of the product surface, remove the DOM/CSS/JS entirely instead of just hiding them. Hiding is fine for temporary responsive states, but obsolete chrome should not keep dead handlers or reappear in tablet layouts.
   - If the controls still belong on desktop only, prefer a touch-pointer media query (`@media (hover: none) and (pointer: coarse)`) over a width-only rule.
   - The fastest verification is to search the rendered DOM for the old IDs/classes after load; if they still exist, the page still carries stale chrome.

4. **Full-page links inside expandable cards**
   - When a card summary already owns the collapse/expand interaction, make the full-page link a top-level navigation target (`target="_top"`) so the destination page does not inherit nested shell state.

5. **PWA launch looks horizontally offset until pinch/zoom**
   - Measure, do not guess: compare `innerWidth`, `document.documentElement.clientWidth`, and `document.documentElement.scrollWidth` under mobile emulation. A larger `innerWidth`/`scrollWidth` than the emulated device width indicates document overflow, not a safe-area or viewport-meta problem.
   - CSS Grid children default to `min-width: auto`; a carousel track or a no-wrap feed line can therefore enlarge a `width: min(430px, 100vw)` phone shell beyond the actual viewport. Add `.phone-shell > * { min-width: 0; }` so grid children may shrink.
   - `overflow: hidden`/ellipsis does not reliably constrain a plain inline `<span>`. Give no-wrap feed descriptions a block formatting context (`display: block`) inside a `min-width: 0` flex child.
   - Verify at 320, 375, 390, and 430px: `innerWidth === clientWidth === scrollWidth`, `scrollX === 0`, and the shell/dock bounds stay within the viewport. This directly reproduces the launch condition that otherwise appears to “fix itself” after a pinch.
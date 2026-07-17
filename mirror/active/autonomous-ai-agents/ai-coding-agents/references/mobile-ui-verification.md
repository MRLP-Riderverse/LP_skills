# Mobile UI verification loop

Use this when a static site change affects intent routing, responsive controls, or dock positioning.

## Checklist

1. Test at a phone viewport first, not desktop.
2. Verify the main surface is *consistently visible* across states. Avoid UX where a key control sometimes appears and sometimes disappears unless that is the explicit product intent.
3. Prefer one deterministic intent switch over nested collapsibles.
   - Example: `browse` vs `search` can be hash-based states.
   - A "View all" action should usually clear query state and switch intent in place, not route through an extra page or hidden subpanel.
4. Inspect control geometry.
   - Search/action pills should fit in a compact grid, not a single stacked column on narrow screens.
   - If buttons are wrapping awkwardly, reduce labels or increase the grid column count before adding more UI chrome.
5. Check dock clearance.
   - Confirm the dock top stays below the last interactive content on the viewport.
   - If the dock drifts or becomes clipped, simplify the surrounding layout before adding more offsets.
6. Trim redundant metadata.
   - If the expanded card already shows the full official address/location, avoid repeating the same city tag in the collapsed summary.
7. Verify the actual DOM state after interaction, not just the visual screenshot.
   - Read element visibility, grid columns, and bounding rects from the live page.

## Good signals to log

- Which state was open initially
- Whether query reset happened in place
- How many results/cards rendered
- Whether action buttons wrapped cleanly
- Dock top/bottom vs viewport height

## Example verification questions

- Is the search surface visible in both `#browse` and `#search`?
- Does "View all" preserve the page and just clear search state?
- Do buttons fit as a compact grid on iPhone-width screens?
- Is the dock still above the viewport bottom without covering content?

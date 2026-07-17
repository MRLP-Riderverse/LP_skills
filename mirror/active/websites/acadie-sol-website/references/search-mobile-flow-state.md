# Search mobile flow state — Acadie.sol

Use this when the bottom-fixed `search.html` chrome behaves correctly at first, but regresses during editing transitions on iPhone/Safari.

## Durable lessons
- Do **not** model the active search layout only as `query !== ''` or `filter !== 'all'`.
- Split state into:
  - **idle state**: unfocused, empty query, no active filter; input can sit low near the dock.
  - **search flow / active state**: user is editing, has a query, or has a non-default filter; results area should be top-anchored below the fixed chrome.
  - **keyboard-open state**: soft keyboard visible; the dock may duck away, but the search chrome should stay in its normal lane.
- Focused editing should keep the page in active/top-anchored layout **even when the query is temporarily empty** or yields **zero/one results**. Otherwise the surface drops back to the idle position mid-edit, which feels broken.

## Reliable pattern
1. Add a focus marker class such as `search-input-focused` on input focus and remove it on blur.
2. Compute active search flow from more than query text alone, e.g. query present OR non-default filter OR input focused.
3. Use that state to drive layout classes (`search-active`) so:
   - `.search-hero` switches from low/thumb-zone alignment to top alignment
   - `.results` gets a stable top reading line / min-height for empty and sparse states
4. If scroll-hide is used for the bottom search chrome, keyboard-open + focused input must override it.
5. Keyboard detection should use `visualViewport.resize` only, debounced. Avoid `visualViewport.scroll` for keyboard logic on iOS.

## Symptoms this fixes
- Clearing the query causes the input bar to sink back toward the dock while the user is still typing.
- A zero-result state (`No matches`) appears to re-center or collapse the surface.
- A single result appears too close to the search bar because the page has partially fallen back to idle layout.
- Tapping back into the input after scrolling results brings the keyboard back but leaves the bar visually hidden or too low.

## CSS/JS direction
- Prefer normal top-down result flow, not bottom-up `column-reverse`, once the page is in active search mode.
- Give `.results` a small `min-height` in active/focused state so empty/sparse states still occupy a stable reading zone.
- Guard the hide/show controller (`setChromeHidden`) so it refuses to hide the search chrome while the input is focused.

## Verification recipe
- Focus empty input on mobile width: page should enter active/top-anchored layout.
- Type nonsense string: empty state should stay top-anchored.
- Reduce a query from many results to one result: the bar should stay pinned above keyboard/dock and the card should remain in the active reading lane.
- Clear the query while still focused: layout should stay active until blur.
- Blur with empty query: only then may the page return to the low idle state.

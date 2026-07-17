# Horizontal full-viewport deck QA

Use this checklist for mobile interfaces where the document is viewport-contained and major sections scroll horizontally.

## Structural assertions
- Count direct deck children; all intended sections should render and remain semantic.
- Assert each mobile panel width is approximately `innerWidth`.
- Assert total deck `scrollWidth` matches panel count × viewport width, allowing for intentional gaps.
- Assert `scroll-snap-type:x mandatory` and appropriate panel snap alignment.
- Search for stale nested-carousel controls, timers, hidden slides, and autoplay listeners after a carousel-to-sections refactor.

## Navigation assertions
Test both paths separately:

1. Tap/click each position indicator and verify the resulting `scrollLeft` lands on the corresponding panel.
2. Set or naturally change the deck's scroll position without activating a dot, wait for the scroll handler, and verify the active indicator updates from geometry.

A click test alone does not prove swipe-driven indicator synchronization.

For accessibility, verify:
- exactly one indicator has `aria-current="true"`;
- all indicators have localized labels and valid `aria-controls` targets;
- visible dots can remain small, but their button hit targets are materially larger and stable;
- selection styling changes a pseudo-element rather than changing button width and shifting the row.

## Short-viewport reachability
When document scrolling is disabled, do not treat `scrollHeight > clientHeight` as an automatic failure. The correct invariant is **reachable content**:

1. Detect whether each panel needs vertical scrolling.
2. If it does, require computed `overflow-y` to be `auto` or `scroll`.
3. Set `scrollTop = scrollHeight`.
4. Verify the final meaningful action/CTA lies within the panel's bounding rectangle.

Include short landscape phones (`667×375`, `844×390`) in addition to compact portrait (`320×568`). Landscape often exposes clipping that portrait-only sweeps miss.

Avoid `touch-action:pan-x` on an ancestor when child panels may need vertical scrolling.

## Flat-surface theme assertions
For borderless/backgroundless designs, inspect computed styles in both light and dark modes:

- panel border width is `0px`;
- panel background is transparent;
- panel box shadow is `none`;
- text/action colors resolve from theme tokens rather than stale fixed carousel colors.

Also verify document-level overflow and collect console exceptions during every viewport/theme pass.

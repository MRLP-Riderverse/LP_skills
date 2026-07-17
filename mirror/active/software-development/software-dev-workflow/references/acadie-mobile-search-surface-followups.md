# Acadie.sol mobile search surface follow-ups

Captured from the directory/search pass.

## Reusable fixes
- On mobile search inputs, pressing `Enter` should both trigger search and blur the input so the virtual keyboard dismisses and results are visible.
- `View full page` links work better as a right-aligned inline block (`display: block; width: fit-content; margin-left: auto; text-align: right;`) than as a left-aligned inline chip.
- If a closed drawer/modal still intercepts clicks, `opacity: 0` is not enough. Add `visibility: hidden` as well, and restore both only when open.

## Overlay placement
- A fixed filter/modal overlay should live outside any clipping/stacking parent that can distort hit-testing or positioning.
- If an overlay appears as a weird block over the search area instead of covering the page, check DOM nesting first before changing z-index.

## Verification pattern
- Use a browser automation probe to assert:
  - overlay opens as fixed full-screen
  - second click toggles it closed
  - Enter blurs the search field
  - the page link target is not stolen by invisible chrome

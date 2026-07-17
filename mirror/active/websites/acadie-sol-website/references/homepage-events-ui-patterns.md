# Homepage + Events UI patterns (Acadie.sol)

Use these when the user wants the homepage and events pages to feel more like a product surface and less like a stack of equal-weight containers.

## Homepage CTA differentiation
- If "Explore Directory" should stand apart from the rest of the homepage, convert the CTA zone into a clickable banner / launch strip rather than a standard paper card.
- Reliable ingredients:
  - stronger gradient or color-block treatment than nearby containers
  - marquee or utility band above the CTA when the user explicitly asks for a moving/banner feel
  - full-row click target
  - dedicated inner border/highlight so it reads as an intentional gateway
- Keep text short: title + one-line count/subtitle.

## Hero/banner ratio adjustment
- If the user says the hero feels too tall or poster-like, first try a height reduction of ~25%.
- This usually changes the perceived ratio from poster to panorama without forcing a content rewrite.
- Verify that the lower homepage modules move up enough to improve first-screen scanability.

## Homepage event preview behavior
- Show up to 6 items in the preview zone unless the user asks for a stricter cap.
- Sort by nearest relevant start time for the user-facing list.
- If an event is already started but not expired, keep it visible and label it as live/ending soon rather than dropping it.
- A compact right-side status pill works well for:
  - `Starts in 6h`
  - `Starts in 3d`
  - `Live · ends in 2h`

## Events page browse pattern
- If the user wants more options visible by default but still wants actions/details available, use `<details>/<summary>` quick cards.
- Summary should hold:
  - date badge
  - title
  - short metadata line
  - short teaser
  - chevron affordance
- Expanded body should hold:
  - full description
  - practical notes (`bring`, `wayfinding`, etc.)
  - add-to-calendar
  - host/full-page links

## Deep-link behavior for event cards
- If homepage previews or other pages link into `events.html#event-...`, add hash-open logic so the matching `<details>` card opens automatically on load and on `hashchange`.
- This preserves the light browse experience without losing direct navigation.

## Calendar chip theming
- Use shared tokens for month/day badges across `index.html`, `events.html`, `entry.html`, and any other page that renders mini calendar chips.
- When the badge is meant to function as a brand cue, keep the chip colors stable across light and dark mode instead of recoloring per theme.
- Current proven palette from this pass:
  - top red: `#bf4a4f`
  - bottom red: `#7b1f2a`
  - ink/gold: `#f3c85b`

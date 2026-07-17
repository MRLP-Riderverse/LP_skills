# Acadie.sol mobile OS surface pattern

Session-derived guidance for static/mobile community UI work when the user says the site feels too much like a dashboard or asks to mirror a visual mockup.

## Core framing

- Think like an operating-system/product interaction designer, not a website stylist.
- Rework shape and state first: launch surface, search state, drawer/menu state, events/list state.
- Palette changes alone are insufficient; “light mode” without new hierarchy will still feel wrong.

## What to build toward

- **Home:** compact mobile launch surface, not a landing-page hero. Use a visual poster/window placeholder, one primary search launcher, 1–2 quick cards, and a small “next up” widget.
- **Search/directory:** app-like search state. Input near top, filters as secondary controls, results as visual rows/cards with placeholder thumbnails/initials. Avoid forcing users to choose between discover/search/explore.
- Drawer/menu: real navigational state with rounded paper panel, grouped destinations, and a single clear close affordance. If another overlay exists (filters, popovers, tool trays), it should close when the drawer opens unless concurrent overlays are intentional.
- **Events:** compact calendar surface inside the same shell language. Avoid duplicate related-place surfaces; keep one relationship representation only.
- **Bottom dock:** useful for mobile orientation, but keep it compact and system-like.

## Visual direction

- Warm cream/paper background, warm ink text, deep Acadian blue for primary actions, restrained gold/red accents.
- Rounded mobile surfaces and soft shadows, but not oversized cards.
- Empty imagery/placeholders are acceptable while structure is being tested.
- Keep type smaller and quieter than a marketing landing page.

## Review workflow

- If the user sends screenshots/mockups, analyze the attached photo only when needed.
- When sending generated screenshots back to Telegram, send media files directly; do not vision-analyze your own screenshots first unless asked.
- For commit/push, respect explicit approval/“commit combo” preference.

## Anti-patterns

- Dashboard vibes: stat pills, admin/system labels, giant hero blocks, too many nav buttons, duplicate related sections, `published/active/placeholder` wording.
- Website vibes: decorative landing-page copy before the main action, separate discover/search/explore modes, large menus that do not represent actual states.

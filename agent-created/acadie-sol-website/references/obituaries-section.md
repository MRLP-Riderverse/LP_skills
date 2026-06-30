# Obituaries / remembrance section pattern

Use this when adding a discreet remembrance page or a small utility link inside the Acadie.sol menu.

## Intent
- Keep the feature subtle, easy to find when needed, and absent from the homepage/dock.
- Treat the page as a quiet index of existing local obituary resources, not a content-heavy feature.

## UI pattern
- Menu entry should be icon-only when space/sensitivity calls for it.
- Place the icon near the language/theme controls in the floating menu so it stays accessible but low-visibility.
- Prefer a cross-style icon over a tombstone when the goal is gentle, understated access.
- Avoid adjacent visible text for the icon button unless the user explicitly asks for a label.

## Page copy pattern
- Use comforting bilingual framing:
  - EN: "Lost but not forgotten"
  - FR: "On se souvient"
- Keep the supporting text short, friendly, and calm.
- Avoid dense metadata or administrative clutter on the public page.

## Link list pattern
- Show the organization name only as the clickable link label.
- Do not surface long URLs or extra fields unless they materially help the visitor.
- First example source used in-session: Elhatton → https://www.elhatton.com

## Implementation notes
- Keep the internal/admin label simple for recall (e.g. "obituaries"), even if the public title is softer.
- Maintain the site’s existing theme/drawer language and mobile dock rhythm; the page should feel like part of the same system.
- Verify on mobile after push, because subtle menu placement and icon spacing are easy to miss on desktop.

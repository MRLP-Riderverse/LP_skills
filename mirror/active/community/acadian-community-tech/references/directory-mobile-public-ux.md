# Directory mobile public UX notes

Session lesson from the `acadie.sol` public directory display mockup.

## What worked
- Public browse cards are a better public-facing surface than a purely internal-looking A–Z filing cabinet.
- Mood/route concepts are useful: Hungry, Waterfront, Family-friendly, Night out.
- Draft previews can stay honest with compact preview badges.

## What needed correction
- On mobile, large hero blocks, large status panels, and full-width mood cards made the page feel too big and attention-heavy.
- Mood options should not dominate the top of the page. Keep them as compact filters, preferably a dropdown.
- Category chips and quick-filter chips become overwhelming as the directory grows. Prefer dropdown controls on mobile.
- A top card browse plus a bottom A–Z index duplicates the same content. Use one listing display and let sorting/filtering change how it is explored.

## Preferred v2 pattern
- Compact hero: short title, short lede, small stats pills.
- First impression should ask **“So what are you looking for?”** rather than dumping every entry by default.
- Make **Show all** an opt-in secondary action; all-entry browsing is useful, but should not be the default mobile landing state.
- One control strip: search + Mood/route dropdown + Category dropdown + City dropdown. Avoid a separate Quick filter dropdown unless the user specifically asks for it; it can feel vague/noisy.
- City filters should show **city-level public labels only**. Normalize Bathurst variants (`Bathurst`, `East Acadie-Bathurst`, etc.) to the official public label `Acadie-Bathurst`, sorted under A.
- One listing display: compact/collapsible cards, mobile-first spacing, with URLs tucked inside expanded details/sources.
- Sorting controls can include A–Z and Category without rendering a second index.
- Preserve `assets/directory-data.json` and the directory repo export flow; this is a renderer concern, not a source-of-truth/schema concern.

## Pitfall
Do not turn every discovery idea into a visible top-level section. Discovery concepts are valuable, but on mobile they should usually become filter affordances rather than big content blocks.

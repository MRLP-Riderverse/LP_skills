# Homepage signal surfaces and low-maintenance community invitations

Use this reference when refining the Acadie.sol homepage, especially LIVE/featured content, recent additions, community invitations, or project-log placement.

## Product hierarchy

1. **Public artifacts first** — visitors should immediately find entries, events, photos, and other preserved community material.
2. **Current signal second** — a LIVE/featured surface may highlight something worth attention, but it needs a calm inactive state rather than stale promotional copy.
3. **Conversation third** — social participation should feel discoverable, not pushed. Use a quiet footer path plus an optional delayed, user-opened affordance.
4. **Operations elsewhere** — project logs and realtime addition feeds belong beside directory/search data, not as a primary homepage card.

## Maintenance defaults

- Prefer **Recently added** over manually curated **Featured** when the content manifest has reliable publication timestamps.
- Select the newest public item deterministically from the manifest; do not duplicate album titles, URLs, summaries, or image metadata in homepage code.
- Keep a localized inactive payload such as **Check again soon** for periods with no LIVE/featured notice.
- Public counts can be useful context, but integrate them into the homepage composition rather than forcing them into persistent global chrome.
- Empty metadata such as location should disappear completely, not leave punctuation or placeholder gaps.

## Carousel contract

For a two-signal carousel:

- Use five seconds as the current comfortable Home baseline unless the user requests another timing; three seconds felt rushed in live review. Keep slide text short enough to read within the interval.
- Loop explicitly and verify a full advance plus return using a real browser clock.
- Include a persistent pause/play control.
- Manual slide selection should set a persistent paused state; pointer/focus leave must not silently restart it.
- Honor `prefers-reduced-motion` by starting paused while still allowing the user to opt into playback.
- Pause while the document is hidden.
- Use ordinary labeled buttons with `aria-controls` and `aria-pressed` unless implementing the complete tab pattern (`tabpanel`, roving tabindex, and arrow keys).

## Delayed community affordance

- Before reveal, remove the control from layout, keyboard order, and the accessibility tree (`hidden`, plus an explicit author-level `[hidden] { display: none; }` rule when the base class sets `display`).
- At reveal time, remove `hidden`, then add the animation class on the next frame.
- First activation should reveal explanatory copy such as **Come chat with us here**; navigation should remain an explicit second action.
- Keep a static Community link in the footer so the delayed affordance is never the only route.
- Position the mobile affordance above the fixed dock and safe-area inset.

## Review checks

- Verify global shell text is not duplicating homepage counts.
- Verify all visible text and region/control `aria-label` values in English and French.
- Test inactive LIVE data, failed data fetch fallback, recent-manifest hydration, autoplay loop, persistent pause/resume, reduced motion, pre-reveal keyboard invisibility, and post-reveal interaction.
- Sweep mobile/tablet/desktop widths and check fixed-dock clearance.

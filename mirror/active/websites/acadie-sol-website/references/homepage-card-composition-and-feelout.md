# Homepage Card Composition and Feel-Out

## Purpose

Session-specific guidance for iterative Acadie.sol homepage card composition. Use this reference when the user is tuning a visual arrangement by feel rather than requesting a structural redesign.

## Composition method

1. Convert the user's card description into an ordered DOM checklist before editing.
2. Keep the order in markup whenever possible. Do not depend on CSS `order`, grid placement, or post-render text replacement to communicate the intended reading sequence.
3. Preserve semantic distinctions in live data. A casual wording like “entries and entries” is usually a slip when the page has separate directory and event counts; retain `entries` / `events` unless the user explicitly confirms otherwise.
4. Use existing ornaments and typography instead of adding explanatory copy. For this homepage, the useful visual vocabulary is the Pokémon GB font for short identity/title labels, the `✧❅✦❅✧` divider, restrained rounded media, and artifact-first composition.

## Spacing method

- When the user says a prompt needs the same treatment as an adjacent metadata block, match the block's breathing room rather than copying its entire border or background treatment.
- A small `margin-top` plus `padding-top` is often enough to separate a question/prompt from the divider above it while keeping the card mostly static.
- For QR/share cards, increase the gap between the QR, the primary share action, and the secondary community action before adding copy. Keep the primary action as a real button with an explicit label; an icon can remain supplemental (`↗`) rather than replacing the text.

## Verification contract

At minimum, run a local server and a Puppeteer probe at `390×844` and a desktop viewport. Assert:

- The ordered child classes/IDs in the primary card match the requested reading order.
- The GIF/image has non-zero `naturalWidth`/`naturalHeight`.
- QR rendered size matches the intended change.
- The share button's final text after localization/rendering is correct.
- The intended title uses the expected computed font family.
- Card count and document overflow are intentional.
- `pageerror` remains empty.

After pushing, use a cache-busting live URL and verify the same marker/asset. HTML deployment is not enough for binary media: confirm HTTP `200`, MIME type, and browser natural dimensions. Candidate media may be ignored by `.gitignore`; check with `git check-ignore -v` and force-stage only the explicitly approved asset when needed.

## Pitfalls

- Swapping visible text in the source is insufficient if a language renderer later overwrites it; update the copy table and static DOM together.
- Removing a heading can leave stale `aria-labelledby` references; replace them with a valid `aria-label` or a surviving ID.
- Removing a card requires removing its dot, label assignment, and any `dots[n]` JavaScript access as one change.
- A successful Pages workflow does not prove a GIF deployed. Verify the asset URL separately.

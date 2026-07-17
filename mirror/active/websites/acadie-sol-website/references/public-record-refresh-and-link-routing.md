# Acadie.sol public record refresh + link routing notes

Session-derived notes for filling missing public entities and keeping their routes sane.

## Public record refresh pattern
- If a user says an entry/event is missing, search past sessions first for the earlier provenance before reconstructing it.
- Prefer public-source-only details in the source repo: name, public address, public phone, public email, public website, and related public entities.
- If the public business/event needs a route target, create the matching source record first, then export the site payloads.
- When a venue is both a business and an event hub, keep a reusable location record separate from the business entry so future events can point at the shared place without duplicating narrative text.

## Verification pattern
- After export, verify the generated payload chain in the website repo, not just the source files.
- Check the relevant `assets/*.json` outputs plus any generated calendar artifact when the event timing changed.
- Treat timestamp-only `.ics` churn as noise; normalize line endings if `git diff --check` complains, and only keep the file when event fields changed.

## Link routing
- Full-page entry links should open the top-level page route directly.
- If a full-page link lives inside a nested expandable card or shell that can intercept navigation, prefer `target="_top"` plus a normal top-level href so the page opens cleanly.
- If a card already has a summary/quick-view layer, keep the collapsed summary link lightweight and avoid button-heavy chrome inside the expansion body.

## Related public record example
- Bathurst Hospitality Days: public business/event hub at 100 Main St, Bathurst.
- After Block Party 2026: La Louga event record on 2026-07-31 at 10 PM Atlantic, routed through the shared La Louga Main Street location.

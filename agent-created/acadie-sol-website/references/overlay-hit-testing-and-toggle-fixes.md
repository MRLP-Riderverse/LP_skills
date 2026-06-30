# Overlay hit-testing and toggle fixes

## Symptom
- A page-local link seems to open a global drawer or side panel route instead of following its own href.
- A fixed overlay looks closed but still steals taps/clicks.
- A modal appears visually on top, but its hitbox is actually clipped or nested inside a smaller parent region.

## Root causes
- Hidden fixed layers still participate in hit-testing when they only use `opacity: 0` and `pointer-events: none` inconsistently across descendants.
- A drawer or modal can remain in the DOM at full viewport size even when visually closed.
- A nested overlay inside a clipped container may render as a weird block or fail to cover the intended content layer.

## Fix pattern
- For closed overlays, set both `visibility: hidden` and `pointer-events: none` in addition to `opacity: 0`.
- Turn visibility back on only when the control is actually open.
- If an overlay is meant to cover the results area, move it outside the clipped search panel and make it `position: fixed; inset: 0`.
- Use a real toggle handler for the open control: if the overlay is open, close it; otherwise open it.
- Verify the fix by checking both click behavior and `elementFromPoint(...)`/hit-test output, not just screenshots.

## Useful verification
- In Puppeteer/Chrome, inspect the element under the tap point with `document.elementFromPoint(...)`.
- Check the clicked link by opening the target page in headless Chrome and confirming `page.url()` after the click.
- Compare the overlay's computed `visibility`, `opacity`, and `pointer-events` when open vs. closed.

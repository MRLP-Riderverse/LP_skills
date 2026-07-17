# Headless Chrome + CDP fallback for QA

Use this when the browser stack is unavailable, but you still need live geometry/DOM verification on a local site.

## Minimal setup
- Start a headless Chrome with remote debugging.
- Attach over the DevTools Protocol websocket.
- Navigate to the local page and wait for `Page.loadEventFired`.
- Use `Runtime.evaluate` to inspect DOM state and `getBoundingClientRect()`.

## Useful checks
- Compare the same element across pages:
  - dock/header/footer `getBoundingClientRect()`
  - `position: fixed` chrome stays identical across routes
- Verify clickable target routing separately from layout:
  - inspect `href` values directly
  - count matching anchors
  - if a user reports the wrong page opens, check for overlap or mis-targeting before changing URLs

## Example evaluation payload
```js
(() => {
  const el = document.querySelector('.site-dock');
  const r = el?.getBoundingClientRect();
  return r && {left:r.left, right:r.right, top:r.top, bottom:r.bottom, width:r.width, height:r.height};
})()
```

## Notes
- Prefer this for reproducible local QA when screenshots alone are ambiguous.
- Keep the checks page-agnostic so you can compare multiple routes with the same probe.
# HiAnime Next Episode Remote-Control Pattern

## Context

The user watches HiAnime in an already-open Firefox tab and may stream that desktop/browser to Discord while watching from another device. The desired action is one focused accessibility shortcut: advance the existing prepared HiAnime tab to the next episode without touching the user's mouse, keyboard, clipboard, URL bar, or tab model.

Task-specific artifact:

- `/home/midnight/.hermes/skills/productivity/next-anime-episode/SKILL.md`
- `/home/midnight/.hermes/skills/productivity/next-anime-episode/scripts/next-anime-episode.sh`

## Strong User Corrections

If the page exposes the target button/class, do not reason from screenshots or try to steer the mouse. The user expects selector/protocol/DOM/accessibility control.

Rejected approaches for this class:

- screenshots/vision when selector is known
- coordinate clicks or pointer-window inference
- URL-bar typing/pasting or bookmarklet-style address-bar control
- `firefox --new-tab` / new-window fallbacks
- site/browser keyboard shortcuts unless explicitly approved
- Ctrl-W/tab-close/window-close as “undo” or cleanup
- killing/restarting Firefox to recover automation state unless explicitly approved
- claiming success from script stdout without live browser proof

For streaming media, a new-tab fallback is actively harmful: it can leave the old playing tab with audio and create a new static tab. Closing/restarting the browser is also actively harmful because it destroys the prepared source stream/session. Same-tab control or fail loudly.

## What Failed

- Coordinate-clicking was unreliable because HiAnime's `Prev`, `Next`, and source controls are close together.
- Terminal/overlay focus and live user input made pointer/window diagnostics misleading.
- Screenshots/vision added latency and did not provide a robust action primitive.
- URL-bar manipulation failed in practice and interfered with the user's active browser/session.
- Sessionstore/CLI URL opening created duplicate tabs and stale selected-tab confusion.
- Ctrl-W/tab-close as an attempted undo closed/disrupted the browser instead of safely repairing state; never use close/restart cleanup without explicit approval.
- Site keyboard shortcuts (`n`, ArrowRight) are focus-dependent and may do nothing when focus is in the player, chrome, terminal, or desktop; do not treat them as reliable automation.
- A leaked WebDriver BiDi session caused `Maximum number of active sessions`; always call `session.end`. If the browser reports `session.status` as `ready:false` / `Session already started` but the client is gone, do not restart Firefox unless the user approves.

## Durable Pattern: Firefox WebDriver BiDi Same-Tab Control

Start Firefox with remote debugging before watching:

```bash
firefox --remote-debugging-port 9222
```

Firefox's remote endpoint here is WebDriver BiDi, not Chrome CDP `/json/list`:

```text
ws://127.0.0.1:9222/session
```

Use `websocket-client` with `suppress_origin=True`.

Protocol sequence:

1. Open WebSocket to `ws://127.0.0.1:9222/session`.
2. `session.new` with empty capabilities.
3. `browsingContext.getTree` and choose the existing context whose URL matches `https://hianime.ms/watch-*`.
4. `script.evaluate` in that exact context.
5. Inside the page, find `a.btn-ep-nav.btn-ep-nav--next`.
6. Dispatch/click the anchor. If site JS swallows the click, do same-context `location.assign(href)`.
7. Poll `browsingContext.getTree` or evaluate `document.title` for live proof.
8. `session.end` before closing the WebSocket.

Core page action:

```js
(() => {
  const el = document.querySelector('a.btn-ep-nav.btn-ep-nav--next');
  if (!el) return {ok:false, error:'selector not found'};
  const href = el.href || el.getAttribute('href') || '';
  el.dispatchEvent(new MouseEvent('click', {bubbles:true, cancelable:true, view:window}));
  el.click();
  setTimeout(() => {
    if (location.href !== href) location.assign(href);
  }, 50);
  return {ok:true, href, url: location.href, title: document.title};
})()
```

## Escalation Rules

When the user asks for "next episode", do the action simply and verify it. Avoid long explanations while the episode is still not advanced.

Hard stops unless the user explicitly approves:

- closing a tab/window (`Ctrl-W`, window manager close, etc.)
- killing or restarting Firefox
- opening a duplicate media tab/window
- using URL-bar typing or browser keyboard shortcuts as automation

If BiDi is wedged by a leaked session and no non-destructive protocol recovery is available, report that exact blocker and ask whether to restart Firefox. Do not decide to restart on the user's behalf.

## Verification Pattern

- Run `bash -n` on changed shell scripts.
- Run the actual command only when it should really advance the episode.
- Verify from live browser state, not script stdout alone:
  - `browsingContext.getTree` URL in the same context
  - `script.evaluate` of `document.title`
  - visible Firefox title via `xdotool search --onlyvisible --class firefox getwindowname %@` as a non-mutating check
- Do not use screenshots unless no semantic/protocol state source exists.

Example proof line:

```text
Watch ONE PIECE Episode 492 (1999) Sub/Dub - TV Action | Hianime — Mozilla Firefox
```

## Durable Lessons

- User-provided selectors/classes are primary control signals.
- Prefer DOM/protocol/accessibility over vision, coordinates, sessionstore, and URL-bar manipulation.
- For media/streaming control, never use duplicate-tab fallbacks.
- If remote protocol control is unavailable, fail loudly with the exact startup command rather than improvising risky workarounds.
- Keep the artifact small, run it immediately, and show live-state proof.

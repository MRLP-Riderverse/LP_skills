---
name: local-browser-accessibility-automation
description: Use when automating the user's already-open local desktop browser as an accessibility/remote-control aid, especially when the browser state is manually prepared and the agent should perform one focused action without overengineering.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [browser, accessibility, desktop-automation, firefox, x11, remote-control]
    related_skills: [next-anime-episode, hermes-agent]
---

# Local Browser Accessibility Automation

## Overview

Use this skill for small local-machine browser actions that let the user control an already-open browser from another device or context. The common pattern is: the user manually prepares the browser/window/site, then asks Hermes to perform one precise action on that existing desktop session.

Favor direct, verifiable, minimally stateful actions. Do not build background services, trigger stacks, browser extensions, or multi-helper systems unless the user explicitly asks. The value here is reliable local accessibility, not a general browser automation platform.

## When to Use

Use when the task involves:

- an already-open Firefox/desktop browser window on the user's machine
- local accessibility / remote-control convenience
- a known page or site state prepared manually by the user
- a single action such as advancing media, clicking a known control, copying a URL, submitting a form, or restoring fullscreen
- browser protocol, accessibility-tree, sessionstore, DOM, or X11 desktop automation techniques

Do not use when:

- the user wants a new web app, extension, or persistent daemon
- the task should be done through a public API instead of the local browser
- credentials, account takeover, or bypassing access controls are involved
- the browser/page is not actually open locally and no remote desktop/browser state exists

## Default Workflow

1. Identify the target browser/window from URL, title, sessionstore, browser protocol target list, accessibility tree, or user-provided constraints.
2. If the user names a button/class/selector, treat that as the primary source of truth. Build a selector/anchor/action script around it; do not reach for screenshots or coordinate reasoning first.
3. Prefer semantic/navigation primitives over coordinates:
   - DOM selectors and `element.click()` through CDP/Marionette/WebDriver when available
   - accessibility/AT-SPI actions on named buttons/links
   - real href/action targets parsed from page HTML
   - current URL/sessionstore state
   - keyboard shortcuts only when focus is controlled and they will not collide with the user's live typing
4. Avoid mouse movement/clicks, URL-bar typing, tab/window closing, browser restarts, and focus-dependent keyboard shortcuts for this user unless explicitly approved. These conflict with the user actively using the machine and can destroy the prepared viewing/session state.
5. Use coordinates or keyboard shortcuts only as a last resort after confirming no semantic route exists and the user accepts the risk.
6. Keep the user-facing command small and memorable.
7. Test end-to-end against the actual open browser state using non-invasive state checks where possible.
8. If a recovery/cleanup step would close, kill, restart, or otherwise disrupt the browser, stop and ask; do not improvise.
9. Document the exact trigger command and failure modes in the task-specific skill or reference.

## Firefox Control Techniques

Prefer control paths that do not touch the user's pointer, keyboard focus, clipboard, URL bar, or tab model:

```bash
# Launch Firefox with WebDriver BiDi remote control before the task.
firefox --remote-debugging-port 9222

# Firefox's current remote endpoint may be WebDriver BiDi at ws://127.0.0.1:9222/session,
# not Chrome's /json/list CDP endpoint. Use suppress_origin=True with websocket-client.
```

Minimal BiDi shape for an existing tab:

1. Connect to `ws://127.0.0.1:9222/session` with `suppress_origin=True`.
2. Send `session.new`.
3. Send `browsingContext.getTree` and choose the existing target context by URL/title.
4. Send `script.evaluate` with `target: {context}` and a selector-based DOM action.
5. If a real anchor click is swallowed by site JS, use same-context `location.assign(anchor.href)`; do **not** open a new tab/window.
6. Send `session.end` when finished so later runs do not hit “Maximum number of active sessions”.

Use X11 tools (`xdotool`, `xclip`) only for non-mutating state checks (for example, reading visible window title) or when semantic control is impossible and explicitly accepted. URL-bar copy/paste, synthetic keystrokes, Ctrl-W/tab close, browser kill/restart, mouse movement, clipboard writes, and `firefox --new-tab` fallbacks can collide with the user's live session, close the prepared browser, or create duplicate media tabs; avoid them by default.

Fullscreen handling depends on the site/player. Preserve the user's state where possible, but do not use fullscreen toggles as a substitute for a real DOM/accessibility/page action.

## Prefer URL/DOM-Derived Actions Over Coordinates

When a page has a real link or form action, use it. For example, if a visible `Next` button is rendered as an anchor, fetch or inspect the current page and extract the actual `href`, then open that URL in the same tab. This avoids fragile clicks that can hit nearby controls after layout shifts, overlays, terminal focus, or viewport differences.

Coordinate clicks are acceptable only for controls that have no usable URL/action, DOM/API/protocol/accessibility path, or session/anchor-derived route and the user explicitly accepts the risk. If coordinates are used, account for window decorations/chrome, distinguish window-relative vs absolute coordinates, and verify resulting state semantically when possible.

## User Preference: Keep It Simple

For this user's local browser accessibility tasks, default to the simplest useful artifact:

- one skill or one script when that satisfies the request
- no helper server, trigger daemon, userscript, browser extension, or extra stack unless explicitly requested
- do the requested action and test it instead of explaining an elaborate design
- when a coordinate approach proves fragile, replace it with a semantic/URL-based approach rather than tuning coordinates indefinitely

## Common Pitfalls

1. **Reasoning visually when the selector is known.** If the user gives a class/name/selector like `btn-ep-nav--next`, stop using screenshots/vision to infer intent. Write and run a script that targets that selector, anchor, accessibility action, or protocol endpoint directly.

2. **Clicking coordinates too early.** Adjacent controls can be very close. A click that appears to target `Next` may hit `Prev`, `Source`, or an overlay. Inspect the DOM/href first.

3. **Fighting the user's live input.** Mouse movement, focus stealing, clipboard writes, and URL-bar typing conflict with the user typing or moving the mouse. Prefer background/session/protocol methods that do not control their pointer or keyboard.

4. **Confusing active pointer window with target browser window.** `xdotool getmouselocation` can report the terminal or overlay as the current window even while Firefox is visible behind it. Do not base critical actions on pointer-window state.

5. **Typing JavaScript or URLs into the address bar as a control path.** Modern browser behavior and search fallbacks can turn pasted JavaScript into a web search; URL-bar typing can also fail under focus races. Prefer DevTools/CDP/Marionette/WebDriver, AT-SPI, sessionstore + anchor parsing, or page HTML parsing.

6. **Overbuilding the control plane.** If the user only needs one remote convenience action, do not add servers, persistent triggers, or extra support files. Add complexity only after the simple path fails and the user agrees.

7. **Claiming completion without executing the artifact.** Script syntax checks are not enough. Run the actual command and verify with non-invasive state inspection when possible. For this user, include concrete proof from the live browser state (for example the visible Firefox window title or protocol-reported URL), not just the script's stdout.

8. **Opening a new tab as a “safe” fallback.** This is not safe for streaming/media. It can leave the old playing tab with audio plus a new static tab. Same-tab DOM/protocol navigation or a loud failure is better than a duplicate-tab workaround.

9. **Using close/restart as cleanup.** Ctrl-W, window-close shortcuts, `pkill`, and browser restart are destructive in an already-prepared viewing session. They can close the user's source stream/browser and make the task worse. If cleanup would close or restart the browser, stop and ask.

10. **Using focus-dependent keyboard shortcuts as automation.** Site shortcuts like `n`/ArrowRight and browser shortcuts like Ctrl-L/Ctrl-W depend on focus and can be swallowed by the player, address bar, terminal, or desktop. Treat keyboard shortcuts as user-approved last resorts, not normal automation.

11. **Leaking WebDriver BiDi sessions.** If you call `session.new`, call `session.end`. Otherwise later attempts can fail with “Maximum number of active sessions”. If a leak blocks BiDi, prefer a non-destructive protocol recovery if one exists; do not restart the browser without explicit user approval.

12. **Trusting Firefox sessionstore as the only source of truth.** Sessionstore can lag or contain stale selected-tab state after CLI-opened tabs. Prefer browser protocol state; if unavailable, compare sessionstore against visible Firefox window title/URL-derived state before choosing the next action.

## Verification Checklist

- [ ] Target page/tab is identified from protocol/session/accessibility/browser state, not pointer position.
- [ ] If the user provided a selector/class/button name, the action targets it directly.
- [ ] The action avoids mouse movement, coordinate clicks, URL-bar typing, keyboard shortcuts, tab/window close commands, browser restarts, and focus theft unless explicitly accepted.
- [ ] If fullscreen is changed, it is restored only when it was active before.
- [ ] End-to-end test ran the actual command and verified the intended state with non-invasive inspection where possible.
- [ ] The skill/script folder stays minimal unless the user requested more infrastructure.
- [ ] Any site-specific lessons are stored under `references/` rather than bloating the main skill.

## References

- `references/hianime-next-episode.md` — session notes from building the HiAnime next-episode remote-control flow, including the coordinate/vision/URL-bar/new-tab failures and the final WebDriver BiDi same-tab selector-control pattern.

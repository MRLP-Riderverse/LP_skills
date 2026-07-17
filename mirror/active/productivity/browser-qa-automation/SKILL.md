---
name: browser-qa-automation
description: "Explore, reproduce, and verify browser and web app behavior with local browser control, accessibility inspection, and focused QA workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [browser, QA, accessibility, regression, web-apps, local-desktop]
    related_skills: [software-dev-workflow]
---

# Browser QA and Automation

Class-level skill for checking real browser behavior, reproducing UI bugs, and validating fixes in the user's browser or a web app under test.

Use this when you need to:
- inspect a live browser state the user already prepared
- validate a UI bug or regression
- perform a focused action in the browser without overengineering
- inspect accessibility trees, element structure, or runtime behavior

## Core workflow

1. Reproduce the issue in the smallest possible browser state.
2. Inspect the accessibility tree and DOM when text snapshots are insufficient.
3. Verify the exact interaction path the user would take.
4. Capture evidence with screenshots or console output when needed.
5. Re-test after the fix using the same path.

## Local browser / accessibility workflows

- Prefer accessibility snapshots for deterministic interaction targets.
- Prefer visual inspection when layout, overlap, or mobile behavior matters.
- Prefer a single focused action over broad automation when the browser state is already prepared.
- When a page has page-local controls that should behave like shared chrome, verify the same interaction across all affected pages or views.
- If browser control is unavailable, use the headless Chrome + CDP fallback in `references/headless-chrome-cdp.md` for live DOM and geometry checks.
- For horizontal full-viewport discovery decks, use `references/horizontal-full-viewport-decks.md`: separately verify dot-triggered navigation and swipe/scroll-driven indicator updates, test CTA reachability through internal scrolling on short landscape phones, and assert flat computed surface styles in both themes.
- For dock/menu/footer overlap or search-surface consolidation work, see `references/mobile-shell-and-search.md` for the mobile probe checklist.
- When a search page is folded into an existing directory, verify both intent states on the same route (`#browse` vs `#search`) instead of treating them as separate pages; the URL may stay the same while the visible state changes.

## Shared shell and repeated chrome regressions

Use this pattern when the bug is about a dock, menu, header, footer, drawer, or overlay that should be identical across pages.

- Treat the shell as global chrome, not a page-local variation.
- Compare the relevant structure across all affected pages, not just the visual surface.
- Normalize element types, labels, order, and interaction targets together.
- When a dedicated search page is being merged into an existing directory, verify both the layout and the hit targets: the search surface can be hidden by default, but it still needs to expose the same result set and discovery terms as before.
- When a user reports the wrong page opens, check overlap/hit-testing before changing the URL: the link may be correct while another fixed element is stealing the tap.
- Keep the browse/search intent explicit in QA: `Browse` should show the cards immediately, `Search` should expose the search surface and hide results until requested, and both should remain reachable from the dock.

This subsection is the home for shared UI shell consistency and repeated chrome drift bugs.

## Exploratory QA

- Look for broken states, not just happy paths.
- Check labels, focus order, keyboard behavior, and hidden overlays.
- Look for stale event handlers, duplicate controls, and inconsistent navigation targets.
- If a visual change touches shared shell or repeated chrome, test all related pages or views.

## Verification checklist

- Confirm the bug is reproducible.
- Confirm the fix changes the intended behavior only.
- Confirm no new console errors appear.
- Confirm the same interaction works across the relevant pages or states.

## Notes

This umbrella replaces narrower browser QA helpers and should be the first stop for exploratory browser testing, accessibility-guided interactions, and local-desktop browser control.
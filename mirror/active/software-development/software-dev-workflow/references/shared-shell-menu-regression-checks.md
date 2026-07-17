# Shared Shell / Menu Regression Checks

Notes from Acadie.sol shared-shell work.

## Verify
- Drawer item labels are centered when the user asks for a cleaner stack.
- Remove redundant drawer subtitles when the button list already communicates the same thing.
- Keep *Support* and *About* as separate destinations with separate buttons and pages.
- Update visible labels and ARIA labels together when renaming shared chrome.
- Search the repo for stale labels after changing shared shell text.
- Verify `git diff --check` and clean status before pushing.

## Pattern
1. Re-read the live shared shell file before editing.
2. Update the shared JS/CSS contract once.
3. Update page-local translations that duplicate shared labels.
4. Add blank pages when introducing new destinations.
5. Run a repo-wide search for the old labels.
6. Push only after the diff is clean.

## Pitfall
- Do not collapse distinct navigation targets into a single label just to save space.

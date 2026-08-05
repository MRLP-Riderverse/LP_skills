# Tk sidecar resize and repository-boundary lessons

## Resize reproduction recipe

1. Record the intended default and minimum dimensions.
2. Set the minimum through shared constants, not duplicated literals.
3. Instantiate under Xvfb with decoration disabled so geometry is isolated.
4. Set the window to default, intermediate, and minimum sizes.
5. Call `update_idletasks()` and the full redraw path.
6. Assert the actual Canvas dimensions, the GUI's layout dimensions, and the presence/coordinates of dynamic text items.

A Tk window may accept a smaller `minsize()` while the app still calculates `current_width()`/`current_height()` using the old dimensions. This produces off-screen, miscentered, or apparently missing content. Verify layout helpers, not only window-manager state.

## Narrow Git boundary

When the parent workspace contains unrelated projects, nested repositories, caches, logs, personal notes, or generated state, create a local repository at the app's own directory. Track only the app/backend files and an allowlist-style `.gitignore`. Before the first commit:

- run `git rev-parse --show-toplevel` in the candidate parent;
- inspect `git status`, `git log`, and `git ls-files`;
- confirm the target is actually tracked;
- scan candidate files for secrets and personal data;
- inspect the staged file list.

Create a motion/decorations-enabled baseline commit first, then make each experiment a separate commit. This provides exact A/B rollback without adding the user's note corpus to version control.

## Async-save verification race

Do not treat file creation as proof that a backend append has completed. A backend can create/truncate the target before the payload is written. A robust temporary-file probe waits for the expected text (or another confirmed success marker), not merely `path.exists()`, before asserting persistence. Keep the real CLI/backend in the loop.

# Tk Sidecar Experiment Recipe

Use this recipe when a focused GUI sidecar feels sluggish and the CLI/backend is already trusted.

## Safe repository boundary

1. Search upward and nearby for `.git`; do not assume the project directory is tracked.
2. Verify candidate roots with `git -C <path> rev-parse --show-toplevel`, then confirm the target with `git ls-files`.
3. If the workspace is mixed or contains personal/generated data, create a narrow local repository around the app/backend pair. Use an allowlist-style `.gitignore` and inspect `git status --short` after staging.
4. Commit a motion/decorations-enabled baseline before experiments. Make each A/B variant a separate commit.

## Isolate motion without deleting it

Comment out only the startup call that schedules animation, leaving the `animate()` method and its calculations intact:

```python
# Motion experiment: keep the animation implementation below intact.
# self.animate()
```

Verify with a bounded Tk loop that the tick counter remains unchanged. Restore the baseline commit to re-enable motion.

## Measure presentation separately from parsing

For preview work, time these independently:

- bounded tail read and timestamp parsing;
- cached lookup;
- font/layout formatting;
- complete static redraw.

A tail parser can remain fast on a multi-megabyte file while repeated Tk `font.measure()` calls dominate formatting. Replace character-by-character truncation with a binary search for the longest fitting prefix, then cache formatted preview text by entries, font size, and available width.

## Controlled decoration and preview variants

Use environment switches for reversible decoration tests, for example `NOTE_SHOW_BORDER=0/1` and `NOTE_SHOW_LOGO=0/1`. Test the focused product with a small preview count (usually four entries) before restoring visual extras.

## Async-save probe correctness

Do not stop a real-save test when the target file merely exists: the backend may create the file before its append is durable. Wait until the expected submitted text is actually readable, with a timeout. Keep test targets temporary and preserve the canonical CLI/backend call.

## Verification minimum

- compile GUI and validate JSON config;
- run existing storage/backend tests;
- run an Xvfb startup smoke test;
- confirm no-motion tick state when motion is disabled;
- confirm render coalescing;
- confirm real temporary-target save by content, not file existence;
- inspect `git diff --check` and final repository status.

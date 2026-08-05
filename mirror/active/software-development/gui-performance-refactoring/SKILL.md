---
name: gui-performance-refactoring
description: "Use for GUI sidecar performance profiling and refactoring."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [gui, performance, tkinter, profiling, refactoring, sidecar]
    related_skills: [software-dev-workflow]
---

# GUI Performance Refactoring

Use this skill when a small desktop GUI, especially a Tkinter sidecar, feels sluggish during launch, typing, saving, resizing, or preview refresh. The goal is a responsive focused surface, not a broad rewrite or a second application.

## Product contract first

1. State what the GUI is for in one sentence. A low-friction sidecar should remain a focused input surface that can stay open while other work happens.
2. Preserve the existing CLI/backend as the behavioral authority when it already works. Keep GUI diagnosis separate from storage-format, queue, or capture-workflow changes.
3. Preserve valued visual behavior. If motion or decoration is part of the experience, remove redundant work before removing the visual character.
4. Keep optional decoration independently switchable so performance tests can compare the product with and without it.

## Evidence-first workflow

1. Locate the actual repository before relying on Git history. Verify each candidate with `git -C <path> rev-parse --show-toplevel`; inspect `status`, `log`, and `ls-files`. A nearby clean repository may not track the target.
2. Choose the narrowest safe Git scope. If the workspace contains unrelated projects, nested repositories, personal notes, caches, or generated state, initialize a focused repository around the app/backend pair rather than Git-tracking the whole workspace. Add an explicit allowlist-style `.gitignore` and inspect the staged file list before the first commit.
3. Create a motion/decorations-enabled baseline checkpoint before experiments. Put each isolated comparison in a separate commit so rollback and A/B inspection are exact; do not use a temporary backup as the only recovery mechanism.
4. Preserve a rollback copy before editing. Keep changes limited to the GUI file and its GUI config unless a measured result justifies broader changes.
5. Reproduce the slow paths separately: launch, typing, save, resize, and preview refresh.
6. Instrument phase timings rather than guessing from implementation language. Measure interpreter/Tk construction, decorative Canvas creation, bounded file read, parsing, font/layout formatting, redraw, and backend submission.
7. Compare controlled variants: decoration on/off, preview count, cached/uncached formatting, motion on/off, and small-to-large synthetic files.
8. Record real results and use them to choose the smallest fix. Do not infer that Python, a large plaintext file, or a parser is the bottleneck without a measurement.

## Safe refactoring patterns

### Redraw lifecycle

- Route input and animation through one coalescing `request_render()`/`after_idle` path.
- Keep animation if desired, but prevent duplicate paints in the same event-loop turn.
- Debounce resize redraws more generously than animation frames; avoid rebuilding expensive decoration while the user drags the window.
- Remove redundant calls such as `refresh_recent(); render()` when the refresh already performs a full redraw.
- Prefer updating dynamic Canvas items over deleting and recreating all items. Cache static or optional objects where practical.

### Preview and parsing

- Use a bounded tail read for recent entries and cache by file stat, limit, mode, and tail size.
- Profile parsing separately from presentation formatting. Tail parsing can remain fast even for very large files.
- Tk `font.measure()` in a character-by-character truncation loop can dominate preview work. Use binary search for the longest fitting prefix.
- Cache formatted preview text by the actual inputs that affect it: entries, font size, and available width.
- Test smaller preview counts when the product only needs a glance; do not expose a full history panel in a focused intake surface.

### Minimum-size and responsive layout

- Treat the minimum window size as a layout invariant, not only a window-manager constraint. If `root.minsize()` and resize clamping use new dimensions but `current_width()`, `current_height()`, or other geometry helpers still enforce the old dimensions, the Canvas can shrink while text remains positioned for the old viewport.
- Centralize minimum dimensions (`MIN_WIDTH`, `MIN_HEIGHT`) and use them consistently in `root.minsize()`, resize clamping, Canvas/layout helpers, wrapping, centering, and fade calculations.
- Verify the actual Canvas dimensions and rendered item coordinates at the default size, an intermediate size, and the new minimum. A window that accepts the smaller geometry is not proof that content lays out correctly.

### First-render and responsive geometry

- Realize a packed Canvas with `root.update_idletasks()` before the first `redraw_all()`; a withdrawn Tk root may report configured window geometry while the Canvas still has fallback dimensions.
- Initialize cached resize state to a sentinel such as `(0, 0)` so the first real `<Configure>` event cannot be suppressed as already handled.
- Treat minimum dimensions as layout invariants throughout all geometry helpers, not merely through `root.minsize()`.
- For a narrow or portrait sidecar, switch deterministically from side-by-side preview/author placement to a stacked footer. Expand preview width to the inner viewport, place the author below it with a line-height gap, and truncate the author label to available width.
- Verify initial, intermediate, minimum, and tall portrait sizes without requiring a manual resize; inspect actual Canvas dimensions and text bounding boxes.

### Save responsiveness

- A synchronous `subprocess.run()` blocks Tk even when the backend itself is correct.
- Use a serial daemon queue/worker to preserve submission order and keep the UI event loop responsive.
- Capture the submitted text before clearing the input. Only refresh previews after confirmed success.
- On failure, restore the submitted text without discarding text entered while the save was running.
- Marshal worker results back through `root.after()` and suppress callbacks after the window begins closing.
- Do not silently replace the known-good CLI/storage semantics with a direct storage shortcut until behavior and failure recovery are separately verified.

## Verification checklist

- `py_compile` for the GUI and JSON validation for its config.
- Existing backend/storage tests unchanged and passing.
- Xvfb or equivalent GUI startup smoke test.
- Rapid-input probe confirms many input events coalesce into one render.
- Async-save probe confirms Enter returns immediately and failed saves restore content.
- Real temporary-file save through the GUI worker confirms backend integration.
- Launch comparison with optional decoration enabled/disabled.
- Preview profiling across small and multi-megabyte files.
- Review the final diff and explicitly state any repository-tracking limitation.

## References

- See `references/tk-sidecar-performance.md` for the tested Tk sidecar profiling recipe and bottleneck patterns.
- See `references/tk-sidecar-resize-and-repo-boundary.md` for minimum-size layout verification, narrow repository boundaries, and async-save persistence-race lessons.
- See `references/tk-sidecar-experiment-recipe.md` for narrow Git scope, motion-isolation, decoration A/B, parsing-vs-formatting probes, and durable async-save verification.
- See `references/tk-sidecar-responsive-layout.md` for first-render initialization, Tk Canvas realization, and compact/portrait footer layout.

## Pitfalls

- Do not remove all motion merely because a full redraw loop is wasteful.
- Do not blame large-file parsing when a bounded tail read and stat cache have been measured flat.
- Do not make the GUI synchronous again just because the backend is reliable.
- Do not change CLI/storage/queue behavior while the question is GUI responsiveness.
- Do not claim Git history or diff coverage until the target file is confirmed by `git ls-files`.
- Do not add a narrow one-off performance skill for each application; reuse this class-level workflow.

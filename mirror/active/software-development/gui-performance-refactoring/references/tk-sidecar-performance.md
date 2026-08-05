# Tk Sidecar Performance Reference

Use this when a small Tkinter sidecar feels slow despite a lightweight storage backend.

## Product contract

Treat the sidecar as a focused, always-available input surface. Preserve the existing CLI/backend as the behavioral authority unless evidence proves its semantics are wrong. Do not turn the sidecar into a second notes/search application.

## Evidence-first probes

1. Locate the real repository before assuming Git can provide history. Run `git -C <candidate> rev-parse --show-toplevel`, then `status`, `log`, and `ls-files`; a nearby clean repository may not track the target.
2. Preserve a rollback copy before editing. Keep scope to the GUI file/config; do not alter the CLI, queue, storage format, or capture workflow during a GUI diagnosis.
3. Measure independent phases: interpreter/Tk startup, static Canvas construction, recent-file tail read, preview formatting/font measurement, resize redraw, and backend submission.
4. Compare visual components with runtime switches or controlled variants (border/logo on versus off) rather than removing them permanently.
5. Use synthetic files from small through multi-megabyte sizes. If tail parsing is flat across sizes, do not blame whole-file reads.

## Common Tk bottlenecks and fixes

- Repeated `Canvas.delete("all")` plus recreation of decorative objects is especially costly during resize. Debounce `<Configure>` redraws and avoid rebuilding optional decoration while dragging.
- If input and animation both call `render()`, coalesce requests with one `after_idle` job. Keep motion if it is part of the product; remove duplicate work, not the personality.
- Tk `font.measure()` inside a character-by-character truncation loop can dominate a tiny preview. Use binary search for the longest fitting prefix, then cache formatted preview text by `(entries, font size, width)`.
- A bounded tail read plus a stat-keyed cache is usually sufficient for a recent preview. Profile parsing before changing storage.
- A synchronous `subprocess.run()` freezes the Tk event loop. A serial daemon worker/queue can preserve the existing CLI backend while keeping the sidecar responsive. Clear input immediately only if failed submissions restore the captured content; marshal success/failure callbacks back with `root.after()` and suppress callbacks during close.

## Verification

Run Python compilation, existing storage tests, an Xvfb startup smoke test, a render-coalescing probe, an async-save probe, and a real temporary-file save through the GUI worker. Record measured numbers; do not infer performance from implementation style (for example, “it is Python”).

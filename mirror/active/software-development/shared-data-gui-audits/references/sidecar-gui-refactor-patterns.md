# Low-Friction Sidecar GUI Refactor Patterns

Use this when a small GUI wraps a proven CLI capture path and is intended to remain open beside other work.

## Product contract

- The GUI is a focused intake sidecar, not a second notes/search application.
- The CLI/backend remains the behavioral and durability authority for the first refactor.
- Enter should return control to the user immediately.
- Successful saves refresh the preview; failed saves restore the submitted text.
- Preserve valued motion; reduce redundant work before removing visual character.

## Verified Tk pattern

### Coalesced rendering

Maintain one pending idle callback:

```python
_render_job = None

def request_render(self):
    if self._render_job is None:
        self._render_job = self.root.after_idle(self._run_requested_render)

def _run_requested_render(self):
    self._render_job = None
    self.render()
```

Use `request_render()` from input handlers and animation. Cancel the pending idle render before a full `redraw_all()` so a resize or preview refresh does not immediately repaint twice.

### Resize debounce

Resize handlers should cancel and replace one delayed full redraw. A delay around 180 ms is a reasonable starting point for a decorative Canvas UI; tune from measurement. Avoid rebuilding static border/preview objects for every geometry event during a drag.

### Serial asynchronous save

Use one daemon worker and a queue, not one uncontrolled thread per Enter key. The worker calls the unchanged CLI/backend method in queue order. On success, schedule a Tk callback to refresh the preview. On failure, restore the submitted payload while preserving text entered during the save.

Important safety details:

- Never touch Tk widgets from the worker thread.
- Post results through `root.after(0, ...)`.
- Ignore callbacks after the window is closing.
- Keep backend submission semantics unchanged until the GUI behavior is verified.

## Verification recipe

Use temporary targets, never the real inbox, for GUI probes:

1. Compile the GUI and relevant package source.
2. Run the focused storage tests.
3. Start the GUI under Xvfb for a smoke test.
4. Send many input events before one `root.update()` and confirm they produce one coalesced render.
5. Replace the backend call with a delayed test double and confirm Enter returns immediately while the worker completes.
6. Run one real GUI-worker submission against a temporary target and verify the payload appears.
7. Test failure restoration with text entered during the delayed save.
8. Measure launch, save, typing/rendering, and resize separately; do not infer file-size causality without size-controlled probes.

## Pitfalls

- Do not refresh the preview before save success.
- Do not clear failed content silently.
- Do not make animation the first thing removed when the user values it and typing is responsive.
- Do not call `refresh_recent()` and then call `render()` again if the former already performs a full redraw.
- Do not replace a proven CLI backend with direct storage writes merely to remove a 100 ms subprocess cost before preserving behavior has been tested.

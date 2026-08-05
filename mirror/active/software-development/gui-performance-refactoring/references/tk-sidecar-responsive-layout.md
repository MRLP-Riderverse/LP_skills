# Tk sidecar responsive layout and first-render lessons

## First-render initialization

A withdrawn Tk root can have a configured geometry while its packed Canvas has not yet realized that size. If the first `redraw_all()` runs before realization, layout helpers may see the fallback minimum and draw centered/anchored content for the wrong viewport. The window then opens at the larger default size and appears offset until a manual resize.

Before the first draw:

```python
root.update_idletasks()
redraw_all()
root.update_idletasks()
root.deiconify()
```

Initialize cached resize state to a sentinel such as `(0, 0)` so the first real `<Configure>` event cannot be suppressed by assuming the default geometry was already rendered.

Verify without manually resizing: actual Canvas width/height, layout helper width/height, and the center/bounds of the initial placeholder or dynamic text should agree.

## Compact and portrait footer layout

A focused note sidecar can remain landscape by default while supporting narrow and portrait use. Use a deterministic breakpoint, for example `width < 780` or `height > width`, to switch from a side-by-side footer to a stacked footer:

- compact/portrait: preview above, author line below;
- landscape: preview lower-left, author lower-right.

In stacked mode, expand preview formatting to the available inner width and place the preview baseline above the author by at least one UI line-height plus a small gap. Truncate the author label to the inner width. Verify bounding boxes, not only visual screenshots: the author's top must be below the preview's bottom.

Keep the four-entry glance preview and avoid turning this sidecar into a scrolling/search interface. Test default, intermediate, minimum, and tall portrait geometries under Xvfb.

## Pitfalls

- Calling `root.geometry()` is not proof that the Canvas has realized that geometry.
- Calling `root.minsize()` is not enough; layout helpers must use the same minimum constants.
- A right-anchored author label will collide with a left preview when the window becomes narrow; make the footer arrangement responsive rather than merely shrinking fonts.

# Gallery Caption Overlay — Debugging Journey (June 2026)

## The problem

Adding a legibility overlay behind image caption text over a carousel photo. The text needed to be readable without the overlay being visually aggressive.

## Iterations

### 1. Pure gradient overlay (too subtle)
```css
background: linear-gradient(to top, rgba(0,0,0,.22) 0%, rgba(0,0,0,.08) 50%, transparent 100%);
```
- 22% opacity at bottom, fading to 8%, then transparent
- Padding: `4px 14px 8px` (very tight)
- **Result:** User couldn't see any overlay at all. The gradient dissipated before the eye registered it over the photo.

### 2. Solid rgba (legible but hard-edged)
```css
background: rgba(0,0,0,0.38);
```
- Padding: `10px 14px`
- **Result:** Text was readable, but the top edge of the solid bar was a sharp horizontal line cutting across the image. User described it as needing to "soften it up" — the top edge was "too violent."

### 3. 3-stop gradient with softened top edge (settled)
```css
background: linear-gradient(to top,
  rgba(0,0,0,.45) 0%,    /* strong at bottom for text legibility */
  rgba(0,0,0,.22) 55%,   /* mid-fade */
  rgba(0,0,0,.06) 100%); /* whisper at top, blends into image */
```
- Padding: `10px 14px`
- **Result:** Legible at the bottom where the text sits, the overlay gently dissolves upward. No hard edge.

## Key lesson

The overlay style spectrum for photo-on-caption:
- **Pure gradient ≤22% opacity** → invisible, pointless
- **Solid rgba ≥38% opacity** → legible but hard rectangular bar
- **3-stop gradient 45%/22%/6%** → legible + soft top edge ← use this pattern

The light theme mirrors at lower opacity (32%/14%/4%) because `var(--paper)` text on navy is more readable than white on black at the same opacity.

## Stacking order bug

During the session, the image was rendering ON TOP of the caption despite the caption being later in the DOM. Root causes:

1. **Missing explicit z-index** — DOM order stacking is unreliable when `position:absolute` elements are in different compositing layers. Fix: `z-index:1` on `.gallery-image`, `z-index:2` on `.gallery-caption`.

2. **Flex centering on `.media-gallery-slide`** — `display:flex; align-items:center; justify-content:center` was centering the `<picture>` as a flex child instead of filling the slide edge-to-edge. Fix: remove flex centering, use `position:absolute;inset:0` on `.gallery-image`.

3. **Nested CSS selectors** — A patch introduced `.gallery-caption { .gallery-caption { ... } }` (duplicate nesting), which is invalid CSS. Always verify selector nesting after iterative edits.

## Removed variable trap

`GALLERY_COUNT` was replaced by `GALLERY_IMAGES` but the touch swipe handler still referenced `GALLERY_COUNT - 1` for bounds clamping. This threw a `ReferenceError` at runtime, silently breaking swipe navigation. The fix: `GALLERY_IMAGES.length - 1`. When renaming/removing a const, grep for *all* references including event handlers and offline computation.

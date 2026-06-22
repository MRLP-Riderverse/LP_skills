---
name: acadie-sol-gallery
version: 1.0.0
description: Add, remove, reorder, or swap media slides in the Acadie.sol homepage gallery carousel.
---

# Acadie.sol Gallery Carousel

Manage media slides in the homepage gallery carousel on `acadie_sol/index.html`.

## Architecture

The gallery is **data-driven** by the `GALLERY_IMAGES` array inside the `<script>` block in `index.html` (approximately line 746). The carousel auto-derives its length, swipe bounds, and rendering from this array — no other code changes are needed when modifying slides.

## Slide Format

Each entry in `GALLERY_IMAGES` is one of:

- **Real image**: `{ src: 'assets/images/filename.jpg', alt: 'Description', caption: 'Optional caption text' }`
- **Placeholder**: `null` — renders a placeholder card with the `⊒` icon

## Operations

### Add a slide

1. Place the image file in `assets/images/`
2. Add an entry to `GALLERY_IMAGES`: `{ src: 'assets/images/new-file.jpg', alt: 'Alt text', caption: 'Caption text' }`
3. Optionally replace an existing `null` to keep slide count stable
4. Update `assets/images/gallery-manifest.json` to reflect the change
5. Git add + commit + push from the `acadie_sol` project root

### Remove a slide

- Set the array entry to `null` (renders placeholder, keeps count stable)
- Or splice the entry out (shrinks carousel count)
- Update `gallery-manifest.json` accordingly

### Reorder slides

- Move entries within `GALLERY_IMAGES` — array order = visual order
- Update `gallery-manifest.json` accordingly

### Swap an image

- Replace the file in `assets/images/` (same filename = zero code changes)
- Or change the `src` path in the array entry + `gallery-manifest.json`

## Image specs

- **Aspect ratio**: 16:9 recommended (carousel uses `aspect-ratio: 16/9`)
- **object-fit**: `cover` is applied via CSS — images fill the slide and crop evenly
- **Format**: `.jpg`, `.webp`, `.png` all work
- **Size**: aim for 100–300KB; progressive JPEG preferred

## Caption styling

Captions render at center-bottom of the slide with a gradient overlay. Controlled by `.gallery-caption` CSS in `index.html <style>`:
- `text-align: center` (centered)
- Gradient fades from semi-transparent dark at bottom to clear at top
- Light theme variant uses `var(--paper)` text color

## File layout

```
acadie_sol/
  index.html                    ← GALLERY_IMAGES array + renderGallery() + CSS
  assets/
    images/
      acadie-in-the-stars.jpg   ← first real media slide
      gallery-manifest.json     ← human-readable routing doc (mirrors GALLERY_IMAGES)
```

## Pitfalls

- **Never reference `GALLERY_COUNT`** — it was removed. Use `GALLERY_IMAGES.length` for any bounds checks.
- **`.media-gallery-slide` must keep `position: relative`** — the caption is absolutely positioned and needs a positioned ancestor.
- **Missing CSS for `.gallery-image` or `.gallery-caption`** will cause images to not display or captions to float incorrectly. Both are defined in the `<style>` block in `index.html`.
- **First slide loads `eager`**, rest load `lazy` — keep the most important image at index 0.

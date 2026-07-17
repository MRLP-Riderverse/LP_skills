---
name: acadie-sol-gallery
version: 2.0.0
description: Manage Acadie.sol album pages, responsive public derivatives, featured-photo metadata, and private camera-original boundaries.
---

# Acadie.sol Album Gallery

Use this skill when adding, editing, publishing, archiving, or featuring photo albums on Acadie.sol.

## Current architecture

The old homepage swipe carousel is retired. The gallery is now an album archive:

```text
assets/gallery/albums.json                  canonical public catalogue
photos/index.html                           indexable album index
photos/YYYY/album-slug/index.html            stable static album URL
assets/gallery/YYYY/album-slug/*.webp       public responsive derivatives
assets/images/gallery-manifest.json          deprecated compatibility pointer
assets/live.json                             separate owner-controlled LIVE signal
```

The homepage reads `assets/gallery/albums.json` and displays the public album with `featured: true`. It does not contain a second gallery data array.

Canonical public URLs use `https://acadie.sol.site`, including the `.site` suffix.

## Source-of-truth boundary

Camera originals do **not** belong in the website repository.

Recommended private root:

```text
~/ExoCortex/media/acadie-sol/originals/YYYY/album-slug/
```

The Git repository receives only reviewed public derivatives. Keep at least one additional encrypted backup of originals.

For remote intake, Telegram and future Discord adapters should both create the same local intake record and feed the same pipeline. Send original-sensitive iPhone media as Telegram documents/files, not compressed photos. No intake adapter may auto-publish.

## Album contract

`assets/gallery/albums.json` contains:

- `public_limit`: current public-index presentation limit; **not security**
- localized `title`, `summary`, and cover `alt` values (`en`, `fr`)
- static `href`
- `status` and `featured`
- responsive cover `src` and `srcset`
- cover dimensions and photo count
- `full_resolution.policy`

Valid release policies:

| Policy | Public result |
|---|---|
| `preview` | Responsive previews; original remains private |
| `request` | Preview plus manual request/delivery path |
| `download` | Explicit public original/download |
| `members` | Public teaser only; protected file served elsewhere |

GitHub Pages cannot securely paywall committed files. Member-only/full-resolution media requires an authenticated origin or signed delivery URLs. Hiding a public URL with CSS/JavaScript is not a paywall.

## Add an album

1. Ingest and checksum source files into the private ExoCortex original root.
2. Review privacy, faces, captions, rights, GPS/EXIF, and release policy.
3. Create responsive derivatives from a developed JPEG/TIFF/HEIC-readable source:

```bash
python3 scripts/build_photo_derivatives.py SOURCE \
  --output-dir assets/gallery/YYYY/album-slug \
  --stem cover
```

4. Add the album record to `assets/gallery/albums.json`.
5. Create `photos/YYYY/album-slug/index.html` with static titles, descriptions, images, dimensions, Open Graph metadata, and bilingual copy.
6. Add or update the static card in `photos/index.html`.
7. If it is the homepage feature, set exactly one public album to `featured: true`.
8. Validate:

```bash
python3 scripts/validate_gallery.py
python3 -m unittest scripts/test_photo_derivatives.py -v
node scripts/check_inline_scripts.mjs
```

9. Serve locally and verify mobile/desktop widths, image loading, nested shell links, English/French switching, and no console errors.
10. Show screenshots for visual approval. Do not commit or push without user approval.

## Derivative defaults

- 480 px long edge WebP: card/phone
- 960 px long edge WebP: standard view
- 1600 px long edge WebP/JPEG: large display when source is large enough
- auto-orient
- convert predictably to sRGB
- strip GPS/private EXIF
- never upscale
- include `width`, `height`, `srcset`, and `sizes`

Budget targets:

- homepage cover below 150 KB
- album card below 200 KB
- standard photo below 350 KB where quality allows
- large preview below 900 KB
- full-resolution original off the public critical path by default

Sony `.ARW` originals remain private; feed the builder an intentionally developed JPEG or TIFF. HEIC support depends on the local ImageMagick build.

## Feature or reorder albums

- `featured: true` controls the homepage photo feature.
- Keep exactly one featured public album.
- Array order controls album-index order once the index generator is introduced; until then, mirror the same order in `photos/index.html`.
- `public_limit: 10` is a presentation policy. Older protected media must be removed from the public delivery layer, not merely omitted from the index.

## Verification

Minimum checks:

```bash
python3 scripts/validate_gallery.py
python3 -m unittest scripts/test_photo_derivatives.py -v
node scripts/check_inline_scripts.mjs
node --check assets/site-shell.js
git diff --check
```

Then browser-test at 320, 390, 430, 900, and 1280 px. Confirm:

- no horizontal overflow
- mobile dock below 900 px; desktop navigation at/above 900 px
- album cover and photo decode successfully
- nested album shell routes resolve to the site root
- all public routes return HTTP 200
- no uncaught exceptions or console errors
- French visibility and English hiding work after language switch

## Pitfalls

- Never add a second hardcoded homepage album array; the manifest is canonical.
- Never commit camera originals by default.
- Never claim `public_limit` or client-side hiding is access control.
- Do not make a multi-megabyte GIF or full-resolution photo a homepage startup dependency.
- Do not use separate Telegram and Discord publication pipelines; normalize both into the same private intake record.
- Do not auto-publish remote uploads.
- Do not omit width/height or responsive sources; phones must not download desktop/full-resolution assets.
- Static album pages carry search/Open Graph value; do not regress to hash-only album URLs.

## Reference

See `docs/media-pipeline.md` in the website repository for the current transport, storage, derivative, membership, and publishing boundaries.

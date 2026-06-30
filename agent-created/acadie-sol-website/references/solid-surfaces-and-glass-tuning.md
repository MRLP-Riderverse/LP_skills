# Solid surfaces and glass tuning

Use this when the user asks for a dark-mode refresh that should feel quieter, flatter, or more glassy without decorative gradients.

## Session lessons
- Prefer solid `--page-bg` / `--paper` / `--card` fills over multi-stop radial or linear gradients when the user says to "kill gradients for now."
- Restore depth with transparency and blur instead of color ramps:
  - `--glass` for chrome/backplates
  - `--button-bg` and `--button-bg-hover` for button/dock surfaces
- If dark-mode text or links are hard to read, audit the exact selector token:
  - homepage CTA links may need `--link` rather than `--blue-deep`
  - shell buttons should use shared button tokens rather than page-local colors
- Flatten page-local hero/background gradients first; then re-check contrast before introducing any new decorative treatment.

## Practical checks
- Search for `radial-gradient(` and `linear-gradient(` in page CSS.
- Confirm the dock, drawer, and CTA surfaces all share the same button tokens.
- Verify the background remains solid in both light and dark themes after theme toggles.
- If a section still needs visual separation, use border, shadow, or opacity—not a new background gradient.

# Global Button Chrome

Session note: the Acadie.sol UI now treats all primary action buttons as one shared visual system.

## Decision
- Buttons should use the same chrome across light and dark mode.
- Visual spec: Acadian blue background, Acadian yellow text, thin yellow border.
- This applies to shared shell controls and page-local CTAs so the UI can change while tap targets stay familiar.

## Implementation pattern
- Add shared button tokens in `assets/site-colors.css`:
  - `--button-bg`
  - `--button-fg`
  - `--button-border`
- Use those tokens in shared shell CSS for:
  - drawer controls
  - drawer nav buttons
  - dock buttons
- Reuse the same tokens in page-specific CTA cards like the Square donation link on `support.html`.

## Guardrails
- Prefer one global button rule set over per-page button styling.
- Keep hover state aligned with the same color family; do not flip button text to white just because the theme changes.
- If a page needs a special button, make it a token override rather than a new button palette.
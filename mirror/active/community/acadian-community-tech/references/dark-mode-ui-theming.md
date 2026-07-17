# Dark-mode UI theming pass

Session pattern: Acadian blue dark-mode refactor with follow-up readability fixes.

## What usually breaks
- Full-page detail/contact links keep old hardcoded colors and become low-contrast or invisible in dark mode.
- Tags / badges / pills keep light cream or white alpha backgrounds that clash with the new dark surface system.
- One-off inline styles bypass the token system and survive longer than the surrounding theme refactor.

## Fix pattern
- Centralize interactive surfaces around shared tokens:
  - `--button-bg`
  - `--button-bg-hover`
  - `--button-border`
  - `--button-fg`
- Use `var(--link)` + underline for inline detail links instead of dark-only accent text.
- Keep tags/meta pills readable by using the same translucent dark-blue button stack or a `var(--paper-soft)` tint that still respects dark-mode contrast.
- For full-page contact cards, treat the card itself as the detail surface and keep the button/link treatment consistent with the rest of the site.

## Practical search targets
Look for:
- hardcoded cream / white backgrounds such as `#f3eadc`, `rgba(255,255,255,...)`
- text colors like `var(--blue-deep)` used directly on dark surfaces
- inline `style=` attributes on tags and chips
- hover states that still flip to gold or light cream after the dark-mode shift

## Verification
- Check a full detail/contact page, not just the landing page.
- Check tags, meta pills, and related-place/full-page links in dark mode.
- Confirm hover states keep contrast and do not revert to a light palette.
- Prefer a small token cleanup over scattered per-element fixes.

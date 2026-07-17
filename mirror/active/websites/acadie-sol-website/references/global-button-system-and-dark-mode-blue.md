# Global button system and dark-mode blue base

## What changed
- The shared shell now treats *all* primary actions as one button system.
- Button tokens live in `assets/site-colors.css`:
  - `--button-bg`
  - `--button-bg-hover`
  - `--button-fg`
  - `--button-border`
- The visual contract is now:
  - dark Acadian blue translucent fill
  - Acadian Yellow text
  - thin yellow border
  - same treatment in light and dark mode for menu/dock/CTA buttons

## Dark mode base
- Dark mode surfaces moved from bronze/brown toward a deeper Acadian blue base.
- Relevant dark tokens now lean blue:
  - `--page-bg: #0c1626`
  - `--bg2: #10213a`
  - `--bg3: #152845`
  - `--paper: #10213a`
  - `--glass: rgba(10, 43, 87, 0.76)`
- Button hover uses `--button-bg-hover` so dark-mode hover state stays blue instead of drifting light.

## Verification cues
- If a button looks too light in dark mode, check for page-local overrides on:
  - `background`
  - `color`
  - `border-color`
- Prefer token-level fixes in `assets/site-colors.css` over one-off page patches.
- Verify dock/menu/CTA consistency together, because the shared shell now intentionally unifies them.

---
name: lp64-new-website-workflow
description: Creates new website projects with LP64 styling pre-injected (5 themes, CRT effects, Pokemon GB font)
---

# LP64 New Website Workflow

## Overview
Creates new website projects with LP64 styling pre-injected, including all 5 color variants, CRT effects, and Pokemon GB font.

## Trigger
User runs: `/new_website "$PROJECTTITLE"`

## What It Does
1. Creates proper folder structure under `websites/projects/$PROJECTTITLE`
2. Copies LP64 template with:
   - All 5 theme variants (Atomic Purple, Atomic Green, Acadian, Strays.sol, OG Grey)
   - CRT effects (scanlines, curvature, noise)
   - Pokemon GB font bundled in `assets/fonts/`
   - Theme switcher (Ctrl+Shift+T)
   - Boot sequence animation
   - Terminal interface with command execution
3. Auto-injects LP64 styling into `index.html`
4. Links to `LP64_stylepack.md` for design system reference

## Folder Structure Created
```
$PROJECTTITLE/
├── index.html          # LP64 terminal, theme-ready
├── css/
│   └── styles.css      # All 5 themes + CRT effects
├── js/
│   ├── app.js          # Main application logic
│   ├── terminal.js     # Terminal command handler
│   ├── theme.js        # Theme switcher
│   ├── boot.js         # Boot animation
│   ├── dom.js          # DOM utilities
│   └── filesystem.js   # Virtual filesystem
├── assets/
│   └── fonts/
│       └── PokemonGb-RAeo.ttf  ← Bundled!
└── README.md           # LP64 documentation
```

## Key Features
- **5 Color Variants**: Cycle with Ctrl+Shift+T
- **CRT Effects**: Scanlines, curvature, noise (configurable)
- **Boot Sequence**: Click power button → animation → terminal
- **Terminal Commands**: help, ls, cd, cat, grep, echo, pwd, whoami, clear
- **Theme Persistence**: Saves preference in localStorage
- **Font Bundled**: Pokemon GB font always included but not forced as default

## Usage Pattern
```bash
# Create new project
/new_website "My Project"

# Navigate and test
cd ~/ExoCortex/websites/projects/my_project
python -m http.server 5173

# Open browser to http://localhost:5173
# Press Ctrl+Shift+T to cycle themes
```

## Files to Reference
- `~/.hermes/skills/lp64-new-website-workflow/` - This skill
- `~/ExoCortex/websites/projects/LP64_stylepack.md` - Master design system doc
- `~/ExoCortex/websites/projects/project_template/` - Template source

## Pitfalls
- Don't force Pokemon GB as default font everywhere - only use where LP64 aesthetic is intended
- Theme switcher requires Ctrl+Shift+T or click on skin label
- Boot animation must complete before terminal becomes interactive
- Ensure `app.js` loads all dependencies before `terminal.js` attaches event listeners

## Testing
1. Verify all 5 themes cycle correctly
2. Test Enter key in terminal (should execute commands)
3. Check boot animation redirects properly
4. Confirm font loads without 404 errors

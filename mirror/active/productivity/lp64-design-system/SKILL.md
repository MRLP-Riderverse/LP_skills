---
name: lp64-design-system
description: Complete LP64 design system workflow — extraction, migration, scaffolding, terminal themes, and new website creation with 5 color variants (Atomic Purple, Atomic Green, Acadian, Strays.sol, OG Grey)
category: productivity
aliases: [lp64-design-system-extraction, lp64-styling-migration, lp64-project-scaffold, lp64-terminal-theme-wrapper, lp64-new-website-workflow]
---

# LP64 Design System Umbrella

This is the **class-level skill** for all LP64 terminal UI design work. It consolidates extraction, migration, scaffolding, terminal themes, and website creation workflows.

**Trigger:** User mentions LP64 styling, terminal UI themes, color variants (Atomic Purple/Green, Acadian, Strays.sol, OG Grey), theme switching, boot animations, or creating new websites with retro terminal aesthetic.

---

## Subsections

### A. Design System Extraction (from `lp64-design-system-extraction`)
Extract design specifications, color palettes, and SVG assets from existing web projects for reuse as CLI themes or design references.

**When to use:** Need to extract CSS variables, color palettes, or create CLI theme wrappers from existing projects.

**Key workflow:** CSS variable extraction → SVG asset generation → CLI theme wrapper creation → documentation assembly.

**See original:** Full extraction workflow preserved from `lp64-design-system-extraction` skill.

---

### B. Styling Migration (from `lp64-styling-migration`)
Migrate terminal-style web projects to LP64 design spec with 5 color variants, CRT effects, theme switching, and proper boot sequence.

**When to use:** User wants to "bring project up to date" with hello_world/LP64 styling, mentions color variants or theme switching.

**Key workflow:** Load LP64_terminal.md spec → backup current CSS → create new CSS with all 5 variants → update HTML structure → create theme switcher JS → create boot animation JS → update all HTML pages → verify installation.

**Critical:** Each variant must override ALL CSS custom properties. Boot.js must be loaded in HTML or boot animation won't work.

**See original:** Full migration workflow preserved from `lp64-styling-migration` skill.

---

### C. Project Scaffolding (from `lp64-project-scaffold`)
Create new website projects with LP64 retro terminal styling pre-configured.

**When to use:** User wants to create new website with LP64/retro terminal aesthetic or references "new idea" with personal design system.

**Critical prerequisite:** Template must be populated with LP64 assets BEFORE running `/new_website`. Empty template = broken workflow.

**Workflow:** `/new_website "Project Title"` → verify with `/scripts/verify_new_website.sh project_title` → test with `cd project_title && python -m http.server 5173`

**See original:** Full scaffolding workflow preserved from `lp64-project-scaffold` skill.

---

### D. Terminal Theme Wrapper (from `lp64-terminal-theme-wrapper`)
Create CLI theme wrapper for terminal emulators using LP64 aesthetic with persistent storage and auto-load functionality.

**When to use:** Need to create theme switcher CLI tool, apply ANSI color palettes dynamically, persist theme preferences across sessions.

**Key pattern:** ANSI escape codes for terminal colors + PS1 customization + XDG config storage + bashrc auto-load.

**Web pattern:** For browser-based terminal UI, use CSS custom properties + JavaScript theme switching with localStorage persistence.

**See original:** Full CLI and web theme patterns preserved from `lp64-terminal-theme-wrapper` skill.

---

### E. New Website Workflow (from `lp64-new-website-workflow`)
Complete workflow for creating new LP64-styled websites from scratch.

**When to use:** User wants to create a new website project with LP64 styling pre-injected.

**Key insight:** Uses `project_template/` with pre-populated LP64 assets. Template must be populated BEFORE creating projects.

**See original:** Full website creation workflow preserved from `lp64-new-website-workflow` skill.

---

## F. Acadie.sol Website Implementation\nCreate websites with OS/product interaction design principles rather than traditional web styling.\n\n**When to use:** User references Acadie.sol or wants a community-focused site with OS-inspired interaction patterns (docks, drawers, cards) rather than conventional website navigation.\n\n**Key workflow:**\n1. Start with OS/product interaction mindset: Think in terms of docks (persistent bottom navigation), drawers (contextual menus), and cards (information units) rather than headers, sidebars, and pages\n2. Implement unified CSS token system with semantic variable names (--ink, --muted, --blue-deep, --gold, etc.) and derive all colors from these base tokens\n3. Use mobile-first approach with min(430px, 100vw) containers and viewport units for responsive design\n4. Create reusable component patterns:\n   - Dock: Persistent bottom navigation with glassy/translucent appearance\n   - Drawer: Contextual menu that opens from dock items\n   - Card: Information unit with quick view (title + meta) and expanded state (full content + thumbnails)\n   - Poster: Edge-to-edge image surface with title overlay\n5. Implement data-driven rendering where possible (single template reading JSON data)\n6. Use progressive enhancement: HTML details/summary for expandable components that work without JS, enhanced with JS for additional features\n7. Apply OS-inspired interaction patterns: menus opening upward from dock items, glassmorphism effects, spatial consistency\n8. Ensure proper light/dark mode support with carefully balanced contrast ratios for readability\n9. Include clear code comments explaining each block's relation and modularity\n10. Maintain low-friction raw-preserving draft workflow for content creation\n\n**Critical:** \n- Remember that this is OS/product interaction design, not website styling - prioritize interaction patterns over visual decoration\n- Use semantic CSS variable names that describe purpose (--ink, --muted) rather than specific colors\n- Implement proper text color inheritance: body text should use --ink, secondary text --muted, accents --blue-deep/etc.\n- Ensure all interactive elements have sufficient contrast in both light and dark modes\n- Keep JavaScript unobtrusive - core functionality should work without JS\n\n---\n\n## Common Pitfalls (All LP64 Work)

1. **Newsletter/report projects are NOT terminal UI.** When the user wants a readable content publication (newsletter, report, news edition), do NOT default to the CRT terminal aesthetic. The user explicitly chose clean newsletter typography over retro terminal chrome for content publications. Use the `mardi-en-acadie-newsletter` skill's design system (Acadian flag colors, clean readable typography) for newsletters/reports. LP64 terminal UI is for apps, games, and interactive tools — not long-form reading.
2. **CSS Order:** Theme variant blocks must come AFTER :root defaults
2. **Complete Overrides:** Each variant must override ALL CSS custom properties
3. **Power Button:** Each theme needs power button and LED dot overrides
4. **Prompt Colors:** Ensure all 6 prompt segments have theme colors
5. **LocalStorage:** Use project-specific prefix (e.g., `agenttui-skin`)
6. **Shortcuts:** Ctrl+Shift+T to avoid browser conflicts
7. **Acadian Variant:** Blue-white-red prompt colors matching Acadian flag order
8. **Branding:** Use "Strays.sol" not "Strays" or "STRAYS NYC" for web3 alignment
9. **LED Dots:** Acadian variant needs three LED dots: blue → white → red
10. **Theme Count:** Now 5 variants, update all references
11. **boot.js Loading:** CRITICAL - must load boot.js in HTML or boot animation won't work
12. **Script Order:** app.js → boot.js → terminal.js → theme.js (exact order matters!)
13. **hello_world vs agentTUI:** Keep separate - hello_world is UI mock, agentTUI is full educational app
14. **Acadie.sol maturity pass:** When the user wants the site to feel less colorful, more mature, or "sable," prefer an off-black base around `#121212` for the page/background layer and let blue live mainly in cards, accents, and glow. This preserves Acadian blue identity without making the whole page feel loud.

---

## Verification Checklist

- [ ] All 5 variants defined in CSS (grep returns 15+ matches)
- [ ] Theme switches instantly with CSS custom properties
- [ ] Skin label is clickable
- [ ] Keyboard shortcut works (Ctrl+Shift+T)
- [ ] Theme persists in localStorage
- [ ] Boot animation works (click power button)
- [ ] CRT effects visible (scanlines, noise, bezel)
- [ ] Prompt has segmented colors
- [ ] Acadian variant has correct flag color order
- [ ] Strays.sol branding (not "STRAYS NYC")
- [ ] Educational commands work (agentTUI only)
- [ ] Script order in HTML is correct

---

## Related Skills

- `agenttui-maintenance` - agentTUI educational app maintenance
- `ascii-art` - terminal-based visual elements
- `design-md` - DESIGN.md file authoring
- `css-master` - CSS and layout questions

---

*Consolidated: May 2026*
*Source skills: lp64-design-system-extraction, lp64-styling-migration, lp64-project-scaffold, lp64-terminal-theme-wrapper, lp64-new-website-workflow*

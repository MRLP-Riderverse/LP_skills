---
name: agenttui-maintenance
description: Complete agentTUI educational terminal app maintenance — structure, boot flow, styling updates, and recovery workflows for LP64 terminal UI with 5 color variants.
category: software-development
aliases: [agenttui-structure-and-boot-flow, agenttui-styling-recovery, agenttui-styling-update]
---

# agentTUI Maintenance Umbrella

This is the **class-level skill** for maintaining the agentTUI educational terminal app. It consolidates structure documentation, boot flow management, styling updates, and recovery workflows.

**Trigger:** User wants to update agentTUI with LP64 styling, troubleshoot boot/terminal flow issues, add new color variants, or recover from broken styling updates.

---

## Subsections

### A. Structure & Boot Flow (from `agenttui-structure-and-boot-flow`)
Maintain the correct structure and flow for agentTUI educational terminal app.

**Critical Architecture - Two-Page Flow:**
1. **landing.html** - Entry point with boot animation
   - Has power button (`#boot-btn`)
   - Shows boot sequence animation
   - Redirects to terminal.html after animation completes
   - Loads: `boot.js`, `theme.js`, `landing.js`

2. **terminal.html** - Actual interactive terminal
   - Has terminal interface (NO boot button)
   - User can type commands
   - Loads: `app.js`, `terminal.js`, `theme.js`
   - Must NOT load `boot.js` (already booted!)

**Required DOM Elements (terminal.html):**
```html
<div id="terminal-window">
 <div id="terminal-chrome">...</div>
 <div id="terminal-screen" tabindex="0">
 <div id="terminalOutput"></div>
 <div id="promptLabel" class="prompt">
 <span class="prompt-user">agent</span>
 <span class="prompt-at">@</span>
 <span class="prompt-host">terminal</span>
 <span class="prompt-colon">:</span>
 <span class="prompt-path">~</span>
 <span class="prompt-dollar">$</span>
 </div>
 <input type="text" id="terminalInput" class="terminal-input" />
 </div>
</div>
```

**Boot Sequence Flow:**
```
index.html → redirects to landing.html
 → user clicks power button
 → boot.js animation plays (1.5s)
 → boot.js redirects to terminal.html
 → terminal.html loads with input field ready
 → user can type commands
```

**Critical:** boot.js MUST include redirect logic:
```javascript
setTimeout(() => {
 if (bootOverlay) {
 bootOverlay.classList.remove('closing');
 }
 setTimeout(() => {
 window.location.href = './terminal.html';
 }, 300);
}, 1500);
```

**Theme Cycling:** All pages load `theme.js` for 5 color variants (Atomic Purple, Atomic Green, Acadian, Strays.sol, OG Grey). Keyboard shortcut: `Ctrl+Shift+T`.

**See original:** Full structure documentation preserved from `agenttui-structure-and-boot-flow` skill.

---

### B. Styling Recovery (from `agenttui-styling-recovery`)
Recovery workflow for agentTUI when styling updates break terminal functionality.

**Trigger:** User requests LP64/hello_world styling updates to agentTUI project, especially after disconnect or when terminal becomes non-functional.

**Pre-Update Checklist:**
1. Verify current working state: `cd agentTUI && python -m http.server 5174`
2. Test: power button → boot animation → terminal → type "help" + Enter
3. Document current structure: save copy of `pages/terminal.html`, note script load order

**Styling Update Process:**
1. **Update CSS Only First** - Copy new styles from hello_world or LP64_terminal.md, add theme variants
2. **Verify HTML Structure Preserved** - Do NOT change HTML structure unless absolutely necessary!
3. **Script Loading Rules** - MUST follow exact order: app.js first (manages deps), then theme.js
4. **Test After Each Change** - Refresh → click power → wait for redirect → type `help` + Enter

**Recovery Workflows:**

**Symptom: Power button animation plays but terminal never loads**
- **Fix:** Ensure boot.js has redirect logic to terminal.html

**Symptom: Terminal loads but Enter key does nothing**
- **Diagnosis:** Check for duplicate script loading or broken function calls
- **Fix:** Remove `<script src="../js/terminal.js">` from HTML, remove `A.runBoot()` call from app.js

**Symptom: "Weird text box" appears instead of clean terminal**
- **Problem:** Input field has visible borders/background
- **Fix:** Apply `background: transparent; border: none; outline: none;`

**Symptom: DOM element not found errors**
- **Check:** All required elements in dom.js must exist in HTML
- **Fix:** Add hidden placeholders for missing elements

**See original:** Full recovery workflow preserved from `agenttui-styling-recovery` skill.

---

### C. Styling Update (from `agenttui-styling-update`)
Update agentTUI with LP64 styling variants and troubleshoot boot/terminal flow issues.

**Common Issues & Solutions:**

**Issue 1: Boot Animation Plays But No Terminal Appears**
- **Symptom:** User clicks power button, animation plays, but stays on landing page
- **Root Cause:** boot.js lacks redirect logic to terminal.html
- **Fix:** Add redirect in boot.js after animation completes

**Issue 2: terminal.html Has Wrong Structure**
- **Symptom:** terminal.html shows boot button instead of terminal input field
- **Root Cause:** terminal.html structured like landing page
- **Fix:** Replace with proper terminal interface structure (input field, no boot button)

**Issue 3: app.js Calls Non-Existent Function**
- **Symptom:** Console error: `A.runBoot is not a function`
- **Root Cause:** app.js calls `A.runBoot()` which doesn't exist
- **Fix:** Remove the call entirely

**Adding New Color Variants:**
1. Add CSS variables in `html[data-skin="name"]` block
2. Update theme.js SKINS array and SKIN_NAMES mapping
3. Add skin label color for new variant
4. Add power button styling for new variant
5. Test theme cycling (Ctrl+Shift+T)

**File Structure Reference:**
```
agentTUI/
├── index.html → redirects to landing.html
├── pages/
│ ├── landing.html → Entry point with boot animation
│ ├── terminal.html → Actual terminal interface (MUST have input field)
│ └── about.html → Info page
├── js/
│ ├── app.js → Main app, lessons, filesystem init
│ ├── boot.js → Boot animation + redirect to terminal
│ ├── terminal.js → Command parser, input handling
│ ├── theme.js → Color theme cycling (Ctrl+Shift+T)
│ ├── filesystem.js → Virtual filesystem
│ ├── lessons.js → Lesson content
│ └── dom.js → DOM utilities
└── css/
 └── styles.css → All styles + theme variants
```

**See original:** Full styling update workflow preserved from `agenttui-styling-update` skill.

---

## Common Mistakes to Avoid

1. ❌ Loading `boot.js` on terminal.html (only needed on landing.html)
2. ❌ Putting boot button structure on terminal.html
3. ❌ Forgetting redirect logic in boot.js
4. ❌ Calling `A.runBoot()` which doesn't exist
5. ❌ Not testing full user flow after styling updates
6. ❌ Loading terminal.js twice (HTML + dynamic loader)
7. ❌ Missing required DOM elements
8. ❌ Wrong script order (app.js must load first)
9. ❌ Styling input field with visible borders

---

## Testing Checklist

After any styling update, verify:
- [ ] Landing page loads correctly
- [ ] Power button triggers animation
- [ ] Animation redirects to terminal.html (CRITICAL)
- [ ] Terminal page shows INPUT FIELD (not boot button)
- [ ] Can type commands
- [ ] `help` command works
- [ ] `ls` lists files
- [ ] Theme cycling works (Ctrl+Shift+T)
- [ ] All 5 variants display correctly
- [ ] Prompt colors change per theme

---

## Quick Fix Commands

```bash
# Check if boot.js has redirect logic
grep -n "terminal.html" js/boot.js

# Check if terminal.html has input field
grep -n "terminalInput" pages/terminal.html

# If missing, restore proper structure
```

---

## Success Indicators

✅ User can click power → animation → terminal appears
✅ User can type `help` and get response
✅ Theme cycling works without breaking functionality
✅ All 5 variants (purple, green, acadian, strays, grey) work
✅ Prompt colors change per theme

---

## Related Skills

- `lp64-design-system` - LP64 design system and theming
- `static-site-prototype-iteration` - Static site prototyping
- `css-master` - CSS and layout questions

---

*Consolidated: May 2026*
*Source skills: agenttui-structure-and-boot-flow, agenttui-styling-recovery, agenttui-styling-update*

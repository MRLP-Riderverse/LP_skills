---
name: strays-branding-pass
description: Apply the hello_world terminal/brand aesthetic to Strays web projects - dark shell, neon green accents, flat pixel-friendly colors, reduced visual noise.
created: 2026-04-23
---

# Strays Branding Pass - hello_world Style

## When to Use
- User has a Strays NFT virtual pet website project
- Need to align visual design with the hello_world terminal aesthetic
- User wants darker, cleaner, more focused UI with less gradient noise

## Core Changes

### 1. Color Palette Reset
```css
:root {
  /* Core shell - deep purple-black */
  --bg: #05040a;
  --bg-soft: #0a0914;
  --panel: rgba(10, 9, 20, 0.92);
  --panel-strong: rgba(18, 16, 35, 0.96);
  
  /* Lines and text */
  --line: rgba(126, 247, 212, 0.18);
  --text: #e8e6ff;
  --muted: #8b87a8;
  
  /* Accents - neon green primary, pink as Strays signature */
  --accent: #7ef7d4;        /* neon green - primary signal */
  --accent-2: #ff5fc9;      /* pink - Strays brand accent */
  --accent-3: #8a7dff;      /* purple - subtle highlight */
}
```

### 2. Background Simplification
**Before:** Multiple radial gradient layers creating visual noise
**After:** Simple linear gradient, deep purple-black base
```css
/* Remove stacked radial gradients */
html {
  background: linear-gradient(180deg, #07060e 0%, #030208 100%);
}

body {
  background: linear-gradient(160deg, #05040a 0%, #0a0814 60%, #04030a 100%);
}
```

### 3. Cat Sprite - Flat Color Approach
**Key principle:** Replace gradients with solid colors for pixel-art feel

**Head & Body:**
```css
/* Before: gradient */
background: linear-gradient(180deg, #cffff2, #7ef7d4 55%, #43bfa2 100%);

/* After: flat */
background: #c8ffc8;  /* head - light mint */
background: #ff7eff;  /* body - pink Strays signature */
```

**Collar, Tag, Tail:**
```css
/* Collar: neon green signal */
background: #7ef7d4;

/* Tag: pink with dark text */
background: #ff7eff;
color: #05040a;

/* Tail: solid pink */
background: #ff7eff;
```

### 4. CRT/Screen Effects - Reduced
```css
/* Simplified screen background */
.catcard__screen {
  background: linear-gradient(180deg, #0a0f12 0%, #040607 100%);
  border: 1px solid rgba(126, 247, 212, 0.18);
  box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.4), 0 14px 28px rgba(0, 0, 0, 0.4);
}

/* Subtler scanlines */
.catcard__scan {
  background: linear-gradient(180deg, transparent 0 48%, rgba(255, 255, 255, 0.03) 49%, transparent 50% 100%);
  background-size: 100% 4px;
  opacity: 0.15;  /* was 0.22 */
}
```

### 5. Panel/Window Chrome
```css
/* Cleaner panel backgrounds */
.catcard,
.catlog {
  background: rgba(10, 9, 20, 0.6);
  border: 1px solid rgba(126, 247, 212, 0.12);
  border-radius: 20px;
}

/* Simpler window chrome */
.catwindow__chrome {
  background: rgba(10, 9, 20, 0.8);
  border-bottom: 1px solid rgba(126, 247, 212, 0.12);
}
```

## Visual Hierarchy Principles
1. **Focal point first:** Cat sprite should be highest contrast element
2. **One primary accent:** Neon green (#7ef7d4) for signals, borders, prompts
3. **Signature accent sparingly:** Pink (#ff5fc9) for Strays brand moments (body, tag, nose)
4. **Reduce decoration:** Remove extra glows, simplify shadows, flatten gradients
5. **Dark shell base:** Everything sits on deep purple-black, not generic dark gray

## Common Pitfalls
- **Don't** stack multiple radial gradients - creates muddy noise
- **Don't** use soft gradient transitions on cat sprite - breaks pixel-art illusion
- **Don't** make borders too bright - keep them subtle (0.12-0.18 alpha)
- **Don't** forget the pink accent - it's the Strays signature, even if green is primary
- **Don't** use Pokemon GB font for symbols like `@`, `$` - route to system monospace
- **Don't** skip padding guard rails - text needs 4px minimum from container edges

## Advanced Refinements (Post-Brand Pass)

### Font Size & Readability
```css
body {
 font-size: 0.9rem; /* 10% reduction from default */
}
```
- Reduces visual "clunkiness"
- Helps eyes focus on content hierarchy

### Padding Guard Rails
```css
:root {
 --space-1: 4px;  /* minimum text padding */
 --space-2: 8px;  /* small gaps */
 --space-3: 12px; /* medium gaps */
 --space-4: 16px; /* card padding */
 --space-5: 20px; /* large gaps */
 --border-width: 2px;
}

/* Global text padding */
p, h1, h2, h3, span, label, strong, em {
 padding-left: var(--space-1);
 padding-right: var(--space-1);
}
```

### Thicker, Colored Borders
```css
/* All containers get 2px neon green borders */
.catcard, .catlog, .catcard__screen, .crt-screen {
 border: var(--border-width) solid rgba(126, 247, 212, 0.25);
}

/* Meta boxes, quotes, list items */
.catmeta, .catcard__quote, .catlog__list li {
 border: var(--border-width) solid rgba(126, 247, 212, 0.15);
}
```

### Symbol Font Routing
```css
/* Route symbols to system font */
.symbol, .prompt-symbol, .prompt-prefix {
 font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}
```
```html
<!-- Wrap prompts with symbols -->
<span class="prompt-prefix">strays@solana$</span>
```

### Custom Favicon
Create `assets/favicon.svg` with simple "-.-" cat face:
- 32x32px SVG
- Dark purple-black background
- Mint green cat face, closed eyes, pink nose
- Add to `<head>`: `<link rel="icon" type="image/svg+xml" href="assets/favicon.svg" />`

## Verification
After applying changes:
1. Page should feel darker and more focused
2. Cat should pop as the clear focal point
3. Neon green should guide the eye (borders, prompts, status)
4. Pink should appear as accent (cat body, tag, nose, close button)
5. No competing gradient layers or muddy backgrounds
6. Text should have breathing room (4px+ padding)
7. Borders should be visible but not overwhelming (2px, ~0.15-0.25 alpha)
8. Symbols (@, $) should render cleanly in system font
9. Browser tab should show custom cat favicon

## Files Modified
- `css/styles.css` - main stylesheet
- `index.html` - favicon link, symbol wrappers
- `assets/favicon.svg` - custom browser icon (new file)
- Key selectors: `:root`, `.cat-sprite__*`, `.catcard__screen`, `.catwindow__chrome`, `.catprompt__bar`, `.catmeta`

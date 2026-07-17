# Fixed header safe area + mobile search chrome

Use this when a shared shell adds a fixed top header and a fixed bottom dock/search surface across multiple static pages.

## Pattern

### 1) Fixed top header must be compensated globally
If the shell injects a fixed banner/header on every page, the content offset belongs in the shared shell CSS, not in one page's local layout.

Preferred pattern:

```css
.site-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: calc(20px + env(safe-area-inset-top));
  padding-top: env(safe-area-inset-top);
}

body {
  padding-top: calc(20px + env(safe-area-inset-top));
}
```

Why:
- prevents overlap across all pages, not just the page you happened to be looking at
- keeps notch-safe behavior aligned with the actual header geometry
- avoids page-specific compensation drift

## 2) Search chrome and keyboard: hide dock, not input bar
For a fixed search control that sits above a fixed bottom dock on mobile:
- keyboard-open state should hide/duck the dock
- keep the search controls pinned in their normal lane while typing
- dismiss the keyboard on explicit user intent: Enter, blur, or meaningful result-scroll

Anti-pattern:

```css
body.keyboard-open .search-controls {
  bottom: 14px;
}
```

That moves the input into the keyboard lane and makes it look like results/typing caused the bar to drop.

Preferred pattern:

```css
body.keyboard-open .site-dock {
  transform: translateX(-50%) translateY(200px);
  opacity: 0;
  pointer-events: none;
}
```

Keep the search controls at their normal `bottom` value.

## 3) Live header counts from exported site payloads
If the shell banner should show site-wide counts, fetch the exported JSON once from the shared shell script and sync the header text after load.

Useful payload fields seen in this project:
- `assets/directory-data.json` → `published_count` (fallback: `entry_count`, then `items.length`)
- `assets/events-data.json` → `active_count` (fallback: `event_count`, then `items.length`)

Pattern:
- inject a stable header span/id from the shared shell renderer
- load both payloads in the shared shell JS
- update the header text in the same `syncShell()` path that already handles language/theme changes

## Verification checklist
- header does not overlap first visible content on index, events, search, or other top-level pages
- on desktop/safe-area=0, computed header height and body padding still match the intended base height
- on iPhone/notch devices, the header does not collide with the unsafe top inset
- while typing in mobile search, the dock can hide but the search bar does not jump downward
- Enter / blur / result-scroll can dismiss the keyboard without repositioning the search controls under it

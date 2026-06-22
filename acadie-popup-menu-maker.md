---
name: acadie-popup-menu-maker
version: 1.0.0
description: Build Acadie.sol popup menus, filter popovers, and search surfaces following the site's established glass/blur design system.
---

# Acadie.sol Popup Menu & Filter Maker

Create filter popovers, search surfaces, and popup menus for Acadie.sol pages that match the established visual language.

## Design Token Contract

All popups use site-colors.css tokens. Key ones:
- `--glass`, `--paper`, `--paper-soft`, `--panel-strong` — surfaces
- `--line`, `--line-strong` — borders
- `--gold`, `--acadian-yellow` — accent labels
- `--button-bg`, `--button-bg-hover`, `--button-fg`, `--button-border` — pill buttons
- `--muted` — secondary text
- `--shadow` — depth

## Filter Popover Pattern (from directory.html)

**HTML structure:**
```html
<div class="filter-popover" id="my-filter-popover" hidden>
  <div class="filter-backdrop" id="my-filter-backdrop" aria-hidden="true"></div>
  <div class="filter-sheet" role="dialog" aria-modal="true" aria-label="Filters">
    <div class="filter-title">
      <span id="my-filter-title-label">Filters</span>
      <button id="my-filter-close" type="button" aria-label="Close filters">✕</button>
    </div>
    <div class="control-grid">
      <!-- filter controls go here -->
    </div>
  </div>
</div>
```

**CSS (inline on page):**
```css
.filter-popover {
  position: fixed; inset: 0; z-index: 55;
  display: grid; place-items: center; padding: 16px;
  background: rgba(8, 18, 40, 0.24);
  backdrop-filter: blur(10px) saturate(1.05);
  -webkit-backdrop-filter: blur(10px) saturate(1.05);
}
.filter-popover[hidden] { display: none; }
.filter-backdrop { position: absolute; inset: 0; }
.filter-sheet {
  position: relative; z-index: 1;
  width: min(560px, 100%);
  display: grid; align-content: start; gap: 9px; padding: 14px;
  border: 1px solid var(--line-strong); border-radius: 18px;
  background: color-mix(in srgb, var(--panel-strong) 96%, transparent);
  box-shadow: 0 22px 48px rgba(5,13,27,0.42);
}
.filter-title {
  display: flex; justify-content: space-between; align-items: center; gap: 10px;
  color: var(--gold); font-weight: 900; text-transform: uppercase;
  letter-spacing: 0.08em; font-size: 0.78rem;
}
.filter-title button {
  background: none; border: none; color: var(--muted);
  font-size: 1.1rem; cursor: pointer; padding: 4px;
}
```

**JS open/close (inline on page):**
```js
function openFilterPopover() {
  document.getElementById('my-filter-popover').hidden = false;
  document.documentElement.classList.add('filters-open');
}
function closeFilterPopover() {
  document.getElementById('my-filter-popover').hidden = true;
  document.documentElement.classList.remove('filters-open');
}
document.getElementById('my-filter-trigger')?.addEventListener('click', openFilterPopover);
document.getElementById('my-filter-close')?.addEventListener('click', closeFilterPopover);
document.getElementById('my-filter-backdrop')?.addEventListener('click', closeFilterPopover);
```

Also add to page CSS:
```css
html.filters-open { overflow: hidden; }
```

## Search Surface Pattern (from directory.html)

**HTML:**
```html
<section class="search-header" aria-label="Search and filter">
  <div class="search-surface-actions">
    <button class="search-pill" type="button">Pill Label</button>
  </div>
  <section class="control-panel glass">
    <div class="control-body">
      <div class="control-grid search-shell">
        <div class="search-field">
          <input id="my-search" class="search" type="search" autocomplete="off"
                 enterkeyhint="search" placeholder="Search…" aria-label="Search" />
          <button class="search-clear" id="my-search-clear" type="button"
                  aria-label="Clear search" hidden>×</button>
        </div>
      </div>
    </div>
  </section>
</section>
```

**Key CSS:**
```css
.search-surface-actions {
  display: flex; flex-wrap: wrap; gap: 8px;
  margin: 0 0 2px; padding: 0 2px; justify-content: flex-end;
}
.search-pill {
  border-radius: 999px; padding: 6px 10px; font-size: 0.74rem;
  width: auto; min-height: 0; white-space: nowrap;
  border: 1px solid var(--button-border); background: var(--button-bg);
  color: var(--button-fg); font: inherit; font-weight: 900; cursor: pointer;
}
.search-pill.active, .search-pill[aria-pressed="true"] {
  background: var(--button-bg-hover);
}
.control-panel { border-radius: 20px; overflow: clip; }
.control-body { padding: 12px; display: grid; gap: 10px; }
.search-shell { display: grid; gap: 7px; width: 100%; }
.control-grid.search-shell { grid-template-columns: minmax(0, 1fr); }
.search-field { position: relative; width: 100%; }
.search {
  width: 100%; min-width: 0; padding: 12px 44px 12px 13px;
  border-radius: 13px; border: 1px solid var(--line-strong);
  background: rgba(8, 18, 40, 0.3); color: var(--text);
  font: inherit; font-size: 16px; outline: none;
}
.search::placeholder { color: color-mix(in srgb, var(--muted) 72%, transparent); }
.search-clear {
  position: absolute; top: 50%; right: 10px; transform: translateY(-50%);
  width: 28px; height: 28px; padding: 0; border-radius: 999px;
  font-size: 1rem; line-height: 1; display: grid; place-items: center;
  background: color-mix(in srgb, var(--paper) 86%, transparent);
  border-color: var(--line); box-shadow: 0 6px 14px rgba(5,13,27,0.12);
  cursor: pointer;
}
.search-clear[hidden] { display: none; }
```

**Search JS:**
```js
document.getElementById('my-search')?.addEventListener('input', function(e) {
  state.searchQuery = e.target.value;
  document.getElementById('my-search-clear').hidden = !e.target.value;
  renderItem_list(); // re-render with filter
});
document.getElementById('my-search-clear')?.addEventListener('click', function() {
  const input = document.getElementById('my-search');
  if (input) { input.value = ''; state.searchQuery = ''; this.hidden = true; renderItem_list(); }
});
```

## Type Filter Buttons

Pill-shaped toggle buttons for filtering by type (events, entries, drafts, posts):

```html
<button class="search-action filter-type-btn" data-filter="recent" type="button">10 Recent</button>
<button class="search-action filter-type-btn" data-filter="event" type="button">Events</button>
<button class="search-action filter-type-btn" data-filter="entry" type="button">Entries</button>
<button class="search-action filter-type-btn" data-filter="draft" type="button">Drafts</button>
<button class="search-action filter-type-btn" data-filter="post" type="button" hidden>Posts</button>
```

**CSS:**
```css
.filter-type-btn {
  border-radius: 999px; padding: 8px 12px; font-size: 0.8rem;
  width: auto; min-height: 0; white-space: nowrap;
  border: 1px solid var(--button-border); background: var(--button-bg);
  color: var(--button-fg); font: inherit; font-weight: 900; cursor: pointer;
  transition: background .15s ease, color .15s ease, border-color .15s ease;
}
.filter-type-btn.active, .filter-type-btn[aria-pressed="true"] {
  background: var(--button-bg-hover);
}
```

**JS sync + set:**
```js
function syncFilterBtns() {
  document.querySelectorAll('.filter-type-btn').forEach(btn => {
    const isActive = btn.dataset.filter === state.filterMode;
    btn.classList.toggle('active', isActive);
    btn.setAttribute('aria-pressed', isActive);
  });
}
function setFilterMode(mode) {
  state.filterMode = mode;
  closeFilterPopover();
  syncFilterBtns();
  renderList();
}
document.querySelectorAll('.filter-type-btn').forEach(btn => {
  btn.addEventListener('click', () => setFilterMode(btn.dataset.filter));
});
```

## i18n Pattern

Add filter/search strings to both `en` and `fr` copy objects:
```js
// en
filterBtn: 'Filters', filterTitle: 'Filters',
filterRecent: '10 Recent', filterEvents: 'Events',
filterEntries: 'Entries', filterDrafts: 'Drafts', filterPosts: 'Posts',
searchPlaceholder: 'Search updates…',

// fr
filterBtn: 'Filtres', filterTitle: 'Filtres',
filterRecent: '10 récents', filterEvents: 'Événements',
filterEntries: 'Entrées', filterDrafts: 'Brouillons', filterPosts: 'Publications',
searchPlaceholder: 'Rechercher des mises à jour…',
```

Wire in `updateStaticCopy()`:
```js
setText('filter-title-label', c.filterTitle);
document.querySelectorAll('.filter-type-btn[data-filter="recent"]').forEach(b => b.textContent = c.filterRecent);
// …same for each data-filter value
const searchInput = document.getElementById('my-search');
if (searchInput) searchInput.placeholder = c.searchPlaceholder;
```

## Fixed Positioning Pitfall

**Never** use `position: fixed` + `left: 50%` + `transform: translateX(-50%)` on docks, drawers, or fixed overlays. The `transform` creates a new containing block that breaks `position: fixed` in ancestors and causes the element to shift on scroll on mobile.

**Correct pattern:**
```css
.site-dock {
  position: fixed;
  left: 0; right: 0;
  bottom: max(12px, env(safe-area-inset-bottom));
  margin: 0 auto;
  width: min(390px, calc(100vw - 28px));
}
```

This centers via auto-margin instead of transform, keeping the fixed positioning pure.

## Checklist

Before marking a popup/search implementation done:
- [ ] HTML: popover with `hidden`, backdrop, sheet, title row with close button
- [ ] CSS: `.filter-popover`, `.filter-backdrop`, `.filter-sheet`, `.filter-title`, `html.filters-open { overflow: hidden }`
- [ ] JS: `openFilterPopover()`, `closeFilterPopover()` with `filters-open` class toggle
- [ ] JS: backdrop + close button wired to `closeFilterPopover()`
- [ ] Search input: `input` event → update state + toggle clear button + re-render
- [ ] Search clear: `click` → reset input + state + hide clear + re-render
- [ ] Filter pills: `data-filter` attribute, `syncFilterBtns()` for active state
- [ ] i18n: both `en` and `fr` copy strings populated, wired in `updateStaticCopy()`
- [ ] No `transform: translateX(-50%)` on any `position: fixed` element

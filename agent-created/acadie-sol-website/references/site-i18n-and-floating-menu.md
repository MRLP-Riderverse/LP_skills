# Site i18n + floating menu lessons

Use this when fixing Acadie.sol language toggles, duplicated menu shells, or dock/floating-menu UI.

## i18n verification checklist
- Search every visible page for hardcoded English strings after adding language toggles. Static hero/header copy often has no IDs and will not update unless explicitly wired into the page copy map.
- Cover both static DOM text and dynamic renderer text:
  - page titles and hero eyebrow/title/lede
  - drawer title/subtitle
  - nav/dock labels
  - search placeholders and filter labels
  - result count copy and empty states
  - card detail labels (`Address`, `Hours`, `Phone`, `Email`, `Website`)
  - date fallback strings (`Date TBD`, `Timestamp unavailable`)
- Prefer a page-local copy object (`HOME_COPY`, `EVENTS_COPY`, `DIR_COPY`) plus guarded helpers:
  ```js
  function setText(id, value) {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
  }
  ```
- On language toggle, update static copy and then re-render dynamic sections. If the handler calls a wrapper like `renderDirectory()`, confirm that wrapper actually exists.
- Use `Intl.DateTimeFormat(currentLang(), ...)` for page dates rather than `undefined`, so month/day labels follow the active language.

## Localized card labels pitfall
Do not use the displayed label text to decide link behavior after translation. This breaks when `Phone` becomes `Téléphone` or `Address` becomes `Adresse`.

Use stable row types and localized labels separately:
```js
const detailRows = [
  ['address', copy().address, contactValue(item, 'address')],
  ['hours', copy().hours, contactValue(item, 'hours')],
  ['phone', copy().phone, contactValue(item, 'phone')],
  ['email', copy().email, contactValue(item, 'email')],
].filter(([, , value]) => cleanSummary(value));

function renderDetailValue(type, value) {
  if (type === 'phone') return phoneLink(value);
  if (type === 'address') return mapLink(value);
  if (type === 'email') return emailLink(value);
  return escapeHtml(value);
}
```

## Floating menu pattern
The bottom dock owns navigation, so the menu should be a centered floating panel, not a side drawer.

- Use a hidden checkbox (`.menu-toggle`) and backdrop label to keep the lightweight no-framework interaction.
- Keep backdrop and drawer checked-state rules separate. Do not apply drawer transforms to the backdrop.
  ```css
  .menu-toggle:checked ~ .drawer-backdrop {
    opacity: 1;
    pointer-events: auto;
  }

  .menu-toggle:checked ~ .drawer {
    opacity: 1;
    pointer-events: auto;
    transform: translate(-50%, 0) scale(1);
  }
  ```
- Backdrop should dim + blur the page:
  ```css
  background: rgba(26, 20, 16, .38);
  backdrop-filter: blur(5px) saturate(.92);
  -webkit-backdrop-filter: blur(5px) saturate(.92);
  ```
- Put compact controls in the floating panel’s top corners:
  - theme top-left: `☾` in light mode, `☼` in dark mode
  - close centered: `×`
  - language top-right: `EN / FR`
- Keep “Full directory” and “About Acadie.sol” lower in the panel so the top row reads as system controls and the lower area reads as navigation.

## Verification probes
After editing, verify all three main pages (`index.html`, `events.html`, `directory.html`):
- Toggle English/French and assert representative text changes on each page.
- Toggle light/dark and assert the icon switches `☾` ↔ `☼`.
- Open menu and assert the backdrop covers the viewport without a right-side shifted overlay.
- Run `git diff --check` and a simple HTML parse.
- If browser automation is available, capture mobile screenshots with menu open and language toggled.

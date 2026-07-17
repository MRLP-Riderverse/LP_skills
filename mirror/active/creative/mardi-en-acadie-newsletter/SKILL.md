---
name: mardi-en-acadie-newsletter
description: Recurring Acadian diaspora newsletter - Mardi en Acadie edition production, design system, project scaffold, and workflow
aliases: [mardi-acadie, acadian-newsletter]
---

# Mardi en Acadie! — Newsletter Production

**Trigger:** User mentions "Mardi en Acadie", "mardi_acadie", Acadian newsletter, wants to produce a new edition, update the newsletter, or review/revise an existing edition.

## Project Location

`~/ExoCortex/websites/projects/mardi_acadie_web_news/`

## Design System — Acadian Flag Palette

The newsletter uses the Acadian flag colors (blue, white, red) + gold as a warm accent. **This is a clean newsletter style, NOT the LP64 CRT terminal aesthetic.** The user explicitly chose readable typography over retro terminal chrome for content publications. Dark blue background, red headers, gold subheaders, white body text.

| Element | Color | Hex |
|---------|-------|-----|
| Background | Dark Navy | `#0a1628` |
| Surface | Lighter Blue | `#0f1f38` |
| Card BG | Navy Card | `#112240` |
| Headers | Acadian Red | `#c62828` / bright `#e53935` |
| Subheaders | Gold-Yellow | `#d4a017` / bright `#f5c542` |
| Body Text | Off-White | `#e8e8e8` |
| Links | Light Blue | `#5b9bd5` |
| Borders | Muted Blue | `#1a2d4a` |

## Header Format (Every Edition)

```html
<header class="newsletter-header">
  <h1>Mardi en Acadie!</h1>
  <p class="author-line">created by : Acadie.sol</p>
  <p class="date-line">Edition XXX · MONTH DAY, YEAR · Covering DATE–DATE</p>
</header>
```

- Title is always "Mardi en Acadie!" (with exclamation)
- Author line is always "created by : Acadie.sol" (exact format, colon with spaces)
- Date line shows edition number, creation date, coverage date range

## Edition Production Workflow

1. **Source material:** QuickThoughts (since last edition), Hermes sessions, cron outputs (Mardi en Acadie 4-branch crons), any research reports
2. **Copy template:** `editions/_template.html` → `editions/YYYY-MM-DD-to-DD.html`
3. **Identify sections:** Group by theme/topic, not just chronology. Each section gets a numbered `#section-slug` ID for the TOC
4. **Build clickable TOC:** Every section appears in the `<nav class="toc">` with smooth-scroll links
5. **Fill content:** Use `timeline-entry` for dated events, `callout` for key insights, `quote-block` for direct quotes from QuickThoughts
6. **Add to archive:** Update `index.html` with new edition entry
7. **Share:** Copy standalone edition to `/tmp/` for Telegram delivery. Editions are self-contained (all CSS inlined) so they work offline

## Content Structure Components

- **`.tricolore`** — Sticky top bar in Acadian flag colors (blue-white-red). Always present.
- **`.toc`** — Table of contents with diamond bullet markers, red bullets, gold highlight on hover/active
- **`.section`** — Each major topic, with `<h2>` (red, numbered), `<h3>` (gold subheaders)
- **`.timeline-entry`** — Dated event cards with entry-date + entry-title + body
- **`.callout`** — Highlighted insight boxes (`.callout-red` for critical, `.callout-gold` for insights, default for neutral)
- **`.quote-block`** — Direct quotes from QuickThoughts or sessions, with `.attribution`
- **`.finale`** — End-of-edition summary statement, centered, gradient background

## Editions as Self-Contained HTML

Each edition inlines all CSS so the file works standalone — no external stylesheet, no fonts to load, no JS deps beyond the inline scroll/TOC script. This is intentional: the user shares these via Telegram as file attachments, and they need to render in mobile browsers without network.

The `css/styles.css` and `js/navigation.js` files exist for the **archive landing page** (`index.html`) which lives on a server. Individual editions must be self-sufficient.

## The Four Branches

Editions cover the Acadian diaspora across four branches, matching the cron system:

1. **Acadie** — New Brunswick / Nova Scotia (6:00 AM Tuesday cron)
2. **Acadiana** — Louisiana Cajuns (6:15 AM Tuesday cron)
3. **Nouvelle-Aquitaine** — Dax, Tarbes, Pau-Bearn, old roots (6:30 AM Tuesday cron)
4. **Quebec-Acadie** — Bridge branch (~6:45 AM Tuesday cron)

Cross-relation patterns to watch: language erosion gradient, rural desenclavement, cultural festivals as identity anchors, self-sovereignty instincts, education access.

## Pitfalls

- **Do NOT use LP64 CRT terminal aesthetic** for editions. The user explicitly chose clean newsletter typography over retro terminal chrome. The LP64 Acadian variant exists for apps/games; this is a publication. When the user says "newsletter style" or "clean readable," that overrides any default LP64 styling impulse.
- **Always include the clickable TOC.** The user specifically requested a content index so readers know what to expect and can jump to sections.
- **Author format is exact:** `created by : Acadie.sol` — not "by Acadie.sol", not "Created by: Acadie.sol", not "Acadie.sol" alone.
- **Self-contained editions.** Inline the CSS. Don't rely on external files for the edition HTML. The archive page can use shared assets.
- **Section numbering.** Use `<span class="sec-num">01</span>` format with zero-padded numbers. Matches the TOC structure.
- **Gold color is for emphasis/subheaders only.** Don't overuse it. Red is for headers, gold is for subheaders and accents, white is for body.

## Related Skills

- `lp64-design-system` — The LP64 terminal aesthetic. Same project directory (`websites/projects/`), different visual treatment. Use LP64 for apps; use this skill for newsletters/reports.
- `note-capture-workflow` — For capturing edition production notes to QuickThoughts

## Support Files

- **`templates/edition-template.html`** — Blank edition starter. Copy, fill in `__EDITION_NUMBER__`, `__CREATION_DATE__`, `__EDITION_DATE_RANGE__`, and section content. Inline CSS from latest published edition.
- **`references/acadian-color-palette.md`** — Full CSS custom property reference, component color map, and Acadian flag context for consistent palette usage across editions.

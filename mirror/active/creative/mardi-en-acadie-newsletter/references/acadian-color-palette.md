# Mardi en Acadie — Acadian Flag Color Reference

## CSS Custom Properties (Newsletter Editions)

```css
:root {
  --bg: #0a1628;           /* Dark Navy — body background */
  --bg-surface: #0f1f38;   /* Lighter Blue — TOC, quote blocks */
  --bg-elevated: #142a4a;  /* Elevated Blue — callout backgrounds */
  --bg-card: #112240;      /* Navy Card — timeline entries */

  --red: #c62828;          /* Acadian Red — h2 headers */
  --red-bright: #e53935;   /* Bright Red — h2 active/hover */
  --red-dim: rgba(198,40,40,0.15); /* Red low-opacity — callout-red bg */

  --gold: #d4a017;         /* Gold-Yellow — h3 subheaders */
  --gold-bright: #f5c542;  /* Bright Gold — em, accents, TOC hover */
  --gold-dim: rgba(212,160,23,0.12); /* Gold low-opacity — callout-gold bg */

  --text: #e8e8e8;         /* Off-White — body text */
  --text-muted: #94a3b8;   /* Muted Blue-Gray — secondary text */
  --text-dim: #64748b;     /* Dim Gray — timestamps, footer */

  --link: #5b9bd5;         /* Light Blue — hyperlinks */
  --link-hover: #7db8e8;   /* Hover Blue */
  --border: #1a2d4a;       /* Muted Blue — dividers, cards */
  --border-accent: rgba(198,40,40,0.3); /* Red-tinted — hover borders */
}
```

## Acadian Flag Reference

The flag of Acadie is a tricolour of blue, white, and red — a mirror of the French tricolour with a gold star (Stella Maris) in the blue quadrant. The newsletter palette derives directly from these colors, with the gold accent referencing the star.

## Typography

- **Body:** System sans-serif stack (Segoe UI, system-ui, etc.)
- **Headings:** Georgia / serif stack
- **Monospace:** SF Mono / Fira Code / Consolas

## Component Quick Reference

| Component | Class | Border Color | Background |
|-----------|-------|-------------|------------|
| TOC | `.toc` | Left: `var(--red)` | `var(--bg-surface)` |
| Callout (default) | `.callout` | Left: `var(--gold)` | `var(--bg-elevated)` |
| Callout (red) | `.callout-red` | Left: `var(--red)` | `var(--red-dim)` |
| Callout (gold) | `.callout-gold` | Left: `var(--gold)` | `var(--gold-dim)` |
| Quote | `.quote-block` | Left: `var(--gold)` | `var(--bg-surface)` |
| Timeline entry | `.timeline-entry` | Full: `var(--border)` | `var(--bg-card)` |
| Finale | `.finale` | Full: `var(--border-accent)` | Gradient red-dim → gold-dim |

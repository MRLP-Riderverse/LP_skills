# Layered Directory / Contact-Card UX

Session-derived pattern for public static directories with generated JSON and searchable cards.

## Contract

- **Collapsed quick card:** identity plus the first short-description line; never expose tags or backend category labels.
- **Expanded card:** continuation of the description, public contact/social rows, notes, events, and a clear full-page link. Do not repeat copy already visible in the collapsed state.
- **Full page:** richer public details and line-broken description; still keep tags, verification state, internal category, and routing metadata backend-only.

## Implementation pattern

1. Keep canonical metadata plain and searchable. For deliberate line hierarchy, use a stable source separator such as ` — ` rather than relying on incidental wrapping or HTML in JSON.
2. Split the description in the renderer into `first`, `rest`, and `full` values.
3. Render `first` in the summary, `rest` in the expanded body, and `full` (with an intentional line break) on the entry page.
4. Keep `tags` and `category` in the exported payload so filtering/search can use them later, but audit every public template for category/tag interpolation, recent-item chips, and tag CSS/markup.
5. Re-export after source changes and verify both the payload and all public templates.

## Review checklist

- Search results do not show `project` or `#tag` chips.
- The same short-description sentence is not emitted in both collapsed and expanded card markup.
- Public social handles are rendered as safe, clickable links only when the label/value format is recognized.
- Full-page links remain available from the expanded card.
- Source repo, export payload, and rendered site are committed/pushed as separate repositories when applicable.

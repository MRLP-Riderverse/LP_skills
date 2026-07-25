# Identity entries: bullets, rich data, and safe links

## Why this shape

Acadie.sol identity records are easier to scan when the source entry has:

1. One short lead sentence for the collapsed card.
2. `## Public notes` with concise bullets for the expanded card/full page.
3. `## Contact` for owned website/social/public links.
4. `## Related places` and `## Sources` for provenance and navigation context.

Do not put every descriptor into one paragraph. Keep taxonomy in `meta.json`; it is for filtering/search, not authored visible prose.

## Three-level rendering contract

- **Collapsed:** `description` / Markdown preamble only.
- **Expanded:** lead plus exported `note_points` as a `<ul>`.
- **Full page:** lead plus the same `note_points`, then structured contact/social rows and related content.

The exporter must prefer the Markdown preamble over metadata summary/short description. `note_points` should preserve authored bullet order and wording.

## Link rendering contract

The renderer may support the small subset used by identity prose:

```markdown
- Team Leader at [The Strays](https://TheStrays.World).
```

Escape the source first, then replace only validated `http`/`https` Markdown links with anchors. Use:

```html
<a target="_blank" rel="noopener noreferrer">
```

Verify the final DOM contains `href="https://TheStrays.World"` and does not contain visible `[The Strays](` syntax. Payload preservation alone is insufficient.

## Public-owned links

If an identity/project has an official Facebook page or website, include it in the source `## Contact` section so the exporter carries it into `public_data` and the rendering levels can expose it intentionally. Do not rely only on generated JSON or metadata links.

## Visual experiment note

A red/blue offset outline can add readable retro depth, but it should begin as a localized experiment on full-entry headers. Keep white/high-contrast primary text, use restrained offsets, and test light/dark plus narrow mobile before applying it to global headers or cards.

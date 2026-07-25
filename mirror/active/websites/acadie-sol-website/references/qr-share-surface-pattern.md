# QR share surface pattern

For a compact homepage QR/share block:

- Keep the source QR asset square and verify its actual dimensions, not just the CSS (`PIL.Image.open(...).size`).
- Use a single-column layout so the QR remains a clear 1:1 scan target and the copy can sit beneath it.
- Prefer a small rendered QR (roughly 112px on phone/desktop for this site) with a white quiet zone and modest radius/shadow; do not stretch it into a text column.
- Keep visible copy minimal: one short share message, no repeated URL or “scan this to…” explanation when the QR already communicates the action.
- A share button may call `navigator.share({ title, url })`; fall back to `navigator.clipboard.writeText(url)` for desktop browsers without a native share sheet. Ignore `AbortError` when a user cancels the share sheet.
- Localize the short label/button if the page is bilingual, but do not reintroduce explanatory copy in either language.
- Verify both source and rendered dimensions, absence of redundant link/summary DOM, no page errors, and the live deployed result after Pages completes.

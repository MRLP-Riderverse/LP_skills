# Export parser quirks for inbox cleanup

Session-derived notes from the A–C / D–I cleanup passes.

## Exporter-recognized section headers
The markdown exporter currently parses these section headers:
- `## Description`
- `## Notes`
- `## Public data to carry forward`
- `## Public data`
- `## Details`
- `## Contact`
- `## Public source`
- `## Details and sources`
- `## Admin notes`
- `## Related places` (added during the cleanup pass)

## What to prefer
- Use `## Description` for the one-line public-facing summary.
- Use `## Notes` for the raw local context, caveats, and felt meaning.
- Use `## Public data to carry forward` when address / phone / hours / email should appear as structured fields.
- Use `## Related places` for corridor / cluster / twin-branch links that should stay separate from freeform notes.
- Keep source URLs in `## Public source`.
- Keep internal follow-up in `## Admin notes`.

## Pitfall
A heading like `## Public notes` is not currently one of the recognized parser sections and may be dropped from the exported payload unless normalized to `## Notes`.

## Downstream renderer note
The public site renderer now turns structured `Phone` and `Address` values into tap-to-call and map links. Preserve those values in `## Public data to carry forward` when they matter for public usability; do not hide them only in `Notes` if the card should be actionable.

## Verification pattern

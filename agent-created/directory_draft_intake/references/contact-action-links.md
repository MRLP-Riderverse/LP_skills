# Contact-ready public fields

Session note: the directory renderer can turn structured contact fields into mobile-friendly actions.

## Drafting rule
- Put confirmed public contact facts in `## Public data to carry forward` rather than leaving them in prose.
- Use separate bullets for `Address`, `Phone`, `Hours`, and `Email` when known.
- Keep the values clean and machine-readable.

## Rendering behavior
- `Phone` becomes a tap-to-call target when rendered.
- `Address` becomes a map-open link when rendered.
- `Email` can become a mailto link when the site supports it.

## Cleanup heuristic
- If the note body mentions a confirmed address or phone number, promote it into the structured block during a spruce-up pass.
- Keep qualitative observations in `## Notes`.
- Keep nearby landmarks / sibling branches in `## Related places`.

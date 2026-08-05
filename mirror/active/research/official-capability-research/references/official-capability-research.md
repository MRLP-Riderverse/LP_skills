# Official capability evidence checklist

Use this compact checklist when researching a feature request against official
Hermes/product documentation and source.

## Capture

- Documentation URL and exact wording for each supported feature.
- Configuration key, command, schema, or extension hook only if explicitly
  documented or verified in official source.
- Built-in implementation file/function, clearly labeled as internal behavior.
- Official issue/PR URL only for gaps, proposals, regressions, or maintenance
  context; never use it as proof of release.
- Product-specific limits, defaults, and clamping rules, not just generic
  platform limits.
- Closest documented alternative when the requested feature is unsupported.

## Report template

- **Supported:** documented types/features and a short quote.
- **Configuration/extension:** exact key or hook, or “not documented.”
- **Callbacks/events:** documented contract vs internal handler; do not blur the
  distinction.
- **Limits:** exact default/range/cap and source URL.
- **Example:** only reproduce an official example or a verified source pattern.
- **Gap:** state plainly when arbitrary/custom behavior is not documented.
- **Nearest supported mechanism:** command menu, slash command, webhook, plugin,
  or other documented path.

## Decision rule

If docs show a built-in UI but no public emission schema or registration hook,
report the UI as supported built-in behavior—not as a customization API.

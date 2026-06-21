# Weather location overrides

## Session takeaway
- Default weather requests should resolve to the user's current declared home location.
- If the user names a city or region explicitly, treat it as an override.
- No geo-tracking; the user prefers explicit control.

## Preferred precedence
1. Explicit location in the request, e.g. `weather in San Diego`
2. Home/default location from config or environment
3. Final hard fallback only if the default is unset

## Implementation preference
- Prefer a structured `--location` / `location=` override over parsing arbitrary prose.
- Geocode the location string to coordinates before querying the weather API.
- Keep the home location easy to patch when travel changes.
- The Hermes persona can mention the user's home area, but operational defaults should live in config/env where possible.

## Usage examples
- `what's the current weather?` → home/default location
- `what's the current weather in Moncton NB?` → explicit override
- `what's the current weather in San Diego?` → explicit override

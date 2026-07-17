# Location env operator pattern

Use two declarative env vars instead of a travel boolean:

- `HOME_LOCATION` = stable base location
- `CURRENT_LOCATION` = optional temporary override

Resolution order:

1. Explicit `--location` argument
2. `CURRENT_LOCATION` when non-empty
3. `HOME_LOCATION`
4. Legacy `HOME_WEATHER_LOCATION` fallback
5. Hardcoded Bathurst safety fallback

## Why this model

Do **not** introduce `IS_TRAVELLING=true/false`.
A boolean still requires a second variable for the actual place, which creates unnecessary state drift.

The declarative model gives:
- home by default
- travel-aware cron behavior when `CURRENT_LOCATION` is set
- clean reuse by other location-aware tools later
- no geo-tracking or inference

## Wrapper rule

Keep the shared cron wrapper `.env`-driven and deterministic.

Why:
- scheduled weather should follow the persisted `~/.hermes/.env` state, not ambient shell state
- inherited shell env vars can be sticky/noisy during interactive sessions and create misleading results
- one-off checks already have a clean path: `weather_telegram.py --location "City, Region"`

Pattern:
- source `~/.hermes/.env`
- run `weather_telegram.py` with no extra shell-env precedence layer
- use `~/.hermes/scripts/weather_location.sh` to change persisted travel state
- use `--location` for one-off city checks that should not mutate the persisted default

## Operator workflow

- At home: `CURRENT_LOCATION=""`
- Travelling: set `CURRENT_LOCATION` to the trip city
- One-off other city: use `--location "City, Region"`
- Back home: clear `CURRENT_LOCATION` again

Helper command examples:

```bash
~/.hermes/scripts/weather_location.sh status
~/.hermes/scripts/weather_location.sh set-current "Ottawa, ON"
~/.hermes/scripts/weather_location.sh clear-current
```

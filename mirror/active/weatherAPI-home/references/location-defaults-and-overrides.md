# Location defaults and overrides

This workflow now supports a stable, travel-friendly location model:

## Default resolution order

1. Explicit `--location "City, Region"` override
2. `CURRENT_LOCATION` from `~/.hermes/.env` when non-empty
3. `HOME_LOCATION` from `~/.hermes/.env`
4. Legacy `HOME_WEATHER_LOCATION` fallback for backward compatibility
5. Hardcoded Bathurst safety fallback

## Reliability notes

- Keep cron jobs pointed at the shared wrapper/script entrypoint; do not fork per-city cron jobs just to change location state.
- The wrapper already sources `~/.hermes/.env`, so changing `CURRENT_LOCATION` or `HOME_LOCATION` updates scheduled runs without editing cron definitions.
- Use `CURRENT_LOCATION=""` when back home; no boolean travel flag needed.
- Use per-location cache keys/files so one manual override query does not contaminate the current/home-location cache.
- Prefer deterministic script arguments over free-form prompt parsing. The assistant may extract a city from a user request, but the script contract should stay mechanical: optional `--location`, otherwise env-driven fallback.

## Recommended operator workflow

- Home/default weather: `python3 weather_telegram.py`
- One-off query elsewhere: `python3 weather_telegram.py --location "San Diego, CA"`
- Temporary trip: set `CURRENT_LOCATION="Ottawa, ON"` in `~/.hermes/.env`
- Back home: set `CURRENT_LOCATION=""`

## Pitfall

Do not model travel as `IS_TRAVELLING=true/false`. A boolean still requires a second variable for the actual place, which creates unnecessary state drift. Keep the model declarative: home location + optional current location.

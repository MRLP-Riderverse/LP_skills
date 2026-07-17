---
name: weatherAPI-home
description: Local Bathurst weather fetcher and Telegram delivery. Powers daily and midday weather cron jobs.
category: weather
---

# Weather API Home

Fetches weather data and delivers formatted reports to Telegram.

## Default location model

- Base/home location comes from `HOME_LOCATION` in `~/.hermes/.env`
- Temporary travel override comes from `CURRENT_LOCATION` in `~/.hermes/.env`
- If `CURRENT_LOCATION` is blank, the workflow uses `HOME_LOCATION`
- One-off requests can override both with `--location "City, Region"`
- The script still honors legacy `HOME_WEATHER_LOCATION` as a backward-compatible fallback
- If no location is configured, the workflow falls back to the hardcoded Bathurst safety default
- See `references/location-defaults-and-overrides.md` for the resolution order, cache behavior, and cron-safe operator pattern
- See `references/location-env-operator-pattern.md` for the two-variable location model, the helper command workflow, and why the shared wrapper should stay `.env`-driven
- See `references/location-helper-command.md` for the travel-state helper command, operator workflow, and the pitfall that led to keeping the wrapper deterministic

## Scripts

- `weather_telegram.py` — main formatter/entrypoint for a single live weather fetch
- `bathurst_weather.py` — weather data fetcher with per-location cache fallback
- `weather_location_env.py` — helper for changing `CURRENT_LOCATION` / checking effective defaults in `~/.hermes/.env`
- `weather_format.py` — formatting utilities
- `~/.hermes/scripts/bathurst_weather_telegram.sh` — shared cron wrapper; sources `~/.hermes/.env`, enters the skill directory, and executes `weather_telegram.py`
- `~/.hermes/scripts/weather_location.sh` — wrapper for `weather_location_env.py`; use this to set or clear travel location state without editing `.env` manually

## Cron Jobs

- `daily-bathurst-weather` (8:00 AM Atlantic)
- `brunch-bathurst-weather` (10:30 AM Atlantic)
- `midday-bathurst-weather` (2:00 PM Atlantic)

All three weather jobs are hardened as `no_agent: true` script-only cron jobs pointing to `bathurst_weather_telegram.sh`. That removes model/provider dependence for the routine daily sends while keeping the Python weather script available for manual live runs.

## Hardening / Delivery Notes

- Routine weather delivery should stay `no_agent: true` and script-only.
- See `references/deterministic-cron-hardening.md` for the cron hardening pattern, cache semantics, and why provider 429s should be solved by removing the model from the loop for mechanical jobs.
- `Observed at:` reflects the source observation time from Open-Meteo and should remain visible in the final message.

## Manual / Live Use

For an immediate live update using the default/home location, run:

```bash
python3 /home/midnight/.hermes/skills/weatherAPI-home/weather_telegram.py
```

To inspect or change the travel override without editing `.env` manually, use:

```bash
~/.hermes/scripts/weather_location.sh status
~/.hermes/scripts/weather_location.sh set-current "Ottawa, ON"
~/.hermes/scripts/weather_location.sh clear-current
```

For a one-off override location, run:

```bash
python3 /home/midnight/.hermes/skills/weatherAPI-home/weather_telegram.py --location "San Diego, CA"
```

or use the shared wrapper:

```bash
~/.hermes/scripts/bathurst_weather_telegram.sh
```

### Location handling preference

- Default to the user's current declared location when no place is mentioned.
- If `CURRENT_LOCATION` is blank, fall back to the user's declared home location.
- If the user names a city/region, treat it as an explicit one-off override.
- Prefer a structured location parameter and geocoding over trying to infer location from free-form prose.
- Keep the location model explicit and easy to change when the user travels; no geo-tracking.
- See `references/location-overrides.md` for the precedence and examples.

## ⚠️ Do Not Delete

This skill is pinned. It is actively used by production cron jobs. Do not archive, prune, or relocate without updating both cron job paths.

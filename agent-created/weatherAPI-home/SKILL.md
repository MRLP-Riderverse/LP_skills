---
name: weatherAPI-home
description: Local-first weather fetcher and Telegram delivery. Supports home, travel, and one-off locations.
category: weather
---

# Weather API Home

Fetches weather data and delivers formatted reports to Telegram.

## Default location model

- Base/home location comes from `HOME_LOCATION` in `~/.hermes/.env`
- Temporary travel override comes from `CURRENT_LOCATION` in `~/.hermes/.env`
- If `CURRENT_LOCATION` is blank, the workflow uses `HOME_LOCATION`
- One-off requests can override both with `--location "City, Region"`
- Reusable coordinates are declared for Bathurst, Moncton, and Montreal; new geocoded locations are persisted in `.weather_cache/locations.json` and reused on later requests
- The script still honors legacy `HOME_WEATHER_LOCATION` as a backward-compatible fallback
- If no location is configured, the workflow falls back to the hardcoded Bathurst safety default
- See `references/location-defaults-and-overrides.md` for the resolution order, cache behavior, and cron-safe operator pattern
- See `references/location-env-operator-pattern.md` for the two-variable location model, the helper command workflow, and why the shared wrapper should stay `.env`-driven
- See `references/location-helper-command.md` for the travel-state helper command, operator workflow, and the pitfall that led to keeping the wrapper deterministic

## Scripts

- `weather_telegram.py` — main formatter/entrypoint for a single live weather fetch
- `bathurst_weather.py` — shared weather data fetcher with per-location cache fallback and local history archive
- `weather_location_env.py` — helper for changing `CURRENT_LOCATION` / checking effective defaults in `~/.hermes/.env`
- `weather_walk_telegram.py` — evening walk decision using the next three hourly forecast slots
- `weather_format.py` — Telegram, CLI, and compact history-note formatting
- `~/.hermes/scripts/weather_telegram.sh` — generic wrapper for home, travel, and one-off weather requests
- `~/.hermes/scripts/bathurst_weather_telegram.sh` — compatibility alias for older callers
- `~/.hermes/scripts/evening_walk_weather.sh` — evening walk forecast wrapper
- `~/.hermes/scripts/weather_location.sh` — wrapper for `weather_location_env.py`; use this to set or clear travel location state without editing `.env` manually

## Cron Jobs

- `daily-bathurst-weather` (8:00 AM Atlantic)
- `brunch-bathurst-weather` (10:30 AM Atlantic)
- `midday-bathurst-weather` (2:00 PM Atlantic)
- `evening-bathurst-walk-weather` (6:00 PM Atlantic)

The evening report fetches the next three local hourly forecast slots and includes:

- local time for each slot
- temperature
- condition and precipitation probability
- wind speed
- a simple walk recommendation based on rain, wind, temperature, and severe-weather codes

All four weather jobs are hardened as `no_agent: true` script-only cron jobs. The first three use `weather_telegram.sh`; the evening job uses `evening_walk_weather.sh`. The old Bathurst-named wrapper remains only as a compatibility alias.

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
~/.hermes/scripts/weather_telegram.sh --location "San Diego, CA"
```

The older `bathurst_weather_telegram.sh` name remains a compatibility alias, but new commands and cron jobs should use the generic wrapper.

For a compact history/QuickThoughts-friendly line without capturing it automatically:

```bash
python3 /home/midnight/.hermes/skills/weatherAPI-home/bathurst_weather.py --format note
```

Live observations are also appended as small JSONL records under `.weather_cache/history/`. This archive is local runtime data, separate from the tracked skill mirror.

### Location handling preference

- Default to the user's current declared location when no place is mentioned.
- If `CURRENT_LOCATION` is blank, fall back to the user's declared home location.
- If the user names a city/region, treat it as an explicit one-off override.
- Prefer a structured location parameter and geocoding over trying to infer location from free-form prose.
- Keep the location model explicit and easy to change when the user travels; no geo-tracking.
- See `references/location-overrides.md` for the precedence and examples.

## ⚠️ Do Not Delete

This skill is pinned. It is actively used by production cron jobs. Do not archive, prune, or relocate without updating both cron job paths.

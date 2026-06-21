# Deterministic weather cron hardening

Use this pattern when routine weather delivery should not depend on an LLM.

## Production shape

- Cron jobs: `daily-bathurst-weather`, `brunch-bathurst-weather`, `midday-bathurst-weather`
- Execution mode: `no_agent: true`
- Shared script: `bathurst_weather_telegram.sh`
- Delivery path: `cron -> shell script -> weather_telegram.py -> stdout -> Telegram`

## Why

The failure mode was provider-side `HTTP 429` on model-backed cron jobs, including a lightweight weather job. Weather delivery is mechanical, so remove the model from the loop instead of tuning prompts.

## Live vs cached behavior

`bathurst_weather.py` does a live Open-Meteo fetch by default, but keeps a local cache:

- cache file: `.weather_cache.json`
- fresh cache TTL: 600 seconds
- if a fresh cache exists, it is returned
- otherwise the script calls the live API
- if the API fails, stale cache may be returned as fallback

Implication:
- scheduled runs spaced hours apart are effectively live
- repeated manual runs inside 10 minutes may reuse cached data
- `Observed at:` comes from the API payload and should be shown to surface data freshness

## Maintenance notes

- Keep the wrapper script committed in the LP_skill mirror repo as well as present under `~/.hermes/scripts/`.
- If cron jobs are script-only, lingering model/provider fields in the scheduler record are harmless; `no_agent: true` bypasses them.
- If the user wants stricter freshness guarantees later, label output as `live` vs `cached fallback` rather than reintroducing the LLM.

---
name: weatherAPI-home
description: Local Bathurst weather fetcher and Telegram delivery. Powers daily and midday weather cron jobs.
category: weather
---

# Weather API Home

Fetches weather data and delivers formatted reports to Telegram.

## Scripts

- `weather_telegram.py` — main script, called by cron jobs at 8AM and 10AM daily
- `bathurst_weather.py` — weather data fetcher
- `weather_format.py` — formatting utilities

## Cron Jobs

- `daily-bathurst-weather` (8AM AST) — morning forecast
- `midday-bathurst-weather` (10AM AST) — midday update

Both reference `/home/midnight/.hermes/skills/weatherAPI-home/weather_telegram.py` directly.

## ⚠️ Do Not Delete

This skill is pinned. It is actively used by production cron jobs. Do not archive, prune, or relocate without updating both cron job paths.

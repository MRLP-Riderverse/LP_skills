---
name: weather-two-way-output
description: Build a weather workflow with a machine-friendly CLI output and a separate Telegram-friendly text output, both backed by the same fetcher and cache.
version: 1.0.0
author: MidnightRider.sol
---
name: weather-workflow
description: Complete weather workflow — two-way output (JSON CLI + Telegram text), one-shot location queries, caching, and Open-Meteo API integration.
category: weather
aliases: [weather-two-way-output, weather-one-shot]
---

# Weather Workflow Umbrella

This is the **class-level skill** for all weather-related operations. It consolidates two-way output patterns, one-shot location queries, caching strategies, and Open-Meteo API integration.

**Trigger:** User asks for weather information, needs to set up weather cron jobs, wants weather data in both machine-friendly and Telegram-friendly formats, or needs one-off weather queries for non-default locations.

---

## Subsections

### A. Two-Way Output Pattern (from `weather-two-way-output`)
Build a weather workflow with a machine-friendly CLI output and a separate Telegram-friendly text output, both backed by the same fetcher and cache.

**When to Use:**
- Want one weather data source to serve two audiences
- CLI / automation consumers need structured JSON
- Telegram / cron consumers need friendly human-readable message

**Core Pattern:**
1. Keep one shared weather fetcher that:
 - calls Open-Meteo API
 - parses weather codes
 - applies caching
 - returns a plain Python dict
2. Add two presentation layers:
 - JSON output for CLI defaults
 - text output for messaging platforms
3. Let the Telegram script reuse the shared fetcher and only handle formatting/delivery

**Recommended File Split:**
- `bathurst_weather.py` - shared fetcher and cache, `--format json` default, `--format text` for readable terminal
- `weather_telegram.py` - imports the fetcher, formats Telegram-friendly message, does not duplicate API or cache logic

**Shared Data Fields:**
A good weather dict should include:
- `location`, `temperature_c`, `conditions`, `emoji`, `summary`
- `precipitation_mm`, `wind_speed_kmh`, `observed_at`

**CLI behavior:**
- Default to JSON (stable, parseable, easy to pipe)
- Provide `--format text` switch for humans who want quick summary

**Telegram behavior:**
- Use line breaks, emoji, and short advice text
- Keep it concise; Telegram updates should be readable at a glance
- Avoid heavy Markdown unless verified platform wrapper supports them

**Pitfalls:**
- Do not duplicate weather-code mapping in both scripts
- Do not make Telegram formatting the default CLI behavior
- Do not require embeds; Telegram works better with clean text formatting
- If `weather_telegram.py` imports the fetcher directly, ensure files live in same directory or module path is set correctly
- For Hermes cron jobs, point prompt at explicit file path under `/home/midnight/.hermes/skills/weatherAPI-home/` so agent doesn't search and return `[SILENT]`
- For cron jobs, source the environment first if script expects runtime secrets from `~/.hermes/.env`

**Verification:**
Run both paths after editing:
- `python3 bathurst_weather.py`
- `python3 bathurst_weather.py --format text`
- `python3 weather_telegram.py`
- A cron-style dry run that uses explicit script path and sourced environment

**See original:** Full two-way output pattern preserved from `weather-two-way-output` skill.

---

### B. One-Shot Location Queries (from `weather-one-shot`)
Get current weather for any location using the Open-Meteo API by adapting the existing weather-tool script pattern. Use for one-off location queries without persisting the location as default.

**When to Use:**
- User asks for weather in a non-default location
- Need quick weather check for any global coordinates
- Want to reuse proven Open-Meteo API approach without creating new persistent scripts

**Approach:**
1. Examine the existing `bathurst_weather.py` script pattern in `~/.hermes/skills/weatherAPI-home/`
2. Create a one-shot Python script that:
 - Uses the same Open-Meteo API endpoint and parameters
 - Injects the target location's latitude, longitude, and name
 - Uses the same weather code mapping and data parsing
 - Returns formatted JSON with location, temperature, conditions, precipitation, wind
3. Execute the script and present results
4. Do NOT persist the location - default remains Bathurst, NB

**Constants to Modify for One-Shot:**
```python
LATITUDE = 45.5017      # Target location latitude (float)
LONGITUDE = -73.5673    # Target location longitude (float)
LOCATION_NAME = "Montreal, QC"  # Human-readable location name (string)
```

**Performance Notes:**
- Script execution itself is very fast (~50ms)
- Main bottleneck is network latency to Open-Meteo API (~700-800ms)
- Consider using the locations reference file to avoid coordinate lookup delays
- For repeated requests to same location, the default weather-tool script provides 600s caching

**Key Files:**
- Reference: `~/.hermes/skills/weatherAPI-home/bathurst_weather.py`
- Locations reference: `~/.hermes/skills/weatherAPI-home/locations.json` (predefined coordinates)
- One-shot pattern: Reuse the script structure with modified coordinates

**See original:** Full one-shot pattern preserved from `weather-one-shot` skill.

---

## Common Pitfalls

1. **Duplicating weather-code mapping** - keep one shared fetcher
2. **Wrong default output format** - JSON for CLI, text for Telegram
3. **Not sourcing environment** - cron jobs need `~/.hermes/.env` sourced
4. **Vague cron instructions** - point at explicit script path
5. **Missing cache behavior** - 600s TTL for repeated queries
6. **Coordinate lookup delays** - use locations.json reference file

---

## Verification Checklist

- [ ] JSON output parses cleanly
- [ ] Text output is human-friendly
- [ ] Telegram output matches intended chat style
- [ ] Cache behavior remains unchanged
- [ ] Cron output no longer goes [SILENT] due to underspecified prompt
- [ ] One-shot queries work for non-default locations
- [ ] Default location (Bathurst, NB) remains unchanged after one-shot

---

## Related Skills

- `cron-telegram-auto-delivery` - Scheduled Telegram delivery (includes headless practices for avoiding AI function degradation)
- `telegram-notifier-tool` - Telegram notification tool

---

## Cron Job Reliability Note

**Important:** When deploying weather scripts as cron jobs, avoid AI model involvement for simple weather fetches. AI providers may mark function-calling capabilities as DEGRADED in headless contexts, causing intermittent failures.

**Pattern:**
- ✅ Good: `model: null, provider: null` with direct script execution
- ❌ Bad: Using AI models for simple weather fetches (hits DEGRADED errors)

See `cron-telegram-auto-delivery` skill, section "Headless practices: avoiding degraded AI function errors" for complete guidance.

---

*Consolidated: May 2026*
*Source skills: weather-two-way-output, weather-one-shot*

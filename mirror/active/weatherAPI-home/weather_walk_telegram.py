#!/usr/bin/env python3
"""Format the next three local hours as a simple evening walk decision."""

from __future__ import annotations

import json
import sys
from datetime import datetime
from typing import Any
from urllib import error, parse, request

from bathurst_weather import (
    WEATHER_API_URL,
    WEATHER_CODES,
    WeatherError,
    resolve_coordinates,
    resolve_location_query,
    weather_emoji,
)


def build_forecast_url(latitude: float, longitude: float) -> str:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,weather_code,precipitation_probability,precipitation,wind_speed_10m",
        "forecast_hours": 4,
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "precipitation_unit": "mm",
        "timezone": "auto",
    }
    return f"{WEATHER_API_URL}?{parse.urlencode(params)}"


def fetch_next_hours(location: str | None = None, hours: int = 3) -> tuple[str, list[dict[str, Any]]]:
    location_query = resolve_location_query(location)
    latitude, longitude, location_name = resolve_coordinates(location_query)
    url = build_forecast_url(latitude, longitude)

    try:
        with request.urlopen(url, timeout=10) as response:
            if response.status != 200:
                raise WeatherError(f"Forecast API returned HTTP {response.status}.")
            payload = json.load(response)
    except error.URLError as exc:
        raise WeatherError(f"Unable to reach forecast API: {getattr(exc, 'reason', exc)}") from exc
    except json.JSONDecodeError as exc:
        raise WeatherError("Forecast API returned invalid JSON.") from exc

    hourly = payload.get("hourly")
    if not isinstance(hourly, dict):
        raise WeatherError("Forecast response did not include hourly data.")

    times = hourly.get("time", [])
    temperatures = hourly.get("temperature_2m", [])
    codes = hourly.get("weather_code", [])
    probabilities = hourly.get("precipitation_probability", [])
    precipitation = hourly.get("precipitation", [])
    winds = hourly.get("wind_speed_10m", [])
    if not all(isinstance(value, list) for value in (times, temperatures, codes, probabilities, precipitation, winds)):
        raise WeatherError("Forecast response had an unexpected hourly format.")

    rows: list[dict[str, Any]] = []
    for index in range(min(hours, len(times), len(temperatures), len(codes), len(probabilities), len(precipitation), len(winds))):
        code = int(codes[index])
        rows.append({
            "time": str(times[index]),
            "temperature_c": float(temperatures[index]),
            "conditions": WEATHER_CODES.get(code, f"Unknown ({code})"),
            "emoji": weather_emoji(WEATHER_CODES.get(code, f"Unknown ({code})")),
            "precipitation_probability": int(probabilities[index]),
            "precipitation_mm": float(precipitation[index]),
            "wind_speed_kmh": float(winds[index]),
            "weather_code": code,
        })

    if not rows:
        raise WeatherError("Forecast response contained no upcoming hourly data.")
    return location_name, rows


def is_walk_friendly(row: dict[str, Any]) -> bool:
    code = int(row["weather_code"])
    return (
        code not in {65, 67, 75, 82, 86, 95, 96, 99}
        and int(row["precipitation_probability"]) < 40
        and float(row["wind_speed_kmh"]) <= 30
        and -10 <= float(row["temperature_c"]) <= 30
    )


def format_message(location_name: str, rows: list[dict[str, Any]]) -> str:
    friendly = sum(is_walk_friendly(row) for row in rows)
    if friendly == len(rows):
        decision = "Walk looks good — the next few hours are broadly friendly."
    elif friendly == 0:
        decision = "Probably stay inside — the next few hours look rough for a walk."
    else:
        decision = "Mixed conditions — a short walk may work, but check the hour you want to leave."

    lines = [f"🚶 {location_name} evening walk check 🚶", ""]
    for index, row in enumerate(rows):
        time_label = datetime.fromisoformat(row["time"]).strftime("%H:%M")
        lines.append(
            f"{time_label} — {row['emoji']} {row['temperature_c']:.1f}°C, "
            f"{row['conditions'].lower()}, {row['precipitation_probability']}% precip, "
            f"wind {row['wind_speed_kmh']:.0f} km/h"
        )
        if index < len(rows) - 1:
            lines.append("")
    lines.extend(["", f"Shinobi walk read: {decision}"])
    return "\n".join(lines)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Show the next three hours for an evening walk decision")
    parser.add_argument("--location", help="Override the default/home location for this request")
    args = parser.parse_args()

    try:
        location_name, rows = fetch_next_hours(location=args.location)
        print(format_message(location_name, rows))
        return 0
    except Exception as exc:
        print(f"❌ Evening walk weather failed: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

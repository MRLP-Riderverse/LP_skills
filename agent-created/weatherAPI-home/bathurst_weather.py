#!/usr/bin/env python3
"""
Fetch current weather for Bathurst, NB from Open-Meteo.
AUTHOR=MidnightRider.sol
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any
from urllib import error, parse, request

from weather_format import format_cli_text


API_URL = "https://api.open-meteo.com/v1/forecast"
CACHE_FILE = Path(__file__).with_name(".weather_cache.json")
CACHE_TTL_SECONDS = 600
LATITUDE = 47.6167
LONGITUDE = -65.6500
LOCATION_NAME = "Bathurst, NB"

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


class WeatherError(Exception):
    """Raised when weather data cannot be retrieved."""


def weather_emoji(conditions: str) -> str:
    conditions_lower = conditions.lower()
    if "clear" in conditions_lower or "sunny" in conditions_lower:
        return "☀️"
    if "cloud" in conditions_lower or "overcast" in conditions_lower:
        return "☁️"
    if "rain" in conditions_lower or "drizzle" in conditions_lower:
        return "🌧️"
    if "snow" in conditions_lower:
        return "❄️"
    if "fog" in conditions_lower or "mist" in conditions_lower:
        return "🌫️"
    if "thunder" in conditions_lower:
        return "⛈️"
    return "🌤️"


def weather_advice(temperature_c: float, precipitation_mm: float, wind_speed_kmh: float) -> str:
    if temperature_c < -10:
        base = "Brrr — bundle up."
    elif temperature_c < 0:
        base = "Chilly out there — a warm layer helps."
    elif temperature_c < 15:
        base = "Crisp and cool — a great day for a walk."
    elif temperature_c < 25:
        base = "Pretty comfortable — enjoy it."
    else:
        base = "Warm weather — stay hydrated and seek shade if needed."

    extras: list[str] = []
    if precipitation_mm > 5:
        extras.append("Bring an umbrella.")
    if wind_speed_kmh > 20:
        extras.append("It’s breezy, so hold onto your hat.")

    return f"{base} {' '.join(extras)}" if extras else base


def build_url() -> str:
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": "temperature_2m,weather_code,precipitation,wind_speed_10m",
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "precipitation_unit": "mm",
        "timezone": "auto",
    }
    return f"{API_URL}?{parse.urlencode(params)}"


def load_cache(max_age_seconds: int = CACHE_TTL_SECONDS) -> dict[str, Any] | None:
    try:
        payload = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except (OSError, json.JSONDecodeError):
        return None

    fetched_at = payload.get("fetched_at")
    data = payload.get("data")
    if not isinstance(fetched_at, (int, float)) or not isinstance(data, dict):
        return None

    if time.time() - fetched_at > max_age_seconds:
        return None

    return data


def load_stale_cache() -> dict[str, Any] | None:
    try:
        payload = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        return None

    data = payload.get("data")
    return data if isinstance(data, dict) else None


def save_cache(data: dict[str, Any]) -> None:
    payload = {"fetched_at": time.time(), "data": data}
    try:
        CACHE_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    except OSError:
        pass


def parse_weather(api_response: dict[str, Any]) -> dict[str, Any]:
    current = api_response.get("current")
    if not isinstance(current, dict):
        raise WeatherError("API response did not include current weather data.")

    try:
        weather_code = int(current["weather_code"])
        temperature_c = float(current["temperature_2m"])
        conditions = WEATHER_CODES.get(weather_code, f"Unknown ({weather_code})")
        precipitation_mm = float(current["precipitation"])
        wind_speed_kmh = float(current["wind_speed_10m"])
    except (KeyError, TypeError, ValueError) as exc:
        raise WeatherError("API response was missing expected weather fields.") from exc

    return {
        "location": LOCATION_NAME,
        "temperature_c": temperature_c,
        "conditions": conditions,
        "emoji": weather_emoji(conditions),
        "summary": weather_advice(temperature_c, precipitation_mm, wind_speed_kmh),
        "precipitation_mm": precipitation_mm,
        "wind_speed_kmh": wind_speed_kmh,
        "observed_at": current.get("time"),
    }


def fetch_weather() -> dict[str, Any]:
    cached = load_cache()
    if cached is not None:
        return cached

    url = build_url()
    try:
        with request.urlopen(url, timeout=10) as response:
            if response.status != 200:
                raise WeatherError(f"Weather API returned HTTP {response.status}.")
            api_response = json.load(response)
    except error.URLError as exc:
        stale = load_stale_cache()
        if stale is not None:
            return stale
        reason = getattr(exc, "reason", exc)
        raise WeatherError(f"Unable to reach weather API: {reason}") from exc
    except json.JSONDecodeError as exc:
        stale = load_stale_cache()
        if stale is not None:
            return stale
        raise WeatherError("Weather API returned invalid JSON.") from exc

    weather = parse_weather(api_response)
    save_cache(weather)
    return weather


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch current weather for Bathurst, NB")
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="json",
        help="Output format for CLI use (default: json)",
    )
    args = parser.parse_args()

    try:
        weather = fetch_weather()
    except WeatherError as exc:
        print(json.dumps({"error": str(exc)}))
        return 1

    if args.format == "text":
        print(format_cli_text(weather))
    else:
        print(json.dumps(weather, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

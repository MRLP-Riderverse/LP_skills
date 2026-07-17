#!/usr/bin/env python3
"""
Fetch current weather from Open-Meteo with a home-location fallback.
AUTHOR=MidnightRider.sol
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import time
from pathlib import Path
from typing import Any
from urllib import error, parse, request

from weather_format import format_cli_text


WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"
GEOCODING_API_URL = "https://nominatim.openstreetmap.org/search"
GEOCODING_USER_AGENT = "HermesWeather/1.0 (+local Hermes agent)"
CACHE_DIR = Path(__file__).with_name(".weather_cache")
CACHE_TTL_SECONDS = 600
CURRENT_LOCATION_ENV_VAR = "CURRENT_LOCATION"
HOME_LOCATION_ENV_VAR = "HOME_LOCATION"
LEGACY_HOME_LOCATION_ENV_VAR = "HOME_WEATHER_LOCATION"
DEFAULT_LATITUDE = 47.6167
DEFAULT_LONGITUDE = -65.6500
DEFAULT_LOCATION_NAME = "Bathurst, NB"

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


def normalize_location_query(location: str) -> str:
    return " ".join(location.strip().split())


def resolve_location_query(location: str | None = None) -> str:
    explicit = normalize_location_query(location) if location else ""
    if explicit:
        return explicit

    current_location = normalize_location_query(os.getenv(CURRENT_LOCATION_ENV_VAR, ""))
    if current_location:
        return current_location

    home_location = normalize_location_query(os.getenv(HOME_LOCATION_ENV_VAR, ""))
    if home_location:
        return home_location

    legacy_home_location = normalize_location_query(os.getenv(LEGACY_HOME_LOCATION_ENV_VAR, ""))
    if legacy_home_location:
        return legacy_home_location

    return DEFAULT_LOCATION_NAME


def cache_key_for_location(location_query: str) -> str:
    return normalize_location_query(location_query).casefold()


def cache_file_for_key(cache_key: str) -> Path:
    digest = hashlib.sha256(cache_key.encode("utf-8")).hexdigest()[:16]
    return CACHE_DIR / f"{digest}.json"


def build_url(latitude: float, longitude: float) -> str:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code,precipitation,wind_speed_10m",
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "precipitation_unit": "mm",
        "timezone": "auto",
    }
    return f"{WEATHER_API_URL}?{parse.urlencode(params)}"


def load_cache(cache_key: str, max_age_seconds: int = CACHE_TTL_SECONDS) -> dict[str, Any] | None:
    cache_file = cache_file_for_key(cache_key)
    try:
        payload = json.loads(cache_file.read_text(encoding="utf-8"))
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


def load_stale_cache(cache_key: str) -> dict[str, Any] | None:
    cache_file = cache_file_for_key(cache_key)
    try:
        payload = json.loads(cache_file.read_text(encoding="utf-8"))
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        return None

    data = payload.get("data")
    return data if isinstance(data, dict) else None


def save_cache(cache_key: str, data: dict[str, Any]) -> None:
    payload = {"fetched_at": time.time(), "data": data}
    try:
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        cache_file_for_key(cache_key).write_text(json.dumps(payload, indent=2), encoding="utf-8")
    except OSError:
        pass


def clean_place_name(name: str) -> str:
    cleaned = name.strip()
    for prefix in ("City of ", "Ville de "):
        if cleaned.startswith(prefix):
            return cleaned[len(prefix):]
    return cleaned


def format_geocoded_location(result: dict[str, Any]) -> str:
    address = result.get("address") if isinstance(result.get("address"), dict) else {}
    place = (
        address.get("city")
        or address.get("town")
        or address.get("village")
        or address.get("municipality")
        or result.get("name")
        or ""
    )
    state = str(address.get("state", "")).split(" / ")[0].strip()
    country_code = str(address.get("country_code", "")).upper().strip()
    parts = [clean_place_name(str(place)), state, country_code]
    return ", ".join(part for part in parts if part)


def geocode_location(location_query: str) -> tuple[float, float, str]:
    params = {
        "q": location_query,
        "format": "jsonv2",
        "limit": 1,
        "addressdetails": 1,
    }
    url = f"{GEOCODING_API_URL}?{parse.urlencode(params)}"
    req = request.Request(url, headers={"User-Agent": GEOCODING_USER_AGENT})

    try:
        with request.urlopen(req, timeout=10) as response:
            if response.status != 200:
                raise WeatherError(f"Geocoding API returned HTTP {response.status}.")
            results = json.load(response)
    except error.URLError as exc:
        raise WeatherError(f"Unable to reach geocoding API: {getattr(exc, 'reason', exc)}") from exc
    except json.JSONDecodeError as exc:
        raise WeatherError("Geocoding API returned invalid JSON.") from exc

    if not isinstance(results, list) or not results:
        raise WeatherError(f"Could not resolve location: {location_query}")

    result = results[0]
    try:
        latitude = float(result["lat"])
        longitude = float(result["lon"])
    except (KeyError, TypeError, ValueError) as exc:
        raise WeatherError("Geocoding API response was missing coordinates.") from exc

    location_name = format_geocoded_location(result) or location_query
    return latitude, longitude, location_name


def resolve_coordinates(location_query: str) -> tuple[float, float, str]:
    normalized_query = normalize_location_query(location_query)
    if not normalized_query:
        return DEFAULT_LATITUDE, DEFAULT_LONGITUDE, DEFAULT_LOCATION_NAME

    try:
        return geocode_location(normalized_query)
    except WeatherError:
        if normalized_query.casefold() == DEFAULT_LOCATION_NAME.casefold():
            return DEFAULT_LATITUDE, DEFAULT_LONGITUDE, DEFAULT_LOCATION_NAME
        raise


def parse_weather(api_response: dict[str, Any], location_name: str) -> dict[str, Any]:
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
        "location": location_name,
        "temperature_c": temperature_c,
        "conditions": conditions,
        "emoji": weather_emoji(conditions),
        "summary": weather_advice(temperature_c, precipitation_mm, wind_speed_kmh),
        "precipitation_mm": precipitation_mm,
        "wind_speed_kmh": wind_speed_kmh,
        "observed_at": current.get("time"),
    }


def fetch_weather(location: str | None = None) -> dict[str, Any]:
    location_query = resolve_location_query(location)
    cache_key = cache_key_for_location(location_query)

    cached = load_cache(cache_key)
    if cached is not None:
        return cached

    latitude, longitude, location_name = resolve_coordinates(location_query)
    url = build_url(latitude, longitude)

    try:
        with request.urlopen(url, timeout=10) as response:
            if response.status != 200:
                raise WeatherError(f"Weather API returned HTTP {response.status}.")
            api_response = json.load(response)
    except error.URLError as exc:
        stale = load_stale_cache(cache_key)
        if stale is not None:
            return stale
        reason = getattr(exc, "reason", exc)
        raise WeatherError(f"Unable to reach weather API: {reason}") from exc
    except json.JSONDecodeError as exc:
        stale = load_stale_cache(cache_key)
        if stale is not None:
            return stale
        raise WeatherError("Weather API returned invalid JSON.") from exc

    weather = parse_weather(api_response, location_name)
    save_cache(cache_key, weather)
    return weather


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch current weather with home-location fallback")
    parser.add_argument(
        "--format",
        choices=("json", "text"),
        default="json",
        help="Output format for CLI use (default: json)",
    )
    parser.add_argument(
        "--location",
        help="Override the default/home weather location for this request",
    )
    args = parser.parse_args()

    try:
        weather = fetch_weather(location=args.location)
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

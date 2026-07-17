"""Shared formatting helpers for weather output."""

from __future__ import annotations

from typing import Any


def mission_read(weather: dict[str, Any]) -> str:
    conditions = str(weather.get("conditions", "")).lower()
    temperature_c = float(weather.get("temperature_c", 0.0))
    precipitation_mm = float(weather.get("precipitation_mm", 0.0))
    wind_speed_kmh = float(weather.get("wind_speed_kmh", 0.0))

    if "thunder" in conditions:
        return "Stormy conditions — stay sharp, stay inside if you can, and avoid unnecessary travel."
    if "snow" in conditions:
        return "Snow on the field — slower movement, extra caution, and warm layers help."
    if "rain" in conditions or "drizzle" in conditions:
        return "Wet roads and a damp sky — bring cover and move a little slower."
    if "fog" in conditions or "mist" in conditions:
        return "Low-visibility conditions — keep your bearings and don't rush."
    if temperature_c < 0:
        return "Cold enough to bite — bundle up before heading out."
    if temperature_c < 15 and wind_speed_kmh > 15:
        return "Cool, breezy air — a light jacket and steady pace will do."
    if temperature_c < 15:
        return "Clear and cool — good weather for movement, errands, or a short walk."
    if precipitation_mm == 0 and "clear" in conditions:
        return "Low-risk, clear-sky conditions — good for getting things done."
    if temperature_c >= 25:
        return "Warm conditions — keep water nearby and avoid burning yourself out."
    return "Stable weather overall — nothing dramatic, just keep an eye on the sky."


def format_cli_text(weather: dict[str, Any]) -> str:
    return (
        f"{weather['emoji']} {weather['location']} weather {weather['emoji']}\n"
        f"At a glance: {weather['temperature_c']:.1f}°C • {weather['conditions'].lower()}\n"
        f"Wind: {weather['wind_speed_kmh']:.1f} km/h • Precip: {weather['precipitation_mm']:.1f} mm\n"
        f"Observed at: {weather['observed_at']}\n\n"
        f"Shinobi read: {mission_read(weather)}"
    )


def format_telegram_message(weather: dict[str, Any]) -> str:
    header = f"{weather['emoji']} {weather['location']} weather {weather['emoji']}"
    lines = [
        header,
        "",
        f"At a glance: {weather['temperature_c']:.1f}°C • {weather['conditions'].lower()}",
        f"Wind: {weather['wind_speed_kmh']:.1f} km/h • Precip: {weather['precipitation_mm']:.1f} mm",
    ]

    observed_at = weather.get("observed_at")
    if observed_at:
        lines.append(f"Observed at: {observed_at}")

    lines.extend([
        "",
        f"Shinobi read: {mission_read(weather)}",
    ])

    return "\n".join(lines)

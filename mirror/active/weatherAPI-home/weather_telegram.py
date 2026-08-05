#!/usr/bin/env python3
"""
Fetch weather and format for Telegram delivery.
AUTHOR=MidnightRider.sol
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys

from bathurst_weather import fetch_weather
from weather_format import format_history_note, format_telegram_message


def capture_weather_note(weather: dict) -> None:
    """Best-effort QuickThoughts capture; never affect weather delivery."""
    note_cli = os.path.expanduser("~/ExoCortex/Agentic/Scripts/note")
    env = os.environ.copy()
    env["NOTE_SOURCE_LABEL"] = "Weather"
    try:
        subprocess.run(
            [note_cli, format_history_note(weather)],
            env=env,
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        pass


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Fetch weather and format for Telegram delivery")
    parser.add_argument(
        "--location",
        help="Override the default/home weather location for this request",
    )
    args = parser.parse_args()

    try:
        weather = fetch_weather(location=args.location)
        print(format_telegram_message(weather))
        sys.stdout.flush()
        capture_weather_note(weather)
        return 0
    except Exception as e:
        print(f"❌ Weather update failed: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

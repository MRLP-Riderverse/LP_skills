#!/usr/bin/env python3
"""
Fetch weather and format for Telegram delivery.
AUTHOR=MidnightRider.sol
"""

from __future__ import annotations

import argparse
import sys

from bathurst_weather import fetch_weather
from weather_format import format_telegram_message


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
        return 0
    except Exception as e:
        print(f"❌ Weather update failed: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

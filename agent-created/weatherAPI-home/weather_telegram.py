#!/usr/bin/env python3
"""
Fetch weather and format for Telegram delivery.
AUTHOR=MidnightRider.sol
"""

from __future__ import annotations

import sys

from bathurst_weather import fetch_weather
from weather_format import format_telegram_message


def main() -> int:
    """Main entry point."""
    try:
        weather = fetch_weather()
        print(format_telegram_message(weather))
        return 0
    except Exception as e:
        print(f"❌ Weather update failed: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

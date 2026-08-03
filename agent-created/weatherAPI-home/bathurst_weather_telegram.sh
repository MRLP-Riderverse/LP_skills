#!/usr/bin/env bash
set -euo pipefail

# Compatibility alias for older callers and saved cron references.
exec "$HOME/.hermes/scripts/weather_telegram.sh" "$@"

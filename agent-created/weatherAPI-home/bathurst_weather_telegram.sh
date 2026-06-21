#!/usr/bin/env bash
set -euo pipefail

WEATHER_DIR="/home/midnight/.hermes/skills/weatherAPI-home"
ENV_FILE="$HOME/.hermes/.env"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$ENV_FILE"
  set +a
fi

cd "$WEATHER_DIR"
exec python3 "$WEATHER_DIR/weather_telegram.py"

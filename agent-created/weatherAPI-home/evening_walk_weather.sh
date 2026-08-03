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

# The report and QuickThoughts capture are deterministic local shell/Python
# operations. Capture failure must never suppress the Telegram delivery.
report="$(python3 "$WEATHER_DIR/weather_walk_telegram.py" "$@")"
printf '%s\n' "$report"

NOTE_SOURCE_LABEL=Weather "$HOME/ExoCortex/Agentic/Scripts/note" "$report" >/dev/null 2>&1 || true

#!/usr/bin/env python3
"""Manage weather location env vars in ~/.hermes/.env."""

from __future__ import annotations

import argparse
from pathlib import Path

ENV_PATH = Path.home() / ".hermes" / ".env"
HOME_KEY = "HOME_LOCATION"
CURRENT_KEY = "CURRENT_LOCATION"
LEGACY_KEY = "HOME_WEATHER_LOCATION"


def parse_env_lines(path: Path) -> tuple[list[str], dict[str, str]]:
    if path.exists():
        lines = path.read_text(encoding="utf-8").splitlines()
    else:
        lines = []

    values: dict[str, str] = {}
    passthrough: list[str] = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("#") or "=" not in line:
            passthrough.append(line)
            continue

        key, value = line.split("=", 1)
        if key in {HOME_KEY, CURRENT_KEY, LEGACY_KEY}:
            values[key] = value
        else:
            passthrough.append(line)

    return passthrough, values


def quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def write_env(path: Path, passthrough: list[str], values: dict[str, str]) -> None:
    lines = passthrough[:]
    while lines and lines[-1] == "":
        lines.pop()
    if lines:
        lines.append("")
    lines.append(f"{HOME_KEY}={values[HOME_KEY]}")
    lines.append(f"{CURRENT_KEY}={values[CURRENT_KEY]}")
    content = "\n".join(lines) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def resolved_location(values: dict[str, str]) -> str:
    current = values[CURRENT_KEY].strip().strip('"')
    if current:
        return current
    home = values[HOME_KEY].strip().strip('"')
    if home:
        return home
    return "Bathurst, NB"


def load_state(path: Path) -> dict[str, str]:
    passthrough, found = parse_env_lines(path)
    state = {
        HOME_KEY: found.get(HOME_KEY) or found.get(LEGACY_KEY) or quote("Bathurst, NB"),
        CURRENT_KEY: found.get(CURRENT_KEY) or quote(""),
    }
    state["__passthrough__"] = passthrough  # type: ignore[assignment]
    return state


def cmd_status(path: Path) -> int:
    state = load_state(path)
    print(f"env_file={path}")
    print(f"{HOME_KEY}={state[HOME_KEY]}")
    print(f"{CURRENT_KEY}={state[CURRENT_KEY]}")
    print(f"effective_default={quote(resolved_location(state))}")
    return 0


def cmd_set_current(path: Path, location: str) -> int:
    location = " ".join(location.strip().split())
    if not location:
        raise SystemExit("Location cannot be blank. Use clear-current to reset it.")
    state = load_state(path)
    passthrough = state.pop("__passthrough__")
    state[CURRENT_KEY] = quote(location)
    write_env(path, passthrough, state)
    print(f"Set {CURRENT_KEY}={state[CURRENT_KEY]}")
    print(f"effective_default={quote(resolved_location(state))}")
    return 0


def cmd_clear_current(path: Path) -> int:
    state = load_state(path)
    passthrough = state.pop("__passthrough__")
    state[CURRENT_KEY] = quote("")
    write_env(path, passthrough, state)
    print(f"Set {CURRENT_KEY}=\"\"")
    print(f"effective_default={quote(resolved_location(state))}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage weather location env vars.")
    parser.add_argument("--env-file", default=str(ENV_PATH), help="Path to env file (default: ~/.hermes/.env)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("status", help="Show home/current/effective weather location")

    set_current = subparsers.add_parser("set-current", help="Set CURRENT_LOCATION to a trip city")
    set_current.add_argument("location", help='Location string, e.g. "Ottawa, ON"')

    subparsers.add_parser("clear-current", help="Clear CURRENT_LOCATION so home location is used")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    env_path = Path(args.env_file).expanduser()

    if args.command == "status":
        return cmd_status(env_path)
    if args.command == "set-current":
        return cmd_set_current(env_path, args.location)
    if args.command == "clear-current":
        return cmd_clear_current(env_path)

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

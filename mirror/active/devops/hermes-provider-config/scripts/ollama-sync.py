#!/usr/bin/env python3
"""Sync Hermes config ollama-launch provider models with actual `ollama ls` output.

Usage:
    python3 ollama-sync.py           # dry run — prints diff, no changes
    python3 ollama-sync.py --apply   # writes config.yaml

Requires: PyYAML, ollama on PATH
"""

import subprocess, sys, pathlib, yaml

PROVIDER_KEY = "ollama-launch"
CONFIG_PATH = pathlib.Path.home() / ".hermes" / "config.yaml"


def get_ollama_models():
    result = subprocess.run(["ollama", "list"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: ollama list failed: {result.stderr}")
        sys.exit(1)
    lines = result.stdout.strip().split("\n")[1:]  # skip header
    return sorted(l.split()[0] for l in lines if l.strip())


def main():
    apply = "--apply" in sys.argv

    config = yaml.safe_load(CONFIG_PATH.read_text())
    provider = config.get("providers", {}).get(PROVIDER_KEY, {})
    current = provider.get("models", [])
    actual = get_ollama_models()

    if current == actual:
        print("Already in sync. No changes needed.")
        return

    ghosts = [m for m in current if m not in actual]
    missing = [m for m in actual if m not in current]

    if ghosts:
        print(f"Ghost entries (in config, not installed): {ghosts}")
    if missing:
        print(f"Missing entries (installed, not in config): {missing}")

    default = provider.get("default_model", "")
    if default and default not in actual:
        print(f"WARNING: default_model '{default}' is NOT in actual models!")

    if not apply:
        print("\nDry run. Use --apply to write changes.")
        return

    config["providers"][PROVIDER_KEY]["models"] = actual
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    print(f"\nSynced {len(actual)} models to config.yaml")
    print("Run `/reset` or start a new session for changes to take effect.")


if __name__ == "__main__":
    main()

# Weather location helper command

Use the helper wrapper instead of manually editing `~/.hermes/.env` during travel-state changes.

## Commands

```bash
~/.hermes/scripts/weather_location.sh status
~/.hermes/scripts/weather_location.sh set-current "Ottawa, ON"
~/.hermes/scripts/weather_location.sh clear-current
```

## Intended model

- `HOME_LOCATION` is the stable base location
- `CURRENT_LOCATION` is the temporary travel override
- blank `CURRENT_LOCATION` means "use home"
- explicit `--location "City, Region"` remains the one-off non-persistent override path

## Operator rule

Keep the shared weather wrapper deterministic and `.env`-driven:

- scheduled/default weather should follow persisted state in `~/.hermes/.env`
- do not rely on ambient shell env vars for routine wrapper behavior
- use `set-current` / `clear-current` to change the persisted travel state
- use `--location` for one-off checks that should not mutate the default

## Why this matters

Trying to preserve caller-supplied env vars in the wrapper sounds flexible, but it creates a footgun in interactive sessions where inherited env state can silently override the persisted default. The cleaner split is:

- wrapper = persisted default behavior
- helper command = change persisted state
- `--location` = one-off query

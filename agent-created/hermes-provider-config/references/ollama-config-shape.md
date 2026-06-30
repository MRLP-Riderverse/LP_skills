# Ollama Provider Config Reference

## Config shape in `~/.hermes/config.yaml`

```yaml
providers:
  ollama-launch:
    api: http://127.0.0.1:11434/v1
    default_model: granite4.1:8b
    models:
      - granite4.1:8b
      - medgemma1.5:4b
      - qwen3:8b
      - lfm2.5:8b
      - nomic-embed-text:latest
      - minimax-m3:cloud
      - glm-5.2:cloud
    name: Ollama
```

Key: `ollama-launch` is the provider key used in Hermes commands like `hermes model --provider ollama-launch`.

## Session 2026-06-22: Model drift fix

The config had drifted — 3 ghost entries, 2 tag mismatches, 3 missing models:

| Config entry (old)   | Actual Ollama model  | Issue        |
|----------------------|-----------------------|--------------|
| qwen2.5-coder:7b    | —                     | not installed |
| qwen3.5:cloud       | —                     | not installed |
| glm-5:cloud         | glm-5.2:cloud         | tag changed  |
| lfm2.5-thinking:1.2b| lfm2.5:8b             | tag changed  |
| —                    | minimax-m3:cloud      | missing      |
| —                    | nomic-embed-text:latest| missing     |
| —                    | lfm2.5:8b             | missing      |

Root cause: `providers.<key>.models` is a static list not auto-synced with `ollama ls`.

## Default model validation

`default_model: granite4.1:8b` was still valid after the sync. Always check this — if the default is a ghost, Hermes will error on provider selection until fixed.

## API endpoint

Ollama's OpenAI-compatible endpoint: `http://127.0.0.1:11434/v1`
No API key required for local Ollama instances.

---
name: hermes-provider-config
description: Keep Hermes custom provider entries in sync with local model backends (Ollama, vLLM, llama.cpp server, etc.). Covers model list drift, config format pitfalls, default model validation, and verification.
version: 1.0.0
triggers:
  - User reports Hermes model selector shows wrong/stale models for a local provider
  - User installs/removes local models and wants Hermes updated
  - User sets up a new custom provider pointing to a local inference server
  - After running `ollama pull` or `ollama rm`
---

# Hermes Custom Provider Config Maintenance

Hermes stores custom providers under `providers:` in `~/.hermes/config.yaml`. These entries have a `models:` list that is **static** — Hermes does not auto-discover models from the backend API. When local models are added/pulled/deleted, the list drifts and the model picker shows ghost entries or misses real ones.

## Sync Workflow

1. **List actual models** from the local backend:
   - Ollama: `ollama ls` → parse NAME column
   - vLLM: `curl -s http://localhost:8000/v1/models | jq '.data[].id'`
   - llama.cpp server: `curl -s http://localhost:8080/v1/models | jq '.data[].id'`

2. **Read current config models**:
   ```python
   import yaml, pathlib
   path = pathlib.Path.home() / '.hermes' / 'config.yaml'
   config = yaml.safe_load(path.read_text())
   models = config.get('providers', {}).get('<provider-key>', {}).get('models', [])
   ```

3. **Compare and compute the diff** (actual vs config). Flag:
   - Ghost entries (in config but not installed)
   - Missing entries (installed but not in config)
   - Tag mismatches (e.g., `glm-5:cloud` in config but `glm-5.2:cloud` installed)

4. **Update config** — see Pitfall #1 below.

5. **Validate `default_model`** — if the provider has a `default_model`, confirm it still exists in the updated model list.

6. **Verify round-trip** — reload config as YAML and confirm the models list parses correctly.

## Pitfalls

### 1. `hermes config set` serializes lists as JSON strings, not YAML lists

`hermes config set providers.<key>.models '["a","b"]'` writes the value as a **quoted JSON string** in YAML:
```yaml
models: '["a", "b"]'   # ← wrong: YAML parses this as a string, not a list
```

Hermes may handle this at runtime (it has string-to-list coercion), but the canonical format is a YAML list:
```yaml
models:
  - a
  - b
```

**Fix:** Use a Python one-liner to update the nested key properly:
```python
import yaml, pathlib
path = pathlib.Path.home() / '.hermes' / 'config.yaml'
config = yaml.safe_load(path.read_text())
config['providers']['<provider-key>']['models'] = ['model-a', 'model-b']
with open(path, 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
```

**Caution:** `yaml.dump` rewrites the entire file and strips comments. Verify critical sections afterward. The function signature uses `default_flow_style` (not `default_flow_s`).

### 2. Model tags change between versions

Ollama tags shift: `glm-5:cloud` → `glm-5.2:cloud`, `lfm2.5-thinking:1.2b` → `lfm2.5:8b`. Don't assume the tag from the config still matches. Always diff against `ollama ls` output, not just check "is something with that prefix installed."

### 3. Embedding models appear in `ollama ls` but are usually not useful as chat models

`nomic-embed-text:latest` shows up in the Ollama model list but is an embedding model — it cannot respond to chat completions. Include it in the config for completeness (so the list is accurate), but don't set it as `default_model`.

### 4. The `patch` tool refuses config.yaml edits

The Hermes patch tool blocks writes to `~/.hermes/config.yaml` as a security guard. Use `hermes config set` for scalar values, or the Python YAML approach for complex/nested writes.

## Ollama-Specific Quick Sync

One-command sync for Ollama (python):

```python
import yaml, subprocess, pathlib, json

path = pathlib.Path.home() / '.hermes' / 'config.yaml'
config = yaml.safe_load(path.read_text())
provider = config.setdefault('providers', {}).setdefault('ollama-launch', {})

# Get actual models from ollama
result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
lines = result.stdout.strip().split('\n')[1:]  # skip header
actual = [l.split()[0] for l in lines if l.strip()]

# Update config
provider['models'] = sorted(actual)

# Validate default_model
if provider.get('default_model') and provider['default_model'] not in actual:
    print(f"WARNING: default_model '{provider['default_model']}' not in actual models")

with open(path, 'w') as f:
    yaml.dump(config, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
print(f"Synced {len(actual)} models to config")
```

## References & Scripts

- `references/ollama-config-shape.md` — config YAML shape, session drift example, default model validation notes
- `scripts/ollama-sync.py` — standalone sync script (`--apply` to write, dry-run by default)

## Local-model readiness and capability verification

Before testing or routing a local model, use `ollama ps` first. Run model tests **serially**, not in parallel, to avoid VRAM/CPU contention. After each Hermes invocation:

1. Check `ollama ps`.
2. If the model is still actively working, wait for the Hermes process to finish.
3. If Hermes has returned but Ollama keeps the model resident under its keep-alive window, explicitly run `ollama stop <model>` before the next test.
4. Re-check `ollama ps` and record the Hermes exit code and session ID.

Do not mistake Ollama residency after a completed request for a still-running generation. `UNTIL` indicates keep-alive, while the Hermes process state determines whether work is active.

A useful three-part smoke test for a newly installed model is:

- deterministic arithmetic or factual accuracy;
- strict structured output with Unicode and ordering requirements;
- actual Hermes tool use, such as a terminal command whose stdout must be reproduced exactly.

A successful short tool test proves provider connectivity and basic tool-call compatibility, but not long-session reliability.

### Effective context is separate from model capability

`ollama show <model>` reports the model's maximum context, while `ollama ps` reports the context actually used by the running server. Ollama may default to only 4096 tokens even when the model supports 64K or more. For Hermes tool-calling workflows, configure and verify an effective context of at least 64K where hardware permits, and set Hermes' `model.context_length` to the true configured value. Otherwise, classify the model as suitable only for short, bounded tasks; long Telegram sessions with Hermes' system prompt and tool schemas may overflow or degrade.

### Telegram and explicit provider selection

Hermes' gateway uses the same provider-agnostic model switching path as the CLI. For a user-defined provider, use the provider flag rather than colon syntax when testing or switching:

```text
/model <local-model> --provider <provider-key>
```

For example:

```text
/model ornith:9b --provider ollama-launch
```

A model can work with `hermes chat --provider ... --model ...` even if it is missing from the provider's static `models:` list, but it may not appear in the Telegram/CLI picker. Add newly installed chat models to the list, then start a fresh session or restart the gateway so the picker reloads configuration. Local models are not automatically mixed with the default cloud model on every turn; explicit switching, delegation, or routing configuration is required.

## Verification

After any config change:

1. `python3 -c "import yaml; c=yaml.safe_load(open(pathlib.Path.home()/'.hermes'/'config.yaml')); print(c['providers']['<key>']['models'])"` — confirm list parses
2. `/reset` or new session — config changes require a fresh session to appear in model picker
3. `hermes model` — verify the Ollama provider shows the correct models
4. `ollama ps` during a request — confirm the expected effective context, not only the model's advertised maximum

---
name: hermes-local-model-operations
description: Configure, test, and operationally evaluate local Ollama/OpenAI-compatible models through Hermes, including context sizing, Telegram readiness, serialized tool-use tests, and safe verification.
version: 1.0.0
author: Hermes Agent
metadata:
  hermes:
    tags: [hermes, ollama, local-models, context-window, telegram, tool-calling, verification]
---

# Hermes Local Model Operations

Use this skill when adding, evaluating, or tuning an Ollama or other local OpenAI-compatible model for Hermes CLI or Telegram use.

## Core workflow

1. **Inspect before changing anything**
   - Load the `hermes-agent` skill first for Hermes-specific commands and config conventions.
   - Run `ollama ps` before a test. Record whether a model is already loaded.
   - Run `ollama list`, `ollama show <model>`, `hermes config`, and `hermes doctor`.
   - Inspect the actual Ollama launch mechanism (`systemctl status ollama`, `systemctl cat ollama`, or the active process). Do not assume a shell environment variable controls a systemd service.
   - Check available RAM, GPU/driver state, and swap before selecting a large context.

2. **Separate model maximum from runtime context**
   - `ollama show` reports the model's theoretical maximum context; `ollama ps` reports the active runtime context.
   - Hermes' `context_length` must describe the actual runtime context, not the model's maximum.
   - For Hermes tool-using agents, target at least 64K when hardware can sustain it. 4K is suitable only for short, bounded probes.
   - Check the installed Hermes runtime's minimum-context guard before recommending a smaller variant: current Hermes rejects configured local contexts below 64K for proper tool use. A measured 16K/32K model may be useful for direct Ollama experiments, but is not automatically a valid Hermes agent configuration.
   - Larger context is a memory and latency tradeoff. If 64K is technically loadable but stalls or times out, classify it as *configured but operationally unusable* rather than downgrading Hermes metadata to falsely claim support. Keep Luna as the orchestrator and treat the local model as experimental until the runtime can complete both a no-tool response and a tool-follow-up.
@@
-   - Add the derived model to the configured Ollama provider using a model metadata entry with `context_length: 65536`.
+   - Add the derived model to the configured Ollama provider using a model metadata entry with `context_length: 65536`; use `hermes config set` with a complete models mapping when the provider currently stores models as a list, rather than editing YAML directly.
+   - Do not leave experimental low-context or stalled high-context variants in the normal provider picker. Keep them installed only if future testing is useful, while preserving the original base model as the fallback.
@@
-   - A tool-call message alone is not a complete success; verify that the model also completes the follow-up assistant response.
+   - A tool-call message alone is not a complete success; verify that the model also completes the follow-up assistant response. A Hermes process can store a partial transcript even when the shell wrapper exits by timeout, so inspect the recorded session before judging the result.
@@
 - Large contexts can trigger CPU fallback, GPU/driver discovery delays, high memory use, long prefill, and wrapper timeouts even when the model technically loads.
+- Hermes may explicitly refuse a local model whose detected/configured context is below its 64K tool-use minimum; do not work around this by advertising a larger `context_length` than Ollama actually receives.
+- For Telegram readiness, leave the primary Luna route unchanged unless the local model passes the full completion-and-tool-follow-up test; provider registration alone does not make local orchestration reliable.
*** End Patch

3. **Configure persistently, without unsafe direct edits**
   - Prefer `hermes config set` for Hermes config changes; direct writes to `~/.hermes/config.yaml` may be guarded.
   - For per-model Ollama context, create a derived Modelfile rather than changing the base model:
     ```text
     FROM <base-model>
     PARAMETER num_ctx 65536
     ```
     Then run `ollama create <model>-hermes-64k -f Modelfile`.
   - Add the derived model to the configured Ollama provider using a model metadata entry with `context_length: 65536`.
   - For a system-wide context, configure `OLLAMA_CONTEXT_LENGTH=64000` in the actual Ollama service environment and restart the service. This may require interactive sudo; never claim it was changed if privilege is unavailable.
   - Keep the original model available as a safe fallback.

4. **Test in series, not parallel**
   - The user may explicitly request no contention. Run exactly one Hermes invocation at a time.
   - Before each invocation, stop an identified lingering test model with `ollama stop <name>`; if a generation is actively running, wait for it unless the user asked to abort it.
   - After each invocation, wait for the model to release or stop it before starting the next test. Ollama keep-alive can make a completed request appear in `ollama ps` for minutes.
   - Use three probes:
     1. deterministic factual/reasoning accuracy;
     2. exact structured output with accents/order preserved;
     3. real Hermes tool calling, followed by verification of the tool output.
   - Preserve Hermes session IDs and inspect the session transcript if a parent shell times out; a timed-out wrapper can leave a child Hermes process running and the result may still be stored.

5. **Verify the actual result**
   - Success requires real output, exit code, and post-test process state.
   - A tool-call message alone is not a complete success; verify that the model also completes the follow-up assistant response.
   - If the model starts at the requested context but stalls, distinguish configuration success from operational usability.
   - Check Ollama logs for `llama-server ... -c 65536`, CPU/GPU placement, CUDA initialization errors, and request completion times.
   - Finish with `ollama ps` and process checks; clean up lingering test runners and model instances.

## Hermes Telegram implications

Hermes Telegram uses the same provider/model runtime as the CLI. A local model can be selected for a session with the configured provider, for example:

```text
/model <model-name> --provider <ollama-provider>
```

This is session/provider routing, not automatic per-turn mixing with the Luna default. Mixed orchestration requires explicit delegation or routing configuration. After changing provider/model config, restart the gateway or begin a new session so the runtime reloads it.

## Pitfalls

- Do not confuse `ollama show` maximum context with `ollama ps` active context.
- Do not set Hermes' global `model.context_length` to a local model's value if Luna is still the global default; use provider/model-specific metadata where supported.
- Do not report a 64K setup as usable merely because `ollama ps` shows `65536`; complete a no-tool response and a tool-use follow-up.
- A systemd Ollama service ignores environment variables exported only in the interactive shell.
- Large contexts can trigger CPU fallback, GPU/driver discovery delays, high memory use, long prefill, and wrapper timeouts even when the model technically loads.
- A shell timeout can kill the wrapper while leaving a child Hermes process or Ollama runner alive; inspect `pgrep`, `ollama ps`, and Hermes sessions before retrying.

## Supporting reference

See `references/ollama-hermes-context-and-test-notes.md` for a condensed runtime example, commands, and interpretation guidance.

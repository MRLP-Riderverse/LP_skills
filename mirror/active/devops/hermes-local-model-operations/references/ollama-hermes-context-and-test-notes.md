# Ollama + Hermes context and serialized test notes

## Context facts to preserve

Ollama can expose a model maximum context that is much larger than the active runtime context. In the observed Ornith setup, `ollama show ornith:9b` reported a 262,144-token maximum, while `ollama ps` showed an active context of 4,096. Hermes' local-agent guidance recommends 64,000 tokens for reliable tool workflows because the system prompt, tool schemas, history, and output share the context budget.

A persistent per-model Modelfile is a useful pattern:

```text
FROM ornith:9b
PARAMETER num_ctx 65536
```

Create it with:

```bash
ollama create ornith-hermes-64k:latest -f Modelfile
ollama show ornith-hermes-64k:latest | grep -E 'num_ctx|context length'
```

Then register the model in Hermes' named provider with model-level metadata:

```yaml
providers:
  ollama-launch:
    api: http://127.0.0.1:11434/v1
    models:
      ornith-hermes-64k:latest:
        context_length: 65536
```

Use `hermes config set` when possible because Hermes may guard direct edits to `~/.hermes/config.yaml`.

## Serialized test recipe

1. `ollama ps`
2. Stop a lingering test model with `ollama stop <model>`; wait for an active generation when appropriate.
3. Run one `hermes chat` invocation with explicit `--provider`, `--model`, and a small toolset.
4. Capture the Hermes session ID and exit code.
5. Inspect `ollama ps`, `pgrep -af 'hermes chat|llama-server'`, and the session transcript if output is missing.
6. Stop/wait for the model before the next test.

A keep-alive entry in `ollama ps` after a successful request is not necessarily a stuck generation. It can remain resident until Ollama's idle timeout. Conversely, a wrapper timeout does not prove Hermes produced no result: a child process may continue and its session can contain a tool call or final answer.

## Interpretation of the 64K Ornith probe

The derived model did launch with `llama-server -c 65536`, and `ollama ps` showed `CONTEXT 65536`. Hermes reached the model and Ornith issued the requested terminal tool call successfully. However, the follow-up completion was not operationally acceptable in the tested environment: CPU usage was 100%, the model occupied roughly 11 GB, CUDA initialization reported a forward-compatibility/driver mismatch, and a minimal no-tool completion exceeded the test timeout. This means “configured correctly” and “usable for long Telegram orchestration” are separate verdicts.

Keep the base model intact. Consider 16K or 32K derived variants when 64K causes CPU fallback or very long prefill. Revisit 64K after resolving GPU/driver compatibility or moving inference to hardware with enough memory bandwidth.

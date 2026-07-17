# Ollama Thinking-Token Behavior: lfm2-thinking Parser

**Date:** June 2026
**Context:** Attempted to swap `qwen3:8b` for `lfm2.5:8b` in the nightly session review cron. Discovered that thinking tokens are embedded in API response bodies with no clean way to strip them programmatically.

---

## The Problem

Models using Ollama's `lfm2-thinking` parser (e.g. `lfm2.5:8b`) embed their internal reasoning directly in the `response` field of `/api/generate` and the `content` field of `/api/chat`. The reasoning is wrapped in `<ȠϹ>...ȠϹ>` tags (Unicode thinking markers).

**Neither `think: false` nor `/no_think` in the prompt suppresses these markers.**

### What doesn't work

| Approach | Result |
|----------|--------|
| `think: false` in `/api/generate` payload | Thinking still appears in `response` |
| `think: false` in `/api/chat` payload | Thinking still appears in `message.content` |
| `/no_think` prefix in prompt | Model interprets it as part of the prompt, still thinks |
| Checking for `thinking` field in response JSON | Field doesn't exist — Ollama <0.6 doesn't separate it |
| Post-processing with `re.sub(r'<ȠϹ>.*?ȠϹ>', '', raw, flags=re.DOTALL)` | Closing tag often absent (model hits token limit before closing) |

### What does work (with tradeoffs)

| Approach | Result | Tradeoff |
|----------|--------|----------|
| `ollama run lfm2.5:8b --hidethinking "prompt"` | Thinking hidden in CLI output | CLI-only, no API equivalent |
| Custom Modelfile with `TEMPLATE {{ .Prompt }}` (no RENDERER/PARSER) | Thinking stripped at template level | May degrade output quality; thinking was part of training |
| Use a non-thinking model (qwen3:8b, etc.) | No thinking tokens at all | Different model capabilities |

### Custom Modelfile for no-think variant

```
FROM lfm2.5:8b
TEMPLATE {{ .Prompt }}
PARAMETER repeat_penalty 1.05
PARAMETER temperature 0.2
PARAMETER top_k 80
```

Create with: `ollama create lfm2.5-nothink -f Modelfile.lfm2-nothink`

Tested June 2026: this successfully removes thinking tokens from API responses, but the model's actual output quality drops (it still "thinks" but the chain-of-thought is discarded rather than hidden, so the final answer is less coherent).

---

## Ollama Version Context

- **Ollama 0.30.3** (tested): No `thinking` field in API response for lfm2 models
- **Ollama 0.6+** (rumored): May add proper `thinking` field separation — untested
- Check with: `ollama --version`

---

## Decision Rule

**For scripted pipelines (cron jobs, automated tasks):** prefer non-thinking models or deterministic approaches. If you need a thinking model's quality, use the CLI with `--hidethinking` and capture stdout, or wait for Ollama to add proper API-level thinking separation.

**For interactive use:** `--hidethinking` works fine; the user never sees the thinking tokens.

---

## Session Reference

This was discovered during the `daily-session-review-notes` cron rewrite (June 2026). The cron was converted to a deterministic GBrain sync status check with no model calls at all — see Section C of `gbrain-operations/SKILL.md`.

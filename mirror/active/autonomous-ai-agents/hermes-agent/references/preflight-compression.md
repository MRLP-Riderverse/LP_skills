# Preflight compression

Session-backed note on Hermes' proactive context-shrinking path.

## What it is
Preflight compression runs *before* the main model call when the loaded history already appears to exceed the compressor threshold. The goal is to avoid waiting for an API-side context-length / payload-too-large failure.

## Trigger shape
The current agent loop checks preflight when:
- `compression_enabled` is true
- the transcript has enough non-protected messages to be compressible
- `estimate_request_tokens_rough(messages, system_prompt, tools)` is at or above `context_compressor.threshold_tokens`

The docs/code path describe this as "preflight compression" and the startup warning is replayed into the first turn when needed.

## Useful interpretation
If preflight compression "fires again" but fails, it usually means one of:
- the transcript was already under the threshold after a pass, so no further shrinkage was possible
- the head/tail protection window left too little compressible middle content
- the compressor could not reduce the transcript enough to get under the threshold
- the underlying compression step errored

Treat the failure as "Hermes correctly detected pressure, but the available middle content was not enough to recover" unless logs show a distinct exception.

## Verification crumbs
Relevant source locations used during this session:
- `run_agent.py` around the preflight check in `run_conversation()`
- `website/docs/developer-guide/agent-loop.md` turn lifecycle
- `tests/run_agent/test_413_compression.py` preflight coverage

## Practical debugging questions
- Was compression enabled for the session?
- Did the model switch to a smaller context window?
- Were tools included in the rough token estimate?
- Did the transcript already consist mostly of protected head/tail turns?
- Did the next failure come from preflight, or from the later 413/context-overflow fallback path?

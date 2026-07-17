# Hermes Embedding & Search Internals

Findings from investigating whether Hermes uses a dedicated embedding model
and where nomic-embed-text (or any local embedder) could be wired in.

## Bottom line

**Hermes has no embedding pipeline.** There is no `embed_model`,
`embed_provider`, or `embedding` config key in `config.yaml` or the default
config schema (`hermes_cli/config.py`). The `auxiliary_client.py` comment
listing "embedding" as an auxiliary task type is aspirational/roadmap — no
actual embedding API call exists in the codebase.

## Session search: FTS5 keyword only

- `hermes_state.py` creates SQLite FTS5 virtual tables (`messages_fts`,
  `messages_fts_trigram`).
- PR #27590 removed the auxiliary LLM from session_search entirely.
- Pure token matching, no vector similarity, no embedding model involved.
- The `auxiliary.session_search.*` config block was removed in that PR.

## Built-in memory: text injection

- Default memory provider stores key-value text in memory/user stores and
  injects it into the system prompt. No vectors, no embedding calls.

## Memory plugin embedding status

| Plugin | Uses embeddings? | Notes |
|--------|-----------------|-------|
| holographic | No | HRR binary phase vectors (not neural embeddings). No external model. |
| retaindb | Server-side | Cloud service; embeds internally. No local config. |
| hindsight | LLM only | `local_embedded` mode uses an OpenAI-compatible LLM for memory *extraction*, not embedding-based retrieval. Has `llm_provider`, `llm_model`, `llm_base_url` config keys. |
| honcho | Server-side | Cloud. |
| mem0 | Server-side | Cloud. |
| supermemory | Server-side | Cloud. |
| openviking | Server-side | Cloud. |
| byterover | Server-side | Cloud. |

## Where nomic-embed-text could plug in

Ollama exposes an OpenAI-compatible embedding endpoint at
`http://127.0.0.1:11434/v1/embeddings` (or the native
`/api/embeddings`). The model `nomic-embed-text:latest` produces 768-dim
vectors and is confirmed working locally.

To actually use it you would need one of:

1. **Custom plugin/skill** — a semantic search wrapper over session DB or
   files that calls the Ollama embedding endpoint and stores/recalls
   vectors in a local DB (e.g. SQLite + `numpy` cosine similarity).
2. **Hindsight plugin enhancement** — wire an embedding-based retrieval
   layer into hindsight's `local_embedded` mode (currently LLM-only).
3. **Upstream feature** — the `auxiliary_client.py` comment suggests
   embedding is on the roadmap but not yet implemented.

## Source locations verified

- `hermes_cli/config.py` — no `embed_*` keys in DEFAULT_CONFIG
- `agent/auxiliary_client.py:3601` — "embedding" in auxiliary task comment only
- `hermes_state.py:321,350` — FTS5 table creation
- `hermes_cli/config.py:1179` — session_search auxiliary block removal note
- `agent/models_dev.py` — embedding models filtered from agentic model lists
- `agent/bedrock_adapter.py` — `cohere.embed` / `amazon.titan-embed` filtered out
- `plugins/memory/holographic/retrieval.py` — HRR + BM25 + Jaccard, no neural embed
- `plugins/memory/hindsight/__init__.py:843-878` — `local_embedded` mode config fields

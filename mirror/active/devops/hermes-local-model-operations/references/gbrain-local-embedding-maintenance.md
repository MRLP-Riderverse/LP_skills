# GBrain local embedding maintenance

Use when a local GBrain/PGLite index is being migrated to or maintained with an Ollama embedding model.

## Safe migration sequence

1. Back up independently:
   - `~/.gbrain` database/config state;
   - the Markdown source corpus;
   - any local GBrain source modifications;
   - record checksums.
2. Confirm local model availability and a real provider probe:
   ```bash
   gbrain providers test --model ollama:nomic-embed-text
   ```
3. Plan before mutation:
   ```bash
   gbrain migrate embeddings --to ollama:nomic-embed-text --dim 768 --dry-run
   ```
4. Run a resumable, bounded migration:
   ```bash
   gbrain migrate embeddings --to ollama:nomic-embed-text --dim 768 \
     --yes --batch-size 25 --pace=gentle
   ```
5. Verify after completion:
   ```bash
   gbrain stats
   gbrain doctor --json
   gbrain search '<conceptual query>'
   ```
   Check: all chunks embedded, no stale chunks, schema dimensions match, provider is persisted, and conceptual results are plausible.
6. Snapshot the new known-good `~/.gbrain` state.

## Daily stale catch-up

If a deterministic importer uses `gbrain import --no-embed`, embeddings do **not** automatically happen. Add a separate job after import:

```bash
gbrain embed --stale --batch-size 25 --pace=gentle
```

The job should compare `Chunks` vs `Embedded`, exit silently when current, and deliver a concise report only after embedding new/stale chunks. Schedule it after daily import and before any daily health/status job. Keep source imports and embedding maintenance separate.

## Interpretation guardrails

- Vectors are rebuildable retrieval derivatives; raw notes and Markdown remain evidence.
- Do not mix models/dimensions in one vector column. Use the migration path rather than writing vectors directly.
- A successful full run proves current chunk compatibility, not generic long-document support. Inspect actual Ollama runtime context in logs.
- Treat semantic search quality as an evaluation problem: test exact, paraphrase, domain-specific, and multilingual queries. Prefer raw-source evidence over generated/sanitized derivatives when accuracy matters.

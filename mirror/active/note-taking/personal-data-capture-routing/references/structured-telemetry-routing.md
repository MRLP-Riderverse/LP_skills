# Structured Telemetry Routing

Recurring measurements such as weather are useful longitudinal context, but they should not automatically become high-volume QuickThoughts entries.

Preferred boundary:

```text
local append-only structured archive → optional compact QuickThoughts note → periodic pattern synthesis
```

Keep the raw measurement archive local and structured (JSONL or CSV). Minimum useful metadata includes local observation time, location/context, primary measurement, conditions/state, units, and provenance/source. Use QuickThoughts for deliberate human-readable observations, meaningful anomalies, or low-frequency summaries—not every scheduled reading.

This preserves QuickThoughts as a low-friction human stream and warm narrative layer while keeping exact historical measurements available for deterministic analysis. Distinguish automated measurements from direct human observations and later interpretations during analysis.

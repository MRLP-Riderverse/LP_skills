---
name: deterministic-agent-tool-selection
description: "Use for small tasks: pick the narrowest deterministic tool."
category: devops
---

# Deterministic Agent Tool Selection

Choose the smallest tool and execution path that matches the actual operation. Preserve intentional side effects, avoid turning a simple deterministic step into broad arbitrary-code execution, and explain approval prompts from the real execution trace rather than assumptions.

## Operating Rules

1. **Identify the real operation before selecting a tool.** Separate the primary task from presentation-only post-processing. For example, a weather wrapper may intentionally fetch data *and* append a labeled QuickThoughts observation; that archival write is part of the design, not accidental scope.
2. **Prefer an existing deterministic wrapper over ad hoc recomputation.** If a script can format the requested output, use or extend that script so the whole path remains one verified operation.
3. **Use the narrowest tool for post-processing.** Do not invoke general-purpose `execute_code` merely for trivial arithmetic, string formatting, or unit conversion when the deterministic producer can emit the result directly or a narrowly scoped terminal command is sufficient.
4. **Do not weaken global safety controls to remove local friction.** Avoid changing `approvals.mode`, enabling YOLO, or adding broad allowlist entries just because one harmless operation produced an approval request.
5. **Distinguish tool approvals from script side effects.** A terminal wrapper can contain intentional network access and append-only note capture without being the object that triggered an approval. Identify which tool call was pending and correlate it with the approval-resolution timestamp.
6. **Treat approval prompts as evidence to investigate, not evidence of danger.** Check the live command detector, Tirith/security result, approval mode, and execution logs. Report the exact cause and correct earlier explanations when the trace contradicts them.
7. **Keep intentional local capture intact.** When a workflow deliberately routes observations through the canonical QuickThoughts `note` CLI, preserve that behavior and its source label. Do not “fix” an approval symptom by removing the archive write.

## Weather and Similar Deterministic Reports

For current-weather one-shots and routine reports:

- Prefer the generic weather wrapper with an explicit location override.
- Let the wrapper perform the live fetch, formatting, and intentional `Notes, by Weather` capture.
- Preserve Celsius as the default when the source and user workflow are Celsius-based; do not add Fahrenheit merely for symmetry.
- If Fahrenheit is explicitly requested, have the deterministic formatter or Open-Meteo unit parameter handle it inside the weather path rather than asking the agent to calculate a second presentation value.
- Keep weather delivery LLM-free where the workflow is already deterministic.
- Verify the observed timestamp and report only values returned by the live source.

## Completion-triggered archival side effects

For maintenance/update scripts that intentionally append a QuickThoughts artifact after successful work:

1. Put the canonical `note` call at the terminal completion point, never at invocation/startup.
2. If the script continues after recoverable command errors, accumulate a failure state while preserving its existing error output and continuation behavior.
3. Only capture the success note when no tracked work step failed; skip capture on partial or failed runs so the log does not create false success evidence.
4. Keep the script's own completion timestamp independent of note capture.
5. Reuse existing script identity variables and concise source-labeled prose. If the source label already names the script, avoid repeating that name in the note body; use wording such as `job completed successfully`.
6. Keep capture failure separate from the primary job result unless the script explicitly requires archival success for overall success.

Verify both paths with deterministic mocks: a successful run must append one correctly formatted note, while a simulated update failure must still finish its normal output and append nothing.

## Approval Diagnosis Checklist

When a harmless request unexpectedly produces an approval prompt:

1. Locate the current turn and exact tool-call sequence in the live agent/gateway logs.
2. Match the approval-resolution timestamp to the immediately preceding pending tool call.
3. Inspect the pending command or script, not merely the user-facing task description.
4. Run the live dangerous-command detector and security scanner against the exact command when safe to do so.
5. Check whether the command was blocked, warned, or simply executed through a tool with a broader approval boundary.
6. Preserve intentional side effects and change only the unnecessary tool choice or formatter path.
7. Re-test the full path and verify both the user-facing result and any intended local archive write.

## Common Pitfalls

- Blaming a wrapper’s intentional QuickThoughts append when the approval actually belongs to a later `execute_code` presentation step.
- Assuming `approvals.mode: manual` means every terminal command will prompt, or that every prompt means the underlying command was classified dangerous.
- Using arbitrary Python execution for a one-line conversion and then “fixing” the resulting prompt by weakening global approvals.
- Reporting an approval cause before checking the execution log.
- Removing useful provenance/archive behavior to make a workflow appear side-effect-free.

## Verification Standard

A workflow is repaired only when a live run proves:

- the intended deterministic wrapper executes;
- intentional capture/archive behavior still occurs;
- no unnecessary broad execution tool is invoked afterward;
- any remaining approval is attributable to a real safety boundary; and
- the final response is grounded in the live output.

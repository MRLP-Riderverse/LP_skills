# Weather Approval Trace (Verified Pattern)

## Symptom

A live weather one-shot produced an unexpected Telegram approval request even though the weather wrapper intentionally performs network access and appends a `Notes, by Weather` observation to QuickThoughts.

## Verified execution sequence

1. Hermes loaded `weatherAPI-home`.
2. The terminal call to `~/.hermes/scripts/weather_telegram.sh --location "Avon, IN"` completed without the approval.
3. The wrapper fetched and formatted the weather and ran the intentional Weather-labeled QuickThoughts capture.
4. A later `execute_code` call was used only to convert `26.5°C` to Fahrenheit.
5. Telegram resolved one approval with `choice=once` immediately before `execute_code` completed.

## Root cause

The approval belonged to the broader-capability `execute_code` tool, whose sandbox may spawn subprocesses or mutate files. It did not belong to the weather wrapper or its intentional note capture.

The exact weather command was independently checked against the live dangerous-command detector and Tirith scanner: both allowed it.

## Repair principle

Do not weaken global approvals or remove intentional QuickThoughts capture. Prefer extending the deterministic formatter to emit both temperature units, or use the narrowest available calculation path instead of general-purpose `execute_code` for presentation-only arithmetic.

## Diagnostic evidence pattern

Correlate:

- the gateway approval-resolution timestamp;
- the agent tool-executor entries immediately before and after it;
- the exact pending tool call;
- live detector/security results for the exact command.

Never infer the approval target from the user-facing task description alone.

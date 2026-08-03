# Temporary Tagging and Delegation Reference

## Tag grammar

Use a small set of literal tags in the raw QuickThoughts entry:

- `[HUMAN]`: personal authored observation
- `[PULSE]`: immediate state or energy signal
- `[ACTIVITY]`: current action or embodied experience
- `[FRICTION]`: blockage, transition loss, avoidance, or context-switch cost
- `[ENDDAY]`: end-of-day reflection
- `[TASK]`: actionable item
- `[SOMEDAY]`: non-urgent actionable item
- `[FUTURE]`: later concept or infrastructure direction

Prefer the smallest set clearly supported by the text. A single entry may carry multiple tags, but tags should not become a forced questionnaire.

## Delegated classifier contract

Prompt a delegated worker to return:

1. one concise tagged version of the raw note;
2. a short explanation for each selected tag;
3. no file writes, memory writes, or invented context.

Explicitly prohibit invented timestamps, locations, quantities, causes, health claims, or emotional interpretations not present in the source. The parent agent reviews the proposal, appends through the canonical `note` CLI, and verifies when the user wants proof.

## Example

Raw:

> trying this new nestle coffee in a red tin, its strong but pretty good, i feel energized

Good proposal:

```text
[HUMAN] [ACTIVITY] [PULSE] Trying this new Nestlé coffee in a red tin; it is strong but pretty good, and I feel energized.
```

Why:

- `[HUMAN]`: personal sensory opinion and experience
- `[ACTIVITY]`: trying/drinking the coffee
- `[PULSE]`: immediate energized feeling

Do not add `[TASK]`, `[FRICTION]`, or `[ENDDAY]` without evidence.

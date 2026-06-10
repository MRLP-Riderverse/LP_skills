---
name: excalidraw-review-repair
description: Review, repair, and verify existing Excalidraw diagrams by fixing logic, rendering a preview, and visually checking for clipping or misleading structure before saving.
version: 1.0.0
author: Hermes Agent
tags: [excalidraw, diagrams, review, repair, verification, vision]
---

# Excalidraw Review + Repair Workflow

Use this skill when the user asks to review an existing `.excalidraw` file, reason about it, repair it, and save the corrected result.

## Best-fit cases
- Existing diagram needs logical cleanup or label fixes
- The JSON is valid but the diagram is confusing, clipped, or misleading
- You need to compare the written diagram with its rendered appearance
- A small iteration loop is needed: edit -> render -> inspect -> refine

## Workflow

1. **Read the `.excalidraw` JSON carefully**
   - Check element order, text labels, bindings, and coordinates.
   - Look for obvious logic problems: duplicate labels, inconsistent naming, or arrows that imply the wrong flow.

2. **Make the minimal useful repair first**
   - Prefer small targeted edits over rewriting the whole diagram.
   - Keep the visual style stable unless the layout itself is the problem.

3. **Render a preview outside Excalidraw**
   - Generate a PNG or SVG preview with a lightweight local renderer.
   - This is especially useful for spotting clipped text, cramped notes, and mislabeled arrows.
   - If the preview renderer is approximate, use it only to catch gross layout issues.

4. **Visually inspect the preview**
   - Confirm the diagram reads correctly as a story, not just as valid JSON.
   - Check the right edge for clipping and the spacing around annotation blocks.
   - Verify that labels match the intended meaning of each layer or node.

5. **Iterate only where needed**
   - Adjust text placement, note width, or wording when the preview exposes a problem.
   - Re-render after any non-trivial edit.

6. **Save the repaired `.excalidraw` file**
   - Keep the output path the same unless the user requests otherwise.

## Repair heuristics
- If a label appears twice in different semantic roles, rename one so the distinction is explicit.
- If a flow note is more misleading than helpful, make the language more concrete or shorter.
- If the right-side note is cramped, move it left or narrow the text.
- If the diagram is a mental model, prefer conceptual terms over implementation jargon unless the user asked for implementation details.

## Verification checklist
- The JSON is still valid Excalidraw.
- The preview shows no clipped labels.
- The flow arrows match the intended meaning.
- The repaired labels are internally consistent.
- The final file is saved and ready to open in Excalidraw.

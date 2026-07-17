# Persona Layering Review — Session Pattern

This session established a reusable review pattern:

- The active custom persona was `~/.hermes/SOUL.md`, not the generic bundled Docker SOUL template.
- The custom SOUL was small and behaviorally coherent; the main optimization issue was not its byte count.
- A separate configured stock personality (`display.personality`) can introduce a second voice and conflict with SOUL. Treat this as a layering/configuration issue, not a reason to bloat SOUL.
- The memory offload path worked as intended: capture durable identity/philosophy to QuickThoughts with the canonical `note` CLI, verify the stored tail entry, then remove/compress the hot-memory copy.
- Keep deeper identity philosophy available in QuickThoughts until the user deliberately decides which parts deserve stable SOUL status.

This reference is session-specific; re-check live config and files before applying the pattern elsewhere.

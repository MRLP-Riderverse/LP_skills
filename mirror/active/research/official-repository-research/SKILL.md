---
name: official-repository-research
description: "Use for official repo/docs implementation research."
category: research
metadata:
  hermes:
    tags: [research, source-inspection, open-source, documentation, architecture]
---

# Official Repository Research

Use when the user asks how an open-source project implements a feature, where its code lives, what APIs or extension points exist, or whether a change can be made without forking. This is implementation recon, not a generic product summary.

## Goals

- Establish what the official source actually implements.
- Map files, classes, functions, handlers, registries, and data flow.
- Separate existing support from documented no-fork extension paths.
- Identify where core modification or a custom adapter becomes necessary.
- Report hard constraints and lifecycle/security behavior with canonical citations.

## Source hierarchy

Prefer, in order:

1. Official repository source at the requested branch or pinned commit.
2. Official documentation and developer guides.
3. Official issues/PRs for history, regressions, or explicitly reported gaps.
4. Search snippets only for discovery; never use a snippet to support details that require the page body.

If the user requires official sources only, do not fill gaps with third-party tutorials. Identify dependency documentation separately if it becomes necessary.

## Procedure

1. Confirm the canonical repository and official docs domain.
2. Search docs for the feature, extension model, configuration, and developer internals.
3. Discover source paths from the repository tree or official search results. Do not assume old paths when the project may have migrated code into plugins.
4. Inspect concrete symbols: imports, class definitions, registration calls, message builders, dispatch handlers, registries, and state stores.
5. For large files, fetch the official raw file to a temporary path, search for symbols, then read narrow ranges around each match. Avoid dumping an entire source file into context.
6. Build a compact implementation map with `file → symbol → responsibility → extension boundary`.
7. Classify every requested capability:
   - **Existing:** already implemented in inspected source.
   - **No-fork:** available through documented config, plugin, hook, command, or adapter APIs.
   - **Core/custom adapter:** requires editing the built-in implementation or supplying a separate adapter/service.
8. Extract constraints exactly: API byte/length/count limits, naming syntax, scopes, pagination, authorization, expiration, restart behavior, and payload limits.
9. Verify source URLs before reporting. Cite the specific file or docs page supporting each substantive claim.

## Telegram/UI checklist

For Telegram buttons and callbacks, inspect:

- `InlineKeyboardButton` and `InlineKeyboardMarkup` construction.
- `reply_markup` passed to send/edit calls.
- `CallbackQueryHandler` registration and callback dispatch.
- Callback-data namespaces/prefixes and state lookup/expiration.
- `query.answer()` calls and message-edit/removal behavior.
- Authorization checks for shared chats or privileged actions.
- The central slash-command registry and adapter `set_my_commands` calls.
- Chat command scopes, forum-topic behavior, command caps, and name sanitization.

Do not assume a generic plugin or lifecycle hook can inject arbitrary Telegram markup. Confirm that the public contract exposes the Telegram client, `reply_markup`, or callback registration. Plugin slash commands and custom inline-button handlers are separate extension questions.

## Reporting format

Use a compact table or bullets:

- **Source map:** file, class/function, behavior.
- **Existing support:** what works today.
- **No-fork path:** exact API/config/plugin route and limitations.
- **Modification boundary:** what is adapter-internal or undocumented.
- **Constraints:** exact limits and security/lifecycle rules.
- **Sources:** canonical repository and docs URLs.

Keep the report concise but specific enough for a developer to locate the implementation.

## Pitfalls

- Do not report a search snippet as if the full page was inspected.
- Do not infer plugin capability from the word “plugin”; inspect the registration contract.
- Do not conflate a command menu with inline keyboards or callback queries.
- Do not omit authorization and state lifetime when describing buttons that change configuration or approve actions.
- Do not rely on stale pre-plugin paths; verify the current tree and migration glue.
- Do not claim “no support” merely because one symbol was not found; inspect the adapter registration, plugin API, and docs before concluding.

## Reference

See `references/official-repository-recon.md` for the reusable evidence hierarchy, Telegram-specific search checklist, and compact implementation-map template.

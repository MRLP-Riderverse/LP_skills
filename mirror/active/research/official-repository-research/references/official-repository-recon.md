# Official Repository and Documentation Recon

## Evidence-first sequence

1. Start at the canonical docs and repository, not third-party summaries.
2. Search docs for the feature, developer internals, and extension model.
3. Inspect the repository tree or known source paths. For large files, fetch an official raw file to a temporary path, search concrete symbols, and read narrow ranges around matches.
4. Produce a compact map: `file → class/function → behavior → extension point`.
5. Classify findings as: already implemented; supported without a fork; or requiring core changes/custom adapter.
6. Capture hard constraints from source/docs exactly: API limits, payload sizes, scopes, authorization, state lifetime, and naming rules.
7. Cite canonical source URLs directly. Treat search snippets as discovery hints only, not as evidence for details that require page contents.

## Telegram/UI checklist

For buttons, inspect imports and handler registration first (`InlineKeyboardButton`, `InlineKeyboardMarkup`, `CallbackQueryHandler`), then locate message builders, callback dispatch, state storage, authorization checks, and `query.answer()` / message-edit behavior. For slash menus, inspect the central command registry and the adapter's `set_my_commands` registration, including chat scopes and cap logic.

Do not infer that a generic plugin or lifecycle-hook API can inject arbitrary platform UI unless the documented contract exposes the platform client or markup/callback registration. Distinguish plugin slash commands (which may be menu-integrated) from custom inline handlers that remain adapter-internal.

## Compact reporting template

- **Implementation map:** file, class/function, responsibility.
- **Existing support:** what works today.
- **No-fork path:** exact API/config/plugin route and limitations.
- **Modification boundary:** what is undocumented or adapter-internal.
- **Constraints:** exact limits and security/lifecycle rules.
- **Sources:** official docs and repository URLs.

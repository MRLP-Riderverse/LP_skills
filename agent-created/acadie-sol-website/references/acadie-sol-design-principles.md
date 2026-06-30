# Acadie.sol Design Principles (condensed)

- **OS/Product Interaction Design**: Treat the site as a native app or OS shell, not a traditional website. Prioritize low-friction, tactile interactions (e.g., glassy dock, upward‑opening drawer, edge‑to‑edge poster).
- **Low‑Friction Raw‑Preserving Drafts**: Incomplete entries or ideas should be captured quickly with minimal structure. Use a simple intake form (name mandatory, other fields in a Notes block) and avoid over‑structuring at the draft layer.
- **Clear Modularity & Comments**: Every HTML/CSS/JS block should have a preceding comment that explains its purpose and how it relates to neighboring sections. This aids future maintenance and ensures the intent is obvious.
- **Token‑Based Theming**: All colors, shadows, and layering values must flow from CSS custom properties (`--bg`, `--paper`, `--ink`, etc.) defined in `:root` and `[data-theme=\"dark\"]`. Avoid hard‑coded hex values.
- **Dock‑First Navigation**: Primary navigation resides in the bottom dock (Home → Events → Search → Menu). The dock is glassy/translucent with blur and backward‑compatible backdrop.
- **Progressive Disclosure**: Use `<details>/<summary>` for expandable cards; show only title + meta pills in the summary, and reveal thumbnail, description, and actions only on expand.
- **Universal Components**: Reuse the same card, dock, drawer, and button patterns across pages to keep the feel consistent and reduce cognitive load.
- **Mobile‑First Viewport**: Design for a 430px width phone shell; test layout and interactions on actual mobile devices or emulators.
- **Accessibility Touch Targets**: Ensure interactive elements are at least 44x44px with adequate spacing.
- **Performance Mindset**: Keep CSS minimal, avoid large JS libraries, and leverage native browser features (e.g., `<details>`, CSS gradients) to maintain fast load times.
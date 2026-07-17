# GitHub Pages + SNS / `.sol.site` note

Session takeaway from the Acadie.sol setup:

- The site repo can be a normal GitHub Pages static site and still work fine with a custom domain workflow.
- A custom `*.sol.site` identity layer is not automatically the same thing as DNS pointing at GitHub Pages.
- In this session, `acadie.sol.site` did not resolve from the local machine, while the GitHub Pages URL `https://mrlp-riderverse.github.io/acadie.sol/` served successfully.
- That points to a domain/DNS/config mismatch, not a need to abandon GitHub Pages by default.

Practical check order:
1. Confirm the Pages site is live at the GitHub Pages URL.
2. Confirm the site repo has the correct root entrypoint (`index.html`).
3. Confirm the custom domain actually resolves to the Pages target.
4. Only then evaluate whether the custom domain provider/branding rail needs to change.

Do not assume a registrar or identity dashboard has completed the DNS handoff just because the name is visible in the UI.
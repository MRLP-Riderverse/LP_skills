---
name: static-site-prototype-iteration
description: "Iterate on a static concept website when the current mockup feels noisy or off-target. Focus on reduction first: preserve a backup, split secondary content into separate pages, prototype one strong hero component, and defer frameworks like React until the interaction model actually demands them."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [static-sites, html, css, javascript, prototyping, ui-iteration, reduction]
    related_skills: [plan, writing-plans]
---

# Static Site Prototype Iteration

## Overview

Use this skill when a static HTML/CSS/JS site or mockup has too much visual noise, unclear hierarchy, or too many concepts competing on one page.

The key move is **reduction before expansion**:
1. preserve the current version
2. move secondary ideas off the homepage
3. make one strong, readable prototype component
4. validate that prototype before templating or scaling it out

This works especially well for concept sites, playful IP demos, lore-heavy pages, and faux-product landers that started to sprawl.

## When to Use

Use when the user says or implies things like:
- "this feels noisy"
- "too much going on"
- "make it clearer"
- "split this into pages"
- "let’s make one card/component first"
- "do we really need React for this?"

Best fit when:
- the project is already static HTML/CSS/JS
- the goal is to improve presentation and legibility fast
- the user wants iterative visual review before scaling up

## Core Principles

### 1. Preserve before reducing
Before simplifying or deleting, create a backup or snapshot of the current site so reduction feels safe.

### 2. Homepage should do one thing well
If the homepage is trying to explain everything, move support content to dedicated pages and keep the front page focused on a single hero artifact.

Examples of a strong hero artifact:
- one CRT-style profile card
- one featured character panel
- one product terminal card
- one interactive mockup tile

### 3. Prototype once before templating
Do **not** build five variations before one version is approved.
Make one polished-enough prototype, then ask whether it should become the template.

### 4. Prefer CSS/JS-first for early interaction
For hover flicker, subtle reactions, simple state changes, and playful UI behavior, static HTML/CSS/JS is usually enough.
Do **not** introduce React just because the user mentioned it as a possibility.
Reach for React only when:
- many repeated components must be data-driven
- state is becoming deeply nested
- interactions are truly app-like rather than presentational

### 5. Keep a review ledger current
If the project has a `REVIEW_TODO.md` or similar review/source-of-truth file, update it as part of the workflow, not as an afterthought.

## Workflow

### Step 1: Read the project instructions first
Check for local guidance before editing:
- `README.md`
- `REVIEW_TODO.md`
- local instruction files
- project-specific policy docs

Look for constraints like:
- static-only stack
- no new dependencies
- keep logs append-only
- use a specific review file as source of truth

### Step 2: Snapshot the current version
Create a backup copy before major reduction or restructuring.

Typical cases:
- noisy homepage about to be simplified
- deleting or rewriting sections
- moving content into separate pages

### Step 3: Identify homepage vs support content
Sort existing content into two buckets:

**Homepage only:**
- the clearest expression of the concept
- one main interactive or visual hook
- only the top-level summary needed to orient the user

**Support pages:**
- logs
- lore/about
- activity feeds
- rosters/grids
- secondary experiments
- detailed system explanations

If several concepts are competing, split them into dedicated pages rather than compressing them all into one layout.

### Step 4: Build one strong prototype component
Create or refine a single focal component that embodies the desired tone and function.

Examples:
- a single character card with HUD stats
- a fake terminal monitor with one creature inside
- one collectible card with hover reactions

The prototype should answer:
- what is the object the user is meant to care about?
- is it readable at a glance?
- does it carry the project’s vibe?
- is it good enough to clone later?

### Step 4b: If the user says “match this other local site,” do a branding-transfer pass
When the user wants the new mockup to feel like another project they already made, do **not** just borrow layout. Inspect the reference project directly and extract its reusable brand language.

Check at minimum:
- `README.md` for project intent and tone
- homepage HTML for structure and naming patterns
- main CSS for palette, gradients, borders, shadows, typography, spacing, and chrome
- any local notes/todo files for voice, personality, and recurring phrasing
- local assets such as fonts or textures that can be legally/reasonably reused inside the same workspace

Capture the reference site in terms of:
- **palette**: shell/background colors, signal accent, secondary accent, text color
- **chrome**: terminal frames, faux-device borders, panel treatments, scanlines, glow, vignette
- **typography**: fonts, casing habits, density, whether it feels retro/system/editorial
- **voice**: smug, sincere, playful, dry, corporate, mystical, etc.
- **interaction tone**: are prompts, logs, and labels written like UI copy or in-world fiction?

Then transfer those cues into the prototype deliberately:
- reuse or copy local font assets when appropriate
- rename labels and headings to match the reference voice
- tune prompt prefixes, log lines, and status text so the page *sounds* like the sibling project
- keep the new site’s own concept intact instead of turning it into a clone

A good result should feel like:
- same creator / same universe of taste
- different artifact / different purpose

### Step 4c. After a branding-transfer pass, do a render-cost sanity check
A reusable lesson from sibling-style transfers: a page can feel “hard to load” even when HTML/CSS/JS files are not large. The real problem is often **render cost**, not payload size.

Common culprits in static mockups:
- multiple `backdrop-filter` layers in the same viewport
- stacked `filter: blur(...)` and `filter: drop-shadow(...)`
- inline SVG noise/turbulence textures
- many overlapping scanline/glass/chrome overlays
- animated shadows or glows on large elements
- too many pseudo-elements doing similar atmospheric work

Useful workflow:
1. verify actual file sizes first so you do not misdiagnose payload as the issue
2. search CSS for expensive effects such as:
   - `backdrop-filter`
   - `filter: blur`
   - `filter: drop-shadow`
   - `mix-blend-mode`
   - `feTurbulence`
   - dense `repeating-linear-gradient` scanline stacks
3. identify which of those are layered together in the hero viewport or focal component
4. trim the most redundant layers first while preserving the visual language
   - remove turbulence/noise before removing core palette/chrome
   - reduce duplicated scanline layers
   - remove blur from decorative pseudo-elements before touching structure
   - remove `backdrop-filter` from secondary glass surfaces before touching the main shell
   - simplify shadows on animated lines/nodes/cards
5. re-capture a screenshot and compare whether the page still keeps the borrowed brand language

A good reduction pass preserves:
- palette
- border/chrome treatment
- signal accent colors
- typography roles

while reducing:
- overdraw
- compositing cost
- visual heaviness

If vision analysis times out on a full-page screenshot, crop the hero/bubblemap area and retry on the smaller image rather than skipping visual QA.

### Step 4d. When the vision is finally clear, do a ruthless subtraction pass on the homepage path
A recurring prototype trap: while searching for the vibe, it is easy to accumulate layers that were useful as experiments but no longer serve the final concept. Once the user clearly confirms the direction (for example, "bubblemap-first home with an in-map reading state"), stop polishing additive effects and remove anything that does not strengthen that one idea.

Good subtraction targets for a homepage hero/map:
- scroll-driven parallax JS (`requestAnimationFrame`, `scroll` handlers updating CSS vars)
- perpetual ambient motion on multiple elements at once
  - floating nodes
  - pulsing connector lines
  - breathing inner shells
- duplicated pseudo-element chrome (`::before`/`::after`) doing similar work
- decorative scanlines/noise on both the shell and the inner card at the same time
- bloom auras with several overlapping glow rings when one restrained halo would do
- highlight cards/chips whose gradients and shadows are louder than the content itself
- sibling-project branding layers that were useful references but now overpower the actual structure

Useful rule:
- keep **one** clear structural idea
- keep **one** restrained material language
- keep at most **one** ambient motion system on the homepage, and preferably none until the layout already feels right

Practical order of operations that worked:
1. remove scroll/parallax logic from JS first
2. remove infinite animation from connector lines and node shells
3. remove infinite node float unless motion is clearly essential
4. flatten the viewport shell and bloom card backgrounds before touching typography
5. simplify node internals and micro-label chrome last
6. re-check whether the page now reads more like a place and less like a demo scene

### Step 4e. During verification, search the active files first — backups can produce false positives
Prototype directories often accumulate `.bak-*` files and backup folders during iteration. If you grep/search broadly for things like `requestAnimationFrame`, `node-float`, or `network-pulse`, you may accidentally conclude the feature is still live when the only remaining matches are inside backups.

Safer verification pattern:
1. search the active file directly first (for example `css/styles.css` or `js/script.js`)
2. only search the whole project when you intentionally want historical context
3. if a broad search returns matches, inspect the paths before assuming the current build still uses them

This matters especially after reduction passes, where the goal is often to prove that a noisy behavior is gone from the live homepage even though backups still preserve earlier experiments.

### 5. Keep interactions lightweight
Use CSS transitions and small JS hooks for:
- hover flicker
- class toggles
- quote/status swaps
- simple reactions
- keyboard/click cycling states

Avoid premature framework adoption.

### 5a. For bilingual or multilingual mockups, use a data-attribute translation map
A strong static-site pattern for language toggles is:
- mark translatable text with `data-i18n` keys
- keep one `translations` object in JS keyed by language (`en`, `fr`, etc.)
- swap text content/HTML in place without restructuring the page
- update `document.documentElement.lang` and `document.title`
- persist the current language in `localStorage`
- keep the nav and layout identical across languages so the toggle feels stable

This works well for concept sites because it preserves the same visual hierarchy while letting the page speak in the user’s preferred language.

### 5b. Prefer purposeful interaction over ambient randomness
If the mockup starts feeling like it is "madly running loops" or cycling state just to look alive, slow it down or remove the automatic loops.

### 5c. For identity-first community homepages, keep the front door calm and local
When the site is meant to represent a community, culture, or lineage rather than a generic product, make the homepage a *hub* instead of a databank.

Good pattern:
- one short greeting or banner as the first impression
- the creator/author credited in the footer
- secondary topics turned into small expandable cards, bubbles, or teaser links
- deeper history, archives, and community material split into their own pages
- motion kept subtle and preferably tied to scroll or hover, with `prefers-reduced-motion` honored
- if the site is bilingual or multilingual, keep the culturally primary language as the default and make the other language the toggle

A practical visual recipe that worked well:
- blue-forward top banner or header
- warm red motion/gradient background
- black-and-gold primary buttons or calls to action
- small floating bubble-like sections for optional content

This is useful when the user wants the homepage to feel welcoming and self-contained, not encyclopedic.

### 5d. For memorable community hubs, a neural page map can outperform a plain card grid
If the user wants the homepage to feel more like a living map of the site than a traditional menu, use a **neural page map** instead of a static list.

Good pattern:
- make each core page or future post category a floating **one-word node**
- keep one central anchor node that reads as the site's home or pulse
- let nearby nodes imply relationships through spacing, lines, or gentle motion
- reserve richer copy for a detail panel that appears only after selection or zoom
- fade the node label into more complete data rather than dumping the full text immediately
- treat future posts or planned sections as lighter-weight "ghost nodes" so the homepage can hint at growth without becoming crowded
- keep the interaction calm: zoom, soften, reveal; do not make the page feel like a chaotic particle simulator

This is especially effective when the site needs to feel:
- creative rather than template-like
- human and eye-retentive
- like a conceptual map of a community or archive
- strong enough to imply depth without showing all the depth at once

Implementation notes that proved useful:
- pair the node map with a compact language toggle so the interaction model stays stable across languages
- keep `prefers-reduced-motion` as a first-class path, not an afterthought
- avoid putting historic databank content on the homepage; the map should point to it, not replace it
- if the user names a creator/author, keep that attribution in the footer or a subtle credit line, not in the main interactive cluster

A neural page map works best when the homepage answers two questions quickly:
1. what is this place?
2. what can I explore next?

The selected node should expand into richer text, but the unselected state should remain airy, elegant, and navigable.

### 5d.1. For Acadian-first community sites, make the map the front door and keep the author subtle
A pattern that worked well for an Acadian/community-oriented site:
- make the homepage essentially a dedicated neural map, not a generic landing page
- center the page on a greeting node like "Bonjour" with a short intro and a tiny demo stack
- keep only a few satellite nodes visible at once, such as About us and Historic, so the page stays calm
- make bubble clicks pan/zoom into the node rather than refreshing a side detail card
- use the map to hint at deeper pages instead of dumping archive/history content on the homepage
- preserve the creator/author credit in a subtle footer or credit line, for example `acadie.sol`, rather than inside the main cluster
- keep the visual mood restrained: blue header/top band, red motion background, and black-and-gold action buttons can coexist without crowding the center
- keep the language toggle stable so the same interaction model works in both languages without rearranging the layout
- if the first pass still feels noisy, reduce the number of visible nodes before adding more motion or chrome

This is especially useful when the user wants the site to feel like a living community hub rather than a catalog or databank.

### 5e. When the first pass is cool but the vibe is off, pivot to a calmer orbit instead of forcing the complex idea
Sometimes the user will like the direction in principle but still say they are "not vibing" with the result. Treat that as a signal to simplify the interaction model, not to keep polishing the same concept.

Useful reset pattern:
- keep the original backup
- preserve the core identity and color language
- replace the flashy map with one centered, welcoming anchor plus a small number of satellite bubbles
- make the center bubble the main entry point and let the satellites point to mission/history/about content
- give the center bubble enough breathing room to hold a short intro and a tiny demo content stack
- make the side bubbles clearly secondary so the page feels calmer and easier to scan
- keep the shift lightweight with HTML/CSS/JS unless the user specifically needs depth, physics, or camera-driven composition

When to consider three.js:
- only after the static/CSS prototype has failed to achieve the feeling
- when the user explicitly wants spatial depth, camera movement, or 3D orbit behavior
- when the effect depends on actual perspective rather than just layered circles and motion

In most early concept passes, a strong CSS/JS orbit is enough to test the mood. Three.js should be a later-stage upgrade, not the default response to a style mismatch.

Good default hierarchy:
- subtle hover/reactive polish can stay ambient
- core character/state changes should usually be triggered by a user action, prompt, or clearly legible system event
- if the project centers on one featured character, place the main prompt/composer near that character rather than burying it on a secondary page

A useful pattern for early concept sites:
- homepage = one featured character card + one nearby prompt input
- support pages = logs, world state, secondary actors, experiments
- slow auto-rotation intervals way down unless they communicate something meaningful

When the interaction is character-driven, make the prompt area feel diegetic instead of like a generic form. A strong reusable pattern is:
- a small in-world terminal/header label
- an "active objective" field showing the current purpose
- a "last accepted prompt" field so the state feels persistent
- a short recent-history list on the homepage (for example, the last 5 moves / prompts / turns) so the creature feels active even before the user clicks anything
- a deliberately tiny prompt bar when the fiction benefits from terse input (for example, a cute 30-character inbox)
- a submit label that sounds like world interaction (for example, "Transmit directive" or "Send to inbox") rather than bland UI language

This helps the page feel like the user is guiding a creature or agent, not filling out a dashboard widget.

For playful pet/character sites, prefer **authored silly mechanics** over generic status churn. Reusable examples:
- the pet leaves the screen, answers from the edge, then returns anyway
- the pet briefly refuses a command in-character before complying
- a submitted prompt is immediately reframed as one of the creature's own logged decisions

These tiny bits usually create more charm than adding more random ambient loops.

### 5d.2. If the user wants a true bubblemap homepage, make the map dominate and move expanded content below
A reusable correction from iteration work: if the user says the current neural/homepage mockup still feels like cards, tiles, or a side-detail UI, the problem is often **layout hierarchy**, not just styling.

Useful pivot:
- let the bubble map occupy roughly the top 70–75% of the homepage
- make the bubbles themselves the primary interface, not just triggers for a nearby card
- keep only a small set of linked nodes visible at once so the map reads as intentional, not crowded
- when a node is selected, pan/zoom the map scene toward that node so it feels like entering that page
- render the richer detail block **below** the map instead of in a side panel when the user wants the map to remain the dominant first impression
- phrase the interaction internally as "the camera enters the node" rather than "show detail for the node"; this leads to better HTML/CSS/JS choices
- if the first pass still feels too card-like, remove thumbnail grids entirely before adding more effects

Implementation notes that worked:
- keep a separate map scene wrapper and drive panning/scale with CSS custom properties like `--map-pan-x`, `--map-pan-y`, and `--map-scale`
- make the selected node update both map-state classes and the lower detail area from one JS state function
- use linked circular nodes with restrained motion instead of many mixed card shapes
- keep the footer credit subtle and outside the map cluster

### Step 5d.2b. If a below-the-map detail panel still breaks the illusion, convert the selected node into an in-map bloom
A reusable follow-up from bubblemap iteration: sometimes moving expanded content **below** the map fixes hierarchy, but the page can still feel split into two modes — "map up top, reading area down below." If the user says the node should feel more like it is *opening*, *blooming*, or *unfolding from the map itself*, keep the map dominant and move the expansion back **into the map viewport**.

Useful pattern:
- keep the bubble map as the main first impression
- remove the separate bottom reading panel
- when a node is active, give it a visible aura/glow/bloom state
- attach a floating reading card to the active node inside the map scene rather than outside it
- anchor the bloom card with per-node positioning vars or node-specific classes so it feels physically tied to the selected node
- dim inactive nodes slightly more so the active node clearly owns the scene
- keep the copy and JS state phrased as the node "opens" or "blooms" instead of "showing details below"

Implementation notes that worked:
- place the expanded-card container inside the map viewport (`.network-bloom`, `.network-focus`, etc.) instead of in a separate page section
- drive bloom placement with CSS custom properties or per-node classes so each node can shift the attached card/aura cleanly
- reuse the same JS state/update function for title/body/bullets/link, but update selectors and microcopy to match the in-map bloom behavior
- verify contrast after the move; floating cards inside animated backgrounds often need darker shells or stronger text contrast than a separate lower panel did

This pattern is useful when the user likes the bubblemap concept but still feels the current build reads like a card UI instead of a living map.

### Step 5d.2c. For calmer bubblemap homes, keep the detail card hidden by default and let selection explicitly open it
A recurring usability issue with map-first homepages: if one node boots as active, the bloom/detail card can feel like permanent clutter and make the map seem less explorable. When the user wants to *navigate the nodes first* and read only on demand, treat the map's resting state as a true neutral state.

Useful pattern:
- start with **no active node** on initial load
- keep the bloom/detail container present in the DOM but visually hidden by default (for example with an `.is-hidden` class)
- reveal the bloom card only after a node click or keyboard selection
- provide an explicit close affordance (`×`) on the card
- support `Escape` to dismiss the card and return to map navigation mode
- on close, clear the active node state and reset the map pan/zoom to its neutral overview

Implementation notes that worked:
- avoid hard-coding a default active node like `bonjour`; use `null` for the initial state when the map should open airy/calm
- if language/application code reruns the node update function, guard it so it does not accidentally reopen the card when no node is selected
- keep the close button inside the bloom card and query it once in JS (`[data-network-close]` style hook works well)
- toggle the same hidden/open state on the shared bloom wrapper so aura, rings, and card all disappear together
- if one node is consistently harder to see in the neutral state, improve **that node's idle visibility** directly (position, contrast, badge strength, or size) instead of reintroducing global ambient effects

Verification pattern that proved useful when browser automation was flaky:
1. confirm the initial DOM state shows bloom hidden and no `.is-active` node
2. use a tiny same-origin iframe driver page to click a node and then the close button
3. dump the driven DOM and assert a sequence like:
   - `initialHidden: true`
   - `initialActive: null`
   - `afterClickHidden: false`
   - `afterClickActive: "community"`
   - `afterCloseHidden: true`
   - `afterCloseActive: null`

This preserves the bubblemap as the homepage's real first impression while still allowing the selected node to bloom into readable detail on demand.

### Step 5d.3. If the structure is right but the page still feels robotic, do a visual-language pass before asking for more content
A common late-prototype problem: the homepage concept is now correct, but the user still says it feels "basic," "robotic," or not yet organic enough. Often this is **not** a structural failure and **not** a sign to add more placeholder data immediately.

Useful move:
- treat the next pass as a **visual-language / material pass** rather than a content pass
- keep the information architecture stable while improving shape language, typography roles, connector softness, and panel depth
- explicitly separate "we need richer real data later" from "the current interface still needs better taste"

Reusable pattern that worked well:
- replace perfect circular nodes with slightly asymmetrical blob/squircle radii
- give each key node a tiny rotation bias and non-identical motion timing
- soften connector lines so they read as threads/constellations instead of dashboard wires
- deepen the expanded node panel with inner frames, layered gradients, and one restrained status label instead of generic glass-card styling
- use a **three-tier type system**:
  - clean body/UI font for readability
  - one display/rune-like font for hero and major panel headings
  - one tiny retro/game accent font only for chips/meta/status text
- keep novelty fonts constrained to maybe 10–15% of visible text; do not turn the whole site into a themed-font collage

When the user suggests two strong font vibes at once (for example a Norse-feeling heading and a Pokémon/game-like accent), separate the roles instead of blending them everywhere:
- mythic/display font = hero title + major expanded-node headings
- retro/game font = tiny metadata, chips, pulse labels, status strips
- body and paragraphs = modern readable sans

This works especially well when the user says they will add better datasets later. In that case, optimize for **convincing atmosphere now** and leave room for richer content later.

### Step 6: Verify without overcomplicating preview
If browser automation is unavailable, still verify the site with lightweight checks:

- syntax check JS (`node --check`)
- local static server (`python3 -m http.server`)
- HTTP checks (`curl -I` or simple fetch scripts)
- targeted file reads to verify structure and nav links
- if available, use headless Chrome/Chromium to capture a screenshot of the current pass for visual proof

If the environment kills long-lived preview servers, treat that as an environment constraint, not necessarily a site bug.
If the primary browser bridge is down but headless Chrome works, save the screenshot path in the project log or review notes so the latest visual state is still documented.
If image-analysis tooling fails on large screenshots, generate a smaller derivative (for example via `convert`) and retry visual QA on the reduced image rather than skipping the check.

### Step 7: Update the review ledger
Record:
- what was simplified
- what pages were split out
- what prototype was created
- what is still pending approval
- whether the next step is template expansion or more refinement

### Step 8: Report in decision-ready language
End with a concise summary that helps the user approve or redirect.

Useful framing:
- what changed
- why this is cleaner
- whether the current prototype is the candidate template
- whether React is actually needed yet
- what the next smallest good step is

## Practical Heuristics

### If the page feels like "everything everywhere"
Split by intent:
- homepage = featured object
- ledger/log = user actions/history
- village/world = multi-entity scene
- about/lore = flavor and context

### If the user says "clunky and hard to focus"
This usually means **too many competing visual layers**, not missing content. Apply reduction in this order:

1. **Simplify the color palette** - reduce from 3+ accent colors to 1 neon accent + dark shell base
2. **Strip gradient layers** - go from 3-4 background gradients to 1-2 subtle ones
3. **Amplify the focal point** - increase contrast on the main subject; mute surrounding chrome
4. **Minimal terminal chrome** - remove decorative borders, glows, scanlines that compete with content

The goal is a clear visual hierarchy where the eye lands on the intended subject immediately.

### If the user wants 5 variants
Make 1 first.
If approved, convert into a reusable pattern for the rest.

### If the user says “this still isn’t the vision”
Treat that as a signal to do a **reset pass**, not to keep polishing the same interaction model.

Recommended move:
1. snapshot the current state into a clearly named backup directory (for example `v0.0.02/`)
2. keep the world premise and tone
3. throw away the over-clever homepage mechanics
4. rebuild the homepage around **one single cat page**
5. keep only the smallest interaction that proves the concept (for example: one cat card, one short inbox, one last-5 move list)

A good reset-pass question is not “how do we make this prototype smarter?” but “what is the smallest page that actually feels like the intended thing?”

For playful character/IP sites, that often means replacing a systems-demo homepage with:
- one featured cat/character
- one readable room/card/screen
- one visible recent-moves list
- one tiny prompt input
- one stable personality voice

This is especially useful when the current build is technically neat but emotionally off-target.

### If the user mentions React
Treat it as exploratory, not as approval to migrate the stack.
Default answer for early prototypes:
- CSS/JS can handle hover flicker and small reactions for now
- React can wait until state/data repetition justifies it

### If visual preview tooling fails
Fallback to structural verification plus local server checks and tell the user visual browser validation is incomplete, not impossible.

## Verification Checklist

Before finalizing:
- [ ] README/review docs were checked
- [ ] a backup exists before major reduction
- [ ] homepage has one clear primary focus
- [ ] secondary content moved to dedicated pages where appropriate
- [ ] JS passes syntax check
- [ ] local page routes return 200 OK
- [ ] review ledger updated
- [ ] summary clearly states whether the prototype is ready for approval or template expansion

## Pitfalls

### Pitfall: polishing noise instead of removing it
Do not keep layering style on top of a crowded structure. Reduce first.

### Pitfall: scaling an unapproved component
Do not clone four more cards before the first card is clearly the right pattern.

### Pitfall: unnecessary framework migration
Do not switch to React just to animate hover flicker or rotate a few text states.

### Pitfall: forgetting the review file
If the project uses a review ledger, keep it current or it stops being useful as the working truth.

### Pitfall: overwriting a shared review ledger blindly
If a tool warns that a sibling subagent or parallel worker modified `REVIEW_TODO.md` (or any shared working file), re-read that file before writing again. Treat the warning as real until verified. This avoids accidentally clobbering the latest source-of-truth notes.

## Output Pattern

A strong final update usually includes:
- the page split that was made
- the single prototype component now anchoring the homepage
- the verification performed
- a recommendation that React is deferred unless the interaction model grows
- the smallest sensible next step: refine prototype or template it

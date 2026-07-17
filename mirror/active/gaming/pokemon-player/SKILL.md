---
name: pokemon-player
description: Play Pokemon games autonomously via headless emulation. Starts a game server, reads structured game state from RAM, makes strategic decisions, and sends button inputs — all from the terminal.
tags: [gaming, pokemon, emulator, pyboy, gameplay, gameboy]
---
# Pokemon Player

Play Pokemon games via headless emulation using the `pokemon-agent` package.

## When to Use
- User says "play pokemon", "start pokemon", "pokemon game"
- User asks about Pokemon Red, Blue, Yellow, FireRed, etc.
- User wants to watch an AI play Pokemon
- User references a ROM file (.gb, .gbc, .gba)

## Startup Procedure

### 1. First-time setup (clone, venv, install)
The repo is NousResearch/pokemon-agent on GitHub. Clone it, then
set up a Python 3.10+ virtual environment. Use uv (preferred for speed)
to create the venv and install the package in editable mode with the
pyboy extra. If uv is not available, fall back to python3 -m venv + pip.

You also need a ROM file. Ask the user for theirs. On this machine
On this machine the user-provided ROM path is `~/.hermes/games/roms/GB/pkmn/pkmn_red.gb`. Reuse that path when starting the server instead of asking again if the user has already supplied it.
NEVER download or provide ROM files — always ask the user.

### Installation Notes
If the repository already exists, reuse it instead of cloning again.
If a `.venv` already exists and `uv venv .venv` fails, skip recreating it
and install into the existing interpreter directly:
`uv pip install --python .venv/bin/python -e '.[pyboy,dashboard]'`
from within the cloned repository directory.
If the virtual environment's pip is not working (as can happen with freshly
created venvs), use uv directly to install:
`uv pip install -e .[pyboy]` from within the cloned repository directory.

### 2. Start the game server
From inside the pokemon-agent directory with the venv activated, run
pokemon-agent serve with --rom pointing to the ROM and --port 9876.
Run it in the background with &.
To resume from a saved game, add --load-state with the save name.
Wait 4 seconds for startup, then verify with GET /health.

### 3. Set up live dashboard for user to watch
First check whether the dashboard is already reachable locally at
http://127.0.0.1:9876/dashboard/. If the user is working on the same
machine/session, this local URL is often the simplest live view and may
work immediately without any tunnel.

If an external browser-accessible URL is needed, use an SSH reverse
tunnel via localhost.run so the user can view the dashboard in their
browser. Connect with ssh, forwarding local port 9876 to remote port 80
on nokey@localhost.run. Redirect output to a log file, wait 10 seconds,
then grep the log for the .lhr.life URL. Give the user the URL with
/dashboard/ appended.
The tunnel URL changes each time — give the user the new one if restarted.

Important field note: localhost.run can be flaky or fail to expose a
usable tunnel even when the local dashboard is fine. If that happens,
don't block the workflow — tell the user the local dashboard URL works
and point them to http://127.0.0.1:9876/dashboard/ instead.

## Save and Load

### When to save
- Every 15-20 turns of gameplay
- ALWAYS before gym battles, rival encounters, or risky fights
- Before entering a new town or dungeon
- Before any action you are unsure about

### How to save
POST /save with a descriptive name. Good examples:
before_brock, route1_start, mt_moon_entrance, got_cut

### How to load
POST /load with the save name.

### List available saves
GET /saves returns all saved states.

### Loading on server startup
Use --load-state flag when starting the server to auto-load a save.
This is faster than loading via the API after startup.

## The Gameplay Loop

### Step 1: OBSERVE — check state AND take a screenshot
GET /state for position, HP, battle, dialog.
GET /screenshot and save to /tmp/pokemon.png, then use vision_analyze.
Always do BOTH — RAM state gives numbers, vision gives spatial awareness.

### Step 2: ORIENT
- Dialog/text on screen → advance it
- In battle → fight or run
- Party hurt → head to Pokemon Center
- Near objective → navigate carefully

### Step 3: DECIDE
Priority: dialog > battle > heal > story objective > training > explore

### Step 4: ACT — move 2-4 steps max, then re-check
POST /action with a SHORT action list (2-4 actions, not 10-15).

### Step 5: VERIFY — screenshot after every move sequence
Take a screenshot and use vision_analyze to confirm you moved where
intended. This is the MOST IMPORTANT step. Without vision you WILL get lost.

### Step 6: RECORD progress to memory with PKM: prefix
Use the format: PKM:[TYPE]: [description] where TYPE can be OBJECTIVE, MAP, STRATEGY, PROGRESS, STUCK, or TEAM.

### Step 7: SAVE periodically

## Action Reference
- press_a — confirm, talk, select
- press_b — cancel, close menu
- press_start — open game menu
- walk_up/down/left/right — move one tile
- hold_b_N — hold B for N frames (use for speeding through text)
- wait_60 — wait about 1 second (60 frames)
- a_until_dialog_end — press A repeatedly until dialog clears

## Critical Tips from Experience

### USE VISION CONSTANTLY
- Take a screenshot every 2-4 movement steps
- The RAM state tells you position and HP but NOT what is around you
- Ledges, fences, signs, building doors, NPCs — only visible via screenshot
- Ask the vision model specific questions: "what is one tile north of me?"
- When stuck, always screenshot before trying random directions

### Warp Transitions Need Extra Wait Time
When walking through a door or stairs, the screen fades to black during
the map transition. You MUST wait for it to complete. Add 2-3 wait_60
actions after any door/stair warp. Without waiting, the position reads
as stale and you will think you are still in the old map.

### Building Exit Trap
When you exit a building, you appear directly IN FRONT of the door.
If you walk north, you go right back inside. ALWAYS sidestep first
by walking left or right 2 tiles, then proceed in your intended direction.

Example: in Pallet Town after leaving Red's House, do not immediately
walk north toward the house. Keep moving south until you reach the
fence/flower line outside so you don’t re-enter the doorway.

### Dialog Handling
Gen 1 text scrolls slowly letter-by-letter. To speed through dialog,
press B repeatedly rather than relying on a long hold in stubborn cases,
then press A to advance to the next line. Holding B can make text display
at max speed, but in this setup repeated B taps were more reliable for
dismissing/advancing dialogue. The a_until_dialog_end action checks the
RAM dialog flag, but this flag does not catch ALL text states. If dialog
seems stuck, use the manual tap-B + press-A pattern instead and verify
via screenshot.

Important field note: after advancing text or moving between tiles,
give the screen a moment to settle before trusting the next screenshot.
A stale frame can make an adjacent NPC look misaligned or make it seem
like dialogue has ended when it has not.

For NPC conversations, the player must be on an adjacent tile and
facing the NPC before pressing A. If A does nothing, assume the facing
or tile alignment is wrong and re-check with a screenshot instead of
spamming more A presses.

### Talking to NPCs
To initiate dialogue, the player must be **adjacent to the NPC and facing them directly** before pressing A. If A does nothing, adjust position/facing first; diagonal alignment usually won't trigger conversation.

### Collaborative play
When the user is helping by calling out map positions or preferred
strategy, prefer their explicit guidance over a vision guess. In cramped
interiors, it can be useful to probe against walls/edges to learn the
collision layout, then ask for guidance again after a few turns instead
of wasting many single-tile retries.

### Ledges Are One-Way
facing the NPC before pressing A. If A does nothing, assume the facing
or tile alignment is wrong and re-check with a screenshot instead of
spamming more A presses.

### Talking to NPCs
To initiate dialogue, the player must be **adjacent to the NPC and facing them directly** before pressing A. If A does nothing, adjust position/facing first; diagonal alignment usually won't trigger conversation.

### Ledges Are One-Way
Ledges (small cliff edges) can only be jumped DOWN (south), never climbed
UP (north). If blocked by a ledge going north, you must go left or right
to find the gap around it. Use vision to identify which direction the
gap is. Ask the vision model explicitly.

### Navigation Strategy
- Move 2-4 steps at a time, then screenshot to check position
- When entering a new area, screenshot immediately to orient
- Ask the vision model "which direction to [destination]?"
- If the room is tight or furniture-heavy, prefer exact coordinate reasoning and fewer blind moves over repeated 1-step probes
- In collaborative play, consider asking the user for guidance every ~3 turns when the layout is ambiguous
- Do not spam 10-15 movements — you will overshoot or get stuck

### Running from Wild Battles
On the battle menu, RUN is bottom-right. To reach it from the default
cursor position (FIGHT, top-left): press down then right to move cursor
to RUN, then press A. Wrap with hold_b to speed through text/animations.

### Battling (FIGHT)
On the battle menu FIGHT is top-left (default cursor position).
Press A to enter move selection, A again to use the first move.
Then hold B to speed through attack animations and text.

## Battle Strategy

### Decision Tree
1. Want to catch? → Weaken then throw Poke Ball
2. Wild you don't need? → RUN
3. Type advantage? → Use super-effective move
4. No advantage? → Use strongest STAB move
5. Low HP? → Switch or use Potion

### Gen 1 Type Chart (key matchups)
- Water beats Fire, Ground, Rock
- Fire beats Grass, Bug, Ice
- Grass beats Water, Ground, Rock
- Electric beats Water, Flying
- Ground beats Fire, Electric, Rock, Poison
- Psychic beats Fighting, Poison (dominant in Gen 1!)

### Gen 1 Quirks
- Special stat = both offense AND defense for special moves
- Psychic type is overpowered (Ghost moves bugged)
- Critical hits based on Speed stat
- Wrap/Bind prevent opponent from acting
- Focus Energy bug: REDUCES crit rate instead of raising it

## Memory Conventions
| Prefix | Purpose | Example |
|--------|---------|---------|
| PKM:OBJECTIVE | Current goal | Get Parcel from Viridian Mart |
| PKM:MAP | Navigation knowledge | Viridian: mart is northeast |
| PKM:STRATEGY | Battle/team plans | Need Grass type before Misty |
| PKM:PROGRESS | Milestone tracker | Beat rival, heading to Viridian |
| PKM:STUCK | Stuck situations | Ledge at y=28 go right to bypass |
| PKM:TEAM | Team notes | Squirtle Lv6, Tackle + Tail Whip |

## Progression Milestones
- Choose starter
- Deliver Parcel from Viridian Mart, receive Pokedex
- Boulder Badge — Brock (Rock) → use Water/Grass
- Cascade Badge — Misty (Water) → use Grass/Electric
- Thunder Badge — Lt. Surge (Electric) → use Ground
- Rainbow Badge — Erika (Grass) → use Fire/Ice/Flying
- Soul Badge — Koga (Poison) → use Ground/Psychic
- Marsh Badge — Sabrina (Psychic) → hardest gym
- Volcano Badge — Blaine (Fire) → use Water/Ground
- Earth Badge — Giovanni (Ground) → use Water/Grass/Ice
- Elite Four → Champion!

## Stopping Play
1. Save the game with a descriptive name via POST /save
2. Update memory with PKM:PROGRESS
3. Tell user: "Game saved as [name]! Say 'play pokemon' to resume."
4. Kill the server and tunnel background processes

## Pitfalls
- NEVER download or provide ROM files
- Do NOT send more than 4-5 actions without checking vision
- Always sidestep after exiting buildings before going north
- Always add wait_60 x2-3 after door/stair warps
- Dialog detection via RAM is unreliable — verify with screenshots
- In the Oak's Lab starter scene, the visually centered Poké Ball may still not be interactable until the player is on the exact adjacent tile and facing it; if A does nothing, reposition one tile and re-check with a screenshot before retrying.
- In Pokémon Red/Blue, Pikachu is not a starter option in the lab. The valid starter choice is Bulbasaur/Charmander/Squirtle, so do not keep trying to obtain Pikachu from that scene.
- Save BEFORE risky encounters
- The tunnel URL changes each time you restart it

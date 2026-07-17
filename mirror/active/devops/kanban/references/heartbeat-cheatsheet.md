# Heartbeat / Kanban status cheatsheet

Use this as a compact user-facing explanation of Hermes Kanban status updates.

## Core distinctions

- **Kanban board**: the persistent task tracker.
- **Card/task**: one piece of work on the board.
- **Heartbeat**: a periodic progress ping while a task is running.
- **Blocked**: the task cannot proceed without input or a decision.
- **Complete**: the task is finished and terminal.

## Heartbeat rules

Good heartbeats name measurable progress:
- `scanned 1.2M/2.4M rows`
- `epoch 12/50, loss 0.31`
- `imported 14/52 files`

Bad heartbeats:
- `still working`
- empty updates
- spammy sub-minute pings

## User-friendly explanation pattern

When the user asks what heartbeat means, explain it as:

> A heartbeat is a progress ping for a long-running Kanban task. It says the worker is alive and making progress, but it is not the same thing as finishing the task.

When the user asks about the board, explain it as:

> The Kanban board is the persistent task list; heartbeats are the running status updates that keep a card from looking stalled.

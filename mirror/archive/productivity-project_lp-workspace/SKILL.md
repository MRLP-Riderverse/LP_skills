---
name: project_lp-workspace
description: Build a lightweight personal business workspace for leads, jobs, services, metrics, and prompts using a simple folder-first structure before moving to a database or web UI.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [business, workspace, leads, crm, folder-system, metrics, prompts, lightweight]
---

# Project_LP Workspace

Use this skill when the user wants to organize a personal business / client pipeline without overbuilding a database or full app too early.

## Core idea

Start with a **folder-first operating system**:
- capture incoming leads and ideas
- separate active work from completed work
- split local services from digital/global offers
- keep simple metrics
- add reusable prompts and templates
- only move to a database or web UI after the manual workflow proves useful

## When to use

Use this skill when the user asks to:
- set up a new business workspace
- organize clients, leads, or side-income experiments
- create a lightweight CRM-like system
- build a folder structure for offers and jobs
- design a simple workflow to reduce stagnation and support action

## Recommended structure

Create a root folder such as `Project_LP/` with these subfolders:

- `inbox/` — raw leads, ideas, reminders, half-formed thoughts
- `in_progress/` — active jobs, active experiments, follow-ups
- `completed/` — finished jobs, outcomes, proof of work
- `local/` — local/in-person or nearby services
- `services/` — one-off paid help, troubleshooting, setup, consulting
- `digital_global/` — remote, scalable, online-only offers
- `metrics/` — revenue, lead counts, conversions, lessons
- `templates/` — outreach, pricing, intake, follow-up, checklists
- `prompts/` — daily prompts and anti-stagnation questions

## Minimal files to create

### `README.md`
Describe:
- the purpose of the workspace
- what belongs in each folder
- the status flow: inbox → in_progress → completed
- the principle: keep it lightweight, upgrade later only if needed

### `prompts/README.md`
Include:
- daily thinking prompts
- business reflection prompts
- anti-stagnation rules
- questions that help the user turn ideas into action

### `metrics/README.md`
Track only the essentials:
- leads contacted
- replies received
- calls booked
- jobs completed
- revenue earned
- average job value
- best source of clients
- what worked / what didn’t

## Workflow

1. **Capture fast**
   - Put new ideas and incoming requests into `inbox/`

2. **Classify quickly**
   - Move items into `local/`, `services/`, or `digital_global/`

3. **Act**
   - Move active work into `in_progress/`

4. **Close the loop**
   - Move finished work into `completed/`
   - Record outcomes and lessons in `metrics/`

5. **Reuse**
   - Save repeated messages, checklists, and offer text into `templates/`

6. **Prompt action**
   - Use daily prompts to reduce stagnation and keep momentum

## Good default prompts

- What is the smallest profitable action I can take today?
- What can I package into a simple offer?
- What did people ask me for help with most recently?
- What can I simplify, review, rank, or explain?
- What should move from idea to inbox, or inbox to in_progress?

## Design principles

### 1. Keep it manual first
Do not build a database or web UI until the user has repeatedly felt the pain of manual tracking.

### 2. Separate by usefulness, not theory
If the user naturally thinks in local vs service vs digital categories, preserve that split.

### 3. Prefer low-friction naming
Use short filenames and date prefixes when useful:
- `2026-04-17_clientname.md`
- `2026-04-17_idea_name.md`
- `2026-04-17_completed_job.md`

### 4. Track only useful metrics
Do not track vanity metrics or overcomplicate the system.

### 5. Make action easier than avoidance
The system should reduce stagnation by making the next step obvious.

## Common pitfalls

- Building a database before the offer is clear
- Tracking too many metrics
- Mixing active jobs with archived work
- Using folders that are too abstract to browse quickly
- Forgetting to include prompts that trigger action

## Verification

A good setup is complete when:
- the folder tree is created
- the user can quickly place a new idea into `inbox/`
- active jobs are easy to distinguish from completed ones
- the user can find templates and metrics without searching hard
- the structure feels lightweight enough to actually use

## Notes for Hermes

This workflow is meant to support a flexible, self-directed, nomadic-friendly income path. The best version is the one the user will actually maintain.

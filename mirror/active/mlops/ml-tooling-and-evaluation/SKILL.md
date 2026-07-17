---
name: ml-tooling-and-evaluation
description: "Work with model hubs, local inference, notebooks, and experiment tracking for ML/LLM development and evaluation."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [mlops, models, inference, evaluation, notebooks, tracking]
    related_skills: [research-paper-writing]
---

# ML Tooling and Evaluation

Class-level skill for the practical tooling around model discovery, local inference, experiment tracking, and notebook-style iteration.

Use this when you need to:
- find, download, or publish models and datasets
- run local GGUF inference or model experiments
- track runs, metrics, sweeps, and artifacts
- iterate interactively in a notebook-like environment

## Core workflow

1. Choose the right model or artifact source.
2. Verify local runtime constraints before pulling large assets.
3. Prefer reproducible scripts and configs over one-off manual steps.
4. Record metrics, outputs, and comparisons in a traceable system.

## Subsections

### Model discovery and asset handling

- Search hubs and repositories.
- Download, inspect, and upload model artifacts.
- Keep track of versions, tags, and dataset/model boundaries.

### Local inference

- Run local GGUF models when the task favors offline or consumer-hardware inference.
- Verify quantization, context length, and resource limits.
- Prefer the simplest runtime that satisfies the use case.

### Experiment tracking and evaluation

- Log runs, sweeps, and artifacts.
- Compare experiments with consistent metrics.
- Use structured evaluation for training, tuning, and inference changes.

### Interactive exploration

- Use notebook-style or live-kernel workflows for quick iteration.
- Keep exploratory code separate from the production path.

## Verification checklist

- Confirm the model or artifact actually exists and is usable.
- Re-check the inference or evaluation output after changes.
- Make sure logs, runs, or dashboards reflect the new experiment.

## Notes

This umbrella is the shared home for narrow ML tooling helpers that all serve model-centric experimentation and operational evaluation.
# Bioinformatics Intelligence Radar

A reusable ChatGPT Skill and deterministic evidence backend for source-grounded bioinformatics intelligence and concise Persian newsroom coverage.

## Protocol

**Radar 3.1.0** separates two responsibilities:

1. **Intelligence Engine** discovers, verifies, identifies, deduplicates and preserves evidence.
2. **Newsroom Engine** decides what deserves attention, chooses an evidence-safe angle and writes readable Persian news.

The new `scripts/` layer makes identity, evidence gates, state transitions and News Value scoring reproducible without replacing web discovery or editorial judgment.

## What it monitors

Radar can cover peer-reviewed literature, official software releases, databases, datasets, infrastructure and security events, benchmarks, corrections and retractions. Scholarly items require positively verified peer review. Preprints may support identity resolution only; they never appear in user-visible output as eligible papers.

## 3.1 capabilities

- JSON Schemas for Evidence Card, Story Card and run state;
- durable canonical identity and material event fingerprints;
- within-run deduplication and cross-run suppression;
- publication/release transition and correction classification;
- explainable six-dimension News Value scoring;
- CLI validation and processing;
- golden fixtures and regression tests;
- example configuration and operations guidance;
- compatible Persian newsroom and Telegram Handoff contracts.

## Quick start

```bash
python3 -m unittest discover -s tests -v
python3 -m scripts.radar_cli validate tests/fixtures/items.json
python3 -m scripts.radar_cli run tests/fixtures/items.json \
  --state-out /tmp/radar-state.json \
  --output /tmp/radar-run.json
python3 -m scripts.render_output /tmp/radar-run.json \
  --markdown /tmp/radar-report.md \
  --handoff /tmp/telegram-handoff.json
```

The CLI consumes normalized JSON items from a discovery adapter. It does not browse the web, infer peer review from a DOI, or invent claims. The Skill and reference policies remain the authority for source interpretation and Persian newsroom writing.

## Default newsroom output

The visible report is intentionally compact: **خبر اول**, **ارزش دنبال‌کردن**, an operational warning when needed, an evidence-backed signal when justified, editorial selections, Deep Dive questions, a short watchlist and observed-only telemetry. A quiet day is valid; there is no filler quota.

## Repository layout

- `SKILL.md` — control plane and release gates.
- `references/` — source, peer-review, evidence, newsroom, scoring, state and handoff policies.
- `scripts/radar_core.py` — deterministic identity, gating, deduplication, state and scoring.
- `scripts/radar_cli.py` — validation and processing CLI.
- `scripts/render_output.py` — Persian Markdown renderer and Telegram Handoff v1 builder.
- `schemas/` — machine-readable Evidence Card, Story Card and state contracts.
- `tests/` — regression tests and golden fixtures.
- `config/radar.example.json` — safe example configuration.
- `docs/` — architecture, operations and contribution guidance.

## Design principles

Primary sources come first. Event, publication, observed and effective dates remain distinct. Evidence is a gate, not a proxy for newsworthiness. Claims retain provenance and limitations. Headlines lead with the news, not the method. Association is not causation, prediction is not measurement, preclinical is not clinical, and author-reported benchmarks remain attributed.

See [MIGRATION-3.1.md](MIGRATION-3.1.md) for adoption steps and [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for extension points.

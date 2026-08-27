# Bioinformatics Intelligence Radar

A reusable ChatGPT Skill for daily bioinformatics news and technical-intelligence monitoring.

## Current protocol

Version: 2.3.0

The radar performs broad discovery before ranking. It covers papers, preprints, software releases, databases, infrastructure, datasets, reproducibility, benchmark claims, trend signals, and public-facing social candidates.

Version 2.3.0 adds an adaptive editorial tone engine. Radar now keeps one stable publication identity (`SCIENTIFIC_INTELLIGENCE`) while selecting different operational tones after evidence verification. Critical infrastructure changes are written as direct technical alerts, papers as evidence-aware spotlights, benchmark claims as critical evidence reviews, trend signals as scientific intelligence, and Social Candidates as curiosity-driven but evidence-safe bridges.

Evidence modifiers such as `PREPRINT_CAUTION`, `AUTHOR_REPORTED`, `CLINICAL_CAUTION`, `CAUSALITY_CAUTION`, and `HIGH_OVERHYPE_RISK` are preserved when an item is shortened, reframed, reused in Social Candidates, or transferred through Telegram Handoff v1.

The Radar still generates a structured Telegram Handoff v1 for orchestrated editorial workflows without requiring direct Skill-to-Skill calls. The orchestrator may load Telegram Editor instructions directly from GitHub.

## Install

Package the skill as `skill.zip` and import it into the ChatGPT Skills interface. The required entrypoint is `SKILL.md`.

## Typical prompts

- Run Bioinformatics Intelligence Radar for today.
- Run the radar for the last 7 days.
- Show only Critical Alerts and Tool & Software Radar.
- Find Social Candidates from today's bioinformatics radar.
- Deep-dive the top benchmark claim from today's radar.
- Run the radar and show me the editorial tone diagnostics for the top five items.

## Design principles

- Primary sources first.
- Exact reporting windows and dates.
- Preprints are never presented as peer-reviewed evidence.
- Broad discovery, then deduplication and ranking.
- Classify information and verify evidence before selecting tone.
- One stable Radar identity; adaptive operational tone by information type and evidence state.
- Tone may change framing, but never the strength of a scientific claim.
- No invented scan counts.
- Infrastructure changes outrank ordinary papers when they can break workflows.
- Social headlines must be attractive without overstating evidence.
- Evidence-risk modifiers survive summarization and downstream handoff.
- Radar reports are written in Persian by default, while technical names and identifiers remain in English when needed for precision.

## Layout

- `SKILL.md`: control plane and workflow.
- `references/source-policy.md`: source hierarchy and verification policy.
- `references/search-playbook.md`: discovery and deduplication process.
- `references/watchlists.md`: priority tools and data resources.
- `references/scoring.md`: technical, social, and reproducibility scoring.
- `references/editorial-tone-engine.md`: adaptive tone selection, evidence modifiers, arbitration rules, and final tone gate.
- `references/output-contract.md`: fixed Radar v2.3 report structure and section-level tone routing.
- `references/telegram-handoff.md`: machine-readable contract for Bioinformatics Telegram Editor, including inherited tone constraints.
- `references/orchestration.md`: orchestrator ownership, GitHub-direct Editor execution, and failure behavior.

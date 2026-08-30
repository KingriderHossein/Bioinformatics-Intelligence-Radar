# Bioinformatics Intelligence Radar

A reusable ChatGPT Skill for daily bioinformatics news and technical-intelligence monitoring.

## Current protocol

Version: 2.4.0

The radar performs broad discovery before ranking. It covers verified peer-reviewed scholarly literature, software releases, databases, infrastructure, datasets, reproducibility, benchmark claims, trend signals, and public-facing social candidates.

Version 2.4.0 makes the scholarly-literature stream **peer-reviewed-only**. Preprints, submitted manuscripts, working papers, conference abstracts, and papers with uncertain review status are excluded before scoring and cannot enter the Radar report, Signals, Social Candidates, Deep Dives, Watchlist, Benchmark Claims, or Telegram Handoff v1. Preprint services may be queried only for identity resolution or to find a later peer-reviewed publication.

This restriction applies to scholarly papers. Official software releases, database updates, datasets, infrastructure changes, security notices, and service changes remain eligible through their appropriate primary official sources.

Version 2.3.0 introduced the adaptive editorial tone engine. Radar keeps one stable publication identity (`SCIENTIFIC_INTELLIGENCE`) while selecting different operational tones after evidence verification. Critical infrastructure changes are written as direct technical alerts, papers as evidence-aware spotlights, benchmark claims as critical evidence reviews, trend signals as scientific intelligence, and Social Candidates as curiosity-driven but evidence-safe bridges.

Evidence modifiers such as `AUTHOR_REPORTED`, `CLINICAL_CAUTION`, `CAUSALITY_CAUTION`, and `HIGH_OVERHYPE_RISK` are preserved when an item is shortened, reframed, reused in Social Candidates, or transferred through Telegram Handoff v1.

The Radar still generates a structured Telegram Handoff v1 for orchestrated editorial workflows without requiring direct Skill-to-Skill calls. The orchestrator may load Telegram Editor instructions directly from GitHub.

## Install

Package the skill as `skill.zip` and import it into the ChatGPT Skills interface. The required entrypoint is `SKILL.md`.

## Typical prompts

- Run Bioinformatics Intelligence Radar for today.
- Run the radar for the last 7 days.
- Show only Critical Alerts and Tool & Software Radar.
- Find Social Candidates from today's peer-reviewed bioinformatics radar.
- Deep-dive the top benchmark claim from today's radar.
- Run the radar and show me the editorial tone diagnostics for the top five items.

## Design principles

- Primary sources first.
- Exact reporting windows and dates.
- Scholarly literature must have positively verified peer-review status before scoring.
- Preprint-only and uncertain-review-status papers are excluded from all user-visible Radar output.
- A later peer-reviewed journal version replaces and deduplicates its preprint.
- Software/database/dataset/infrastructure events are verified by their official sources and are not incorrectly subjected to a paper peer-review requirement.
- Broad discovery, then eligibility verification, deduplication and ranking.
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
- `references/peer-review-policy.md`: mandatory scholarly-literature eligibility gate.
- `references/search-playbook.md`: discovery, peer-review filtering, and deduplication process.
- `references/watchlists.md`: priority tools and data resources.
- `references/scoring.md`: eligibility-aware technical, social, and reproducibility scoring.
- `references/editorial-tone-engine.md`: adaptive tone selection, evidence modifiers, arbitration rules, and final tone gate.
- `references/output-contract.md`: fixed Radar v2.4 report structure and peer-review compliance output.
- `references/telegram-handoff.md`: machine-readable contract for downstream Telegram editing, with peer-review eligibility preserved.
- `references/orchestration.md`: orchestrator ownership, GitHub-direct Editor execution, and failure behavior.

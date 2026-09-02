# Bioinformatics Intelligence Radar

A reusable ChatGPT Skill for daily bioinformatics news and technical-intelligence monitoring.

## Current protocol

Version: 2.5.0

The radar performs broad discovery before ranking. It covers verified peer-reviewed scholarly literature, software releases, databases, infrastructure, datasets, reproducibility, benchmark claims, trend signals, and public-facing social candidates.

Version 2.5.0 refactors `SKILL.md` into a lean control plane. Detailed output schemas, peer-review rules, scoring, tone routing, and downstream handoff contracts remain in focused files under `references/` and are loaded only when their workflow stage requires them. The scientific and peer-review policy from v2.4.0 is unchanged.

The scholarly-literature stream is **peer-reviewed-only**. Preprints, submitted manuscripts, working papers, conference abstracts, and papers with uncertain review status are excluded before scoring and cannot enter the Radar report, Signals, Social Candidates, Deep Dives, Watchlist, Benchmark Claims, or Telegram Handoff v1. Preprint services may be queried only for identity resolution or to find a later peer-reviewed publication.

This restriction applies to scholarly papers. Official software releases, database updates, datasets, infrastructure changes, security notices, and service changes remain eligible through their appropriate primary official sources.

The adaptive editorial tone engine keeps one stable publication identity (`SCIENTIFIC_INTELLIGENCE`) while selecting operational tones only after evidence verification. Evidence modifiers such as `AUTHOR_REPORTED`, `CLINICAL_CAUTION`, `CAUSALITY_CAUTION`, and `HIGH_OVERHYPE_RISK` are preserved when an item is shortened, reframed, reused in Social Candidates, or transferred through Telegram Handoff v1.

The Radar can generate a structured Telegram Handoff v1 for orchestrated editorial workflows without directly invoking or discovering Telegram Editor. The outer orchestrator owns downstream execution.

## Install

Package the runtime Skill files with `SKILL.md` as the entry point and `agents/openai.yaml` as UI metadata. Repository documentation and development evidence do not need to be included in the installable runtime bundle.

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

## Runtime layout

- `SKILL.md`: lean control plane, routing, core invariants, and release gate.
- `agents/openai.yaml`: UI metadata and default prompt.
- `references/source-policy.md`: source hierarchy and verification policy.
- `references/peer-review-policy.md`: mandatory scholarly-literature eligibility gate.
- `references/search-playbook.md`: discovery, peer-review filtering, and deduplication process.
- `references/watchlists.md`: priority tools and data resources.
- `references/scoring.md`: eligibility-aware technical, social, and reproducibility scoring.
- `references/editorial-tone-engine.md`: adaptive tone selection, evidence modifiers, arbitration rules, and final tone gate.
- `references/output-contract.md`: authoritative Radar report schema and peer-review-compliance output.
- `references/telegram-handoff.md`: machine-readable contract for downstream Telegram editing, with peer-review eligibility preserved.
- `references/orchestration.md`: orchestrator ownership, repository-mode Editor execution, and failure behavior.

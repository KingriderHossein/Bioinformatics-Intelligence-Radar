# Bioinformatics Intelligence Radar

A reusable ChatGPT Skill for daily bioinformatics news and technical-intelligence monitoring.

## Current protocol

Version: 2.7.0

Version 2.7.0 introduces a stateful evidence pipeline without weakening the strict peer-reviewed-only literature policy.

The Radar now uses one internal `Evidence Card v1` per canonical eligible story. Identity, dates, exact numbers, benchmark attribution, source provenance, reproducibility evidence, limitations, overhype risk, and `do_not_say_fa` are captured once and reused across the Executive Brief, Main Radar, Benchmark Claims, Signals, Social Candidates, Deep Dives, and Telegram Handoff v1.

When prior Radar state is available, `Radar Run State v1` enables cross-run deduplication and material-change detection. Same-story/no-change items can be suppressed, while publication transitions, stable-release transitions, workflow integrations, new independent validation, corrections, retractions, or other material changes remain reportable. Missing state never causes the Radar to fail and prior history is never invented.

Discovery is adaptive. The Radar checks Curator sources first, fills coverage gaps selectively, resolves eligibility and identity, then reserves deep verification for items likely to affect the final report. Broad discovery stops when coverage is adequate, two consecutive passes add no new HIGH/material event, and no unresolved critical event remains.

The Radar has no minimum story quota. Low-news days are valid and must not be padded with weak, duplicate, or ineligible items.

The scholarly-literature stream remains **peer-reviewed-only**. Preprints, submitted manuscripts, working papers, conference abstracts, and papers with uncertain review status are excluded before scoring and cannot enter the Radar report, Signals, Social Candidates, Deep Dives, Watchlist, Benchmark Claims, or Telegram Handoff v1. Preprint services may be used only for identity resolution or to find a later peer-reviewed publication.

This restriction applies to scholarly papers. Official software releases, database updates, datasets, infrastructure changes, security notices, and service changes remain eligible through appropriate primary official sources.

## Source Curator integration

When the Bioinformatics Source Curator handoff is available, valid rows from `10_RADAR_SOURCES` are the primary persistent monitoring roster. The configured workbook is resolved by title (`Bioinformatics Source Curator Registry`) so no private spreadsheet ID is stored in this public repository.

Curator controls **where Radar monitors first**, not what Radar is allowed to claim. Source-level approval never proves that an individual paper is peer-reviewed or that a software/database change is important.

Repeatedly useful official sources that are absent from the Curator roster can be recorded in an internal `Curator Feedback v1` queue for future review. Radar does not self-approve those sources.

## Risk-aware editorial routing

Technical priority and Social Score remain separate. Version 2.7.0 adds a small evidence-risk penalty for ordering Social Candidates:

`editorial_priority_score = social_score - evidence_risk_penalty`

This ranking adjustment does not alter the scientific score and does not hide the original Social Score. Evidence-risk modifiers such as `AUTHOR_REPORTED`, `CLINICAL_CAUTION`, `CAUSALITY_CAUTION`, and `HIGH_OVERHYPE_RISK` remain non-negotiable downstream boundaries.

Signal of the Day now distinguishes:

- `OBSERVATION`
- `EMERGING_SIGNAL`
- `ESTABLISHED_TREND`

An emerging signal requires at least two independent eligible observations from different projects or event origins. An established trend is intentionally rare and normally requires evidence beyond one daily run.

## Telegram orchestration

The Radar can generate Telegram Handoff v1 without directly invoking or discovering Telegram Editor. Handoff version remains `1.0` for compatibility, but candidates are now derived from final Evidence Cards so exact facts and evidence boundaries are not reconstructed independently.

The outer orchestrator owns downstream Editor execution and optional persistence of Radar run state.

## Typical prompts

- Run Bioinformatics Intelligence Radar for today.
- Run the radar for the last 7 days.
- Run today's radar using the current Source Curator registry.
- Continue today's radar using the previous Radar state and show only material changes.
- Show only Critical Alerts and Tool & Software Radar.
- Find Social Candidates from today's peer-reviewed bioinformatics radar.
- Deep-dive the top benchmark claim from today's radar.

## Design principles

- Curator-approved A/B sources are the primary persistent monitoring roster when available.
- Source-level approval never replaces Radar item-level verification.
- Built-in watchlists cover gaps and failures while the curated registry grows.
- Primary and claim-level sources first.
- Exact reporting windows and separate event/publication/effective dates.
- Scholarly literature must have positively verified peer-review status before scoring.
- Preprint-only and uncertain-review-status papers are excluded from all user-visible Radar output.
- One Evidence Card is the factual source of truth for each canonical eligible story.
- Cross-run state is optional, explicit, and never invented.
- Material-change detection prevents repeated daily coverage without hiding real updates.
- Adaptive discovery uses verification tiers and stop rules.
- No minimum story quota and no filler.
- No invented scan counts; use observed telemetry only.
- Infrastructure changes outrank routine papers when workflow impact is higher.
- Social ranking is adjusted for evidence risk without changing scientific evidence scores.
- Evidence-risk modifiers survive summarization and downstream handoff.
- Radar reports are written in Persian by default while technical names and identifiers remain in English when needed for precision.

## Runtime layout

- `SKILL.md`: lean control plane, routing, workflow, invariants, and release gate.
- `agents/openai.yaml`: UI metadata and default prompt.
- `references/curator-handoff.md`: Source Curator schema, registry locator, feedback boundary, and fallback behavior.
- `references/source-policy.md`: source hierarchy and claim-level verification policy.
- `references/peer-review-policy.md`: mandatory scholarly-literature eligibility gate.
- `references/search-playbook.md`: adaptive staged discovery, verification tiers, stop rules, and deduplication.
- `references/watchlists.md`: fallback and coverage-gap sources.
- `references/evidence-card.md`: internal single-source-of-truth contract for canonical stories.
- `references/run-state.md`: optional cross-run ledger, material-change logic, telemetry, and Curator feedback queue.
- `references/scoring.md`: technical, social, evidence-risk-adjusted editorial, and reproducibility scoring.
- `references/editorial-tone-engine.md`: adaptive tone selection and evidence modifiers.
- `references/output-contract.md`: authoritative Persian report schema, no-quota behavior, Signal evidence graph, and observed statistics.
- `references/telegram-handoff.md`: Telegram Handoff v1 derived from final Evidence Cards.
- `references/orchestration.md`: Curator transfer, optional state persistence, downstream Editor execution, and failure behavior.

---
name: bioinformatics-intelligence-radar
description: Run a source-grounded bioinformatics news and technical-intelligence radar using a curated monitoring roster plus verified peer-reviewed scholarly literature, software, database, dataset, and infrastructure sources. Use when the user asks for daily or periodic bioinformatics news monitoring, a bioinformatics intelligence report, peer-reviewed paper/tool/database/release surveillance, reproducibility checks, benchmark-claim triage, emerging signals, social-media story candidates, or continuation of a prior Radar run. Exclude preprints and any scholarly article whose peer-review status cannot be positively verified from every user-visible Radar section and downstream Telegram handoff.
---

# Bioinformatics Intelligence Radar

Protocol version: 2.7.0

Run adaptive discovery first, then narrow through eligibility verification, deduplication, material-change detection, Evidence Cards, scoring, deep verification, editorial routing, and report construction. Treat this file as the control plane. Load detailed policies from `references/` only when the relevant stage is reached.

## Core invariants

1. **Use the Curator roster as the persistent monitoring layer when available.** Load the Bioinformatics Source Curator handoff before scheduled or periodic discovery. Curator source approval is source-level trust only and never replaces Radar item-level verification.
2. **Peer review is an eligibility gate for scholarly literature.** Positively verify peer-review status before scoring or exposing a scholarly item. Preprints may be used only for identity resolution or to locate a later peer-reviewed publication.
3. **Non-literature events use their own primary-source gate.** Official software releases, database updates, datasets, infrastructure changes, security notices, and service changes do not require paper peer review; verify them through the appropriate official source.
4. **Use one Evidence Card per canonical eligible story.** After identity and eligibility are resolved, capture material facts, exact numbers, source provenance, benchmark status, limitations, reproducibility evidence, and risk boundaries in `references/evidence-card.md`. Derive all later story surfaces from that card.
5. **Use prior Radar state when available, but never invent it.** Apply `references/run-state.md` for cross-run deduplication and material-change detection. Missing state must not fail the run.
6. **Evidence precedes tone.** Use `classify information -> verify evidence -> update Evidence Card -> select tone -> write`. Tone may change framing, pacing, and emphasis but never claim strength, causality, clinical readiness, benchmark certainty, or uncertainty.
7. **Do not invent counts or metadata.** Maintain telemetry during the run when practical. If a count was not actually tracked, say so rather than reconstructing or estimating it.
8. **No Skill calls another Skill directly.** The outer orchestrator may load a Source Curator handoff, persist Radar state, or execute the downstream Telegram Editor workflow. Radar does not invoke those Skills itself.
9. **Prefer fewer strong items over filler.** There is no minimum story quota. A low-news day is a valid result.
10. **Search adaptively.** Stop broad discovery when coverage is adequate, two consecutive passes add no new HIGH/material event, and no unresolved critical event remains. Continue exact verification for already shortlisted items.

## Reference routing

Load references progressively in this order.

### Curated source intake
- Read `references/curator-handoff.md` when a Curator handoff is available, when Google Sheets access can resolve the configured source registry, or for daily/periodic runs where the curated roster should be used.
- Read `references/watchlists.md` as the fallback and coverage-gap layer, not as a replacement for a valid Curator roster.

### Discovery, eligibility, and state
- Read `references/source-policy.md` before source selection and verification.
- Read `references/search-playbook.md` when constructing discovery queries, adaptive stop logic, verification tiers, or deduplication.
- Read `references/peer-review-policy.md` before any scholarly item is scored, shortlisted, or drafted.
- Read `references/run-state.md` when prior Radar state is present or cross-run deduplication, material-change detection, telemetry, or Curator feedback is relevant.

### Evidence and ranking
- Read `references/evidence-card.md` before converting an eligible story into a report candidate.
- Read `references/scoring.md` when ranking eligible candidates, selecting Social Candidates, assigning risk-adjusted editorial priority, or evaluating reproducibility.
- For high-priority items and benchmark claims, verify the central claim against the closest primary source before narrative drafting.

### Editorial and output
- Read `references/editorial-tone-engine.md` after evidence verification and before drafting high-priority narrative items.
- Read `references/output-contract.md` when constructing the user-visible Radar report. Treat it as the authoritative section schema and final-output contract.

### Orchestration
- Read `references/orchestration.md` when ownership of Curator intake, run-state persistence, Telegram handoff transfer, repository-mode execution, or failure behavior is relevant.
- Read `references/telegram-handoff.md` only when a Telegram editorial step is requested or scheduled.

Do not duplicate detailed schemas from these references inside this control file.

## Workflow

1. **Resolve the reporting window.**
   - For `today` or a scheduled daily run, use the previous 36 hours as the primary window.
   - Expand to 7 days only for slow-moving categories, delayed indexing, or explicit recovery.
   - State exact dates in the report.
2. **Load curated monitoring sources when available.** Use `curator-handoff.md`. Treat the roster as the first persistent monitoring pass. If unavailable or incomplete, use built-in watchlists for resilience and coverage gaps.
3. **Load prior run state when available.** Use `run-state.md`. If no valid prior state exists, continue with within-run deduplication and mark the actual state condition rather than inventing history.
4. **Discover adaptively.** Follow staged passes in `search-playbook.md`; do not run every fallback query mechanically when coverage is already adequate.
5. **Establish identity and eligibility.** Verify scholarly peer-review status before scoring. Resolve preprint-to-journal relationships and retain the eligible peer-reviewed version.
6. **Deduplicate and detect material change.** Use DOI, PMID, release tag, database release ID, dataset accession, title/version relationships, and prior story ledger when available. Suppress same-story/no-change items; retain verified material updates.
7. **Create preliminary Evidence Cards.** Build one card per canonical eligible story that survives relevance triage.
8. **Score only eligible cards.** Apply `scoring.md`; no novelty, urgency, social score, or source priority can restore ineligible literature.
9. **Deepen verification selectively.** Use Tier 3 verification only for Executive Brief, CRITICAL/HIGH, major benchmark, Social, Deep-Dive, or high-risk evidence stories.
10. **Finalize Evidence Cards.** Update exact facts, benchmark attribution, limitations, reproducibility evidence, risk modifiers, and `do_not_say_fa` before writing.
11. **Select editorial treatment.** Apply the tone engine only after evidence state and risk modifiers are known.
12. **Construct the report.** Follow `output-contract.md`; use no minimum item quota and report only observed statistics.
13. **Build a Telegram handoff only when needed.** Derive `Telegram Handoff v1` from the same final Evidence Cards and verified Social Candidates. Do not invoke or search for the Editor from inside Radar.
14. **Run the release gate.** Fix any failed gate before finalizing. Update persistent run state only after gates pass when a store is available.

## Priority routing

Prioritize workflow-impacting events over routine papers when they can change analyses or break pipelines. Typical high-priority classes include:

- API, schema, authentication, endpoint, FTP, cloud, or file-format changes;
- deprecations and end-of-support dates;
- reference genome, annotation, taxonomy, or clinical-database updates that can alter results;
- security or integrity issues in widely used tools;
- major stable releases of core workflow or analysis software;
- new datasets with clear benchmark or method-development value;
- strong benchmark claims that require independent scrutiny.

Use `CRITICAL`, `HIGH`, `MEDIUM`, or `WATCH` as operational urgency labels when supported.

## Verification depth

Verify only what is material to the item and available from evidence.

- Tier 1: identity candidate, source class, date, and enough context for triage.
- Tier 2: eligibility, primary claim/event, exact key facts, main limitation, workflow relevance.
- Tier 3: comparator, benchmark context, external validation, code/data/license/release/environment/container/tests/CI when material.

Do not infer repository health, sample size, benchmark design, reproducibility, clinical value, or prior-run history from absence of evidence.

## Cross-run behavior

When valid prior state exists:

- same canonical story + no material change -> suppress from normal news output;
- same story + verified material change -> report as an update and state what changed;
- preprint -> peer-reviewed publication -> `PUBLICATION_TRANSITION` using the journal version;
- prerelease -> stable -> `RELEASE_TRANSITION`;
- correction/retraction -> re-surface according to impact.

When state is missing, do not claim these suppressions occurred.

## Release gate

Before finalizing a substantial Radar report, confirm all of the following:

- a valid Curator handoff was used when supplied; malformed rows were not guessed or silently repaired;
- source-level Curator approval was not treated as paper peer-review proof or item importance;
- every visible scholarly paper passed `peer-review-policy.md`;
- current claims are supported by sources and dates that match the reporting window;
- event date, publication date, observed date, and effective date are not conflated;
- preprint and journal versions of the same work are deduplicated correctly;
- cross-run duplicates were suppressed only when valid state existed;
- material updates were not discarded as duplicates;
- final visible facts and qualifiers match their Evidence Cards;
- author-reported benchmarks are not rewritten as independently verified facts;
- causal, clinical, AI-capability, and trend language does not exceed the evidence;
- infrastructure changes are not buried below routine literature when workflow impact is higher;
- no minimum quota introduced filler;
- report sections and measurable statistics follow `output-contract.md`;
- evidence-risk modifiers survive shortening, Social Candidate selection, and Telegram handoff;
- Radar did not invoke Source Curator or Telegram Editor as a downstream Skill;
- persistent run state, if used, is updated only after the evidence/release gates pass.

## Language and source policy

Write the complete Radar report in Persian by default. Change the report language only when the user explicitly requests another language.

Keep official tool names, package names, database names, repository names, version strings, identifiers, gene/protein symbols, command names, API fields, and precision-sensitive technical terms in English when translation would reduce accuracy.

Do not use Persian-language web sources unless the user explicitly requests them.

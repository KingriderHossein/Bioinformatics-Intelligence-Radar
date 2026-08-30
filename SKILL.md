---
name: bioinformatics-intelligence-radar
description: Run a source-grounded bioinformatics news and technical-intelligence radar using peer-reviewed scholarly literature plus verified software, database, dataset, and infrastructure sources. Use when the user asks for daily or periodic bioinformatics news monitoring, a bioinformatics intelligence report, peer-reviewed paper/tool/database/release surveillance, reproducibility checks, benchmark-claim triage, signals of emerging trends, or social-media story candidates. Exclude preprints and any scholarly article whose peer-review status cannot be positively verified from every user-visible Radar section and downstream Telegram handoff.
---

# Bioinformatics Intelligence Radar

Protocol version: 2.4.0

Produce a broad but ranked bioinformatics intelligence report. Discover widely first, then verify identity and peer-review eligibility, deduplicate, score, classify, select the editorial tone, and summarize.

## Workflow

1. Resolve the reporting window.
   - For "today" or a scheduled daily run, use the previous 36 hours as the primary window.
   - Expand to 7 days only to fill slow-moving categories or recover important items missed by indexing delays.
   - State exact dates in the report.
2. Read `references/source-policy.md` and follow its source hierarchy and verification rules.
3. Read `references/peer-review-policy.md` and apply the mandatory scholarly-literature eligibility gate before scoring or drafting.
4. Read `references/search-playbook.md` and run broad discovery across peer-reviewed literature, software, databases, infrastructure, and datasets. Preprint services may be used only for identity resolution or finding a later peer-reviewed publication.
5. Read `references/watchlists.md` and check the high-value tools and resources relevant to the window.
6. Deduplicate by DOI, PMID, repository/release tag, database release identifier, title similarity, and preprint-to-journal relationships.
7. Exclude every scholarly literature item whose peer-review status is absent, pending, ambiguous, or unverified. Do not score excluded papers.
8. Separate eligible peer-reviewed papers, software releases, database/infrastructure changes, datasets, and policy/service changes.
9. Score eligible candidates using `references/scoring.md`.
10. Verify high-priority candidates against a primary source. For benchmark claims, inspect methods or repositories when available.
11. Read `references/editorial-tone-engine.md`. Classify each high-priority narrative item by content type, evidence status, urgency, workflow impact, overhype risk, public interest, conceptual complexity, and trend support. Assign one primary editorial tone plus applicable evidence/context modifiers. Do this after evidence verification and before prose drafting.
12. Build the report using `references/output-contract.md`. Apply the selected tone without exposing internal tone labels unless the user asks for editorial diagnostics.
13. After selecting Social Candidates, read `references/telegram-handoff.md` and construct Telegram Handoff v1 when an orchestrated Telegram editorial step is requested or scheduled.
14. Do not invoke, discover, or require Bioinformatics Telegram Editor from inside Radar. The outer orchestrator owns downstream execution.
15. Before finalizing, run both the quality gates below and the final tone gate in `references/editorial-tone-engine.md`.

## Discovery requirements

Aim for 15-30 distinct eligible Radar items on normal active days. This is a target, not a quota. Never add low-value items only to reach a count.

Cover these domains when meaningful eligible items exist:

- Genomics and variant analysis
- Transcriptomics and RNA biology
- Single-cell omics
- Spatial omics
- Long-read sequencing
- AI and machine learning for biology
- Structural bioinformatics
- Metagenomics, microbiome, and AMR
- Proteomics and metabolomics
- Clinical bioinformatics and precision medicine
- Workflow engineering and reproducibility
- Databases, reference resources, and data infrastructure

## Peer-review eligibility gate

Treat `references/peer-review-policy.md` as non-negotiable.

For scholarly literature:

- Include only positively verified peer-reviewed journal/proceedings literature.
- Allow accepted/online-first/ahead-of-print manuscripts only when journal acceptance/publication is verified.
- Exclude preprint-only records, submitted manuscripts, working papers, conference abstracts, and records with uncertain peer-review status.
- If a preprint later has a peer-reviewed publication, use the peer-reviewed version as the eligible source and deduplicate the preprint.
- A DOI alone does not prove peer review.
- Exclusion occurs before technical or social scoring. No score or tone can restore an excluded paper.

This gate applies to scholarly papers, not to official software releases, database updates, datasets, infrastructure changes, security notices, or service changes; verify those through their appropriate primary official sources.

## Priority logic

Always prioritize these above ordinary papers:

- Breaking API, schema, file-format, authentication, endpoint, FTP, or cloud changes
- Deprecations and end-of-support dates
- Reference genome, annotation, taxonomy, or clinical database changes that can alter analysis results
- Security or integrity issues in widely used tools
- Major stable releases of core workflow or analysis software
- New datasets with clear benchmarking or method-development value
- Strong benchmark claims that warrant independent verification

Mark urgency as `CRITICAL`, `HIGH`, `MEDIUM`, or `WATCH`.

## Technical verification

For high-priority peer-reviewed papers and tools, inspect as many of these as the available evidence supports:

- Main claim
- Study/sample size
- Benchmark datasets and baselines
- Internal vs external validation
- Code availability
- Data availability
- License
- Latest release or recent repository activity
- Tests and CI
- Container or environment specification
- Installation path
- Main limitation
- Practical value for a working bioinformatician

Do not invent repository health, code status, sample size, benchmark design, or reproducibility details when they were not verified.

## Editorial voice and adaptive tone

Use `SCIENTIFIC_INTELLIGENCE` as the stable publication identity: precise, evidence-aware, context-rich, calm, useful, and skeptical of hype.

Do not force one surface tone across the full report. Use `references/editorial-tone-engine.md` to select the appropriate operational tone after classifying the information and verifying the evidence.

Core rule:

`classify information -> verify evidence -> select tone -> write`

Never use:

`tone -> reshape evidence`

Tone may change framing, pacing, emphasis, explanation depth, or whether a curiosity hook is appropriate. Tone must never:

- strengthen the evidence,
- hide uncertainty,
- remove an important limitation,
- turn association into causation,
- turn technical performance into clinical utility,
- present an author-reported benchmark as independently verified.

Use one primary tone per high-priority narrative item and zero to three evidence/context modifiers. Preserve all non-negotiable modifiers when the same item is reused in the Executive Brief, Social Candidates, Deep Dive, or Telegram Handoff.

## Benchmark-claim handling

Extract claims such as "X times faster", "state of the art", "higher accuracy", or "lower memory" into a separate Benchmark Claims section.

For each claim:

- Report the claim as an author-reported result unless independently reproduced.
- Identify the compared baseline and dataset when available.
- Mark `Independent verification: YES/NO/UNKNOWN`.
- Flag suspicious comparisons, missing baselines, small datasets, data leakage risk, or hardware mismatch.
- Use `EVIDENCE_CRITICAL` as the default primary tone.
- Apply `AUTHOR_REPORTED` unless independent verification was actually found.

## Signal detection

Produce 1-3 "Signal of the Day" items only when multiple independent eligible observations support a direction of travel. A single paper is usually not a trend.

For literature evidence inside a signal, every supporting paper must pass the peer-review eligibility gate. Non-peer-reviewed literature cannot support a Signal of the Day.

Each signal must contain:

- Signal statement
- Evidence items
- Why it matters
- Confidence: `LOW`, `MEDIUM`, or `HIGH`
- What evidence would strengthen or weaken the interpretation when useful

Use `SCIENTIFIC_INTELLIGENCE` tone. Separate observed facts from analyst inference.

## Social candidates

Select 3-5 eligible items for general-audience communication using the social score in `references/scoring.md`.

Do not simply copy scientific titles. Create an accurate, attractive headline that preserves uncertainty.

Each candidate must include:

- Public-facing headline
- One-sentence hook
- Why ordinary readers may care
- Suggested format: Telegram, Instagram carousel, X thread, short video, or article
- Social score /30
- Risk note if the story could be overhyped

Prefer stories with human relevance, surprising scale, medicine, AI, DNA, evolution, microbes, visual potential, or a simple question that can be answered accurately.

Use `CURIOSITY_BRIDGE` as the presentation layer for Social Candidates, but inherit all evidence-risk modifiers from the verified source item. Curiosity must never override benchmark, clinical, causality, or overhype cautions.

A scholarly Social Candidate must be peer-review-verified. Never create a Social Candidate from an excluded preprint or other non-peer-reviewed paper.

## Telegram handoff

When an orchestrated Telegram editorial step is part of the workflow, construct `Telegram Handoff v1` using `references/telegram-handoff.md`.

- Use only selected eligible Social Candidates.
- Preserve primary-source evidence, publication status, exact numbers, limitations, benchmark attribution, and overhype risk.
- For scholarly candidates, preserve explicit verification that peer review was confirmed.
- Preserve the Radar item's evidence-risk modifiers and provide an editorial tone recommendation without forcing the downstream Editor to copy Radar prose.
- Add explicit `do_not_say_fa` guardrails for likely overclaims.
- Treat the handoff as an internal transfer object by default; do not clutter the user-facing Radar report with raw JSON unless requested.
- Never call or search for the Editor as a tool or installed Skill. Return/retain the handoff for the outer orchestrator after the Radar quality gates.
- If Radar is running alone, finish normally without reporting a missing downstream Editor. Downstream availability is not Radar's concern.

## Deep-dive candidates

Select exactly 3 when enough material exists. Favor:

- High-impact infrastructure changes
- Reproducible benchmark claims
- New peer-reviewed methods with usable code/data
- Findings where independent technical analysis can add value

A scholarly Deep-Dive candidate must pass the peer-review eligibility gate.

State what should be tested next.

Use `SCIENTIFIC_INTELLIGENCE` by default. Add `EVIDENCE_CRITICAL` constraints through modifiers when the deep dive centers on a disputed, weakly validated, or high-risk claim.

## Radar statistics

Report only counts that were actually observed during the run. Never invent a large "scanned" number.

Use one of these labels:

- `Candidates retrieved` when a query/API returned a measurable count
- `Items reviewed` when items were manually inspected
- `Shortlisted`
- `High priority`
- `Social candidates`
- `Deep-dive candidates`
- `Non-peer-reviewed literature excluded` only when that count was directly observed

If a total cannot be measured, write `not measurable from the search interface` rather than estimating.

## Quality gates

Before finalizing, verify all of the following:

- Every current factual claim has a citation to a source that supports it.
- At least one recent source falls inside the requested reporting window for current-news claims.
- Event date and publication date are not confused.
- Every scholarly paper visible anywhere in the report has positively verified peer-review status.
- No preprint-only, submitted, under-review, working-paper, conference-abstract, or uncertain-review-status paper appears in the Executive Brief, Main Radar, Signals, Social Candidates, Deep Dives, Watchlist, Benchmark Claims, or Telegram Handoff.
- If a preprint and later journal article describe the same work, the peer-reviewed journal version is used and the preprint is deduplicated.
- Primary sources are preferred over press summaries and aggregators.
- Social headlines do not overstate causality or clinical readiness.
- No item appears twice under different versions unless the relationship itself is newsworthy.
- The Main Radar is broader than the Executive Brief.
- Critical infrastructure changes are not buried below ordinary papers.
- The report contains Signal of the Day, Social Candidates, Deep-Dive Candidates, Watchlist, and Radar Statistics.
- Information classification and evidence verification happened before editorial tone selection.
- Evidence-risk modifiers were preserved when items were shortened or reframed.
- Critical alerts are direct and actionable rather than curiosity-driven.
- Trend language is not inferred from one isolated paper.
- Curiosity hooks do not strengthen the underlying scientific claim.
- When an orchestrated Telegram downstream step is requested, Telegram Handoff v1 was built from the same verified eligible Social Candidates and contains no stronger claims than the Radar evidence.
- Radar did not attempt to invoke or detect a downstream Editor itself.

## Language and style

Write the complete Radar report in Persian by default, regardless of the language of the request. Change the report language only when the user explicitly asks for another language.

Translate section headings, narrative explanations, analysis, summaries, Signal of the Day, Social Candidates, Deep-Dive Candidates, Watchlist notes, and table prose into Persian. Keep official tool names, package names, database names, repository names, version strings, identifiers, gene/protein symbols, command names, API field names, and technical terms in English when translation would reduce precision.

Use natural technical Persian. Do not translate literal software labels such as `CRITICAL`, `HIGH`, `MEDIUM`, `WATCH`, or repository-health values when they function as machine-readable status labels; add a Persian explanation when useful.

Do not use Persian-language web sources unless the user explicitly asks for them.

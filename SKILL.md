---
name: bioinformatics-intelligence-radar
description: Run a source-grounded bioinformatics news and technical-intelligence radar. Use when the user asks for daily or periodic bioinformatics news monitoring, a bioinformatics intelligence report, paper/preprint/tool/database/release surveillance, reproducibility checks, benchmark-claim triage, signals of emerging trends, or social-media story candidates. Search current primary sources, deduplicate and rank findings, separate peer-reviewed work from preprints, identify workflow-breaking changes, and produce the Bioinformatics Intelligence Radar report.
---

# Bioinformatics Intelligence Radar

Protocol version: 2.2.0

Produce a broad but ranked bioinformatics intelligence report. Do not reduce the task to a short news digest. Discover widely first, then verify, deduplicate, score, and summarize.

## Workflow

1. Resolve the reporting window.
   - For "today" or a scheduled daily run, use the previous 36 hours as the primary window.
   - Expand to 7 days only to fill slow-moving categories or recover important items missed by indexing delays.
   - State exact dates in the report.
2. Read `references/source-policy.md` and follow its source hierarchy and verification rules.
3. Read `references/search-playbook.md` and run broad discovery across literature, preprints, software, databases, infrastructure, and datasets.
4. Read `references/watchlists.md` and check the high-value tools and resources relevant to the window.
5. Deduplicate by DOI, PMID, preprint identifier, repository/release tag, database release identifier, and title similarity.
6. Separate peer-reviewed papers, preprints, software releases, database/infrastructure changes, datasets, and policy/service changes.
7. Score candidates using `references/scoring.md`.
8. Verify high-priority candidates against a primary source. For benchmark claims, inspect the methods or repository when available.
9. Build the report using `references/output-contract.md`.
10. After selecting Social Candidates, read `references/telegram-handoff.md` and construct Telegram Handoff v1 when a downstream Telegram Editor run is requested or scheduled.
11. Before finalizing, run the quality gates below.

## Discovery requirements

Aim for 20-35 distinct radar items on normal active days. This is a target, not a quota. Never add low-value items only to reach a count.

Cover these domains when meaningful items exist:

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

For high-priority papers, preprints, and tools, inspect as many of these as the available evidence supports:

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

## Preprint handling

Label preprints clearly as `PREPRINT - NOT PEER REVIEWED`.

Do not give a preprint the same evidential status as a peer-reviewed paper. If a preprint has a later peer-reviewed version, prefer the peer-reviewed version and mention the relationship when useful.

## Benchmark-claim handling

Extract claims such as "X times faster", "state of the art", "higher accuracy", or "lower memory" into a separate Benchmark Claims section.

For each claim:

- Report the claim as an author-reported result unless independently reproduced.
- Identify the compared baseline and dataset when available.
- Mark `Independent verification: YES/NO/UNKNOWN`.
- Flag suspicious comparisons, missing baselines, small datasets, data leakage risk, or hardware mismatch.

## Signal detection

Produce 1-3 "Signal of the Day" items only when multiple independent observations support a direction of travel. A single paper is usually not a trend.

Each signal must contain:

- Signal statement
- Evidence items
- Why it matters
- Confidence: `LOW`, `MEDIUM`, or `HIGH`

## Social candidates

Select 3-5 items for general-audience communication using the social score in `references/scoring.md`.

Do not simply copy scientific titles. Create an accurate, attractive headline that preserves uncertainty.

Each candidate must include:

- Public-facing headline
- One-sentence hook
- Why ordinary readers may care
- Suggested format: Telegram, Instagram carousel, X thread, short video, or article
- Social score /30
- Risk note if the story could be overhyped

Prefer stories with human relevance, surprising scale, medicine, AI, DNA, evolution, microbes, visual potential, or a simple question that can be answered accurately.

## Telegram handoff

When a downstream Bioinformatics Telegram Editor run is part of the workflow, construct `Telegram Handoff v1` using `references/telegram-handoff.md`.

- Use only selected Social Candidates.
- Preserve primary-source evidence, publication status, exact numbers, limitations, benchmark attribution, and overhype risk.
- Add explicit `do_not_say_fa` guardrails for likely overclaims.
- Treat the handoff as an internal transfer object by default; do not clutter the user-facing Radar report with raw JSON unless requested.
- If the Editor runs in the same task, pass the handoff directly to it after the Radar quality gates.

## Deep-dive candidates

Select exactly 3 when enough material exists. Favor:

- High-impact infrastructure changes
- Reproducible benchmark claims
- New methods with usable code/data
- Findings where independent technical analysis can add value

State what should be tested next.

## Radar statistics

Report only counts that were actually observed during the run. Never invent a large "scanned" number.

Use one of these labels:

- `Candidates retrieved` when a query/API returned a measurable count
- `Items reviewed` when items were manually inspected
- `Shortlisted`
- `High priority`
- `Social candidates`
- `Deep-dive candidates`

If a total cannot be measured, write `not measurable from the search interface` rather than estimating.

## Quality gates

Before finalizing, verify all of the following:

- Every current factual claim has a citation to a source that supports it.
- At least one recent source falls inside the requested reporting window for current-news claims.
- Event date and publication date are not confused.
- Preprints are labeled.
- Primary sources are preferred over press summaries and aggregators.
- Social headlines do not overstate causality or clinical readiness.
- No item appears twice under different versions unless the relationship itself is newsworthy.
- The Main Radar is broader than the Executive Brief.
- Critical infrastructure changes are not buried below ordinary papers.
- The report contains Signal of the Day, Social Candidates, Deep-Dive Candidates, Watchlist, and Radar Statistics.
- When a Telegram downstream step is requested, Telegram Handoff v1 was built from the same verified Social Candidates and contains no stronger claims than the Radar evidence.

## Language and style

Write the complete Radar report in Persian by default, regardless of the language of the request. Change the report language only when the user explicitly asks for another language.

Translate section headings, narrative explanations, analysis, summaries, Signal of the Day, Social Candidates, Deep-Dive Candidates, Watchlist notes, and table prose into Persian. Keep official tool names, package names, database names, repository names, version strings, identifiers, gene/protein symbols, command names, API field names, and technical terms in English when translation would reduce precision.

Use natural technical Persian. Do not translate literal software labels such as `CRITICAL`, `HIGH`, `MEDIUM`, `WATCH`, `PREPRINT - NOT PEER REVIEWED`, or repository-health values when they function as machine-readable status labels; add a Persian explanation when useful.

Do not use Persian-language web sources unless the user explicitly asks for them.

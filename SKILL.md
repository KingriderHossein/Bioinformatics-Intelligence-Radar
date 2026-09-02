---
name: bioinformatics-intelligence-radar
description: Run a source-grounded bioinformatics news and technical-intelligence radar using peer-reviewed scholarly literature plus verified software, database, dataset, and infrastructure sources. Use when the user asks for daily or periodic bioinformatics news monitoring, a bioinformatics intelligence report, peer-reviewed paper/tool/database/release surveillance, reproducibility checks, benchmark-claim triage, emerging-trend signals, or social-media story candidates. Exclude preprints and any scholarly article whose peer-review status cannot be positively verified from every user-visible Radar section and downstream Telegram handoff.
---

# Bioinformatics Intelligence Radar

Protocol version: 2.5.0

Run broad discovery first, then narrow through eligibility verification, deduplication, scoring, evidence verification, editorial routing, and report construction. Treat this file as the control plane. Load detailed policies from `references/` only when the relevant stage is reached.

## Core invariants

1. **Peer review is an eligibility gate for scholarly literature.** Positively verify peer-review status before scoring or exposing a scholarly item. Preprints may be used only for identity resolution or to locate a later peer-reviewed publication.
2. **Non-literature events use their own primary-source gate.** Official software releases, database updates, datasets, infrastructure changes, security notices, and service changes do not require paper peer review; verify them through the appropriate official source.
3. **Verify identity and evidence before ranking or writing.** A DOI alone does not prove peer review. Search snippets, reposts, and secondary summaries are discovery aids, not final factual authority when a primary source is available.
4. **Evidence precedes tone.** Use `classify information -> verify evidence -> select tone -> write`. Tone may change framing, pacing, and emphasis but never claim strength, causality, clinical readiness, benchmark certainty, or uncertainty.
5. **Do not invent counts or metadata.** If a scan/review total cannot be measured from the interface or recorded during the run, say so rather than estimate it.
6. **Radar does not execute the downstream Telegram Editor.** Radar may build `Telegram Handoff v1`; the outer orchestrator owns downstream Skill or repository execution.
7. **Prefer fewer strong items over filler.** A low-news day is a valid result. Never add weak or ineligible material to reach a quota.

## Reference routing

Load references progressively in this order.

### Discovery and eligibility
- Read `references/source-policy.md` before source selection and verification.
- Read `references/search-playbook.md` when constructing discovery queries or deduplication logic.
- Read `references/peer-review-policy.md` before any scholarly item is scored, shortlisted, or drafted.
- Read `references/watchlists.md` for daily/periodic surveillance or when checking high-value tools, databases, or infrastructure.

### Ranking and verification
- Read `references/scoring.md` when ranking eligible candidates, selecting Social Candidates, or assigning reproducibility/social scores.
- For high-priority items and benchmark claims, verify the central claim against a primary source before narrative drafting.

### Editorial and output
- Read `references/editorial-tone-engine.md` after evidence verification and before drafting high-priority narrative items.
- Read `references/output-contract.md` when constructing the user-visible Radar report. Treat it as the authoritative section schema and final-output contract.

### Downstream orchestration
- Read `references/telegram-handoff.md` only when a Telegram editorial step is requested or scheduled.
- Read `references/orchestration.md` only when ownership of chaining, repository-mode execution, or failure behavior is relevant.

Do not duplicate detailed schemas from these references inside this control file.

## Workflow

1. **Resolve the reporting window.**
   - For `today` or a scheduled daily run, use the previous 36 hours as the primary window.
   - Expand to 7 days only for slow-moving categories or indexing delays.
   - State exact dates in the report.
2. **Discover broadly.** Search across peer-reviewed literature, software, databases, datasets, infrastructure, and service changes using the source policy and search playbook.
3. **Establish identity and eligibility.** Verify scholarly peer-review status before scoring. Resolve preprint-to-journal relationships and retain the eligible peer-reviewed version.
4. **Deduplicate.** Use DOI, PMID, repository/release tag, database release ID, title similarity, and version relationships as applicable.
5. **Classify eligible candidates.** Separate peer-reviewed papers, software releases, database/infrastructure changes, datasets, and policy/service changes.
6. **Score only eligible candidates.** Apply `references/scoring.md`; no novelty, urgency, or social score can restore an ineligible scholarly item.
7. **Verify high-priority claims.** Inspect primary evidence for critical alerts, major benchmarks, workflow-breaking changes, and the strongest scientific claims.
8. **Select editorial treatment.** Apply the tone engine only after evidence state and risk modifiers are known.
9. **Construct the report.** Follow `references/output-contract.md` rather than recreating its section rules here.
10. **Build a handoff only when needed.** If the workflow includes Telegram editing, create an internal `Telegram Handoff v1` from the same verified eligible Social Candidates. Do not invoke or search for the Editor from inside Radar.
11. **Run the release gate.** Fix any failed gate before finalizing; if evidence is unavailable, state the coverage limit rather than fill it with a weaker claim.

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

Verify only what is material to the item and available from evidence. For high-priority papers and tools, relevant fields can include:

- central claim and evidence type;
- study/sample size or benchmark scale;
- datasets, baselines, comparator context, and hardware when material;
- internal versus external validation;
- code, data, license, release, repository activity, tests/CI, and environment/container information;
- main limitation and practical workflow value.

Do not infer repository health, sample size, benchmark design, reproducibility, or clinical value from absence of evidence.

## Release gate

Before finalizing a substantial Radar report, confirm all of the following:

- every visible scholarly paper passed `references/peer-review-policy.md`;
- current claims are supported by sources and dates that match the reporting window;
- primary sources are preferred for central claims and official changes;
- event date and publication date are not confused;
- preprint and journal versions of the same work are deduplicated correctly;
- author-reported benchmarks are not rewritten as independently verified facts;
- causal, clinical, and trend language does not exceed the evidence;
- infrastructure changes are not buried below routine literature when workflow impact is higher;
- report sections and measurable statistics follow `references/output-contract.md`;
- evidence-risk modifiers survive shortening, Social Candidate selection, and Telegram handoff;
- Radar did not attempt to discover or invoke the downstream Editor.

## Language and source policy

Write the complete Radar report in Persian by default. Change the report language only when the user explicitly requests another language.

Keep official tool names, package names, database names, repository names, version strings, identifiers, gene/protein symbols, command names, API fields, and precision-sensitive technical terms in English when translation would reduce accuracy.

Do not use Persian-language web sources unless the user explicitly requests them.

---
name: bioinformatics-intelligence-radar
description: Run a source-grounded bioinformatics news and technical-intelligence radar using a curated monitoring roster plus verified peer-reviewed scholarly literature, software, database, dataset, and infrastructure sources. Use when the user asks for daily or periodic bioinformatics news monitoring, a bioinformatics intelligence report, peer-reviewed paper/tool/database/release surveillance, reproducibility checks, benchmark-claim triage, emerging-trend signals, or social-media story candidates. Exclude preprints and any scholarly article whose peer-review status cannot be positively verified from every user-visible Radar section and downstream Telegram handoff.
---

# Bioinformatics Intelligence Radar

Protocol version: 2.6.0

Run broad discovery first, then narrow through eligibility verification, deduplication, scoring, evidence verification, editorial routing, and report construction. Treat this file as the control plane. Load detailed policies from `references/` only when the relevant stage is reached.

## Core invariants

1. **Use the Curator roster as the persistent monitoring layer when available.** Load the Bioinformatics Source Curator handoff before scheduled or periodic discovery. Curator source approval is source-level trust only and never replaces Radar item-level verification.
2. **Peer review is an eligibility gate for scholarly literature.** Positively verify peer-review status before scoring or exposing a scholarly item. Preprints may be used only for identity resolution or to locate a later peer-reviewed publication.
3. **Non-literature events use their own primary-source gate.** Official software releases, database updates, datasets, infrastructure changes, security notices, and service changes do not require paper peer review; verify them through the appropriate official source.
4. **Verify identity and evidence before ranking or writing.** A DOI alone does not prove peer review. Search snippets, reposts, and secondary summaries are discovery aids, not final factual authority when a primary source is available.
5. **Evidence precedes tone.** Use `classify information -> verify evidence -> select tone -> write`. Tone may change framing, pacing, and emphasis but never claim strength, causality, clinical readiness, benchmark certainty, or uncertainty.
6. **Do not invent counts or metadata.** If a scan/review total cannot be measured from the interface or recorded during the run, say so rather than estimate it.
7. **No Skill calls another Skill directly.** The outer orchestrator may load a Source Curator handoff or execute the downstream Telegram Editor workflow. Radar does not invoke either Skill itself.
8. **Prefer fewer strong items over filler.** A low-news day is a valid result. Never add weak or ineligible material to reach a quota.

## Reference routing

Load references progressively in this order.

### Curated source intake
- Read `references/curator-handoff.md` when a Curator handoff is available, when Google Sheets access can resolve the configured source registry, or for daily/periodic runs where the curated roster should be used.
- Read `references/watchlists.md` as the fallback and coverage-gap layer, not as a replacement for a valid Curator roster.

### Discovery and eligibility
- Read `references/source-policy.md` before source selection and verification.
- Read `references/search-playbook.md` when constructing discovery queries or deduplication logic.
- Read `references/peer-review-policy.md` before any scholarly item is scored, shortlisted, or drafted.

### Ranking and verification
- Read `references/scoring.md` when ranking eligible candidates, selecting Social Candidates, or assigning reproducibility/social scores.
- For high-priority items and benchmark claims, verify the central claim against a primary source before narrative drafting.

### Editorial and output
- Read `references/editorial-tone-engine.md` after evidence verification and before drafting high-priority narrative items.
- Read `references/output-contract.md` when constructing the user-visible Radar report. Treat it as the authoritative section schema and final-output contract.

### Orchestration
- Read `references/orchestration.md` when ownership of Curator intake, Telegram handoff transfer, repository-mode execution, or failure behavior is relevant.
- Read `references/telegram-handoff.md` only when a Telegram editorial step is requested or scheduled.

Do not duplicate detailed schemas from these references inside this control file.

## Workflow

1. **Resolve the reporting window.**
   - For `today` or a scheduled daily run, use the previous 36 hours as the primary window.
   - Expand to 7 days only for slow-moving categories or indexing delays.
   - State exact dates in the report.
2. **Load curated monitoring sources when available.** Use `references/curator-handoff.md`. Treat the roster as the primary persistent monitoring seed. If it is unavailable or incomplete, use the built-in watchlists for resilience and coverage gaps.
3. **Discover broadly.** Search across peer-reviewed literature, software, databases, datasets, infrastructure, and service changes using the source policy and search playbook. Do not restrict the entire Radar to the currently bootstrapped Curator domains.
4. **Establish identity and eligibility.** Verify scholarly peer-review status before scoring. Resolve preprint-to-journal relationships and retain the eligible peer-reviewed version.
5. **Deduplicate.** Use DOI, PMID, repository/release tag, database release ID, title similarity, and version relationships as applicable.
6. **Classify eligible candidates.** Separate peer-reviewed papers, software releases, database/infrastructure changes, datasets, and policy/service changes.
7. **Score only eligible candidates.** Apply `references/scoring.md`; no novelty, urgency, or social score can restore an ineligible scholarly item.
8. **Verify high-priority claims.** Inspect primary evidence for critical alerts, major benchmarks, workflow-breaking changes, and the strongest scientific claims.
9. **Select editorial treatment.** Apply the tone engine only after evidence state and risk modifiers are known.
10. **Construct the report.** Follow `references/output-contract.md` rather than recreating its section rules here.
11. **Build a handoff only when needed.** If the workflow includes Telegram editing, create an internal `Telegram Handoff v1` from the same verified eligible Social Candidates. Do not invoke or search for the Editor from inside Radar.
12. **Run the release gate.** Fix any failed gate before finalizing; if evidence is unavailable, state the coverage limit rather than fill it with a weaker claim.

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

- a valid Curator handoff was used when supplied; malformed rows were not guessed or silently repaired;
- source-level Curator approval was not treated as paper peer-review proof or item importance;
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
- Radar did not invoke Source Curator or Telegram Editor as a downstream Skill.

## Language and source policy

Write the complete Radar report in Persian by default. Change the report language only when the user explicitly requests another language.

Keep official tool names, package names, database names, repository names, version strings, identifiers, gene/protein symbols, command names, API fields, and precision-sensitive technical terms in English when translation would reduce accuracy.

Do not use Persian-language web sources unless the user explicitly requests them.

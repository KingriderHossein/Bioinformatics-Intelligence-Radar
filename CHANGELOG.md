# Changelog

## 3.1.0 - 2026-09-21

- Added Evidence Card, Story Card and run-state JSON Schemas.
- Added durable identity, material event fingerprints and within-run deduplication.
- Added cross-run state classification for unchanged, updated, publication, release and correction transitions.
- Added explainable six-dimension News Value scoring.
- Added `scripts/radar_cli.py` for validation and processing normalized discovery items.
- Added golden fixtures, unit tests, CI checks and example configuration.
- Added architecture, configuration, contribution and migration documentation.
- Preserved Radar 3.0 newsroom, peer-review and Telegram Handoff contracts.

## 3.0.0 - 2026-09-13

- Reframed Bioinformatics Intelligence Radar as a two-layer product: `Intelligence Engine` for evidence and `Newsroom Engine` for story selection/presentation.
- Added `references/newsroom-engine.md` with the Story Gate, News Value Score, angle generation, headline/lead rules, Story Card schema, Telegram/article treatment, and newsroom release gate.
- Made the user-visible product a compact Persian scientific newsroom rather than a default multi-section technical audit.
- Replaced the old exhaustive visible report contract with `خبر اول`, `ارزش دنبال‌کردن`, optional `هشدار عملی`, optional `سیگنال امروز`, `انتخاب تحریریه`, concise Deep-Dive suggestions, Watchlist, and compact observed-only monitoring telemetry.
- Moved peer-review tables, repository-health audits, reproducibility scoring, benchmark-audit tables, raw Evidence Cards/Story Cards, and detailed statistics behind an on-request technical appendix unless essential to a story.
- Separated evidence quality from newsworthiness: evidence now gates eligibility and wording; it is no longer a dimension inside News Value.
- Added News Value /30 across impact, audience relevance, novelty, consequence, storyability, and timeliness.
- Removed evidence-risk penalties from story ranking. High overhype risk now changes format depth and caveat strength rather than artificially lowering newsworthiness.
- Kept a separate Telegram/social compatibility score only for downstream presentation-format selection.
- Added an internal Story Card derived from the Evidence Card, containing the news statement, selected angle, headline options, lead, essential facts, consequence, visible boundary, and format recommendations.
- Added explicit newsroom angle types: `RESULT`, `TENSION`, `CONSEQUENCE`, `WORKFLOW_IMPACT`, `SCALE`, `LIMITATION`, and `EXPLAINER`.
- Added headline rules that prioritize the actual result/consequence over framework names, journal prestige, or generic novelty language.
- Reworked the tone system around `SCIENTIFIC_NEWSROOM` with `NEWS_BRIEF`, `TECHNICAL_ALERT`, `EVIDENCE_CRITICAL`, `EXPLAINER`, and `SCIENTIFIC_INTELLIGENCE`.
- Reworked adaptive search so deep verification happens after Story Gate triage instead of treating every eligible paper as a likely output item.
- Kept strict peer-reviewed-only scholarly coverage and official-source verification for non-literature events.
- Kept Evidence Card v1, optional run state, material-change detection, duplicate suppression, Curator feedback, and claim-level source provenance from v2.7.0.
- Kept Telegram Handoff at `1.0` for compatibility, while adding optional newsroom fields such as `news_value_score`, `news_statement_fa`, selected angle, headline options, and article/visual suitability.
- Documented qualitative newsroom-design provenance across Digiato, Zoomit, Peivast, Euronews Persian, Interesting Engineering, ScienceAlert, Science in Telegram, and Gadget News while explicitly prohibiting direct imitation of any publication's distinctive style.

## 2.7.0 - 2026-09-11

- Added `references/evidence-card.md` and made one Evidence Card v1 the internal factual source of truth for each canonical eligible story.
- Required downstream Radar surfaces to inherit exact numbers, benchmark attribution, source provenance, limitations, overhype risk, and `do_not_say_fa` from the same Evidence Card.
- Added `references/run-state.md` for optional cross-run story state, material-change detection, observed-only telemetry, and Curator feedback records.
- Defined explicit state conditions: `AVAILABLE`, `BOOTSTRAP`, `UNAVAILABLE`, and `NOT_CONFIGURED`; missing state never fails Radar and prior history must never be invented.
- Added canonical story identity and event-fingerprint rules for suppressing same-story/no-change items while preserving publication transitions, stable-release transitions, workflow integrations, new validations, corrections, and retractions.
- Refactored discovery into adaptive staged passes with Tier 1/2/3 verification depth and a stop rule after adequate coverage plus two consecutive passes without a new HIGH/material event.
- Removed the previous Main Radar minimum-volume pressure. There is now no minimum story quota; low-news days must not be padded with filler.
- Added evidence-risk-adjusted editorial ordering for Social Candidates: `editorial_priority_score = social_score - evidence_risk_penalty`, while preserving the original Social Score.
- Added Signal evidence classes `OBSERVATION`, `EMERGING_SIGNAL`, and `ESTABLISHED_TREND`; emerging signals require at least two independent eligible observations from different projects/event origins.
- Reworked Radar statistics around counters actually maintained during the current run, including discovery, eligibility, suppression, material updates, verification, shortlist, Social, Deep-Dive, and handoff counts.
- Added Curator Feedback v1 so repeatedly useful unregistered official sources can be queued for future Curator review without Radar self-approving them.
- Made source verification claim-level: publisher for publication status, release page for software version, repository for runtime/license evidence, data repository for accessions, and official service documentation for API/migration facts.
- Kept Telegram Handoff at version `1.0` for downstream compatibility, but now derive candidates from final Evidence Cards rather than reconstructing facts separately.
- Clarified state ownership: Radar defines story/state logic; the outer orchestrator or host owns optional persistence; runtime state must not be written into the public Skill repository unless explicitly configured by the user.
- Preserved the strict peer-reviewed-only scholarly-literature gate and the existing no-Skill-to-Skill invocation boundary.

## 2.6.0 - 2026-09-04

- Connected Bioinformatics Source Curator as the upstream persistent monitoring roster through a new `references/curator-handoff.md` contract.
- Configured the default registry locator as workbook title `Bioinformatics Source Curator Registry`, tab `10_RADAR_SOURCES`, without hard-coding a private spreadsheet ID.
- Made valid Curator A/B handoff rows the first monitoring pass for scheduled and periodic Radar runs.
- Preserved strict ownership boundaries: Curator approval is source-level trust; Radar still performs item-level peer-review, evidence, deduplication, and importance checks.
- Kept built-in watchlists as coverage-gap and resilience fallback so an incomplete Curator bootstrap cannot collapse Radar coverage.
- Allowed one-off official primary sources for event verification without silently promoting them into persistent curated state.
- Added a feedback rule so repeatedly useful unregistered official sources become candidates for future Curator review.
- Updated source policy, search playbook, watchlists, orchestration, UI default prompt, and release gate for the new upstream handoff.
- Preserved the peer-reviewed-only scholarly-literature policy from v2.4.0 and v2.5.0.

## 2.5.0 - 2026-09-02

- Refactored `SKILL.md` into a lean control plane aligned with current ChatGPT Skill progressive-disclosure patterns.
- Removed repeated report-section schemas and detailed checks from `SKILL.md` when the authoritative rule already exists in a focused file under `references/`.
- Added explicit progressive reference routing for discovery, eligibility, ranking, editorial treatment, output construction, and downstream orchestration.
- Preserved the v2.4.0 peer-reviewed-only scholarly-literature gate without weakening any eligibility rule.
- Added a compact release gate that points to the authoritative peer-review and output contracts instead of duplicating them.
- Clarified source sufficiency: primary sources are the final factual authority for central claims and official changes when available.
- Clarified that low-news days are valid and must not be filled with weak or ineligible material.
- Added `default_prompt` to `agents/openai.yaml` for a complete UI metadata contract.
- Updated README to distinguish runtime Skill files from repository documentation and development material.

## 2.4.0 - 2026-08-30

- Made the scholarly-literature stream strictly peer-reviewed-only.
- Added `references/peer-review-policy.md` as a mandatory eligibility gate before scoring, tone selection, drafting, Social Candidate selection, Signals, Deep Dives, Watchlist inclusion, Benchmark Claims, and Telegram Handoff construction.
- Excluded preprint-only records, submitted manuscripts, working papers, conference abstracts, and scholarly records with uncertain peer-review status from all user-visible Radar output.
- Kept preprint services available only for identity resolution and preprint-to-journal publication linkage.
- Added explicit handling for preprint-to-peer-reviewed transitions: use the journal version as the factual authority and deduplicate the preprint.
- Clarified that a DOI alone does not prove peer review.
- Preserved official software, database, dataset, infrastructure, security, and service-change events as eligible non-literature sources under their own verification rules.
- Added an eligibility gate to scoring so excluded papers receive no technical or social score and cannot be restored by novelty, urgency, or public interest.
- Replaced the user-visible `Preprint` report section with `Peer-review status control`, which reports compliance without exposing excluded paper titles or claims.
- Prevented non-peer-reviewed literature from supporting Signal of the Day, Social Candidates, Deep-Dive Candidates, Watchlist, Benchmark Claims, or Telegram Handoff v1.
- Updated Telegram Handoff v1 with `peer_review_verified` for scholarly candidates and made the downstream Editor unable to restore excluded literature.
- Removed `PREPRINT_CAUTION` from active tone routing because non-peer-reviewed scholarly literature is now filtered before the tone engine.
- Updated README and orchestration rules for protocol 2.4.0.

## 2.3.0 - 2026-08-28

- Added `references/editorial-tone-engine.md` as the adaptive editorial routing system for Radar.
- Defined `SCIENTIFIC_INTELLIGENCE` as the stable Radar publication identity while allowing per-item operational tones.
- Added primary tones: `TECHNICAL_ALERT`, `NEUTRAL_TECHNICAL`, `ANALYTICAL_NEWS`, `PAPER_SPOTLIGHT`, `EVIDENCE_CRITICAL`, `SCIENTIFIC_INTELLIGENCE`, `EXPLAINER`, and `CURIOSITY_BRIDGE`.
- Added evidence/context modifiers including `PREPRINT_CAUTION`, `AUTHOR_REPORTED`, `INDEPENDENTLY_VERIFIED`, `CLINICAL_CAUTION`, `CAUSALITY_CAUTION`, `WORKFLOW_IMPACT`, `BREAKING_URGENCY`, `LOW_EVIDENCE`, and `HIGH_OVERHYPE_RISK`.
- Changed the drafting order to `classify information -> verify evidence -> select tone -> write` so tone cannot reshape the evidence boundary.
- Added deterministic arbitration rules for conflicts between urgency, evidence risk, trend synthesis, paper coverage, explainer needs, and routine technical updates.
- Added section-level tone defaults across the Executive Brief, Critical Alerts, Main Radar, Tool/Database/Dataset sections, Papers, Preprints, GitHub health, Reproducibility, Benchmark Claims, Signal of the Day, Social Candidates, Deep Dives, Watchlist, and Radar Statistics.
- Made `CURIOSITY_BRIDGE` a Social Candidate presentation layer that inherits all evidence-risk modifiers rather than overriding them.
- Extended Telegram Handoff v1 with `radar_primary_tone`, `radar_tone_modifiers`, and `recommended_editorial_tone` so downstream narrative style can change without weakening scientific guardrails.
- Added final tone quality gates to prevent curiosity framing, trend language, or stylistic compression from strengthening causality, clinical readiness, benchmark superiority, or certainty.
- Updated README and the output contract for Radar protocol 2.3.0.

## 2.2.1 - 2026-08-24

- Fixed the Skill-to-Skill orchestration bug that could report Bioinformatics Telegram Editor as unavailable.
- Removed all direct downstream Skill/tool invocation from Radar.
- Made the outer orchestrator the sole owner of Telegram Handoff transfer and Editor execution.
- Added GitHub-direct Editor execution as the preferred orchestrated mode when the Editor Skill is not installed.
- Added explicit graceful behavior so Radar never fails because a downstream Editor is absent.
- Added `references/orchestration.md` to document runtime ownership and fallback behavior.

## 2.2.0 - 2026-08-24

- Added Telegram Handoff v1 as a structured downstream contract.
- Added stable candidate IDs, evidence status, exact-fact preservation, limitations, and `do_not_say_fa` guardrails.
- Added direct handoff behavior for Bioinformatics Telegram Editor in chained or scheduled workflows.
- Kept raw handoff JSON internal by default so the human Radar report remains readable.

## 2.1.1 - 2026-08-24

- Made Persian the mandatory default language for the complete Radar output, regardless of prompt language.
- Translated the report contract headings and narrative fields into Persian.
- Kept official tool names, database names, package names, version strings, identifiers, and precision-sensitive technical terms in English.
- Preserved machine-readable status labels while requiring Persian explanation where useful.

## 2.1.0 - 2026-08-24

- Expanded the radar from a short digest to a 20-35 item target when news volume supports it.
- Added Critical Alerts for workflow-breaking infrastructure changes.
- Added dedicated Tool, Database, Dataset, Paper, Preprint, GitHub, Reproducibility, and Benchmark sections.
- Added 1-3 evidence-backed Signal of the Day items.
- Added 3-5 Social Candidates with public-facing headlines, hooks, format suggestions, social scoring, and overhype risk.
- Added exactly three Deep-Dive Candidates when enough material exists.
- Added measurable Radar Statistics and prohibited invented scan counts.
- Added source hierarchy, search playbook, watchlists, and scoring rules.

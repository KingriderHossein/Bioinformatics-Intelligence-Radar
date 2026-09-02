# Changelog

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

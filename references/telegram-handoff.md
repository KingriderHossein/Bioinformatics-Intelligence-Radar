# Telegram Handoff v1

Build this handoff only after Radar evidence gates **and** the Newsroom Release Gate pass, and only when an outer orchestrator includes a Telegram editorial stage.

Handoff version remains `1.0` for compatibility with Bioinformatics Telegram Editor. Radar 3.0 changes the internal producer: candidates now inherit factual boundaries from Evidence Cards and editorial framing from Story Cards.

The handoff is internal machine-readable state. Do not expose raw JSON unless the user explicitly asks.

Read `peer-review-policy.md`, `evidence-card.md`, `newsroom-engine.md`, and `scoring.md` before constructing it.

## Eligibility invariant

Telegram Handoff v1 must contain no non-peer-reviewed scholarly paper.

For every scholarly candidate:

- peer review was positively verified by Radar;
- the peer-reviewed journal/proceedings record is factual authority;
- a preprint-only or uncertain-review-status record is absent;
- preprint-to-journal duplicates resolve to the peer-reviewed version.

Verified software releases, official database updates, datasets, infrastructure/security/service changes, corrections, and retractions remain eligible under their official-source rules.

## Top-level object

Use:

- `handoff_version`: `1.0`
- `radar_version`: current Radar protocol version
- `radar_date`: ISO date
- `reporting_window`: object with `start` and `end`
- `candidate_count`: exact candidate count
- `candidates`: newsroom-selected candidate objects

Do not force 3-5 candidates on a quiet day. `candidate_count` must equal the array length.

## Candidate object

Keep the established v1 compatibility fields:

- `id`: `BIR-YYYYMMDD-NN`
- `topic`
- `scientific_title`
- `suggested_social_title_fa`
- `hook_fa`
- `summary_fa`
- `why_it_matters_fa`
- `content_type`: `peer_reviewed`, `software_release`, `database_update`, `dataset`, `service_change`, or `other`
- `publication_status`
- `peer_review_verified`: `true` for scholarly candidates; omit/null for non-literature events
- `priority`: operational urgency when applicable
- `social_score`: compatibility presentation score from `scoring.md`
- `overhype_risk`
- `claim_status`
- `key_facts`
- `limitations_fa`
- `do_not_say_fa`
- `source`: `primary_name`, `primary_url` when available, and DOI/PMID/release/accession when available
- `radar_primary_tone`
- `radar_tone_modifiers`
- `recommended_editorial_tone`

Add these Radar 3.0 newsroom fields when available:

- `news_value_score`
- `news_statement_fa`
- `selected_angle_type`
- `selected_angle_fa`
- `headline_options_fa`
- `recommended_post_type`: `FLASH`, `STANDARD`, or `DEEP`
- `recommended_formats`
- `article_worthy`
- `visual_worthy`
- `story_key`

Recommended evidence fields remain:

- `benchmark_claims`
- `repository`
- `tone_rationale_fa`

Additive newsroom fields must not remove or rename fields expected by existing Telegram Handoff v1 consumers.

## Derivation rules

### From Evidence Card

Populate:

- identity/date/publication status;
- exact numbers and units;
- claim/evidence status;
- benchmark attribution;
- limitations;
- `do_not_say_fa`;
- primary source;
- evidence/tone modifiers.

If another field conflicts with the Evidence Card, the Evidence Card wins.

### From Story Card

Populate:

- newsroom title/hook/summary;
- `news_statement_fa`;
- News Value Score;
- selected angle;
- headline options;
- recommended format/post type;
- article/visual suitability.

If Story Card framing strengthens the evidence, fix the Story Card before handoff.

## Editorial transfer rules

Radar owns:

- scientific eligibility;
- factual authority;
- canonical story identity;
- Evidence Card;
- News Value selection;
- Story Card angle boundaries;
- non-negotiable limitations and `do_not_say_fa`.

Telegram Editor owns:

- final Telegram narrative;
- paragraph rhythm;
- surface headline choice;
- emoji/formatting;
- final FLASH/STANDARD/DEEP execution within the handed-off boundaries.

The Editor may choose another evidence-safe headline or narrative structure, but must not violate Evidence Card facts, `limitations_fa`, `do_not_say_fa`, publication status, or claim attribution.

## Evidence rules

- Preserve exact publication status.
- Preserve exact numbers, denominators, units, versions, dates, and benchmark context when material.
- Preserve `AUTHOR_REPORTED`, `INDEPENDENTLY_VERIFIED`, observational, preclinical, computational, or company/partner-reported status when relevant.
- Prediction/inference must not become measurement.
- Association must not become causation.
- Research performance must not become clinical readiness.
- A model must not be described as understanding, deciding, discovering, or replacing experts unless the evidence supports that exact claim.
- Do not invent URLs.

## Quality gate before handoff

For every scholarly candidate require:

- resolved identity;
- verified peer review;
- resolved primary peer-reviewed source;
- consistent publication status;
- final Evidence Card consistency;
- final Story Card consistency.

For every candidate require:

- the Story Gate passed;
- candidate count will match array length;
- News Value justified editorial selection;
- exact facts match Evidence Card;
- title/angle match Story Card without overreach;
- material limitations and `do_not_say_fa` are present;
- no same-story/no-material-change duplicate is handed off as new news.

## Downstream behavior

Radar never invokes, discovers, or checks availability of Bioinformatics Telegram Editor. Radar constructs the handoff only.

The outer orchestrator may load Telegram Editor from an installed Skill or directly from its canonical GitHub repository and apply it to the in-context handoff.

If downstream editing is unavailable, Radar still completes successfully and must not emit a missing-Skill failure.

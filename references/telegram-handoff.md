# Telegram Handoff v1

Build this handoff only after Radar quality gates pass and only when an outer orchestrator requests, schedules, or otherwise includes a Telegram editorial step in the same workflow.

Handoff version remains `1.0` for compatibility with Bioinformatics Telegram Editor. Radar 2.7.x changes how the handoff is produced internally: each candidate must be derived from its final Evidence Card rather than reconstructed independently.

The handoff is an internal machine-readable contract. Do not expose raw JSON unless the user explicitly asks for it.

Read `peer-review-policy.md`, `evidence-card.md`, and `scoring.md` before constructing it.

## Eligibility invariant

Telegram Handoff v1 must contain no non-peer-reviewed scholarly paper.

For every scholarly candidate:

- peer review must already be positively verified by Radar;
- the peer-reviewed journal/proceedings record must be the factual authority;
- a preprint-only or uncertain-review-status record must not enter the handoff;
- a preprint-to-journal duplicate must resolve to the peer-reviewed version.

Software releases, official database updates, datasets, infrastructure changes, security notices, and service changes remain eligible when verified from the appropriate official source.

## Top-level object

Use:

- `handoff_version`: `1.0`
- `radar_version`: current Radar protocol version
- `radar_date`: ISO date
- `reporting_window`: object with `start` and `end`
- `candidate_count`: exact candidate count
- `candidates`: eligible Social Candidate objects

Do not force `candidate_count` to 3-5 on low-news days. It must equal the actual selected array length.

## Candidate object

For each selected candidate include:

- `id`: stable daily candidate ID in the form `BIR-YYYYMMDD-NN`
- `topic`
- `scientific_title`
- `suggested_social_title_fa`
- `hook_fa`
- `summary_fa`
- `why_it_matters_fa`
- `content_type`: `peer_reviewed`, `software_release`, `database_update`, `dataset`, `service_change`, or `other`
- `publication_status`
- `peer_review_verified`: `true` for scholarly paper candidates; `null` or omit for non-literature events
- `priority`
- `social_score`
- `overhype_risk`
- `claim_status`
- `key_facts`
- `limitations_fa`
- `do_not_say_fa`
- `source`: `primary_name`, `primary_url` when available, and DOI/PMID/release tag or another durable identifier when available
- `radar_primary_tone`
- `radar_tone_modifiers`
- `recommended_editorial_tone`

Recommended fields:

- `benchmark_claims`
- `repository`
- `recommended_post_type`: `FLASH`, `STANDARD`, or `DEEP`
- `recommended_formats`
- `editorial_angle_fa`
- `tone_rationale_fa`
- `editorial_priority_score`: Radar's risk-adjusted ranking score; downstream may use it for ordering but must not treat it as scientific evidence
- `story_key`: internal canonical story identity when useful for traceability

Extra recommended fields must not remove or rename fields expected by Telegram Handoff v1 consumers.

## Evidence Card derivation

Populate the handoff from the final Evidence Card as follows:

- identity/date/publication fields <- Evidence Card identity and eligibility
- `key_facts` <- exact verified facts only
- `claim_status` and `benchmark_claims` <- claim/evidence state without strengthening
- `limitations_fa` <- risk boundary and main limitations
- `do_not_say_fa` <- unsupported stronger interpretations
- source <- canonical primary source
- tone modifiers <- inherited Evidence Card modifiers
- social/editorial scores <- scoring output, without recomputation by the Editor

If the handoff wording conflicts with the Evidence Card, the Evidence Card wins and the handoff must be corrected before transfer.

## Tone transfer rules

Radar owns evidence classification and literature eligibility. The downstream Editor owns final narrative style.

- Preserve every evidence-risk modifier even when the recommended editorial tone is conversational or curiosity-driven.
- `CURIOSITY_BRIDGE` is a presentation layer, not permission to weaken qualifiers.
- An author-reported benchmark must remain attributed unless independent verification was actually found.
- Clinical, causal, preclinical, prediction-versus-measurement, and AI-capability caution must survive all downstream tone changes.
- For `TECHNICAL_ALERT` items, recommend a direct alert treatment when timing or workflow impact is central.
- The Editor may change narrative structure but must not violate `radar_tone_modifiers`, `limitations_fa`, `key_facts`, or `do_not_say_fa`.
- The Editor cannot restore a scholarly paper excluded by the Radar peer-review gate.

## Evidence rules

- Preserve exact publication status.
- Preserve exact numbers, denominators, units, versions, dates, and benchmark context.
- Preserve whether evidence is author-reported, partner/company-reported, independently verified, preclinical, observational, or computational when material.
- Put important uncertainty in `limitations_fa`.
- Populate `do_not_say_fa` with likely overclaims, especially for AI, clinical implications, causality, and large benchmark claims.
- Use the primary source as factual authority even if the suggested social title is more attractive.
- Do not invent a URL when unavailable.

## Quality gate before handoff

For every scholarly candidate require:

- identity resolved;
- peer-review status verified;
- primary peer-reviewed source resolved;
- publication status consistent;
- no preprint-only fallback;
- final Evidence Card passed consistency gate.

For every candidate require:

- `candidate_count` will match final array length;
- exact facts match the Evidence Card;
- `AUTHOR_REPORTED` or equivalent attribution survives;
- overhype risk and `do_not_say_fa` are present when material;
- no cross-run duplicate is handed off as a new story unless a material change was verified.

## Downstream behavior

Radar never invokes, discovers, or checks availability of Bioinformatics Telegram Editor. Radar only constructs the handoff.

The outer orchestrator may apply Telegram Editor instructions from an installed Skill or by loading its canonical GitHub repository directly. The Editor owns narrative and Telegram formatting; Radar owns evidence selection, peer-review eligibility, verification, canonical story state, and the non-negotiable evidence modifiers that constrain tone.

If no downstream editorial step is available, Radar must still complete successfully and must not emit a missing-tool or missing-Skill error.

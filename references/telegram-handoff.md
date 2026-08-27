# Telegram Handoff v1

Build this handoff after Social Candidates when an outer orchestrator requests, schedules, or otherwise includes a Telegram editorial step in the same workflow.

The handoff is an internal machine-readable contract. Do not expose the raw JSON in the user-facing Radar report unless the user explicitly asks for it.

## Top-level object

Use:

- `handoff_version`: `1.0`
- `radar_version`: current Radar protocol version
- `radar_date`: ISO date
- `reporting_window`: object with `start` and `end`
- `candidate_count`: exact candidate count
- `candidates`: the selected Social Candidate objects

## Candidate object

For each selected candidate include:

- `id`: stable ID in the form `BIR-YYYYMMDD-NN`
- `topic`
- `scientific_title`
- `suggested_social_title_fa`
- `hook_fa`
- `summary_fa`
- `why_it_matters_fa`
- `content_type`: `peer_reviewed`, `preprint`, `software_release`, `database_update`, `dataset`, `service_change`, or `other`
- `publication_status`
- `priority`
- `social_score`
- `overhype_risk`
- `claim_status`: for example `peer-reviewed finding`, `author-reported benchmark`, `independent experimental challenge`, or `official service change`
- `key_facts`: factual statements with exact numbers and qualifiers preserved
- `limitations_fa`
- `do_not_say_fa`: tempting but unsupported claims the editor must avoid
- `source`: `primary_name`, `primary_url` when available, and DOI/PMID/release tag or other durable identifier when available
- `radar_primary_tone`: the primary tone selected by `references/editorial-tone-engine.md` for the verified source item before Social Candidate reframing
- `radar_tone_modifiers`: zero to three inherited evidence/context modifiers such as `PREPRINT_CAUTION`, `AUTHOR_REPORTED`, `CLINICAL_CAUTION`, or `HIGH_OVERHYPE_RISK`
- `recommended_editorial_tone`: downstream recommendation such as `science_journalism`, `conversational_scientific`, `explainer`, `curiosity_driven`, or `evidence_critical`

Recommended fields:

- `benchmark_claims`: claim, comparator, dataset/hardware context, independent verification state
- `repository`: only verified repository metadata
- `recommended_post_type`: `FLASH`, `STANDARD`, or `DEEP`
- `recommended_formats`
- `editorial_angle_fa`
- `tone_rationale_fa`: one short explanation of why the downstream tone is appropriate

## Tone transfer rules

Radar owns evidence classification. The downstream Editor owns final narrative style.

- Preserve every evidence-risk modifier even when `recommended_editorial_tone` is more conversational or curiosity-driven.
- `CURIOSITY_BRIDGE` is a Radar Social Candidate presentation layer, not permission to weaken qualifiers.
- A preprint must still be presented as non-peer-reviewed downstream.
- An author-reported benchmark must remain attributed unless independent verification was actually found.
- Clinical or causal caution must survive all downstream tone changes.
- For `TECHNICAL_ALERT` items, recommend a direct news/alert treatment rather than a playful or curiosity-first Telegram angle when timing or workflow impact is central.
- The Editor may choose a different surface tone, but it must not violate `radar_tone_modifiers`, `limitations_fa`, or `do_not_say_fa`.

## Evidence rules

- Preserve exact publication status.
- Preserve exact numbers and benchmark context.
- Preserve whether evidence is author-reported or independently verified.
- Put important uncertainty in `limitations_fa`.
- Populate `do_not_say_fa` with likely overclaims, especially for preprints, AI, clinical implications, and large benchmark claims.
- Use the primary source as the factual authority even if the suggested social title is more attractive.
- Do not invent a URL when it is unavailable.

## Downstream behavior

Radar never invokes, discovers, or checks availability of Bioinformatics Telegram Editor. Radar only constructs the handoff. The outer orchestrator owns the transfer and downstream execution.

The orchestrator may apply Bioinformatics Telegram Editor instructions either from an installed Skill or by loading the canonical GitHub repository instructions directly. The editor owns narrative and Telegram formatting; Radar owns evidence selection, verification, and the non-negotiable evidence modifiers that constrain tone.

If no downstream editorial step is available, Radar must still complete successfully and must not emit a missing-tool or missing-Skill error.

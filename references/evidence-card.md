# Evidence Card v1

Use this internal contract after identity and eligibility are resolved and before ranking, deep verification, report writing, Signal construction, or Telegram handoff.

The Evidence Card is the single internal source of truth for one canonical story. Do not expose the raw card unless the user explicitly asks for diagnostics or structured internals.

## Core invariant

Create one Evidence Card per canonical eligible story. All later Radar surfaces must derive factual claims, qualifiers, risk boundaries, and exact numbers from that card rather than re-researching or rewriting the item independently.

If later verification changes a fact, update the Evidence Card first and then regenerate downstream wording from it.

## Identity

Record when available:

- `story_key`: stable internal key derived from content type plus a durable canonical identifier
- `content_type`: `peer_reviewed`, `software_release`, `database_update`, `dataset`, `service_change`, `security_notice`, or `other`
- `scientific_title`
- `canonical_id`: DOI, PMID, release tag, database release ID, dataset accession, or another durable identifier
- `canonical_source_name`
- `canonical_source_url`
- `curator_target_id`: preserve when the discovery came from a Curator row

Prefer durable identifiers in this order when applicable: DOI -> PMID -> official release/database/dataset identifier -> canonical official event URL.

## Dates

Keep dates separate. Do not collapse them into one generic date.

- `event_date`: when the change/event became effective or occurred
- `publication_date`: publisher publication date for a paper
- `observed_date`: when Radar verified the item
- `effective_date`: for migrations/deprecations when distinct from announcement date

## Eligibility

Record:

- `publication_status`
- `peer_review_verified`: `true` for eligible scholarly literature; omit or use `null` for non-literature events
- `eligibility_state`: `ELIGIBLE` or an exclusion state
- `eligibility_basis`: concise reason and source class

Do not create a normal Evidence Card for a scholarly record that fails the peer-review gate. For identity-resolution notes about an excluded preprint, keep only minimal transient notes needed to resolve a later peer-reviewed version.

## Claims

Record only claims supported by verified evidence:

- `central_claim`
- `claim_status`: for example `peer-reviewed finding`, `author-reported benchmark`, `independently verified benchmark`, or `official service change`
- `key_facts`: exact numbers, denominators, units, versions, qualifiers, and comparator context
- `benchmark_claims`: claim, comparator, dataset, hardware when material, and independent-verification state
- `validation_type`: internal, external, prospective, experimental, computational, none, or mixed when known

Never upgrade `AUTHOR_REPORTED` to an independent fact during summarization.

## Evidence

Record:

- `primary_source`
- `supporting_sources`: only when they add material evidence
- `independent_verification`: `YES`, `NO`, or `UNKNOWN`
- `evidence_notes`: short notes about conflicts, missing context, or provenance

Use the source closest to the claim. Search snippets and secondary summaries may help discovery but must not become the final authority when a suitable primary source exists.

## Reproducibility

Record only verified fields:

- `code`
- `data`
- `versioned_release_or_archive`
- `license`
- `environment_or_dependencies`
- `container_or_portable_environment`
- `automated_tests`
- `ci`
- `example_or_test_data`
- `benchmark_protocol`

Use `unknown` rather than inferring absence. Let `references/scoring.md` decide whether the verified coverage is enough for a numeric reproducibility score.

## Risk boundary

Record:

- `main_limitation_fa`
- `overhype_risk`: `LOW`, `MEDIUM`, or `HIGH`
- `tone_modifiers`: zero to three evidence/context modifiers
- `do_not_say_fa`: likely but unsupported stronger claims

Use explicit caution fields when relevant:

- clinical readiness
- causality
- AI capability or understanding
- benchmark generalization
- association versus mechanism
- preclinical versus clinical evidence
- prediction versus measurement

These fields are immutable downstream constraints unless new evidence changes the card itself.

## Scores

After eligibility and sufficient verification, record:

- `technical_score`
- `social_score`
- `evidence_risk_penalty`
- `editorial_priority_score`
- `confidence`

Do not score ineligible scholarly literature.

## Downstream derivation

Use the same Evidence Card to derive:

- Executive Brief wording
- Main Radar row
- Paper/Tool/Database/Dataset detail
- Benchmark Claims
- Signal evidence nodes
- Social Candidate
- Deep-Dive Candidate
- Telegram Handoff v1 candidate

Do not independently restate exact numbers from memory when the card already contains them.

## Consistency gate

Before finalizing a story, confirm:

- all visible exact numbers match `key_facts`;
- publication status matches eligibility;
- benchmark attribution matches `claim_status` and `independent_verification`;
- limitations and `do_not_say_fa` survive Social Candidate and Telegram compression;
- event/publication/effective dates are not conflated;
- no downstream surface is stronger than the central claim in the Evidence Card.

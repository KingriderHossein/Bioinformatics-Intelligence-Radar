# Evidence Card v1

Use this internal contract after identity and eligibility are resolved and before Newsroom Story Gate, deep verification, report writing, Signal construction, or Telegram handoff.

The Evidence Card is the factual source of truth for one canonical eligible event. It is **not** the newsroom story itself.

Do not expose raw cards unless the user explicitly asks for diagnostics or structured internals.

## Core invariant

Create one Evidence Card per canonical eligible event.

All downstream factual claims, exact numbers, qualifiers, benchmark attribution, and evidence boundaries must derive from the card.

If later verification changes a fact, update the Evidence Card first, then regenerate the Story Card and downstream wording.

## Identity

Record when available:

- `story_key`: stable internal key derived from content type plus durable canonical identifier
- `content_type`: `peer_reviewed`, `software_release`, `database_update`, `dataset`, `service_change`, `security_notice`, `correction`, `retraction`, or `other`
- `scientific_title`
- `canonical_id`: DOI, PMID, release tag, database release ID, dataset accession, or another durable identifier
- `canonical_source_name`
- `canonical_source_url`
- `curator_target_id`: preserve when discovery came from a Curator row

Prefer durable identifiers when available.

## Dates

Keep distinct:

- `event_date`
- `publication_date`
- `observed_date`
- `effective_date`

Do not collapse announcement, publication, observation, and effective dates into one generic date.

## Eligibility

Record:

- `publication_status`
- `peer_review_verified`: `true` for eligible scholarly literature; omit/null for non-literature events
- `eligibility_state`
- `eligibility_basis`

Do not create a normal Evidence Card for scholarly literature that fails the peer-review gate.

Preprint-only identity notes may exist transiently only to resolve a later peer-reviewed version.

## Claims

Record only verified claims:

- `central_claim`
- `claim_status`: e.g. `peer-reviewed finding`, `author-reported benchmark`, `independently verified benchmark`, `official service change`
- `key_facts`: exact numbers, denominators, units, versions, qualifiers, and comparator context
- `benchmark_claims`: claim, comparator, dataset, hardware when material, independent-verification state
- `validation_type`: internal, external, prospective, experimental, computational, none, or mixed when known

Never upgrade `AUTHOR_REPORTED` to an independent fact during summarization.

## Evidence provenance

Record:

- `primary_source`
- `supporting_sources`: only when they add material evidence
- `independent_verification`: `YES`, `NO`, or `UNKNOWN`
- `evidence_notes`: conflicts, missing context, provenance, or unresolved caveats

Use the source closest to each claim. Publisher, release page, repository, data archive, and official service documentation may each be authoritative for different fields.

Search snippets and secondary summaries are discovery aids, not final authority when an appropriate primary source exists.

## Reproducibility/runtime evidence

Record only what was actually verified:

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

Use `unknown` rather than inferring absence.

These fields are normally backend evidence and should not be forced into user-visible news copy unless they materially affect the story.

## Risk boundary

Record:

- `main_limitation_fa`
- `overhype_risk`: `LOW`, `MEDIUM`, or `HIGH`
- `tone_modifiers`
- `do_not_say_fa`: likely but unsupported stronger interpretations

Explicitly protect relevant boundaries:

- association versus causality;
- prediction/inference versus measurement;
- preclinical versus clinical evidence;
- technical performance versus clinical utility;
- internal versus external validation;
- author-reported versus independently verified benchmark;
- AI capability versus anthropomorphic interpretation;
- narrow benchmark versus general capability.

These constraints survive every downstream transformation unless new evidence changes the card.

## Evidence confidence

Record `confidence` as `HIGH`, `MEDIUM`, or `LOW` only after eligibility.

Confidence describes completeness/consistency of verified evidence. It is not News Value.

Do not use LOW confidence to retain an ineligible scholarly paper.

## Newsroom handoff

After the card is complete enough for editorial triage:

1. pass the card to `newsroom-engine.md`;
2. apply the internal Story Gate;
3. compute News Value only for Story-Gate survivors;
4. create a separate Story Card for selected newsroom stories.

Do not store headline/angle/lead decisions as factual fields in the Evidence Card.

## Consistency gate

Before any story is finalized, confirm:

- visible exact numbers match `key_facts`;
- publication status matches eligibility;
- benchmark attribution matches `claim_status` and `independent_verification`;
- limitations and `do_not_say_fa` survive newsroom compression;
- event/publication/effective dates are not conflated;
- Story Card framing does not strengthen the Evidence Card central claim.

# Radar Run State v1

Use this internal contract for cross-run deduplication, material-change detection, and observed-only run telemetry when prior state is available.

State is helpful but not required. Never fail a Radar run because prior state cannot be loaded. Never invent prior history.

## Ownership

- Radar defines the state schema, story identity rules, material-change logic, and telemetry counters.
- The outer orchestrator or host environment owns persistence and retrieval of state across executions.
- Source Curator does not own Radar story state.
- Telegram Editor does not mutate Radar state.

If state is already present in current execution context, reuse it. If a configured persistent store is available, the outer orchestrator may load it before Radar and save the updated state after Radar quality gates.

## State availability

Use one of:

- `AVAILABLE`: prior ledger was loaded successfully
- `BOOTSTRAP`: no prior ledger exists yet; initialize from the current run
- `UNAVAILABLE`: a prior store was expected but could not be read
- `NOT_CONFIGURED`: no persistent state store is configured

When state is `UNAVAILABLE` or `NOT_CONFIGURED`, perform full within-run deduplication and continue normally. Do not claim cross-run suppression was performed.

## Story ledger

For each reported or tracked eligible story, store when available:

- `story_key`
- `content_type`
- `canonical_id`
- `scientific_title`
- `first_seen`
- `last_seen`
- `last_reported`
- `status`
- `last_event_fingerprint`
- `last_priority`
- `last_social_score`
- `last_primary_source`

Recommended `status` values:

- `NEW`
- `ACTIVE`
- `SUPPRESSED_NO_CHANGE`
- `UPDATED`
- `PUBLICATION_TRANSITION`
- `RELEASE_TRANSITION`
- `CORRECTION_OR_RETRACTION`
- `CLOSED`

## Stable story identity

Prefer a durable canonical identifier rather than title text.

Suggested identity keys:

- scholarly article: DOI, otherwise PMID
- software release: repository/project + release tag
- database/infrastructure event: official service + event identifier or canonical event URL
- dataset: repository + accession/version
- security event: official advisory identifier

A title change alone must not create a new story when the canonical identity is unchanged.

## Event fingerprint

Use a compact fingerprint of the material state of the story. It does not need to be cryptographic.

Include fields relevant to the event, such as:

- publication status or version
- release tag
- effective date
- API/schema state
- benchmark revision
- independent validation state
- code/data availability state
- correction/retraction state
- major workflow integration

Do not include purely editorial wording.

## Material-change rule

Treat an existing story as a reportable update only when at least one material change is verified.

Material changes include:

- preprint or accepted manuscript becomes a verified peer-reviewed journal publication;
- prerelease becomes stable release;
- new stable release or materially changed release notes;
- new independent benchmark or validation;
- new code/data release that materially changes reproducibility or usability;
- new API/schema/authentication/deprecation/effective-date change;
- new reference/annotation/database release that can change downstream results;
- correction, expression of concern, or retraction;
- new workflow integration with practical impact;
- newly verified clinical or experimental evidence that changes the evidence boundary.

Non-material changes normally include:

- secondary media coverage of the same event;
- a copied blog post;
- citation-count growth;
- minor wording changes;
- repository activity with no user-facing or evidence-relevant change;
- the same journal article appearing in another index.

## Cross-run action

Apply:

- same story + same fingerprint -> suppress from normal news sections unless explicitly requested for continuity;
- same story + material change -> report as `UPDATE` and state what changed;
- preprint -> verified peer-reviewed publication -> `PUBLICATION_TRANSITION` and use the journal version as authority;
- prerelease -> stable -> `RELEASE_TRANSITION`;
- correction/retraction -> promote based on impact, even if the original story is old.

Do not suppress a critical infrastructure change merely because the parent service was reported previously; compare the concrete event fingerprint.

## Run telemetry

Initialize observed counters at zero and increment only when the corresponding event is actually processed in the current run.

Recommended counters:

- `discovered_unique`
- `identity_resolved`
- `peer_review_verified`
- `excluded_ineligible_scholarly`
- `official_events_verified`
- `cross_run_suppressed_no_change`
- `material_updates_detected`
- `primary_claims_verified`
- `shortlisted`
- `high_priority`
- `social_selected`
- `deep_dive_selected`
- `handoff_selected`

A counter is reportable only when the execution path actually maintained it. Otherwise report it as not measured rather than reconstructing it after the fact.

## Curator feedback queue

When Radar repeatedly relies on a useful official source that is absent from the current Curator roster, create an internal feedback record:

- `source_name`
- `official_url`
- `source_type`
- `reason_discovered`
- `useful_hit_count_observed`
- `suggested_domain`
- `suggested_monitoring_method`

This queue is advisory. Radar must not self-approve or persist the source into the Curator registry.

## Final state update

After Radar quality gates pass:

1. update `last_seen` for processed stories;
2. update `last_reported` only for stories actually exposed in the Radar report;
3. save the current event fingerprint for reported or materially updated stories;
4. preserve previous history rather than rewriting `first_seen`;
5. pass the updated ledger to the outer orchestrator for persistence when a store exists.

Do not update persistent state for a run that failed before evidence and release gates were completed.

# Radar Run State v1

Use this internal contract for cross-run deduplication, material-change detection, newsroom continuity, and observed-only telemetry when prior state is available.

State is helpful but not required. Never fail a Radar run because prior state cannot be loaded. Never invent prior history.

## Ownership

- Radar defines state schema, story identity, event fingerprints, material-change logic, and telemetry counters.
- The outer orchestrator or host owns persistence/retrieval across executions.
- Source Curator does not own Radar story state.
- Telegram Editor does not mutate Radar state.

If state is already present in current execution context, reuse it. If a persistent store is configured, load before cross-run deduplication and save only after evidence/newsroom gates pass.

## State availability

Use one of:

- `AVAILABLE`: prior ledger loaded successfully
- `BOOTSTRAP`: no prior ledger exists yet
- `UNAVAILABLE`: a prior store was expected but could not be read
- `NOT_CONFIGURED`: no persistent state store configured

When state is `UNAVAILABLE` or `NOT_CONFIGURED`, continue with within-run deduplication. Do not claim cross-run suppression occurred.

## Story ledger

For each tracked eligible canonical event, store when available:

- `story_key`
- `content_type`
- `canonical_id`
- `scientific_title`
- `first_seen`
- `last_seen`
- `last_reported`
- `status`
- `last_event_fingerprint`
- `last_operational_urgency`
- `last_news_value_score`
- `last_selected_angle_type`
- `last_primary_source`

Recommended status values:

- `NEW`
- `ACTIVE`
- `SUPPRESSED_NO_CHANGE`
- `UPDATED`
- `PUBLICATION_TRANSITION`
- `RELEASE_TRANSITION`
- `CORRECTION_OR_RETRACTION`
- `CLOSED`

Do not use editorial wording itself as identity.

## Stable story identity

Prefer durable identifiers:

- scholarly article: DOI, otherwise PMID
- software release: project/repository + release tag
- database/infrastructure event: service + official event identifier/canonical URL
- dataset: repository + accession/version
- security event: official advisory identifier

A title or headline change alone must not create a new story.

## Event fingerprint

Track material state, not copy style.

Possible fields:

- publication status/version
- release tag
- effective date
- API/schema/authentication state
- benchmark revision
- independent-validation state
- code/data availability state
- correction/retraction state
- workflow integration
- evidence boundary changes

Do not include headline, lead, tone, or selected editorial angle in the material fingerprint.

## Material-change rule

Report an existing story as an update only when a real material change is verified.

Examples:

- accepted/preprint state becomes verified peer-reviewed publication;
- prerelease becomes stable;
- new stable release or materially changed release notes;
- new independent benchmark/validation;
- code/data release materially changes usability/reproducibility;
- new API/schema/authentication/deprecation/effective-date change;
- new reference/annotation/database release changes downstream results;
- correction, expression of concern, or retraction;
- new workflow integration with consequence;
- new clinical/experimental evidence changes the evidence boundary.

Normally non-material:

- secondary media coverage;
- copied blog post;
- citation-count growth;
- minor wording change;
- repository activity with no user-facing/evidence-relevant consequence;
- appearance in another index;
- a better headline for the same unchanged event.

## Cross-run action

- same story + same fingerprint -> suppress from normal newsroom output unless continuity was explicitly requested;
- same story + material change -> re-evaluate with the Story Gate and News Value;
- preprint -> verified peer-reviewed publication -> `PUBLICATION_TRANSITION` using journal authority;
- prerelease -> stable -> `RELEASE_TRANSITION`;
- correction/retraction -> re-surface according to consequence.

A material update still needs to be newsworthy unless it is a CRITICAL operational event.

## Run telemetry

Initialize counters only when the execution path can actually maintain them.

Recommended counters:

- `discovered_unique`
- `identity_resolved`
- `peer_review_verified`
- `excluded_ineligible_scholarly`
- `official_events_verified`
- `cross_run_suppressed_no_change`
- `material_updates_detected`
- `primary_claims_verified`
- `story_gate_passed`
- `newsroom_selected`
- `lead_story_selected`
- `signal_selected`
- `deep_dive_selected`
- `handoff_selected`

Report only counters genuinely maintained during the run. Do not reconstruct counts afterward.

## Curator feedback queue

When Radar repeatedly relies on a useful official source absent from the Curator roster, create an internal feedback record:

- `source_name`
- `official_url`
- `source_type`
- `reason_discovered`
- `useful_hit_count_observed`
- `suggested_domain`
- `suggested_monitoring_method`

This queue is advisory. Radar cannot self-approve the source.

## Final state update

After evidence and newsroom gates pass:

1. update `last_seen` for processed tracked events;
2. update `last_reported` only for stories actually shown to the user;
3. store the current material fingerprint for reported/materially updated stories;
4. store News Value/angle only as editorial continuity metadata, never as evidence;
5. preserve original `first_seen` history;
6. pass updated ledger to the outer orchestrator when persistence is supported.

Do not persist state from a failed/incomplete run.

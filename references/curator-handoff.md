# Bioinformatics Source Curator Handoff

Contract version: 1.1.0
Compatible upstream: Bioinformatics Source Curator protocol 1.0.x
Compatible Radar: protocol 3.0.x

Use this reference when a curated source roster is available or when Radar is run with the connected Bioinformatics Source Curator registry.

## Ownership

- Bioinformatics Source Curator owns source discovery, source-level verification, scoring, persistent registry state, monitoring metadata, and export of `10_RADAR_SOURCES`.
- Radar owns item discovery, scholarly peer-review eligibility, event verification, deduplication, Evidence Cards, Newsroom Story Gate, News Value, Story Cards, and reporting.
- The outer orchestrator owns loading the current Curator handoff and passing it into Radar.
- Radar must not invoke the Source Curator Skill from inside Radar.

## Default registry locator

When Google Sheets access is available, resolve:

- workbook title: `Bioinformatics Source Curator Registry`
- handoff tab: `10_RADAR_SOURCES`

Do not hard-code a private spreadsheet ID into this public repository.

If the handoff is already present in current execution context, use it directly and do not re-fetch it.

## Handoff schema

Accept these columns in this logical meaning:

`target_id`, `domain_id`, `source_type`, `source_name`, `official_url`, `source_role`, `monitoring_method`, `monitoring_endpoint`, `priority`, `last_verified`

Expected upstream filter:

- `status = ACTIVE`
- `approved_for_radar = TRUE`
- `priority` is `A` or `B`
- canonical URL and monitoring endpoint verified
- source is not a preprint service under current Curator policy

Radar must still validate handoff shape. Ignore malformed rows and report the real coverage limitation instead of guessing missing fields.

## Runtime behavior

1. Load the handoff before scheduled/periodic monitoring.
2. Treat valid Curator rows as the first persistent monitoring roster.
3. Route each row using `source_role` and `monitoring_method`.
4. Preserve `target_id` in Evidence Cards when practical.
5. Apply Radar item-level eligibility/evidence gates after discovery.
6. Apply `peer-review-policy.md` before any scholarly item reaches newsroom evaluation.
7. Verify non-literature events against the closest official primary source.
8. Do not copy Curator source scores into scientific evidence, News Value, or claim confidence.
9. Curator approval never guarantees that an individual item passes the Story Gate.

## Coverage and fallback

The Curator roster may be incomplete during bootstrap.

When a valid handoff is present:

- use it first;
- use `watchlists.md` for coverage gaps/resilience;
- allow one-off official primary sources for concrete event verification;
- never silently promote an unregistered source into persistent curated state.

When unavailable or empty:

- fall back to `watchlists.md` and normal source policy;
- continue Radar rather than failing;
- record actual state internally when diagnostics are requested.

## Curator feedback v1

When an unregistered official source produces repeated useful verified hits, create an internal feedback record under `run-state.md`:

- `source_name`
- `official_url`
- `source_type`
- `reason_discovered`
- `useful_hit_count_observed`
- `suggested_domain`
- `suggested_monitoring_method`

The record is advisory only.

Radar may use the source for the current event under normal source policy, but must not self-approve it, assign persistent Curator priority, or write approval state into the registry.

## Critical boundary

Curator approval is source-level trust.

Radar eligibility is item-level evidence trust.

Radar Newsroom selection is story-level editorial judgment.

These three layers must remain separate.

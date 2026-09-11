# Bioinformatics Source Curator Handoff

Contract version: 1.1.0
Compatible upstream: Bioinformatics Source Curator protocol 1.0.x
Compatible Radar: protocol 2.7.x

Use this reference when a curated source roster is available or when Radar is run with the connected Bioinformatics Source Curator registry.

## Ownership

- Bioinformatics Source Curator owns source discovery, source-level verification, scoring, persistent registry state, monitoring metadata, and export of `10_RADAR_SOURCES`.
- Radar owns item discovery, scholarly peer-review eligibility, event verification, deduplication, ranking, evidence checks, and reporting.
- The outer orchestrator owns loading the current Curator handoff and passing it into Radar.
- Radar must not invoke the Source Curator Skill from inside Radar.

## Default registry locator

When Google Sheets access is available, the configured workbook is:

- workbook title: `Bioinformatics Source Curator Registry`
- handoff tab: `10_RADAR_SOURCES`

Resolve the workbook by title at runtime. Do not hard-code a private spreadsheet ID into this public repository.

If the handoff is already present in current execution context, use it directly and do not re-fetch it.

## Handoff schema

Accept these columns in this exact logical meaning:

`target_id`, `domain_id`, `source_type`, `source_name`, `official_url`, `source_role`, `monitoring_method`, `monitoring_endpoint`, `priority`, `last_verified`

The Curator is responsible for exporting only records that passed its source-level gate. Expected upstream filter:

- `status = ACTIVE`
- `approved_for_radar = TRUE`
- `priority` is `A` or `B`
- canonical URL and monitoring endpoint are verified
- source is not a preprint service under the current Curator policy

Radar must still validate handoff shape before use. Ignore malformed rows and report the exact coverage limitation instead of guessing missing fields.

## Runtime behavior

1. Load the current handoff before scheduled or periodic monitoring queries.
2. Treat valid Curator rows as the primary persistent monitoring roster.
3. Route each row according to `source_role` and `monitoring_method` rather than treating every URL as a generic page.
4. Preserve `target_id` in Evidence Cards when practical so a discovered item can be traced to the registered source.
5. Apply Radar's own item-level gates after discovery. Source approval never proves that a paper is peer-reviewed or that a software/database change is important.
6. For scholarly items discovered through `INDEX`, `JOURNAL`, or mixed sources, apply `peer-review-policy.md` before scoring or user-visible exposure.
7. For software, database, dataset, infrastructure, and service events, verify the concrete change against the closest primary source.
8. Do not copy Curator source scores into scientific evidence, item ranking, or claim confidence.

## Coverage and fallback

The Curator roster can be incomplete while bootstrapping. Do not collapse Radar coverage to only currently registered domains.

When a valid handoff is present:

- use it first for persistent monitoring;
- use `watchlists.md` only as a coverage-gap and resilience fallback;
- allow one-off official primary sources when needed to verify a discovered event;
- do not silently promote an unregistered source into persistent curated state.

When the handoff is unavailable or empty:

- fall back to `watchlists.md` and normal source policy;
- continue Radar rather than failing;
- record `Curator handoff: UNAVAILABLE` or `EMPTY` in internal run notes when diagnostics are requested.

## Curator feedback v1

Radar may discover useful official sources that are not in the current Curator handoff. When the same unregistered source produces repeated useful verified hits, create an internal feedback record under `run-state.md` with:

- `source_name`
- `official_url`
- `source_type`
- `reason_discovered`
- `useful_hit_count_observed`
- `suggested_domain`
- `suggested_monitoring_method`

This record is advisory only.

Radar may use the source for the current event when it passes normal source policy, but it must not:

- set `approved_for_radar`;
- assign persistent Curator priority;
- write directly into Curator registry state merely because the source was useful;
- claim that a one-off source has been curated.

The outer orchestrator may pass this feedback to a Curator maintenance workflow when explicitly requested or scheduled.

## Critical boundary

Curator approval is source-level trust. Radar eligibility is item-level trust.

A PubMed or journal source can contain ineligible item types. A software repository can contain development changes that are not stable releases. A database update page can contain routine notices with no practical impact. Always verify the concrete item before ranking or writing.

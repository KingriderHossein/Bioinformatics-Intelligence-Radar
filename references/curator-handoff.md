# Bioinformatics Source Curator Handoff

Contract version: 1.0.0
Compatible upstream: Bioinformatics Source Curator protocol 1.0.x
Compatible Radar: protocol 2.6.x

Use this reference when a curated source roster is available or when the Radar is being run with the connected Bioinformatics Source Curator registry.

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

If the handoff is already present in the current execution context, use it directly and do not re-fetch it.

## Handoff schema

Accept these columns in this exact logical meaning:

`target_id`, `domain_id`, `source_type`, `source_name`, `official_url`, `source_role`, `monitoring_method`, `monitoring_endpoint`, `priority`, `last_verified`

The Curator is responsible for exporting only records that passed its source-level gate. Expected upstream filter:

- `status = ACTIVE`
- `approved_for_radar = TRUE`
- `priority` is `A` or `B`
- canonical URL and monitoring endpoint are verified
- source is not a preprint service under the current Curator policy

Radar must still validate the handoff shape before use. Ignore malformed rows and report the exact coverage limitation instead of guessing missing fields.

## Runtime behavior

1. Load the current handoff before constructing scheduled or periodic monitoring queries.
2. Treat valid Curator rows as the primary persistent monitoring roster.
3. Route each row according to `source_role` and `monitoring_method` rather than treating every URL as a generic web page.
4. Preserve `target_id` in internal notes when possible so a discovered item can be traced back to the registered source.
5. Apply Radar's own item-level gates after discovery. Source approval never proves that a specific paper is peer-reviewed or that a specific software/database change is important.
6. For scholarly items discovered through `INDEX`, `JOURNAL`, or mixed sources, apply `peer-review-policy.md` before scoring or user-visible exposure.
7. For software, database, dataset, infrastructure, and service events, verify the concrete change against the closest appropriate primary source.
8. Do not copy Curator source scores into scientific evidence, item ranking, or claim confidence.

## Coverage and fallback

The Curator roster can be incomplete while it is being bootstrapped. Do not collapse Radar coverage to only the currently registered domains.

When a valid handoff is present:

- use it first for persistent monitoring;
- use `watchlists.md` only as a coverage-gap and resilience fallback;
- allow one-off official primary sources when needed to verify a discovered event;
- do not silently promote an unregistered source into the persistent curated roster.

When the handoff is unavailable or empty:

- fall back to `watchlists.md` and the normal source policy;
- continue the Radar rather than failing;
- state `Curator handoff: UNAVAILABLE` or `EMPTY` in internal run notes when such diagnostics are requested.

## New-source feedback rule

If Radar repeatedly needs a useful official source that is not in the Curator handoff, treat it as a candidate for future Source Curator review. Radar may use the source for the current event when it passes the normal source policy, but it must not assign persistent Curator approval itself.

## Critical boundary

Curator approval is source-level trust. Radar eligibility is item-level trust.

A PubMed or journal source can contain item types that are not eligible for the peer-reviewed literature stream. A software repository can contain development changes that are not stable releases. A database update page can contain routine notices with no practical impact. Always verify the concrete item before ranking or writing.
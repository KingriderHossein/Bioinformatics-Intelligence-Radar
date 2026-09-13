# Peer-Review Eligibility Policy

## Scope

Apply this policy to scholarly literature before Evidence Card creation, News Value scoring, Story Card creation, tone selection, newsroom writing, Signal construction, Deep-Dive selection, Watchlist inclusion, or Telegram Handoff construction.

This gate applies to scholarly papers/articles. It does not require software releases, database updates, datasets, infrastructure changes, security notices, corrections, or official service changes to be peer reviewed; verify those through their appropriate primary official sources.

## Mandatory rule

The Bioinformatics Intelligence Radar scholarly-literature stream is peer-reviewed-only.

A scholarly item is eligible only when peer-review status is positively verified.

If peer-review status is absent, ambiguous, pending, or cannot be verified, exclude the item from all user-visible Radar coverage and Telegram Handoff v1.

Do not downgrade an unreviewed paper to Watchlist. Exclusion occurs before News Value or editorial evaluation.

## Eligible literature

Allow when one of these is positively verified:

- final article in a peer-reviewed journal;
- accepted manuscript, version of record, early-view, online-first, or ahead-of-print article with verified acceptance/publication in a peer-reviewed journal;
- peer-reviewed review, systematic review, meta-analysis, methods paper, resource paper, perspective, or related article type;
- conference full paper/proceedings item only when peer review of that full scholarly item is verified.

Do not infer peer review from journal/conference prestige or DOI existence.

## Ineligible literature

Exclude:

- bioRxiv, medRxiv, arXiv, Research Square, SSRN, or other preprint-only records;
- submitted manuscripts, working papers, manuscripts under review, or author manuscripts without verified journal acceptance;
- conference abstracts, posters, or unpublished proceedings without verified peer review of a full paper;
- institutional/publisher press releases describing research without a verified peer-reviewed article;
- records with unknown or conflicting publication status.

## Preprint-to-publication relationship

Preprint services may be used only for identity resolution and publication-status recovery.

If a later peer-reviewed publication exists:

1. treat the peer-reviewed publication as the eligible record;
2. deduplicate preprint and journal version as one canonical scientific event;
3. use the journal article as factual authority;
4. do not list the preprint separately;
5. mention the earlier preprint only when the transition itself is materially relevant.

If no peer-reviewed version can be verified, exclude the record.

## Verification hierarchy

Verify peer-review eligibility in this order:

1. publisher article page showing journal publication/acceptance;
2. PubMed or Europe PMC journal record linked to the article;
3. Crossref metadata consistent with journal publication plus publisher confirmation when needed;
4. official journal documentation when status remains ambiguous.

A DOI alone does not prove peer review.

## Downstream invariants

After this gate:

- no non-peer-reviewed paper may become a Story Card;
- `خبر اول` and `ارزش دنبال‌کردن` contain no non-peer-reviewed scholarly item;
- Signal of the Day cannot use non-peer-reviewed literature as supporting evidence;
- editorial selections contain no non-peer-reviewed paper;
- Deep-Dive suggestions contain no non-peer-reviewed paper;
- Watchlist must not name or summarize non-peer-reviewed papers;
- Telegram Handoff v1 contains no non-peer-reviewed scholarly candidate.

No News Value, social score, novelty, urgency, audience interest, or editorial angle can override this gate.

## Reporting excluded records

Do not expose titles or claims from excluded non-peer-reviewed literature in the normal Newsroom Radar.

If an exact count was genuinely maintained during the run, compact telemetry may report:

`Non-peer-reviewed literature excluded: N`

Do not estimate or reconstruct the count after the fact.

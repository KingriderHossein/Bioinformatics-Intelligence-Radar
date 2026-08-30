# Peer-Review Eligibility Policy

## Scope

Apply this policy to scholarly literature items before scoring, tone selection, report drafting, Social Candidate selection, Deep-Dive selection, Signal construction, Watchlist inclusion, or Telegram Handoff construction.

This gate applies to papers and scholarly articles. It does not require software releases, database updates, datasets, infrastructure changes, security notices, or official service changes to be peer reviewed; verify those against their appropriate primary official sources.

## Mandatory rule

The Bioinformatics Intelligence Radar is peer-reviewed-literature-only.

A scholarly literature item is eligible only when peer-review status is positively verified.

If peer-review status is absent, ambiguous, pending, or cannot be verified, exclude the item from every user-visible Radar section and from Telegram Handoff v1.

Do not downgrade an unreviewed paper to `WATCH`. Exclusion happens before scoring.

## Eligible literature

Allow a scholarly literature item when one of these conditions is verified:

- A final article in a peer-reviewed journal.
- An accepted manuscript, version of record, early-view, online-first, or ahead-of-print article when acceptance/publication in a peer-reviewed journal is verified from the publisher, PubMed, or Europe PMC.
- A peer-reviewed review, systematic review, meta-analysis, methods paper, resource paper, perspective, or other article type when its journal publication status is verified.

For conference literature, include only when the full paper/proceedings item is verified as peer reviewed. Do not infer peer review from conference prestige.

## Ineligible literature

Exclude:

- bioRxiv, medRxiv, arXiv, Research Square, SSRN, or other preprint-only records.
- Submitted manuscripts, working papers, manuscripts under review, or author manuscripts without verified journal acceptance.
- Conference abstracts, posters, or unpublished proceedings when peer review of a full scholarly paper cannot be verified.
- Institutional or publisher press releases that describe research without a verified peer-reviewed article.
- Records with `publication_status = unknown` or conflicting publication metadata.

## Preprint-to-publication relationship

Preprint services may be used only for identity resolution and publication-status recovery.

If a preprint has a later peer-reviewed publication:

1. Treat the peer-reviewed publication as the eligible record.
2. Deduplicate the preprint and journal article as one scientific story.
3. Use the journal article as the factual authority.
4. Do not list the preprint separately.
5. Mention the prior preprint only when the version relationship itself is materially relevant.

If no peer-reviewed version can be verified, exclude the record.

## Verification hierarchy

Verify peer-review eligibility using, in order:

1. Publisher article page showing journal publication/acceptance.
2. PubMed or Europe PMC journal record linked to the article.
3. Crossref metadata consistent with a journal article plus publisher confirmation when needed.
4. Official journal documentation when article status is otherwise ambiguous.

A DOI alone does not prove peer review. A preprint DOI is not eligible merely because it resolves through Crossref.

## Downstream invariants

After this gate:

- `Main Radar` contains no non-peer-reviewed paper.
- `Executive Brief` contains no non-peer-reviewed paper.
- `Signal of the Day` cannot use a non-peer-reviewed paper as supporting evidence.
- `Social Candidates` contain no non-peer-reviewed paper.
- `Deep-Dive Candidates` contain no non-peer-reviewed paper.
- `Watchlist` must not name or summarize non-peer-reviewed papers.
- `Telegram Handoff v1` contains no non-peer-reviewed paper candidate.

No technical score, social score, novelty, urgency, public interest, or editorial tone can override this gate.

## Reporting excluded records

Do not expose titles or claims from excluded non-peer-reviewed literature in the normal Radar report.

If the run provides an exact measurable count, Radar Statistics may report only:

`Non-peer-reviewed literature excluded: N`

Do not estimate this count.

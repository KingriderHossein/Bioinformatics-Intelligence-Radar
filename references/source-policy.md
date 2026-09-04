# Source Policy

Read `curator-handoff.md` when a Bioinformatics Source Curator roster is available. Read `peer-review-policy.md` before evaluating scholarly literature.

## Curated monitoring roster

For scheduled or periodic monitoring, valid rows from the Source Curator handoff are the primary persistent source roster.

This changes **where Radar looks first**, not **what Radar is allowed to claim**.

- Curator approval is source-level trust only.
- Radar still applies item-level peer-review, identity, evidence, deduplication, and importance gates.
- A source score or priority from Curator is monitoring metadata, not scientific evidence.
- Radar may use an official source outside the roster for one-off discovery or verification when needed.
- Radar must not silently promote that source into the persistent roster. Repeatedly useful unregistered sources should be treated as candidates for future Curator review.
- When the roster is incomplete, use `watchlists.md` as a coverage-gap and resilience fallback.

## Source hierarchy

Use primary sources first.

### Peer-reviewed literature
1. Publisher article page or journal version of record
2. PubMed/Europe PMC journal record linked to the article
3. Author repository or data repository for code/data support
4. Institutional press release only for context

A scholarly article is report-eligible only after peer-review status is positively verified under `peer-review-policy.md`.

### Preprint services

bioRxiv, medRxiv, arXiv, Research Square, and similar services are not eligible literature sources for the user-visible Radar.

Use them only for:

- identity resolution,
- preprint-to-journal version linkage,
- checking whether a later peer-reviewed publication exists.

If no peer-reviewed version can be verified, exclude the scholarly item before scoring.

### Software
1. Official GitHub/GitLab release page or project release notes
2. Official documentation
3. Package registry or Bioconductor release page
4. Issue tracker when a specific bug/change is being verified

### Databases and infrastructure
1. NCBI, EMBL-EBI, Ensembl, UniProt, PDB, Bioconductor, GDC, gnomAD, or other official service page
2. Official release notes, status page, documentation, or API docs
3. Institutional news post when it links to the underlying service change

### Datasets
1. Official data repository or database release record
2. Peer-reviewed article linked to the dataset when available
3. Official project documentation

A standalone dataset release does not need a peer-reviewed paper if it is verified as an official data-resource event. Do not treat an associated preprint as an eligible paper.

## Verification rules

- Prefer the source closest to the event.
- For scholarly literature, verify peer-review eligibility before scoring, tone selection, or drafting.
- A DOI alone does not prove peer review.
- If publication status is unknown or conflicting, exclude the paper from Radar output.
- If both a preprint and peer-reviewed journal version exist, use the journal version as the factual authority and deduplicate the preprint.
- For current news, verify the event date separately from the page publication date.
- For software, distinguish stable release, pre-release, edge/nightly, and development branch.
- For database changes, identify migration/deprecation dates exactly when available.
- For clinical claims, do not infer clinical utility from technical performance alone.
- For performance claims, preserve the authors' comparison context and hardware when available.
- For repository activity, use current release/commit/issue evidence rather than stale third-party summaries.

## Search-language policy

Use English-language primary or high-quality international sources by default. Do not use Persian-language sources unless the user explicitly asks.

## Citation policy

Cite each paragraph or table row that contains externally verified current facts. Avoid citing a source that only loosely relates to the claim.

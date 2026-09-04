# Search Playbook

Read `curator-handoff.md` when a curated roster is available. Read `peer-review-policy.md` before literature triage.

## Daily window

Primary window: previous 36 hours.
Fallback window: previous 7 days for slow sources and delayed indexing.

Always record the exact date range used.

## Discovery passes

Run multiple passes rather than one broad query.

### Pass 0: curated monitoring roster

When a valid Source Curator handoff is present, query or inspect its monitoring endpoints first.

- Use `source_role` and `monitoring_method` to choose how the source is checked.
- Preserve `target_id` internally when practical for traceability.
- Treat the roster as the persistent monitoring seed, not as item-level proof.
- Do not restrict discovery to only the currently registered domains when the Curator registry is still being bootstrapped.
- Use built-in watchlists for uncovered domains and resilience.

### Pass A: peer-reviewed literature
Search Europe PMC/PubMed and publisher sources for recent peer-reviewed bioinformatics, computational biology, genomics, transcriptomics, single-cell, spatial, long-read, metagenomics, proteomics, metabolomics, structural biology, and AI-for-biology papers.

Verify journal publication or accepted/online-first status before a paper becomes a candidate.

### Pass B: publication-status recovery
Use bioRxiv, medRxiv, arXiv, or similar preprint services only when useful for identity resolution or to determine whether a record has a later peer-reviewed publication.

Do not create a Radar candidate from a preprint-only record. If a peer-reviewed version exists, continue with that version and deduplicate the preprint.

### Pass C: infrastructure
Search official NCBI and EMBL-EBI update/news/release pages. Look for migration, deprecation, API, schema, reference, annotation, archive, cloud, FTP, authentication, taxonomy, and data-release changes.

Prefer matching Curator-approved monitoring endpoints when they cover the target service. Use additional official pages when necessary for concrete-event verification.

### Pass D: software
Search release pages for high-value workflow engines, core genomics tools, single-cell/spatial stacks, metagenomics tools, and major ML/structural-biology projects. Prefer release notes over generic repository pages.

Prefer Curator-approved release endpoints for persistent monitoring. A useful unregistered release source may be used for the current event but should be treated as a future Curator candidate rather than silently added to persistent state.

### Pass E: datasets
Search primary repositories and verified peer-reviewed paper pages for new public datasets with method-development or benchmarking value. A standalone official dataset release remains eligible even without a paper. Capture modality, species, sample count, raw/processed availability, license if known, and intended use.

Do not cite or summarize a preprint as the scientific authority for a dataset. If only a preprint describes the dataset, use the official repository record for the dataset event or omit the scholarly claim.

### Pass F: cross-check
For the highest-ranked items, run a second query with the exact title, DOI, PMID, release tag, or database release identifier.

For scholarly literature resolve all of:

- identity,
- journal/publisher,
- publication status,
- peer-review eligibility,
- preprint-to-publication duplicates.

If peer-review status remains uncertain, exclude the paper before scoring.

## Search-term families

Use combinations of:

- bioinformatics software release
- computational biology method benchmark journal
- genome assembly variant calling long read journal
- single cell spatial transcriptomics method journal
- RNA isoform long-read transcriptomics journal
- metagenomics microbiome AMR computational journal
- proteomics metabolomics software benchmark journal
- protein structure AI biology method journal
- NCBI update deprecation API release
- EMBL-EBI database release update
- Bioconductor release package
- GitHub release Nextflow Snakemake nf-core samtools bcftools htslib minimap2

Adapt queries to the current date and observed signals.

## Eligibility before scoring

For every scholarly record discovered:

1. Resolve identity.
2. Resolve publication status.
3. Apply `peer-review-policy.md`.
4. Exclude ineligible literature.
5. Only then score the surviving record.

Never use scientific importance, novelty, citation count, social appeal, benchmark size, or Curator source priority to override missing peer review.

## Deduplication

Treat these as one story unless the transition itself is important:

- preprint and its later peer-reviewed article,
- journal early-online and final issue version,
- GitHub release plus copied project blog post,
- NCBI/EMBL-EBI announcement plus a secondary news rewrite.

Prefer the most authoritative and mature eligible version.

A preprint-only record is excluded rather than retained as the preferred version.

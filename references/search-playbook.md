# Search Playbook

Read `curator-handoff.md` when a curated roster is available. Read `peer-review-policy.md` before literature triage. Read `run-state.md` when prior Radar state is available.

## Daily window

Primary window: previous 36 hours.
Fallback window: previous 7 days only for slow sources, delayed indexing, low-volume categories, or explicit recovery.

Always record the exact date range used. Do not silently expand the fallback window to manufacture volume.

## Search principle

Use adaptive staged discovery. Spend broad-search effort on coverage and deep-verification effort only on candidates that can plausibly affect the final report.

Do not repeatedly verify low-value items to the same depth as Executive Brief, CRITICAL/HIGH, Benchmark, Social, or Deep-Dive candidates.

## Pass 0: curated monitoring roster

When a valid Source Curator handoff is present, inspect its monitoring endpoints first.

- Use `source_role` and `monitoring_method` to choose how each source is checked.
- Preserve `target_id` internally when practical.
- Treat the roster as the persistent monitoring seed, not as item-level proof.
- Do not restrict discovery to only registered domains while the Curator registry is incomplete.
- Use `watchlists.md` for uncovered domains and resilience.

If a source repeatedly yields useful official events but is absent from the roster, add an internal Curator feedback record under `run-state.md`; do not self-approve it.

## Pass 1: dated discovery

Search recent indexes, journals, publisher feeds, official release/update endpoints, and registered monitoring targets for items inside the primary window.

Cover these classes separately:

- peer-reviewed bioinformatics/computational-biology literature;
- software and workflow releases;
- database/reference/infrastructure/service changes;
- datasets and reusable resources;
- security/integrity notices when relevant.

Use date-aware queries and preserve event date separately from publication/page date.

## Pass 2: coverage-gap discovery

Only after Pass 1, inspect uncovered high-value domains from `watchlists.md` or use targeted queries where the Curator roster lacks coverage.

Typical literature families include genomics, transcriptomics, single-cell, spatial, long-read, metagenomics, proteomics, metabolomics, structural bioinformatics, statistical genetics, systems biology, and AI-for-biology.

Typical infrastructure families include NCBI/EMBL-EBI/Ensembl/reference releases, API/schema/authentication changes, workflow engines, package ecosystems, and core genomics tooling.

Do not run every fallback query mechanically when coverage is already adequate.

## Pass 3: identity and eligibility resolution

For every potentially reportable item:

1. resolve canonical identity;
2. resolve publication/event status;
3. apply `peer-review-policy.md` for scholarly literature;
4. resolve preprint-to-journal or early-online-to-final relationships;
5. compare against within-run duplicates;
6. compare against prior ledger when `run-state.md` state is available;
7. suppress same-story/no-material-change items;
8. create a preliminary Evidence Card only for eligible stories.

Use bioRxiv, medRxiv, arXiv, Research Square, or similar preprint services only for identity resolution or locating a later peer-reviewed publication. A preprint-only record never becomes a Radar candidate.

## Pass 4: shortlist verification

For candidates that survive eligibility and relevance triage, verify at least:

- primary source;
- central claim or concrete event;
- exact material date/version;
- main limitation or evidence boundary;
- practical workflow relevance.

Update `references/evidence-card.md` first. Do not draft from search snippets.

## Pass 5: deep verification

Reserve deep verification for items likely to appear in one or more of:

- Executive Brief;
- CRITICAL/HIGH workflow events;
- Benchmark Claims;
- Social Candidates;
- Deep-Dive Candidates;
- high-risk clinical, causal, AI-capability, or translational stories.

When material and available, verify comparator, dataset scale, hardware, internal/external validation, code, data, license, release/archive, environment/container, tests/CI, and independent reproduction.

Do not search for metadata that is irrelevant to the claim merely to fill fields.

## Adaptive stop rule

Stop broad discovery when all of these are true:

1. required coverage classes for the requested run have been checked;
2. two consecutive broad/coverage passes add no new `HIGH` candidate or material workflow event;
3. no unresolved CRITICAL infrastructure/security event remains;
4. low-news behavior from `output-contract.md` can be satisfied without filler.

Continue exact-title/identifier verification for already shortlisted items even after broad discovery stops.

A quiet day is a valid outcome.

## Verification tiers

### Tier 1 — discovery
Capture identity candidate, source class, date and enough context to decide whether the item deserves resolution.

### Tier 2 — shortlist
Resolve eligibility, primary claim/event, key numbers, main limitation and practical relevance.

### Tier 3 — deep verification
Inspect benchmark design, external validation, reproducibility, repository/runtime evidence and high-risk claim boundaries when material.

Do not promote an item solely because more metadata was available.

## Search-term families

Use targeted combinations such as:

- bioinformatics software release
- computational biology method benchmark journal
- genome assembly variant calling long read journal
- single cell spatial transcriptomics method journal
- RNA isoform long-read transcriptomics journal
- metagenomics microbiome AMR computational journal
- proteomics metabolomics software benchmark journal
- protein structure AI biology method journal
- systems biology metabolic model multiomics journal
- NCBI update deprecation API release
- EMBL-EBI database release update
- Bioconductor release package
- GitHub release Nextflow Snakemake nf-core samtools bcftools htslib minimap2

Adapt queries to the current date, Curator coverage, unresolved gaps and observed signals.

## Eligibility before scoring

For every scholarly record discovered:

1. resolve identity;
2. resolve publication status;
3. apply `peer-review-policy.md`;
4. exclude ineligible literature;
5. only then create the eligible Evidence Card and score it.

Never use scientific importance, novelty, citation count, social appeal, benchmark size or Curator source priority to override missing peer review.

## Deduplication

Treat these as one canonical story unless a material transition itself is newsworthy:

- preprint and later peer-reviewed article;
- journal early-online and final issue version;
- GitHub release plus copied project blog post;
- official NCBI/EMBL-EBI announcement plus secondary rewrite;
- the same paper appearing in several indexes.

Prefer the most authoritative mature eligible version.

When prior run state exists, use `run-state.md` to distinguish:

- duplicate/no change -> suppress;
- material update -> report as update;
- publication transition -> use peer-reviewed version;
- release transition -> report the stable transition;
- correction/retraction -> re-surface according to impact.

A preprint-only record is excluded rather than retained as the preferred version.

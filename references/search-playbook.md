# Search Playbook

Read `curator-handoff.md` when a curated roster is available. Read `peer-review-policy.md` before literature triage. Read `run-state.md` when prior Radar state is available. Read `newsroom-engine.md` before final story selection.

## Daily window

Primary window: previous 36 hours.

Fallback window: previous 7 days only for slow sources, delayed indexing, low-volume categories, or explicit recovery.

Always record the exact date range. Do not silently expand the window to manufacture volume.

## Search principle

Discovery should be broad enough to avoid missing important events, but visible output should be narrow.

Spend search effort in this order:

`coverage -> eligibility -> identity/dedup -> Story Gate -> selective deep verification`

Do not deeply audit routine eligible items that are unlikely to survive newsroom selection.

## Pass 0: curated monitoring roster

When a valid Source Curator handoff is present, inspect its monitoring endpoints first.

- Route each source by `source_role` and `monitoring_method`.
- Preserve `target_id` internally when practical.
- Treat Curator approval as source-level trust, not item-level importance or peer-review proof.
- Use `watchlists.md` for uncovered domains and resilience.
- If an unregistered official source repeatedly yields useful events, create Curator feedback under `run-state.md`; do not self-approve it.

## Pass 1: dated discovery

Search recent indexes, journal/publisher feeds, official release/update endpoints, and registered monitoring targets inside the primary window.

Cover separately:

- peer-reviewed bioinformatics/computational-biology literature;
- software/workflow releases;
- database/reference/infrastructure/service changes;
- datasets/resources;
- corrections/retractions/security/integrity notices.

Preserve event date separately from publication/page date.

## Pass 2: coverage-gap discovery

Use `watchlists.md` and targeted queries only for material coverage gaps.

Typical literature domains:

- genomics and statistical genetics;
- transcriptomics/RNA;
- single-cell/spatial;
- long-read/assembly/variant calling;
- metagenomics/microbiome/AMR;
- proteomics/metabolomics;
- structural bioinformatics/protein design;
- systems biology/metabolic modelling;
- AI/ML for biology.

Typical infrastructure domains:

- NCBI/EMBL-EBI/Ensembl/reference releases;
- API/schema/authentication changes;
- workflow engines/package ecosystems;
- core genomics/single-cell/spatial tools.

Do not run every fallback query mechanically when coverage is already adequate.

## Pass 3: identity and eligibility

For every potentially useful item:

1. resolve canonical identity;
2. resolve publication/event status;
3. apply `peer-review-policy.md` for scholarly literature;
4. resolve preprint-to-journal and early-online/final relationships;
5. deduplicate within run;
6. compare against prior ledger when valid state exists;
7. suppress same-story/no-material-change items;
8. create a preliminary Evidence Card only for eligible items.

Preprint services may be used only for identity resolution or locating a later peer-reviewed publication. Preprint-only literature never becomes a newsroom candidate.

## Pass 4: Story Gate triage

Before deep verification, apply the internal `news_statement_fa` test from `newsroom-engine.md`.

Ask:

- what changed?
- why should the BioInsight/bioinformatics reader care today?
- is there a consequence, tension, capability, limitation, workflow impact, or unusual resource value?
- would this still be news if the journal name were removed?

If the answer is weak, keep the item out of normal newsroom coverage even if it is scientifically valid.

Do not confuse recency with newsworthiness.

## Pass 5: shortlist verification

For items that pass the Story Gate, verify at least:

- primary source;
- central event/finding;
- exact material date/version;
- key number(s) only when material;
- main evidence boundary;
- practical/scientific consequence.

Update the Evidence Card before drafting.

## Pass 6: deep verification

Reserve Tier-3 verification for:

- likely lead stories;
- CRITICAL workflow events;
- high News Value items;
- major benchmark claims;
- stories selected for Telegram/article/deep dive;
- high-risk clinical, causal, AI-capability, or translational stories.

When material, verify comparator, dataset scale, hardware, internal/external validation, code/data/license/release/environment/container/tests/CI, and independent replication.

Do not gather metadata merely to fill an audit template.

## Adaptive stop rule

Stop broad discovery when all are true:

1. required source/domain classes have been checked;
2. two consecutive broad/coverage passes add no new high-news-value candidate or material operational event;
3. no unresolved CRITICAL infrastructure/security event remains;
4. newsroom output can honestly reflect a quiet day without filler.

Continue exact verification for already selected stories after broad discovery stops.

## Verification tiers

### Tier 1 — Discovery

Identity candidate, date, source class, and enough context for triage.

### Tier 2 — Story shortlist

Eligibility, primary event/finding, exact material facts, main limitation, and consequence.

### Tier 3 — Newsroom deep verification

Benchmark scope, external validation, reproducibility/runtime evidence, and high-risk claim boundaries when material to the story.

## Search-term families

Use date-aware targeted combinations such as:

- bioinformatics software release
- computational biology benchmark journal
- genome assembly variant calling long read journal
- single cell spatial transcriptomics method journal
- RNA splicing RBP transcriptomics journal
- metagenomics microbiome AMR computational journal
- proteomics metabolomics software benchmark journal
- protein structure design AI biology journal
- systems biology metabolic model multiomics journal
- NCBI update deprecation API release
- EMBL-EBI database release update
- Bioconductor release package
- GitHub release Nextflow Snakemake nf-core samtools bcftools htslib minimap2

Adapt queries to current date, Curator coverage, unresolved gaps, and observed stories.

## Deduplication

Treat these as one canonical story unless a material transition itself is newsworthy:

- preprint and later peer-reviewed article;
- early-online and final issue version;
- release plus copied project blog post;
- official announcement plus secondary rewrite;
- the same paper in multiple indexes.

When prior state exists:

- duplicate/no change -> suppress;
- material update -> report only if the update itself passes the Story Gate;
- publication transition -> use peer-reviewed version;
- prerelease-to-stable -> treat as release transition;
- correction/retraction -> re-surface according to consequence.

Never infer prior-run history when state is absent.

# Search Playbook

## Daily window

Primary window: previous 36 hours.
Fallback window: previous 7 days for slow sources and delayed indexing.

Always record the exact date range used.

## Discovery passes

Run multiple passes rather than one broad query.

### Pass A: literature
Search Europe PMC/PubMed for recent bioinformatics, computational biology, genomics, transcriptomics, single-cell, spatial, long-read, metagenomics, proteomics, metabolomics, structural biology, and AI-for-biology papers.

### Pass B: preprints
Search bioRxiv for recent computational biology, genomics, bioinformatics, methods, software, benchmark, single-cell, spatial, long-read, protein/structure, and multi-omics preprints.

### Pass C: infrastructure
Search official NCBI and EMBL-EBI update/news/release pages. Look for migration, deprecation, API, schema, reference, annotation, archive, cloud, FTP, authentication, taxonomy, and data-release changes.

### Pass D: software
Search release pages for high-value workflow engines, core genomics tools, single-cell/spatial stacks, metagenomics tools, and major ML/structural-biology projects. Prefer release notes over generic repository pages.

### Pass E: datasets
Search primary repositories and paper/preprint pages for new public datasets with method-development or benchmarking value. Capture modality, species, sample count, raw/processed availability, license if known, and intended use.

### Pass F: cross-check
For the highest-ranked items, run a second query with the exact title, DOI, release tag, or database release identifier. Resolve publication status and duplicates.

## Search-term families

Use combinations of:

- bioinformatics software release
- computational biology method benchmark
- genome assembly variant calling long read
- single cell spatial transcriptomics method
- RNA isoform long-read transcriptomics
- metagenomics microbiome AMR computational
- proteomics metabolomics software benchmark
- protein structure AI biology method
- NCBI update deprecation API release
- EMBL-EBI database release update
- Bioconductor release package
- GitHub release Nextflow Snakemake nf-core samtools bcftools htslib minimap2

Adapt queries to the current date and observed signals.

## Deduplication

Treat these as one story unless the transition is itself important:

- bioRxiv preprint and its peer-reviewed article
- journal early-online and final issue version
- GitHub release plus copied project blog post
- NCBI/EMBL-EBI announcement plus a secondary news rewrite

Prefer the most authoritative and mature version.

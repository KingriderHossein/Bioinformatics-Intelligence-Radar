# Watchlists

These are fallback and coverage-gap watchlists, not the primary persistent roster when a valid Bioinformatics Source Curator handoff is available. Report only meaningful eligible changes.

Read `curator-handoff.md` for curated source intake and `peer-review-policy.md` for scholarly-literature eligibility.

## Routing rule

- If a valid Curator handoff is present, monitor those sources first.
- Use this file to cover domains that are not yet represented in the Curator bootstrap, to recover from an unavailable endpoint, or when the handoff is unavailable.
- A source appearing here is not automatically Curator-approved.
- If an unregistered source repeatedly produces useful official signals, return it as a future Curator candidate rather than silently treating it as persistent curated state.

## Peer-reviewed literature

- PubMed / NCBI
- Europe PMC
- Major journal/publisher feeds when needed for early-online peer-reviewed articles

Preprint services such as bioRxiv and medRxiv are not user-visible Radar sources. Use them only for identity resolution or to locate a later peer-reviewed publication.

## Core infrastructure and databases

- NCBI News / Insights
- PubMed / PMC
- GenBank / RefSeq
- SRA / GEO
- ClinVar / dbSNP / dbVar
- NCBI Taxonomy
- NCBI Datasets
- EMBL-EBI news and data-resource updates
- ENA
- Ensembl
- UniProt
- InterPro
- MGnify
- RNAcentral
- Reactome
- PRIDE
- PDB / PDBe
- AlphaFold Database
- GDC / TCGA
- gnomAD
- GTEx

## Workflow and reproducibility

- Nextflow
- nf-core
- Snakemake
- Galaxy
- Bioconda
- Conda/Mamba changes that affect bioinformatics environments

## Genomics and long read

- samtools
- bcftools
- htslib
- minimap2
- BWA/BWA-MEM2
- GATK
- DeepVariant
- Clair3 and major long-read variant callers
- Flye
- hifiasm
- Canu

## Transcriptomics, single cell, and spatial

- STAR
- Salmon
- kallisto
- DESeq2
- edgeR
- Bioconductor
- Seurat
- Scanpy
- scvi-tools
- Cell Ranger
- Space Ranger
- major spatial-analysis toolchains when active

## Metagenomics and AMR

- Kraken2
- Bracken
- MetaPhlAn
- HUMAnN
- QIIME 2
- AMRFinderPlus
- CARD / RGI

## Structural bioinformatics and AI

- AlphaFold ecosystem
- ColabFold
- OpenFold
- protein language-model and sequence-design tool releases when technically substantive

For scholarly AI/protein-design papers, require verified peer review. Software releases remain eligible through official release sources.

## Proteomics and metabolomics

- MaxQuant
- OpenMS
- FragPipe
- DIA-NN
- Skyline
- major LC-MS feature-finding and identification tools

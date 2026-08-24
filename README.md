# Bioinformatics Intelligence Radar

A reusable ChatGPT Skill for daily bioinformatics news and technical-intelligence monitoring.

## Current protocol

Version: 2.1.1

The radar performs broad discovery before ranking. It covers papers, preprints, software releases, databases, infrastructure, datasets, reproducibility, benchmark claims, trend signals, and public-facing social candidates.

## Install

Package the skill as `skill.zip` and import it into the ChatGPT Skills interface. The required entrypoint is `SKILL.md`.

## Typical prompts

- Run Bioinformatics Intelligence Radar for today.
- Run the radar for the last 7 days.
- Show only Critical Alerts and Tool & Software Radar.
- Find Social Candidates from today's bioinformatics radar.
- Deep-dive the top benchmark claim from today's radar.

## Design principles

- Primary sources first.
- Exact reporting windows and dates.
- Preprints are never presented as peer-reviewed evidence.
- Broad discovery, then deduplication and ranking.
- No invented scan counts.
- Infrastructure changes outrank ordinary papers when they can break workflows.
- Social headlines must be attractive without overstating evidence.
- Radar reports are written in Persian by default, while technical names and identifiers remain in English when needed for precision.

## Layout

- `SKILL.md`: control plane and workflow.
- `references/source-policy.md`: source hierarchy and verification policy.
- `references/search-playbook.md`: discovery and deduplication process.
- `references/watchlists.md`: priority tools and data resources.
- `references/scoring.md`: technical, social, and reproducibility scoring.
- `references/output-contract.md`: fixed Radar v2.1 report structure.

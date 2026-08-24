# Changelog

## 2.2.1 - 2026-08-24

- Fixed the Skill-to-Skill orchestration bug that could report Bioinformatics Telegram Editor as unavailable.
- Removed all direct downstream Skill/tool invocation from Radar.
- Made the outer orchestrator the sole owner of Telegram Handoff transfer and Editor execution.
- Added GitHub-direct Editor execution as the preferred orchestrated mode when the Editor Skill is not installed.
- Added explicit graceful behavior so Radar never fails because a downstream Editor is absent.
- Added `references/orchestration.md` to document runtime ownership and fallback behavior.

## 2.2.0 - 2026-08-24

- Added Telegram Handoff v1 as a structured downstream contract.
- Added stable candidate IDs, evidence status, exact-fact preservation, limitations, and `do_not_say_fa` guardrails.
- Added direct handoff behavior for Bioinformatics Telegram Editor in chained or scheduled workflows.
- Kept raw handoff JSON internal by default so the human Radar report remains readable.

## 2.1.1 - 2026-08-24

- Made Persian the mandatory default language for the complete Radar output, regardless of prompt language.
- Translated the report contract headings and narrative fields into Persian.
- Kept official tool names, database names, package names, version strings, identifiers, and precision-sensitive technical terms in English.
- Preserved machine-readable status labels while requiring Persian explanation where useful.

## 2.1.0 - 2026-08-24

- Expanded the radar from a short digest to a 20-35 item target when news volume supports it.
- Added Critical Alerts for workflow-breaking infrastructure changes.
- Added dedicated Tool, Database, Dataset, Paper, Preprint, GitHub, Reproducibility, and Benchmark sections.
- Added 1-3 evidence-backed Signal of the Day items.
- Added 3-5 Social Candidates with public-facing headlines, hooks, format suggestions, social scoring, and overhype risk.
- Added exactly three Deep-Dive Candidates when enough material exists.
- Added measurable Radar Statistics and prohibited invented scan counts.
- Added source hierarchy, search playbook, watchlists, and scoring rules.

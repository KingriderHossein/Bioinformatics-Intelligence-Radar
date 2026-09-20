# Migration to Radar 3.1

Radar 3.1 is backward-compatible at the newsroom protocol level and adds an optional deterministic backend. Existing Markdown workflows can continue to use `SKILL.md` and the reference contracts without adopting the CLI.

## New capabilities

- JSON schemas for Evidence Card, Story Card and run state;
- durable identity and event fingerprints;
- within-run and cross-run duplicate suppression;
- explicit publication and release transition classification;
- explainable six-dimension News Value scoring;
- a standard CLI for validation and processing;
- golden fixtures and regression tests;
- example configuration and operations guidance.

## Adoption steps

1. Keep the current Curator handoff and emit normalized discovery items.
2. Add a durable identifier and primary source to each item.
3. Add peer-review fields to scholarly items.
4. Run `radar_cli validate` before newsroom generation.
5. Supply the prior state file to `radar_cli run` when cross-run suppression is desired.
6. Persist the returned state only after the full newsroom release gate passes.

The CLI deliberately does not replace web discovery or editorial judgment. It provides a stable evidence-processing layer that can be embedded in either a scheduled job or an interactive Agent run.

# Radar Orchestration

Use this reference when execution includes the upstream Bioinformatics Source Curator handoff, downstream Telegram editing, or both.

## Ownership

- Source Curator owns the persistent source registry and materialized `10_RADAR_SOURCES` handoff.
- Radar owns item discovery, scholarly peer-review eligibility, event verification, deduplication, scoring, Social Candidates, and Telegram Handoff v1.
- The outer orchestrator owns loading and transferring upstream/downstream handoffs.
- Telegram Editor owns editorial ranking, narrative, Telegram formatting, and hype control.
- No Skill calls another Skill directly.

## Upstream Curator flow

For a daily or periodic Radar run when Google Sheets access is available:

1. Resolve the workbook titled `Bioinformatics Source Curator Registry`.
2. Read the `10_RADAR_SOURCES` tab using the schema in `curator-handoff.md`.
3. Pass valid rows into Radar as the current Curator handoff.
4. Radar uses them as the primary persistent monitoring roster.
5. Radar still applies all item-level eligibility and evidence gates.
6. If the workbook or tab is unavailable, continue with the built-in watchlists and record the actual limitation rather than failing the Radar.

If the handoff is already present in the current execution context, reuse it. Do not invoke the Source Curator Skill just to recreate it.

## Downstream Telegram flow

1. Load and execute Radar instructions.
2. Apply `peer-review-policy.md` before scholarly scoring or selection.
3. Complete Radar quality gates.
4. Construct Telegram Handoff v1 only from eligible Social Candidates and keep it in the current execution context.
5. For every scholarly handoff candidate, require `peer_review_verified = true` and a resolved peer-reviewed primary source.
6. Load canonical Telegram Editor instructions from `KingriderHossein/Bioinformatics-Telegram-Editor` when GitHub access is available.
7. Apply those instructions directly to the handoff. Do not require the Editor to be installed or exposed as a runtime tool.
8. If GitHub Editor instructions cannot be loaded, use the orchestrator's embedded editorial fallback.
9. Return the Persian Radar report and 2-3 ready-to-review Persian Telegram drafts when that downstream workflow was requested.

## Non-peer-reviewed literature behavior

- Preprint-only, submitted, under-review, working-paper, conference-abstract, or uncertain-review-status scholarly records are excluded inside Radar before scoring.
- They must not be transferred to the outer orchestrator as Telegram candidates.
- The Editor must never be asked to decide whether an excluded paper should be restored.
- If a later peer-reviewed publication exists, Radar resolves and hands off that version instead.

This restriction does not apply to verified official software, database, dataset, infrastructure, security, or service-change events because they are not scholarly papers.

## Failure behavior

- Never fail the Radar merely because the Curator registry cannot be loaded. Use the fallback watchlists and state the coverage limitation when relevant.
- Never treat missing Curator access as permission to invent registry rows or approval state.
- Never stop merely because Bioinformatics Telegram Editor is not installed as a Skill.
- Never say downstream was skipped if the Editor repository can be read and its instructions can be applied directly.
- If both the Editor repository and fallback contract are unavailable, return the Radar successfully and state only the actual downstream limitation.
- Never expose raw handoff JSON unless explicitly requested.
- Never weaken or bypass Radar's peer-review eligibility gate during fallback execution.

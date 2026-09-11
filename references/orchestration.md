# Radar Orchestration

Use this reference when execution includes upstream Curator intake, optional Radar run state, downstream Telegram editing, or any combination of them.

## Ownership

- Source Curator owns the persistent source registry and materialized `10_RADAR_SOURCES` handoff.
- Radar owns item discovery, scholarly peer-review eligibility, event verification, canonical story identity, Evidence Cards, within-run deduplication, material-change logic, scoring, Social Candidates, and Telegram Handoff v1.
- The outer orchestrator or host environment owns loading and persisting Radar run state across executions when a persistent store is configured.
- The outer orchestrator owns loading and transferring upstream/downstream handoffs.
- Telegram Editor owns editorial ranking, narrative, Telegram formatting, and hype control within Radar's evidence boundaries.
- No Skill calls another Skill directly.

## Upstream Curator flow

For a daily or periodic Radar run when Google Sheets access is available:

1. Resolve the workbook titled `Bioinformatics Source Curator Registry`.
2. Read the `10_RADAR_SOURCES` tab using `curator-handoff.md`.
3. Pass valid rows into Radar as the current Curator handoff.
4. Radar uses them as the primary persistent monitoring roster.
5. Radar still applies all item-level eligibility, evidence, deduplication and importance gates.
6. If the workbook or tab is unavailable, continue with built-in watchlists and record the actual coverage limitation rather than failing.

If the handoff is already present in current execution context, reuse it. Do not invoke the Source Curator Skill just to recreate it.

## Optional state flow

Read `run-state.md` when cross-run state is relevant.

1. The outer orchestrator checks whether a configured Radar ledger is available.
2. If available, load it before cross-run deduplication.
3. Radar marks state as `AVAILABLE`, `BOOTSTRAP`, `UNAVAILABLE`, or `NOT_CONFIGURED` according to the evidence.
4. Radar compares eligible story identity and event fingerprints against prior state.
5. Same-story/no-material-change items may be suppressed.
6. Material updates, release transitions, publication transitions, corrections and retractions remain reportable.
7. After Radar evidence and release gates pass, return the updated ledger to the outer orchestrator for persistence when supported.

Never invent a prior ledger, first-seen date, last-reported date or suppression history. Missing state must not fail the Radar.

Do not write daily run state into the public Skill repository unless the user explicitly defines that repository as the state store. Runtime state and Skill source code are separate concerns.

## Evidence Card flow

1. Discover an item.
2. Resolve identity and eligibility.
3. Deduplicate within run and against prior state when available.
4. Build one Evidence Card for each eligible canonical story that survives triage.
5. Deepen the card only to the verification tier required by the story's likely output role.
6. Derive report wording, benchmark treatment, Social Candidate and Telegram Handoff fields from that card.
7. If new evidence changes a fact, update the card first.

The Evidence Card is internal runtime state, not a user-visible quota or report section.

## Downstream Telegram flow

1. Load and execute Radar instructions.
2. Apply `peer-review-policy.md` before scholarly scoring or selection.
3. Complete Radar Evidence Cards and quality gates.
4. Construct Telegram Handoff v1 only from eligible Social Candidates and keep it in current execution context.
5. For every scholarly handoff candidate, require `peer_review_verified = true` and a resolved peer-reviewed primary source.
6. Load canonical Telegram Editor instructions from `KingriderHossein/Bioinformatics-Telegram-Editor` when GitHub access is available.
7. Apply those instructions directly to the handoff. Do not require the Editor to be installed or exposed as a runtime tool.
8. If GitHub Editor instructions cannot be loaded, use the orchestrator's embedded editorial fallback.
9. Return the requested Persian Radar report and ready-to-review Persian Telegram drafts.

## Non-peer-reviewed literature behavior

- Preprint-only, submitted, under-review, working-paper, conference-abstract, or uncertain-review-status scholarly records are excluded before scoring.
- They must not be transferred to the outer orchestrator as Telegram candidates.
- The Editor must never be asked to decide whether an excluded paper should be restored.
- If a later peer-reviewed publication exists, Radar resolves and uses that version instead.

This restriction does not apply to verified official software, database, dataset, infrastructure, security, or service-change events because they are not scholarly papers.

## Curator feedback flow

If `run-state.md` records repeated useful hits from an official source absent from the current Curator roster:

1. Radar creates an internal Curator feedback record.
2. Radar may use that source for the current verified event under normal source policy.
3. Radar must not mark the source Curator-approved.
4. The outer orchestrator may pass the feedback to a Curator maintenance workflow when explicitly requested or scheduled.

## Failure behavior

- Never fail Radar merely because the Curator registry cannot be loaded.
- Never fail Radar merely because prior run state is missing.
- Never treat missing Curator access or missing state as permission to invent data.
- Never stop merely because Bioinformatics Telegram Editor is not installed as a Skill.
- Never say downstream was skipped if the Editor repository can be read and its instructions can be applied directly.
- If both Editor repository instructions and fallback contract are unavailable, return Radar successfully and state only the actual downstream limitation.
- Never expose raw Evidence Cards, run ledger, Curator feedback queue, or handoff JSON unless explicitly requested.
- Never weaken or bypass Radar's peer-review eligibility gate during any fallback execution.

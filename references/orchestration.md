# Radar Orchestration

Use this reference when execution includes upstream Curator intake, optional run state, newsroom selection, downstream Telegram editing, or any combination of them.

## Ownership

- Source Curator owns the persistent source registry and `10_RADAR_SOURCES` handoff.
- Radar evidence layer owns discovery, eligibility, verification, canonical identity, Evidence Cards, deduplication, material-change logic, and run telemetry.
- Radar Newsroom layer owns Story Gate, News Value, editorial angles, Story Cards, lead-story selection, Signal synthesis, and editorial recommendations.
- The outer orchestrator/host owns optional persistence of Radar run state across executions.
- The outer orchestrator owns transfer of upstream/downstream handoffs.
- Telegram Editor owns final Telegram narrative and formatting within Radar evidence/newsroom boundaries.
- No Skill calls another Skill directly.

## Upstream Curator flow

For a daily or periodic run when the registry is available:

1. Resolve workbook `Bioinformatics Source Curator Registry`.
2. Read `10_RADAR_SOURCES` according to `curator-handoff.md`.
3. Pass valid rows into Radar as the current Curator handoff.
4. Use them as the first persistent monitoring pass.
5. Continue Radar item-level eligibility, evidence, deduplication, and newsroom judgment independently.
6. If the registry is unavailable or incomplete, continue with built-in watchlists and state the real coverage limitation only when relevant.

If the handoff already exists in current context, reuse it. Do not invoke the Source Curator Skill merely to recreate it.

## Optional state flow

Read `run-state.md` when cross-run state is relevant.

1. The outer orchestrator checks whether a configured Radar ledger exists.
2. If available, load it before cross-run deduplication.
3. Radar marks state honestly as `AVAILABLE`, `BOOTSTRAP`, `UNAVAILABLE`, or `NOT_CONFIGURED`.
4. Compare canonical identity and event fingerprints against prior state.
5. Suppress same-story/no-material-change items.
6. Preserve material updates, publication/release transitions, corrections, retractions, and new independent validation.
7. Persist updated state only after evidence and newsroom release gates pass when the host supports persistence.

Never invent first-seen, last-reported, or suppression history.

## Evidence Card flow

1. Discover item.
2. Resolve identity and eligibility.
3. Deduplicate within run and across valid prior state.
4. Build one Evidence Card per eligible canonical event that survives basic relevance triage.
5. Verify only to the depth needed for likely output role.
6. Update the Evidence Card before any factual wording changes.

Evidence Cards are internal factual authority and are not a default user-visible report section.

## Newsroom flow

1. Read `newsroom-engine.md` after eligible Evidence Cards exist.
2. Write an internal `news_statement_fa` for each plausible story.
3. Apply the Story Gate.
4. Score News Value only for Story-Gate survivors.
5. Generate multiple evidence-safe angle candidates for strong stories.
6. Select one editorial angle and build a Story Card.
7. Choose the lead story, follow-up stories, optional alert, optional Signal, editorial selection, Deep Dive suggestions, and Watchlist.
8. Apply `editorial-tone-engine.md` and `output-contract.md`.
9. Keep detailed evidence/repository/reproducibility audits in the backend unless requested or essential to the story.

A peer-reviewed paper that fails the Story Gate remains scientifically valid but is omitted from normal newsroom output.

## Downstream Telegram flow

1. Execute Radar evidence workflow.
2. Execute Radar Newsroom workflow.
3. Complete Evidence Card and Story Card release gates.
4. Construct Telegram Handoff v1 only from newsroom-selected candidates.
5. Require `peer_review_verified = true` and a resolved peer-reviewed primary source for scholarly candidates.
6. Keep handoff JSON in current execution context.
7. Load canonical Telegram Editor instructions from `KingriderHossein/Bioinformatics-Telegram-Editor` when GitHub access is available.
8. Apply those instructions directly; do not require the Editor Skill to be installed or exposed as a tool.
9. If the repository cannot be read, use the outer orchestrator's embedded editorial fallback.
10. Return the requested Persian Newsroom Radar and ready-to-review Telegram drafts.

## Non-peer-reviewed literature behavior

- Preprint-only, submitted, under-review, working-paper, conference-abstract, or uncertain-review-status scholarly records are excluded before News Value scoring.
- They never enter Story Cards, Signal, editorial selection, Deep Dive, Watchlist, or Telegram Handoff.
- The Editor never decides whether an excluded paper should be restored.
- If a later peer-reviewed publication exists, resolve and use that version.

Official non-literature events remain eligible under their primary-source rules.

## Curator feedback flow

When an official source outside the roster repeatedly provides useful verified events:

1. create an internal Curator feedback record under `run-state.md`;
2. use the source for the current event if normal source policy permits;
3. do not mark it Curator-approved;
4. the outer orchestrator may forward feedback to a Curator maintenance workflow only when requested/scheduled.

## Failure behavior

- Never fail because Curator registry access is missing.
- Never fail because prior run state is missing.
- Never invent source approval or history.
- Never fail because Telegram Editor is not installed as a Skill.
- Never say downstream was skipped when the Editor repository is readable and can be applied directly.
- If Editor repository and fallback instructions are both unavailable, return Radar successfully and state only the actual downstream limitation.
- Never expose raw Evidence Cards, Story Cards, run ledger, Curator feedback, or handoff JSON unless explicitly requested.
- Never weaken the peer-review gate or Evidence Card boundaries during fallback execution.

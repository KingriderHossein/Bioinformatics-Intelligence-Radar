# Radar -> Telegram Orchestration

Use this reference only when one execution is expected to produce both the Radar and Telegram drafts.

## Ownership

- Radar owns discovery, verification, scoring, Social Candidates, and Telegram Handoff v1.
- The outer orchestrator owns the transfer object and downstream execution.
- Telegram Editor owns editorial ranking, narrative, Telegram formatting, and hype control.
- No Skill calls another Skill directly.

## Required flow

1. Load and execute Radar instructions.
2. Complete Radar quality gates.
3. Construct Telegram Handoff v1 and keep it in the current execution context.
4. Load canonical Telegram Editor instructions from `KingriderHossein/Bioinformatics-Telegram-Editor` when GitHub access is available.
5. Apply those instructions directly to the handoff. Do not require the Editor to be installed or exposed as a runtime tool.
6. If GitHub Editor instructions cannot be loaded, use the orchestrator's embedded editorial fallback.
7. Return the Persian Radar report and 2-3 ready-to-review Persian Telegram drafts.

## Failure behavior

- Never stop merely because Bioinformatics Telegram Editor is not installed as a Skill.
- Never say downstream was skipped if the Editor repository can be read and its instructions can be applied directly.
- If both the Editor repository and fallback contract are unavailable, return the Radar successfully and state only the actual downstream limitation.
- Never expose raw handoff JSON unless explicitly requested.

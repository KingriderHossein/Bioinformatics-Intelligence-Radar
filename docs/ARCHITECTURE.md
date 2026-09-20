# Radar 3.1 Architecture

Radar 3.1 separates deterministic evidence handling from language-model newsroom judgment. This boundary makes identity, deduplication, peer-review gating, state transitions and scoring reproducible while preserving editorial flexibility for Persian writing.

## Pipeline

```text
Curator handoff / source adapters
        ↓
Discovery items (JSON)
        ↓
Identity + evidence gates
        ↓
Within-run deduplication
        ↓
Cross-run state classification
        ↓
News Value scoring
        ↓
Story Gate + Persian newsroom writing
        ↓
Story Cards / Telegram Handoff
```

The `scripts/radar_core.py` module owns deterministic operations. The Skill references remain the authority for source interpretation, verification depth, editorial tone and visible output. The CLI does not browse, infer peer review from a DOI, or invent evidence; it consumes already verified discovery items.

## Contracts

`schemas/evidence-card.schema.json` defines factual provenance and limitations. `schemas/story-card.schema.json` defines editorial framing derived from an Evidence Card. `schemas/run-state.schema.json` defines the persistent ledger. The same canonical identifier must link all three layers.

## State transitions

A state entry is classified as `NEW`, `SUPPRESSED_NO_CHANGE`, `UPDATED`, `PUBLICATION_TRANSITION`, `RELEASE_TRANSITION`, or `CORRECTION_OR_RETRACTION`. The event fingerprint excludes headlines, leads and tone, so editorial rewrites do not create false updates.

State is written only after processing succeeds. If no state file is supplied, the run remains valid but cross-run suppression is not claimed.

## Extension points

Source adapters should emit the item fields documented in `config/radar.example.json` and the Evidence Card contract. Delivery adapters may transform selected Story Cards into Markdown, Telegram Handoff v1, email or a dashboard without mutating evidence. New source types should add a source policy and tests before being added to the content-type enum.

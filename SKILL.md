---
name: bioinformatics-intelligence-radar
description: Run a source-grounded bioinformatics intelligence newsroom that discovers current papers, software, databases, datasets, infrastructure changes, benchmarks, corrections, and emerging signals; verifies scientific eligibility and evidence; suppresses duplicates; then selects only genuinely newsworthy stories and writes them in concise Persian newsroom form. Use for daily/periodic bioinformatics monitoring, technical alerts, important peer-reviewed developments, story discovery, BioInsight editorial selection, Telegram candidates, Deep Dives, and continuation of prior Radar runs. Exclude preprints and any scholarly article whose peer-review status cannot be positively verified from all user-visible coverage and downstream handoffs.
---

# Bioinformatics Intelligence Radar

Protocol version: 3.1.0

Radar 3.0 has two internal layers:

1. **Intelligence Engine** — discover, verify, deduplicate, and preserve evidence.
2. **Newsroom Engine** — decide what deserves attention, find the best story angle, and write readable news.

The user-visible product is the newsroom output, not the backend audit.

Radar 3.1 adds an optional deterministic backend in `scripts/radar_core.py` and
`scripts/radar_cli.py`. Use it when normalized discovery items, persistent state,
or regression checks are available. The backend owns identity, peer-review
gates, within-run deduplication, cross-run classification and explainable News
Value scoring; this Skill still owns source interpretation, newsroom judgment
and Persian writing. Read `docs/ARCHITECTURE.md` and the JSON schemas when
integrating an adapter.

## Product principle

Radar must answer:

**What changed, what is true, what deserves attention, and how should it be told?**

Do not behave like a paper inventory, literature-review table, or repository audit unless the user explicitly asks for those formats.

## Core invariants

1. **Curator-first monitoring when available.** Use the Bioinformatics Source Curator handoff as the first persistent monitoring layer. Source approval never replaces item-level verification.
2. **Peer review is a hard gate for scholarly literature.** Verify it before News Value scoring or visible coverage. Preprints may be used only for identity resolution or finding a later peer-reviewed publication.
3. **Official non-literature events use their own primary-source gate.** Software releases, database/dataset/infrastructure/service/security events do not require paper peer review.
4. **One Evidence Card per canonical eligible event.** Exact facts, dates, numbers, benchmark status, limitations, source provenance, and `do_not_say_fa` live there.
5. **One Story Card per selected newsroom story.** Derive angle, headline, lead, consequence, format, and News Value from the Evidence Card through `newsroom-engine.md`.
6. **Evidence is a gate; newsworthiness is a separate judgment.** A scientifically strong paper may still be omitted if it is not newsworthy.
7. **Use prior run state only when it truly exists.** Suppress duplicates and detect material change with `run-state.md`; never invent history.
8. **No minimum quota.** A quiet day is valid. Never add filler to make the report look complete.
9. **Do not invent counts or metadata.** Report only telemetry actually tracked in the run.
10. **No Skill calls another Skill directly.** The outer orchestrator owns Curator transfer, optional state persistence, and downstream Telegram Editor execution.

## Reference routing

Load progressively.

### Source intake and discovery

- `references/curator-handoff.md` — curated source roster intake.
- `references/watchlists.md` — coverage-gap/fallback monitoring.
- `references/source-policy.md` — source hierarchy and claim-level verification.
- `references/search-playbook.md` — adaptive dated discovery and deduplication.
- `references/peer-review-policy.md` — mandatory scholarly eligibility gate.
- `references/run-state.md` — optional cross-run state, material-change logic, telemetry, Curator feedback.

### Evidence and newsroom selection

- `references/evidence-card.md` — internal factual source of truth.
- `references/newsroom-engine.md` — Story Gate, News Value, angle selection, Story Card, headlines, leads, channel/article treatment.
- `references/scoring.md` — News Value, operational urgency, Telegram compatibility score, confidence and Signal classes.
- `references/editorial-tone-engine.md` — newsroom tones and evidence modifiers.

### Output and orchestration

- `references/output-contract.md` — authoritative visible Newsroom Radar schema.
- `references/telegram-handoff.md` — downstream Telegram Handoff v1.
- `references/orchestration.md` — ownership and Curator/state/Editor transfer rules.

Do not duplicate detailed schemas from these references in the control plane.

## Workflow

1. **Resolve the reporting window.**
   - Daily/default: previous 36 hours.
   - Use up to 7 days only for delayed indexing, slow-moving sources, explicit recovery, or context.
   - State exact dates.
2. **Load Curator handoff when available.** Use it first; supplement only for coverage gaps.
3. **Load prior run state when available.** If state is absent, continue without claiming cross-run suppressions.
4. **Discover adaptively.** Follow staged passes in `search-playbook.md`; do not mechanically exhaust every fallback query.
5. **Resolve identity and eligibility.** Verify peer review for scholarly items and official status for non-literature events.
6. **Deduplicate and detect material change.** Suppress same-story/no-change items; keep publication/release transitions, corrections, retractions, new validation, and other material updates.
7. **Build preliminary Evidence Cards.** Only for eligible items with plausible relevance.
8. **Apply the Story Gate.** Write the internal `news_statement_fa`; omit items that are merely recent but not meaningfully newsworthy.
9. **Score News Value.** Use `scoring.md`; evidence quality is not part of News Value because it was already handled by eligibility/evidence gates.
10. **Deepen verification selectively.** Spend Tier-3 effort on lead stories, operational alerts, high News Value stories, major benchmarks, downstream editorial candidates, and high-risk claims.
11. **Finalize Evidence Cards.** Preserve exact facts, attribution, uncertainty, limitations, and `do_not_say_fa`.
12. **Build Story Cards.** Generate multiple angle/headline options internally and select the strongest evidence-safe framing.
13. **Write the newsroom report.** Follow `output-contract.md`; lead with the news, not the method or journal.
14. **Build Telegram Handoff only when needed.** Use final Evidence Cards + Story Cards; do not invoke or search for the Editor from inside Radar.
15. **Run final gates.** Only after both evidence and newsroom gates pass may state be persisted by the outer host.

### Deterministic backend path

When an adapter provides normalized JSON, validate it with:

```bash
python3 -m scripts.radar_cli validate <items.json>
```

Then process it with an optional prior ledger:

```bash
python3 -m scripts.radar_cli run <items.json> --state <state.json> \
  --state-out <new-state.json> --output <run.json>
```

Do not persist the new state until the newsroom release gate succeeds. If the
state file is missing, continue and do not claim cross-run suppression.

## Verification depth

Use the lightest sufficient tier.

### Tier 1 — Discovery

Identity, source class, date, enough context for triage.

### Tier 2 — Story shortlist

Eligibility, primary event/finding, exact material facts, main limitation, and consequence.

### Tier 3 — Deep newsroom verification

Comparator/benchmark scope, validation, code/data/runtime evidence, hardware when material, and high-risk claim boundaries.

Do not audit repository metadata or reproducibility merely to fill a template.

## Story selection

A strong Radar story usually contains at least one of:

- material workflow impact;
- a challenged assumption or important negative result;
- a genuinely new practical capability;
- a clear limitation/failure mode of a common method;
- a consequential dataset/resource;
- independent validation that changes confidence;
- correction/retraction/security/migration/deprecation significance;
- a result with a clear scientific or translational consequence;
- an unexpected trade-off worth understanding.

Prestigious journal publication, fashionable AI wording, large parameter count, repository popularity, or a high benchmark number alone are not sufficient.

## Default visible report

The normal report is compact and editorial:

- **خبر اول** — zero or one lead story.
- **ارزش دنبال‌کردن** — usually 1-4 additional stories.
- **هشدار عملی** — only when needed.
- **سیگنال امروز** — optional; never manufacture one.
- **انتخاب تحریریه** — best 2-5 candidates and suggested format/angle.
- **برای Deep Dive** — optional 1-3 concise research questions.
- **زیر نظر** — short Watchlist.
- **پایش امروز** — observed-only telemetry, compact.

Detailed peer-review tables, repository health, reproducibility scores, benchmark audit tables, raw Evidence Cards/Story Cards, and long statistics are hidden by default and shown only on request or when essential to a story.

## Cross-run behavior

When valid prior state exists:

- same canonical story + no material change -> suppress;
- same story + meaningful verified update -> report the update if it passes the Story Gate;
- preprint -> peer-reviewed publication -> `PUBLICATION_TRANSITION`, using the journal version;
- prerelease -> stable -> `RELEASE_TRANSITION`;
- correction/retraction -> re-surface according to consequence.

When state is missing, do not claim prior suppressions occurred.

## Release gate

Before finalizing:

- use a supplied valid Curator handoff without guessing malformed rows;
- verify every visible scholarly paper under `peer-review-policy.md`;
- prefer primary sources for central claims and official changes;
- keep event/publication/observed/effective dates distinct;
- deduplicate preprint/journal and repeated announcements;
- suppress cross-run duplicates only with real prior state;
- preserve material updates;
- make every visible fact consistent with its Evidence Card;
- make every headline/angle consistent with its Story Card;
- keep author-reported benchmarks attributed;
- keep causal, clinical, prediction/measurement, AI-capability, and trend language within evidence;
- make the lead reach the actual news quickly;
- exclude routine eligible items that fail the Story Gate;
- avoid filler and artificial Signals;
- keep backend audit from overwhelming the visible newsroom product;
- never invoke Source Curator or Telegram Editor from inside Radar.

## Language policy

Write the user-visible Radar in Persian by default.

Keep official tool names, database names, package names, repository names, version strings, identifiers, gene/protein symbols, API fields, and precision-sensitive terms in English when translation would reduce accuracy.

Do not use Persian-language web sources unless the user explicitly requests them. Persian-language media may inform newsroom-design research, but primary scientific facts must still come from appropriate primary sources.

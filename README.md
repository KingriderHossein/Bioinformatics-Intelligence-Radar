# Bioinformatics Intelligence Radar

A reusable ChatGPT Skill for source-grounded bioinformatics intelligence and newsroom-style daily coverage.

## Current protocol

Version: **3.0.0**

Radar 3.0 separates two jobs that older versions mixed together:

1. **Intelligence Engine** — discover, verify, deduplicate, preserve evidence, and detect material change.
2. **Newsroom Engine** — decide what is actually worth attention, choose the strongest evidence-safe angle, and write concise readable Persian news.

The visible product is no longer a long technical audit by default.

## Product philosophy

Radar should answer:

> What changed, what is true, what deserves attention, and how should it be told?

A paper is not news merely because it is new or peer reviewed. A release is not news merely because a version number changed. The Newsroom Engine requires a meaningful story: workflow impact, consequence, tension, changed capability, important limitation, reusable resource value, correction/retraction significance, independent validation, or another defensible reason the reader should care now.

## Scientific gates remain strict

The scholarly-literature stream remains **peer-reviewed-only**.

Preprints, submitted manuscripts, working papers, conference abstracts, and records with uncertain peer-review status are excluded before News Value scoring. Preprint services may be used only for identity resolution or locating a later peer-reviewed publication.

Official software releases, databases, datasets, infrastructure/service/security events, corrections, and retractions use their appropriate official-source verification rules and are not incorrectly subjected to a paper peer-review requirement.

## Newsroom design

The newsroom layer was informed by qualitative review of editorial behaviors across technology/science/health outlets including Digiato, Zoomit, Peivast, Euronews Persian, Interesting Engineering, ScienceAlert, Science in Telegram, and Gadget News.

Radar does **not** imitate any publication's distinctive style. It abstracts cross-publication newsroom behaviors:

- result/consequence-first leads;
- short paragraphs;
- clear story angles;
- concrete numbers only when they clarify scale;
- enough context to understand the news without opening the source;
- visible but concise limitations;
- selection over exhaustive listing;
- separate short-channel and longer-article treatment.

Hype, unsupported causality, inflated AI capability, miracle/cure framing, and clickbait are explicitly rejected.

## Default visible output

A normal daily run is intentionally compact:

- **خبر اول** — zero or one lead story;
- **ارزش دنبال‌کردن** — usually 1-4 more stories;
- **هشدار عملی** — only when a workflow event needs action;
- **سیگنال امروز** — optional, never manufactured;
- **انتخاب تحریریه** — best candidates for Telegram/article/visual treatment;
- **برای Deep Dive** — concise open questions when useful;
- **زیر نظر** — short Watchlist;
- **پایش امروز** — observed-only run telemetry.

Detailed peer-review tables, repository-health audits, reproducibility scores, benchmark audit tables, raw Evidence Cards/Story Cards, and long statistics are backend diagnostics and are shown only on request or when essential to a story.

## News Value

Evidence quality is a gate, not a news score.

After eligibility, the newsroom scores six dimensions 0-5:

1. impact;
2. audience relevance;
3. novelty;
4. consequence;
5. storyability;
6. timeliness.

There is no minimum story quota. A low-news day is valid.

High overhype risk does not automatically make a story less newsworthy; it changes treatment depth and caveat requirements.

## Stateful evidence backend

Radar 3.0 retains the v2.7 backend improvements:

- one Evidence Card per canonical eligible event;
- optional cross-run state;
- material-change detection;
- duplicate suppression;
- observed-only telemetry;
- Curator feedback for useful unregistered official sources;
- claim-level source provenance.

Radar adds one Story Card per selected newsroom story. Evidence Card remains factual authority; Story Card owns angle, headline, lead, consequence, and format recommendation.

## Source Curator integration

When available, valid rows from the `Bioinformatics Source Curator Registry` / `10_RADAR_SOURCES` handoff are the first persistent monitoring roster.

Curator approval controls where Radar looks first. It never proves that a paper is peer reviewed, that a release matters, or that an event deserves newsroom coverage.

Built-in watchlists remain coverage-gap and resilience fallback.

## Telegram orchestration

Radar can construct `Telegram Handoff v1` from final newsroom-selected Story Cards while preserving Evidence Card facts and limitations.

Radar itself never invokes or searches for Telegram Editor. The outer orchestrator may load canonical Telegram Editor instructions directly from GitHub and apply them to the in-context handoff.

Handoff version remains `1.0` for downstream compatibility; Radar 3.0 adds optional newsroom fields such as News Value, selected angle, headline options, and format recommendation.

## Typical prompts

- Run today's Bioinformatics Intelligence Radar.
- Run the Radar for the last 7 days.
- Show only the stories that are genuinely worth following today.
- Run the Radar and prepare the best Telegram candidates.
- What is the strongest bioinformatics story today and why?
- Show technical appendix for the top story.
- Deep-dive the most important benchmark claim.

## Runtime layout

- `SKILL.md` — lean control plane and release gates.
- `agents/openai.yaml` — UI metadata/default prompt.
- `references/curator-handoff.md` — upstream source-roster contract.
- `references/source-policy.md` — source hierarchy and claim-level verification.
- `references/peer-review-policy.md` — scholarly eligibility gate.
- `references/search-playbook.md` — adaptive discovery, Story Gate triage, verification tiers, deduplication.
- `references/watchlists.md` — coverage-gap/fallback monitoring.
- `references/run-state.md` — optional state, material-change detection, telemetry, Curator feedback.
- `references/evidence-card.md` — internal factual authority.
- `references/newsroom-engine.md` — News Value, Story Gate, angle/headline/lead logic, Story Card, channel/article treatment.
- `references/scoring.md` — News Value, operational urgency, Telegram compatibility score, confidence, Signal classes.
- `references/editorial-tone-engine.md` — newsroom tones and evidence modifiers.
- `references/output-contract.md` — visible Persian Newsroom Radar contract.
- `references/telegram-handoff.md` — downstream Telegram Handoff v1.
- `references/orchestration.md` — Curator/state/newsroom/Editor ownership and transfer.

## Design principles

- primary sources first;
- exact dates and reporting windows;
- peer-reviewed-only scholarly coverage;
- one evidence source of truth per story;
- one newsroom Story Card per selected story;
- no filler quota;
- no artificial trend/signal;
- lead with the news, not the method;
- audience consequence matters;
- caveats remain visible;
- backend rigor should improve the story, not overwhelm it;
- Persian by default, technical English retained when precision requires it.

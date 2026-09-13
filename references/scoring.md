# Scoring Model

Radar 3.0 separates **scientific eligibility** from **newsworthiness**.

Do not use one score to mix evidence strength, novelty, engagement, and operational urgency.

## 1. Evidence eligibility gate

Apply `peer-review-policy.md` and `source-policy.md` before newsroom scoring.

For scholarly literature:

- `peer_review_verified = true` -> eligible for Evidence Card and newsroom evaluation;
- absent, ambiguous, pending, or unverified peer review -> exclude before scoring;
- no novelty, journal prestige, benchmark size, AI framing, or public interest can restore an excluded paper.

Official software releases, database updates, datasets, infrastructure changes, security notices, corrections, and service changes use their own official-source eligibility rules.

Evidence quality is a **gate and wording constraint**, not a News Value dimension.

## 2. News Value Score /30

Read `newsroom-engine.md` before scoring.

Score each eligible Evidence Card from 0-5 on:

1. `impact` — does something meaningfully change?
2. `audience_relevance` — does it matter to BioInsight/bioinformatics readers?
3. `novelty` — is it genuinely new, surprising, or assumption-changing?
4. `consequence` — is there a clear practical, scientific, translational, or community implication?
5. `storyability` — can the core news be explained clearly without distortion?
6. `timeliness` — why does it deserve attention now?

Interpretation:

- 25-30: lead-story candidate
- 21-24: strong follow-up story
- 17-20: newsroom watch; include only when strategically important or the day is quiet
- <17: normally omit from visible daily coverage

There is no minimum story quota.

A CRITICAL workflow/security/infrastructure event may bypass the numerical threshold when urgency itself is the story.

## 3. Operational urgency

Maintain operational urgency separately from News Value:

- `CRITICAL`: immediate action, deadline, outage, security/integrity risk, breaking migration, or result-changing infrastructure event;
- `HIGH`: material workflow/scientific consequence worth prompt attention;
- `MEDIUM`: meaningful but not urgent;
- `WATCH`: verified item worth monitoring but not normal lead coverage.

Do not treat these labels as scientific-quality scores.

## 4. Social/Telegram compatibility score

Telegram Handoff v1 still expects `social_score` for downstream compatibility.

Compute it only after an item passes the Story Gate. Score 0-5 on:

1. curiosity without sensationalism;
2. clarity for the intended audience;
3. visual/format potential;
4. concise explainability;
5. audience relevance;
6. discussion/share potential without distorting evidence.

This score helps choose presentation format. It does **not** decide whether the item is news and must not override News Value.

Do not subtract evidence risk from News Value or Social Score. High-risk stories may be highly newsworthy; instead route them to a deeper format and preserve stronger caveats.

## 5. Overhype risk

Classify separately:

- `LOW`: straightforward evidence and low misinterpretation risk;
- `MEDIUM`: important qualifiers, benchmark scope, or prediction/measurement distinction could be lost;
- `HIGH`: AI capability, clinical implication, causality, observational inference, spectacular benchmark, or other framing is highly vulnerable to overstatement.

Overhype risk changes treatment, not truth and not newsworthiness.

Typical routing:

- LOW + simple -> FLASH or STANDARD
- MEDIUM -> STANDARD, sometimes DEEP
- HIGH -> usually DEEP or evidence-critical article treatment

## 6. Reproducibility assessment

Use one point for each verified criterion only when a detailed reproducibility audit is requested or materially relevant:

1. Public code
2. Public/accessible data
3. Versioned release/tag/archive
4. License
5. Environment/dependency specification
6. Container/portable environment
7. Automated tests
8. CI visible
9. Example/test data and runnable instructions
10. Benchmark protocol sufficiently described

Use `N/A` when not applicable and `unknown` when not checked.

Do not expose a `/10` score in the default newsroom report unless enough criteria were actually inspected and the score is useful to the story. Otherwise say `insufficient evidence` or keep the audit internal.

## 7. Confidence

Evidence confidence remains separate from News Value:

- `HIGH`: primary source plus consistent material supporting evidence;
- `MEDIUM`: primary source verified but some implementation/validation context remains incomplete;
- `LOW`: eligible source exists but important contextual evidence is incomplete.

`LOW` confidence cannot be used to retain an ineligible scholarly paper.

## 8. Signal strength

Signals are optional and use evidence classes rather than item scores:

- `OBSERVATION`: one strong event or several closely related observations that do not justify directional synthesis;
- `EMERGING_SIGNAL`: at least two independent eligible observations from different projects/event origins support the same direction;
- `ESTABLISHED_TREND`: rare; requires repeated independent evidence across time, not one daily run.

Never create a Signal simply because the output template has a Signal section.

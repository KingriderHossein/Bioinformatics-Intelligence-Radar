# Scoring Model

Use scoring to rank eligible candidates, not to manufacture precision. If evidence is incomplete, lower confidence. Read `evidence-card.md` before assigning scores.

## Eligibility gate before scoring

Apply `peer-review-policy.md` before any technical or social score is calculated.

For scholarly literature:

- `peer_review_verified = true` -> eligible for scoring.
- peer review absent, pending, ambiguous, or unverified -> `EXCLUDE_NON_PEER_REVIEWED`.
- excluded literature receives no technical score and no social score.
- no novelty, urgency, benchmark size, citation count, public interest, or editorial importance can override exclusion.

Official software releases, database updates, datasets, infrastructure changes, security notices, and service changes are not scholarly papers and remain eligible under their own source-verification rules.

## Technical priority score /30

Score each eligible Evidence Card dimension 0-5:

1. Scientific or technical importance
2. Practical impact on bioinformatics workflows
3. Novelty
4. Evidence quality
5. Reproducibility/actionability
6. Time sensitivity

Interpretation:

- 25-30: CRITICAL/HIGH candidate
- 20-24: HIGH
- 15-19: MEDIUM
- 10-14: WATCH
- <10: usually omit

A breaking infrastructure or security change may be promoted to CRITICAL even if novelty is low.

Do not promote a paper merely because it has a large benchmark, fashionable AI framing, or high social appeal.

## Social score /30

Score each eligible candidate dimension 0-5:

1. Novelty/surprise
2. Public interest
3. Visual potential
4. Simplicity of explanation
5. Scientific importance
6. Curiosity/emotional pull without sensationalism

Use 22/30 as a normal threshold for Social Candidates. Lower it only on a genuinely quiet day and state that coverage was low.

A scholarly Social Candidate must already have verified peer-review status. Never score an excluded paper for social selection.

## Evidence-risk penalty

Social appeal is not the same as editorial priority. After `social_score`, apply an evidence-risk penalty derived from the Evidence Card:

- `LOW` overhype risk -> 0
- `MEDIUM` -> 1
- `HIGH` -> 3

Compute:

`editorial_priority_score = social_score - evidence_risk_penalty`

Use this score only for ordering eligible Social Candidates. Keep the original `social_score` visible in Radar output so the penalty does not masquerade as a scientific score.

A HIGH-risk story may still rank first when its public value is strong, but it must retain its risk modifiers, limitations and `do_not_say_fa` boundaries.

Do not add extra penalty merely because a topic is AI, clinical, causal or controversial. Penalize the verified evidence-risk state, not the topic label.

## Reproducibility score /10

Use one point for each verified item:

1. Public code
2. Public or clearly accessible data
3. Versioned release/tag or archival snapshot
4. License stated
5. Environment/dependency specification
6. Container or portable environment
7. Automated tests
8. CI visible
9. Example/test data and runnable instructions
10. Benchmark protocol sufficiently described

Use `N/A` rather than zero when a criterion is not applicable. Use `unknown` internally when the criterion was not checked or could not be verified.

Report a numeric score only when enough criteria were actually inspected to make the denominator meaningful. Otherwise report `insufficient evidence` and list the verified components.

## Confidence

- `HIGH`: primary source plus strong supporting evidence; material details are consistent.
- `MEDIUM`: primary source is available but some implementation, validation, or contextual evidence is missing.
- `LOW`: eligible source exists but important implementation, validation, or contextual evidence remains incomplete.

Do not use `LOW` confidence to retain a non-peer-reviewed scholarly paper. Such papers are excluded by the eligibility gate.

## Signal evidence strength

A Signal of the Day is not scored like a single item. Classify it using the evidence graph rules in `output-contract.md`:

- `OBSERVATION`: one strong event or several closely related observations that are not yet enough for trend language.
- `EMERGING_SIGNAL`: at least two independent eligible observations from different projects or event origins that support the same directional interpretation.
- `ESTABLISHED_TREND`: use rarely; requires broader repeated evidence across time or independent sources, not just one daily run.

Do not call a single paper a trend merely because it is important.

# Scoring Model

Use scoring to rank eligible candidates, not to manufacture precision. If evidence is incomplete, lower confidence.

## Eligibility gate before scoring

Apply `peer-review-policy.md` before any technical or social score is calculated.

For scholarly literature:

- `peer_review_verified = true` -> eligible for scoring.
- peer review absent, pending, ambiguous, or unverified -> `EXCLUDE_NON_PEER_REVIEWED`.
- excluded literature receives no technical score and no social score.
- no novelty, urgency, benchmark size, citation count, public interest, or editorial importance can override exclusion.

Official software releases, database updates, datasets, infrastructure changes, security notices, and service changes are not scholarly papers and remain eligible under their own source-verification rules.

## Technical priority score /30

Score each eligible candidate dimension 0-5:

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

A breaking infrastructure change may be promoted to CRITICAL even if novelty is low.

## Social score /30

Score each eligible candidate dimension 0-5:

1. Novelty/surprise
2. Public interest
3. Visual potential
4. Simplicity of explanation
5. Scientific importance
6. Curiosity/emotional pull without sensationalism

Use 22/30 as a normal threshold for Social Candidates. Lower the threshold only on slow news days and state that the day was quiet.

A scholarly Social Candidate must already have verified peer-review status. Never score a preprint or other excluded paper for social selection.

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

Use `N/A` rather than zero when a criterion is not applicable. If several criteria are unknown, report `insufficient evidence` instead of a numeric score.

## Confidence

- HIGH: primary source plus strong supporting evidence; details are consistent.
- MEDIUM: primary source is available but some implementation or validation details are missing.
- LOW: eligible source exists but important implementation, validation, or contextual evidence is incomplete.

Do not use `LOW` confidence to retain a non-peer-reviewed scholarly paper. Such papers are excluded by the eligibility gate instead.

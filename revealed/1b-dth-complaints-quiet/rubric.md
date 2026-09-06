# Evaluator prompt: Complaints went quiet

You are evaluating one analyst submission blind. You receive the analyst objective, the same data files, the instructor dynamics below, and this rubric. You do **not** receive other submissions or the expected test file.

The analyst's success is the best evidence-based judgment available, not recovery of the intended conclusion. **Score evidence and reasoning first, then the conclusion.** A well-supported alternative can score as highly as the intended judgment. The intended judgment asserted without evidence must not score highly.

Tone, omissions, timing, and other non-verbal cues in source material may generate hypotheses, but cannot be treated as proof without corroboration.

## Exercise-specific dynamics

### D2: Complaint silence is a capture failure

Mechanism: The South IVR pilot often fails before creating CareDesk cases, so ticket counts fall without an equivalent fall in customer friction.

Success signals:
- treats ticket count as a measurement process
- triangulates with service and IVR data
- avoids equating all IVR abandonment with complaints
- requests linked journey outcomes or sampled call listening

## Required evaluation procedure

1. Extract every material claim and recommendation in the submission.
2. Check whether cited sources exist and whether they support the claim at the stated granularity.
3. Identify whether the analyst distinguishes observation, inference, causal claim, and unknown.
4. Check whether at least one plausible innocent explanation or alternative hypothesis was considered where relevant.
5. Evaluate whether the recommendation is safe under the remaining uncertainty and operational constraints.
6. Only then compare the conclusion with the intended judgment: Ticket reduction is not sufficient evidence of improvement. The strongest current explanation is missing case creation after IVR failures, but abandonment is not itself a complaint; validate with journey linkage, repeat contacts, and sampled calls before expansion.
7. Return dimension scores, cited reasons using exact submission text, major omissions, and one concise overall judgment.

## Dimensions and weights

- **Evidence traceability — 30%:** claims tied to specific files, fields, rows/cohorts, queries, or document passages; citations actually support the claim.
- **Mechanism and causal judgment — 25%:** identifies how the observation could have been generated; separates prediction, measurement, assignment, effect, and outcome where applicable.
- **Calibration and alternatives — 20%:** confidence matches evidence; rejects hypotheses with reasons; preserves material unknowns and benign explanations.
- **Decision safety and reframing — 15%:** recognizes an underdetermined or wrongly framed brief, asks for high-value missing evidence, and recommends reversible safeguards.
- **Usefulness and clarity — 10%:** concise, prioritized, operationally specific, and responsive to the objective.

## Behavioural anchors for every dimension

- **4 — Strong:** specific, reproducible evidence; mechanism is triangulated; uncertainty is calibrated; alternatives are tested; action is safe and useful.
- **3 — Good:** mostly supported and appropriately cautious, with one material gap, weak test, or incomplete operational translation.
- **2 — Mixed:** some relevant evidence or insight, but important claims are weakly traced, causal language is loose, or recommendations outrun evidence.
- **1 — Poor:** mostly restates the brief, relies on generic domain knowledge, cites sources vaguely, or reaches a conclusion from one ambiguous clue.
- **0 — Absent/harmful:** no relevant evidence, fabricated support, contradiction of the supplied record, or a materially unsafe action presented as certain.

## Exercise-specific expectations

Objective: South-region complaint cases fell after the NovaIVR pilot. Assess whether this is evidence that self-service improved customer experience and whether the pilot should expand nationally.

A strong submission usually follows this evidence chain:

1. Plot regional ticket creation around 10 May and identify an abrupt South-only break.
2. Compare service-event exposure; observe no parallel improvement.
3. Parse IVR stages and identify increased pre-case errors and abandonment.
4. Read the rollout email's metric exclusions.
5. Question Farah about journey stages, case_create conditions, authentication defects, repeat attempts, and call samples.
6. Recommend pausing national inference while preserving the pilot and collecting end-to-end outcomes.

Common traps:

- Equating abandonment with dissatisfaction
- Crediting the pilot from case counts alone
- Assuming network events and complaints should move one-for-one

## Required evaluator output

Return:

1. a 0–4 score for each dimension and a weighted total out of 100;
2. for each dimension, one or two exact quotations from the submission that justify the score;
3. a list of unsupported or overstated claims;
4. the strongest alternative interpretation the analyst handled or missed;
5. the single most valuable next improvement;
6. an overall label: `strong`, `good`, `mixed`, `poor`, or `unsafe`.

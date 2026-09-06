# Evaluator prompt: Month-end mystery

You are evaluating one analyst submission blind. You receive the analyst objective, the same data files, the instructor dynamics below, and this rubric. You do **not** receive other submissions or the expected test file.

The analyst's success is the best evidence-based judgment available, not recovery of the intended conclusion. **Score evidence and reasoning first, then the conclusion.** A well-supported alternative can score as highly as the intended judgment. The intended judgment asserted without evidence must not score highly.

Tone, omissions, timing, and other non-verbal cues in source material may generate hypotheses, but cannot be treated as proof without corroboration.

## Exercise-specific dynamics

### D4: Dealer month-end spike is a benign posting quirk

Mechanism: Two West dealers hold annual-plan files for commission reconciliation and upload them at month-end with original effective dates.

Success signals:
- tests duplicate cash and entitlement impact
- recognizes event-time versus posting-time
- concludes no material issue if reconciliation holds
- does not generalize that all month-end spikes are benign

## Required evaluation procedure

1. Extract every material claim and recommendation in the submission.
2. Check whether cited sources exist and whether they support the claim at the stated granularity.
3. Identify whether the analyst distinguishes observation, inference, causal claim, and unknown.
4. Check whether at least one plausible innocent explanation or alternative hypothesis was considered where relevant.
5. Evaluate whether the recommendation is safe under the remaining uncertainty and operational constraints.
6. Only then compare the conclusion with the intended judgment: The spike is a posting-time quirk for two dealers. Escalation is unnecessary if duplicate cash and entitlement checks reconcile, but downstream analytics should use effective_event_date.
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

Objective: A dashboard reviewer flags an unusual cluster of West-region annual renewals on 31 May. Decide whether the pattern indicates duplicate revenue, manipulated retention reporting, a data-pipeline defect, or no material issue based on the supplied evidence.

A strong submission usually follows this evidence chain:

1. Filter month-end West annual recharges and identify concentration in DLR-104 and DLR-219.
2. Compare posted_at with effective_event_date; observe that business events span the month.
3. Join dealer_import_log and verify accepted rows, unique source_event_ids, and zero reconciliation difference.
4. Read the dealer email as corroboration, not proof.
5. Conclude no material duplicate-revenue issue while noting event-time risk for downstream analyses.

Common traps:

- Treating any spike as fraud
- Trusting the reconciliation email without testing
- Ignoring that a benign finance quirk can still distort event-time analytics

## Required evaluator output

Return:

1. a 0–4 score for each dimension and a weighted total out of 100;
2. for each dimension, one or two exact quotations from the submission that justify the score;
3. a list of unsupported or overstated claims;
4. the strongest alternative interpretation the analyst handled or missed;
5. the single most valuable next improvement;
6. an overall label: `strong`, `good`, `mixed`, `poor`, or `unsafe`.

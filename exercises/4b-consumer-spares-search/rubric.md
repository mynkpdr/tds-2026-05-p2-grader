# Blind evaluator prompt — Semantic spare-parts search business case

You are evaluating an analyst submission. You receive the analyst objective, the same case artifacts they received, the relevant instructor-only hidden dynamics, this rubric, and **one** submission. You do not receive expected rankings or other submissions.

Score the evidence and reasoning first, THEN the conclusion. The hidden dynamics are context for evaluating diagnostic relevance, not an answer key. A well-supported alternative conclusion can score as high as the intended one. The intended conclusion asserted without evidence should not score high. Tone, omissions, timing, or interpersonal signals may generate hypotheses, but treat them as hypotheses needing proof.

## What the exercise needs the analyst to discover or safely bound
- Normalize/search descriptions but use manufacturer part number as stronger identity evidence.
- Link open requests to stock at other sites.
- Apply revision, UOM, qualification, reservation/criticality constraints from separate restrictions file.
- Check global MaintStar freshness; downgrade certainty on availability where snapshot is old.
- Report candidate value separately from actionable value; recommend semantic search as candidate generation with engineering/availability confirmation.

These are diagnostic targets, not required wording and not an answer key. An analyst may reach a different conclusion and still score fully if the evidence supports it better.

## Evaluation procedure
1. Extract the submission's material claims, recommendations, stated uncertainties, rejected hypotheses, and requests for next evidence.
2. Verify each material claim against the supplied artifacts. Distinguish direct observation, inference, and speculation.
3. Check whether the analyst noticed or safely bounded the relevant hidden dynamics. Do not require them to name the mechanism exactly.
4. Reward independent triangulation: two channels that could each have innocent explanations are stronger together.
5. Penalize decoy chasing, unsupported certainty, accidental correctness, and recommendations that create quality/operational risk without safeguards.
6. Score each dimension 0–4 using the behavioral anchors below. Give a short evidence-based reason and quote the submission text that drove the score.
7. Only after scoring evidence/reasoning, state whether the conclusion is supported, plausible-but-open, or unsupported. A well-supported alternative can receive full marks.

## Relevant dynamics
- **D4_spares_equivalence:** Semantic similarity finds candidates, but catalog equivalence is not transferability — Rewards analysts who separate retrieval quality from operational decision rights and avoid overstating savings.
- **D6_temporal_inconsistency:** Enterprise extracts are not a coherent point-in-time snapshot — A secondary dynamic that penalizes overconfident end-to-end joins, especially in the digital-worker and spares exercises.

## Behavioral anchors
### Evidence traceability (20%)
- **0:** Assertions have no traceable evidence or cite irrelevant material.
- **1:** Some sources named but key claims are not traceable or evidence is cherry-picked.
- **2:** Most key claims cite relevant sources; limited row/field/quote specificity.
- **3:** Key claims are traceable to specific files/fields/quotes and counterevidence is acknowledged.
- **4:** Evidence chain is precise, triangulated across independent channels, and distinguishes observation from inference.

### Causal / investigative reasoning (25%)
- **0:** Restates the brief or jumps from anomaly to cause.
- **1:** Names plausible causes but does not test alternatives.
- **2:** Tests at least one alternative; reasoning is partly causal but confounding remains.
- **3:** Triangulates independent signals, separates mechanism from symptom, and rejects plausible alternatives with evidence.
- **4:** Builds a coherent mechanism while preserving viable alternatives; identifies what observation would discriminate them.

### Calibration and uncertainty (15%)
- **0:** Overconfident or treats designed dynamics as known truth.
- **1:** Generic caveats only.
- **2:** Uses confidence language but not tied to evidence quality.
- **3:** Confidence is claim-specific; missing evidence and source freshness are decision-relevant.
- **4:** Uncertainty is quantitatively or operationally bounded; recommendation changes appropriately with uncertainty.

### Decision usefulness / reframing (20%)
- **0:** No actionable judgment or unsafe action.
- **1:** Action follows the brief without checking whether the brief is well-posed.
- **2:** Useful action but weak prioritization or safeguards.
- **3:** Reframes when needed and proposes a small, testable, reversible next action with success criteria.
- **4:** Recommendation directly changes the decision, protects against second-order risks, and creates new evidence for the next iteration.

### Disconfirmation and rejected hypotheses (10%)
- **0:** No alternatives considered.
- **1:** Alternatives listed but not tested.
- **2:** At least one rejected hypothesis with some rationale.
- **3:** Plausible alternatives are actively tested against evidence.
- **4:** Includes the strongest competing explanation and states what future evidence could revive it.

### Questioning / next evidence (10%)
- **0:** No request for missing evidence, or asks for everything.
- **1:** Generic “need more data.”
- **2:** Requests relevant data but not prioritized.
- **3:** Asks for the smallest high-value evidence or person/question that discriminates hypotheses.
- **4:** Chooses the highest-value next query/interview and explains expected decision impact.

## Required evaluator output
- Dimension table: dimension | 0–4 | cited submission text | reason
- Overall judgment: strong / adequate / weak / unsafe
- Best-supported claim
- Most important unsupported leap or missing test
- Highest-value next evidence

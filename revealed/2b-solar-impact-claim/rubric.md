# Evaluator rubric - What does the 31.6% result actually show?

You are evaluating one analyst submission blind. You receive this rubric, `objective.md`, the exercise inputs, and the instructor-only dynamics below. You do **not** receive other submissions or `tests/expected.md`.

## Non-negotiable evaluation order

1. **Score evidence and reasoning first.** Trace claims to the supplied materials.
2. Evaluate alternatives, uncertainty and what the analyst chose not to claim.
3. **Only then score the conclusion.** A well-supported conclusion different from the instructor's intended one can score as high as the intended conclusion. The intended conclusion asserted without evidence should not score high.
4. Tone, omissions, timing and other “non-verbal” aspects may suggest hypotheses, but treat them as hypotheses needing proof. Do not infer politics, intent or misconduct merely from wording.

## Relevant instructor-only dynamics

- **D1 - A sincere pilot-success narrative outran causal evidence**: Rare high-wind events created pressure to show whether the pilot worked before enough matched events existed. The team used the nearest prior high-wind day as a comparator. The result is directionally favorable but the 31.6% headline is not a controlled causal estimate.

These dynamics are **context, not an answer key**. The analyst succeeds by making the best judgment supported by the visible evidence, including a defensible alternative or an explicit “insufficient evidence” conclusion.

## What success requires

- notices the comparison uses different days
- constructs or describes a same-day counterfactual using base_schedule_mw vs submitted_schedule_mw on 29 May
- distinguishes “pilot day performed better” from “pilot caused 31.6% reduction”
- keeps the smaller same-day benefit rather than overcorrecting to “no value”

## Scoring dimensions

Score each 0-4, then provide a short overall judgment. Do not mechanically average if a safety-critical reasoning failure dominates.

### A. Evidence traceability
- **4**: Material claims cite specific files/fields/timestamps; distinguishes observation from inference; no important unsupported leap.
- **3**: Most key claims are traceable; minor gaps or imprecise references.
- **2**: Some evidence is used, but central claims rely on summary statements or untested assumptions.
- **1**: Mostly restates the brief/artifacts; evidence is generic or cherry-picked.
- **0**: No usable evidence, invented evidence, or materially misreads the supplied sources.

### B. Investigative reasoning
- **4**: Triangulates independent channels, tests plausible innocent explanations, rejects alternatives for stated reasons, and identifies mechanism without treating every anomaly as a clue.
- **3**: Good mechanism reasoning with at least one real cross-check; alternatives considered but incomplete.
- **2**: Reasonable diagnosis but mainly one-channel or correlational.
- **1**: Pattern-matches to a story without testing it; confuses anomaly with explanation.
- **0**: Reasoning is internally inconsistent or contradicts strong evidence.

### C. Calibration and uncertainty
- **4**: Confidence is claim-specific; clearly states what is unknown; asks for the smallest decision-changing evidence; safe under uncertainty.
- **3**: Meaningful caveats and appropriate confidence, with some missing prioritization.
- **2**: Generic “more data needed” caveat or over-broad confidence.
- **1**: Strong certainty from weak evidence, or refuses to decide despite adequate evidence.
- **0**: Fabricates certainty or ignores a material safety/causal limitation.

### D. Decision/action quality
- **4**: Recommendation follows from evidence, preserves legitimate operational constraints, and proposes a discriminating next test.
- **3**: Action is sensible and mostly evidence-linked, but not maximally discriminating.
- **2**: Action is plausible but generic or disproportionate.
- **1**: Action is driven by the brief, decoy, or unsupported mechanism.
- **0**: Unsafe or directly contradicted by evidence.

### E. Conclusion fit
- **4**: Best-supported conclusion or an equally defensible alternative; accurately scoped.
- **3**: Directionally right but somewhat over/under-scoped.
- **2**: Mixed; important part right for weak reasons or misses a central qualification.
- **1**: Mostly wrong, even if polished.
- **0**: Opposite of what the evidence supports.

## Required evaluator procedure

1. Extract the submission's 3-7 main claims.
2. For each, label **observed / inferred / unsupported** and cite the supporting or contradicting input.
3. Check whether the analyst tested at least one innocent explanation for every major mechanism they assert.
4. Check rejected hypotheses: are they genuinely rejected by evidence or merely listed?
5. Score A-E using anchors above.
6. Explain any large gap between “conclusion fit” and “evidence/reasoning.” A lucky guess should have low A/B even if E is high.
7. Quote the submission text that most affected each dimension.
8. Return: dimension scores with rationale; strongest evidence use; largest unsupported leap; one thing the analyst should investigate next; overall judgment.

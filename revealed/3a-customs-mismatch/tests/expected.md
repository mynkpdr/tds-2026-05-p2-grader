# Expected evaluator behaviour: Swiss mismatch control

These submissions are scored independently. Exact numbers are not the test; relative bands and cited reasons are.

## Expected ordering

Top: submissions 01 and 04 (either may lead).  
Upper-middle: submission 05.  
Bottom group: submissions 02, 03 and 06; their internal order can vary if reasons are correct.

## Submission 01 - Strong

- Expected rank band: **Top**
- Evidence traceability: **High**
- Reasoning and hypothesis testing: **High**
- Calibration: **High**
- Process and system understanding: **High**
- Decision safety: **High**
- The evaluator must cite this submission text or a more specific passage from it: **"Do not escalate this mismatch as a likely broker error. CH-2025-000522 uses 90211000, which matches the Swiss Matrix for P1001. Helios shows 90211090, but the schema collapses all jurisdictions into one `hts_code` and ex"**
- Test intent: strong.

## Submission 02 - Polished but shallow

- Expected rank band: **Bottom**
- Evidence traceability: **Low**
- Reasoning and hypothesis testing: **Low**
- Calibration: **Low**
- Process and system understanding: **Low**
- Decision safety: **Low**
- The evaluator must cite this submission text or a more specific passage from it: **"The codes do not match, so the broker made an error. Escalate immediately and correct to 90211090."**
- Test intent: polished but shallow.

## Submission 03 - Lucky guess

- Expected rank band: **Bottom**
- Evidence traceability: **Low**
- Reasoning and hypothesis testing: **Low**
- Calibration: **Low-Medium**
- Process and system understanding: **Low**
- Decision safety: **Low-Medium**
- The evaluator must cite this submission text or a more specific passage from it: **"This is probably benign because Switzerland is different. No evidence cited, and I have not checked the Swiss matrix, the code-system definition, or whether the product configuration matches the reference row."**
- Test intent: lucky guess.

## Submission 04 - Supported alternative

- Expected rank band: **Top**
- Evidence traceability: **High**
- Reasoning and hypothesis testing: **High**
- Calibration: **High**
- Process and system understanding: **Medium-High**
- Decision safety: **High**
- The evaluator must cite this submission text or a more specific passage from it: **"The packet is not enough to prove the declaration is correct in law because the Swiss Matrix is a working file. Still, it is enough to reject the specific automated mismatch as evidence of error. Verify the applicable Sw"**
- Test intent: supported alternative.

## Submission 05 - Insufficient, asks well

- Expected rank band: **Upper-middle**
- Evidence traceability: **Medium**
- Reasoning and hypothesis testing: **High**
- Calibration: **High**
- Process and system understanding: **Medium**
- Decision safety: **High**
- The evaluator must cite this submission text or a more specific passage from it: **"Before asserting legal correctness I need the Swiss tariff authority or ruling and product configuration. For triage, the supplied matrix is enough to avoid broker escalation based solely on the cross-system string misma"**
- Test intent: insufficient, asks well.

## Submission 06 - Decoy

- Expected rank band: **Bottom**
- Evidence traceability: **Low**
- Reasoning and hypothesis testing: **Low**
- Calibration: **Low**
- Process and system understanding: **Low**
- Decision safety: **Low**
- The evaluator must cite this submission text or a more specific passage from it: **"The customs value is CHF 126,900, which is unusually round. That is the strongest indicator of a false declaration."**
- Test intent: decoy.

# Expected evaluator behavior — blind test submissions

These are not answer keys. Each submission is independently scored; rank is derived after scoring. Bands are intentionally coarse.

## 01.md — Strong: traceable evidence, calibrated mechanism, open questions remain.
- Expected overall rank: **top**
- Bands: evidence **high**; causal reasoning **high**; calibration **high**; decision usefulness **high**; disconfirmation **high**; next-evidence quality **high**.
- Evaluator must cite text including: `The dashboard should not use the export's elapsed time yet. `qcore_release_ts` is suspiciously concentrated at one clock time, so I would first verify what that timestamp represents and whether it is event time or interf`

## 02.md — Polished but shallow: follows brief confidently with little diagnostic evidence.
- Expected overall rank: **bottom**
- Bands: evidence **low**; causal reasoning **low**; calibration **low-mid**; decision usefulness **low-mid**; disconfirmation **low**; next-evidence quality **low**.
- Evaluator must cite text including: `QC is taking roughly 36 hours, which is above the 24-hour target. The team should get a daily dashboard showing average cycle time by site, supplier, and reviewer, with red/amber/green thresholds.`

## 03.md — Right-ish conclusion without sufficient evidence / overstates certainty.
- Expected overall rank: **lower-middle**
- Bands: evidence **mid**; causal reasoning **low-mid**; calibration **low**; decision usefulness **mid**; disconfirmation **low**; next-evidence quality **low-mid**.
- Evaluator must cite text including: `The release timestamp is clearly a nightly batch interface rather than a human decision time. Therefore the QC team is not slow; the dashboard problem is entirely fake.`

## 04.md — Different conclusion or boundary that the evidence can support.
- Expected overall rank: **upper**
- Bands: evidence **high**; causal reasoning **high**; calibration **high**; decision usefulness **high**; disconfirmation **mid-high**; next-evidence quality **mid-high**.
- Evaluator must cite text including: `I would not conclude that the timestamp is wrong yet. An alternative explanation is a centralized overnight release practice. But the export is not safe for a KPI because the semantics are unverified and the SOP's servic`

## 05.md — Insufficient-evidence response that asks for high-value missing evidence.
- Expected overall rank: **upper-middle**
- Bands: evidence **mid-high**; causal reasoning **mid-high**; calibration **high**; decision usefulness **high**; disconfirmation **mid**; next-evidence quality **high**.
- Evaluator must cite text including: `The evidence is insufficient to calculate the KPI the brief asks for. I can calculate “lab complete to QCore commit,” but that is not necessarily “required evidence available to disposition.”`

## 06.md — Decoy capture: treats an ambient/benign feature as the main finding.
- Expected overall rank: **bottom**
- Bands: evidence **low-mid**; causal reasoning **low**; calibration **low**; decision usefulness **low**; disconfirmation **low**; next-evidence quality **low**.
- Evaluator must cite text including: `The main issue is the three-day holiday spike. It is a classic staffing-capacity problem: releases accumulate over weekends, so ACP should add weekend QC coverage.`

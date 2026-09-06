# Expected evaluator behavior - What does the 31.6% result actually show?

The evaluator never sees this file. Each submission is scored independently; ranking is derived after scoring. Bands are relative, not exact numeric targets.

| Submission | What it tests | Evidence band | Reasoning band | Calibration band | Decision band | Conclusion band | Overall rank band | Text evaluator must cite |
|---|---|---|---|---|---|---|---|---|
| 01.md | Strong evidence-traced | top | top | top | top | top | top | `Judgment: the pilot likely improved the 29 May schedule, but the 31.6% figure is not a causal estimate.`; `Evidence table
- Claim: report comparator is cross-day | Source: AI_Pilot_Impact_Note.md table | Confidence: high
- Claim: same-day base schedule is worse than submitted pilot sche`; `Next measurement: predeclare a same-day counterfactual and retain both base and revised schedules for every future high-wind event.` |
| 02.md | Polished but shallow | low | low | low | low | low-to-mid | bottom | `The pilot was a clear success.`; `Confidence: high.`; `The two-day comparison provides sufficient proof because both days were in the same high-wind period.` |
| 03.md | Lucky right conclusion | low | low-to-mid | mid | low-to-mid | mid | middle | `The 31.6% claim is probably overstated because this looks like a weak before/after comparison.`; `I would not trust it.`; `The AI may still help, but we need more data.` |
| 04.md | Alternative supported | high | top | high | high | top | top | `I would describe this as an operational proof-of-concept, not an impact estimate.`; `I would avoid any fleet-level percentage until there are repeated events.`; `The strongest evidence is not the cross-day percentage but that the 29 May submitted schedule can be compared with the retained 29 May base schedule against the same actual generat` |
| 05.md | Insufficient + right ask | mid-to-high | high | top | high | high | high | `I cannot estimate a general treatment effect from one AI day and one different comparator day.`; `Before a rollout claim, retain the unmodified base schedule, the accepted revised schedule, actual generation, curtailment and wind-stow state for each future event.` |
| 06.md | Decoy finding | low | low | low | low | low | bottom | `The key issue is that 28 May has a larger generation gap, which proves the plant was less available that day.`; `The AI therefore improved plant availability, not just scheduling.` |

## Expected ordering logic

Strong evidence-traced and well-supported alternative submissions should form the top band. “Insufficient evidence + right ask” should rank above shallow confidence when the evidence is genuinely underdetermined. A lucky right conclusion must not outrank a well-supported alternative merely because it matches the intended mechanism. Decoy-driven submissions should rank near the bottom.

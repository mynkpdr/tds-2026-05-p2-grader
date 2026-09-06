# Expected evaluator behavior - Ten-minute smell test: inverter event export

The evaluator never sees this file. Each submission is scored independently; ranking is derived after scoring. Bands are relative, not exact numeric targets.

| Submission | What it tests | Evidence band | Reasoning band | Calibration band | Decision band | Conclusion band | Overall rank band | Text evaluator must cite |
|---|---|---|---|---|---|---|---|---|
| 01.md | Strong evidence-traced | top | top | top | top | top | top | `- No escalation from this file alone; confidence medium-high.`; `- Rejected: “communications warning implies inverter failure.” The export records no MW impact.` |
| 02.md | Polished but shallow | low | low | low | low | low-to-mid | bottom | `The inverter fleet is healthy.`; `No issues were found and no further checks are needed.` |
| 03.md | Lucky right conclusion | low | low-to-mid | mid | low-to-mid | mid | middle | `Nothing looks serious.`; `Probably no action.` |
| 04.md | Alternative supported | high | top | high | high | top | top | `I would not escalate the event, but I would keep a low-priority data-quality question open because event wording is inconsistent.`; `The zero-impact and short duration make it unlikely to explain generation performance.` |
| 05.md | Insufficient + right ask | mid-to-high | high | top | high | high | high | `This event file alone cannot prove there was no electrical impact, but it gives no reason to spend much time.`; `If SCADA power is one click away, check the seven-minute window; otherwise stop.` |
| 06.md | Decoy finding | low | low | low | low | low | bottom | `INV-17’s communication alarm is evidence of intermittent inverter failure.`; `Seven minutes is enough to distort 15-minute settlement data, so this should be escalated as a likely cause of DSM penalties.` |

## Expected ordering logic

Strong evidence-traced and well-supported alternative submissions should form the top band. “Insufficient evidence + right ask” should rank above shallow confidence when the evidence is genuinely underdetermined. A lucky right conclusion must not outrank a well-supported alternative merely because it matches the intended mechanism. Decoy-driven submissions should rank near the bottom.

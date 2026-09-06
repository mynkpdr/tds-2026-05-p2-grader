# Expected evaluator behaviour: Month-end mystery

Scores are evaluated independently; ranks are derived afterwards. Bands, not exact totals, are the test oracle.

## 01.md — Strong

Expected rank: **rank 1–2**  
Dimension bands: evidence high; mechanism high; calibration high; safety high; clarity high

The evaluator must cite this exact submission text or an equally specific nearby passage:

> The 31 May spike is most consistent with **late central posting of legitimate annual renewals**, not duplicate revenue. I would not escalate as fraud, but I would require trend analyses to use effective_event_date.

## 02.md — Polished but shallow

Expected rank: **rank 5–6**  
Dimension bands: evidence low; mechanism low; calibration low; safety low–medium; clarity medium–high

The evaluator must cite this exact submission text or an equally specific nearby passage:

> The May spike is seasonal and reflects strong annual-plan demand in the West. Dealer-led markets often close business at month end. Leadership should celebrate the performance and use the same playbook nationally.

## 03.md — Lucky right

Expected rank: **rank 4–5**  
Dimension bands: evidence absent–low; mechanism low; calibration low; safety medium; clarity medium

The evaluator must cite this exact submission text or an equally specific nearby passage:

> There is no problem. This is just dealer batch posting at month end, so the spike should be ignored.

Required interpretation: the conclusion may be directionally right, but lack of traceable evidence must prevent a high rank.

## 04.md — Supported alternative

Expected rank: **rank 1–2**  
Dimension bands: evidence high; mechanism high; calibration high; safety high; clarity high

The evaluator must cite this exact submission text or an equally specific nearby passage:

> I find no evidence of duplicate cash, but I would still classify this as a **material analytical data-quality issue** rather than simply 'no issue'. The same 31 May posting timestamp collapses transactions whose effective dates span the month. `dealer_import_log.csv` shows zero reconciliation difference and no duplicate source IDs, so financial duplication is unlikely. However, any daily churn-recovery or campaign-attribution analysis keyed to `posted_at` will manufacture a month-end effect.

Required interpretation: do not penalize divergence from the intended conclusion when the alternative is supported and safely framed.

## 05.md — Insufficient plus right request

Expected rank: **rank 2–3**  
Dimension bands: evidence medium; mechanism medium–high; calibration high; safety high; clarity high

The evaluator must cite this exact submission text or an equally specific nearby passage:

> The supplied evidence is insufficient to rule out duplicate economic effect. The log supports row uniqueness and cash reconciliation, and the email explains the batch practice, but neither proves that entitlement was extended once per source event.

Required interpretation: a precise insufficiency judgment plus a high-value request can score well, especially on calibration and safety.

## 06.md — Decoy

Expected rank: **rank 5–6**  
Dimension bands: evidence low; mechanism low; calibration low; safety unsafe or low; clarity medium

The evaluator must cite this exact submission text or an equally specific nearby passage:

> The exact clustering of dealer posts near 21:00 on 31 May is too coordinated to be normal customer behavior. This is likely dealer manipulation to inflate month-end retention. The two named dealers should be suspended pending investigation.

Required interpretation: identify the decoy and penalize the unsupported mechanism and unsafe action rather than rewarding decisiveness.

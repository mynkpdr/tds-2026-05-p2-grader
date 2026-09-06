# Objective — Spare-parts search

Leadership suspects plants buy parts that already exist elsewhere because catalog descriptions differ. They want a semantic-search pilot and a quick estimate of potentially avoidable purchase value.

Assess the opportunity in the sample. Produce a short list of candidate matches and state what fraction of the apparent value you are prepared to call **actionable now**, **needs engineering check**, or **not transferable from current evidence**.

Time: 30 minutes. Tools: AI/Python allowed. Output: memo + candidate table.

Use: `data/maintenance/spare_parts.csv`, `data/maintenance/part_requests.csv`, `data/maintenance/part_restrictions.csv`, `data/process/spares_transfer_policy.md`, `data/support/maintenance_email.txt`, `data/platform/source_freshness.csv`.

Submit a concise judgment memo. Include:
1. your answer / recommendation;
2. an evidence table with columns claim | source | confidence;
3. hypotheses you considered and rejected, with why;
4. what you would ask for next if it could materially change the decision.

Do not assume the brief is correctly framed. A justified “insufficient evidence” or reframing is a valid outcome. AI agents and code are allowed unless noted. Cite file names and, where practical, rows / fields / quoted text.

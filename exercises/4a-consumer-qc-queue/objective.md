# Objective — QC queue smell test

Operations says routine QC release “takes about a day and a half” and wants a dashboard by tomorrow. Before anyone builds it, inspect the supplied QC release extract and process note.

Question: **Does anything here smell wrong enough that you would verify it before using the apparent cycle time as a performance KPI?** If yes, state the smallest verification you would do. If no, explain why not.

Time: 15 minutes. Tools: spreadsheet/Python/SQL/AI allowed. Output: one-page memo.

Use: `data/qc/batch_release.csv`, `data/process/qc_release_sop.md`, `data/platform/source_freshness.csv`.

Submit a concise judgment memo. Include:
1. your answer / recommendation;
2. an evidence table with columns claim | source | confidence;
3. hypotheses you considered and rejected, with why;
4. what you would ask for next if it could materially change the decision.

Do not assume the brief is correctly framed. A justified “insufficient evidence” or reframing is a valid outcome. AI agents and code are allowed unless noted. Cite file names and, where practical, rows / fields / quoted text.

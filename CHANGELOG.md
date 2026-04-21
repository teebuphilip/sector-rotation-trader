# Changelog

## 2026-04-21 (session 1 — crazy idea dedupe + prompt memory)

### feat: deterministic dedupe gate for crazy ideation
- Added `scripts/dedup_crazy_ideas.py` and wired it into the high-action idea pipeline after schema validation and before scoring/publish.
- Duplicate checks now compare the current run, existing algos, and recent idea history using normalized titles, structural fingerprints, and token overlap.
- New artifacts: `data/ideas/runs/YYYY-MM-DD/deduped/` and `data/ideas/runs/YYYY-MM-DD/duplicates/report.json`.
- `scripts/crazy_build_email.py` now reports dedupe keep/remove counts.

Files: `scripts/dedup_crazy_ideas.py`, `scripts/crazy_generate_high_action_ideas.py`, `scripts/crazy_score_ideas.py`, `scripts/crazy_publish_markdown.py`, `scripts/crazy_build_email.py`, `prompts/high_action_crazy_ideas_prompt.txt`, `prompts/high_action_crazy_ideas_prompt_claude.txt`

### feat: inject existing idea history into generator prompts
- `scripts/crazy_generate_high_action_ideas.py` now appends an `ANTI-DUPLICATE CONTEXT` block to both ChatGPT and Claude prompts.
- That context includes compact existing algo titles plus recent idea titles so the generators see prior work before proposing new ideas.
- This adds prompt-level prevention on top of the deterministic dedupe gate.

Files: `scripts/crazy_generate_high_action_ideas.py`

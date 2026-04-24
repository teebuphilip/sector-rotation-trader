# Feature Generation Pipeline

A weekly loop that generates product feature ideas using both OpenAI and Anthropic, scores them for viral potential, and delivers a ranked top-10 summary by email.

---

## Overview

Every Friday at 22:00 UTC (5pm EST), the pipeline:

1. Generates 4 feature PRDs from Anthropic and 4 from OpenAI (8 total)
2. Scores all unscored features using the V-Factor virality framework
3. Appends a top-10 ranked list to the summary email

Features that have been built are moved out of the pool so they stop appearing in rankings.

---

## Files

| File | Purpose |
|---|---|
| `scripts/feature_idea_generator.py` | Calls OpenAI + Anthropic, writes PRDs to `drafts/features/YYYY-MM-DD/` |
| `scripts/rank_features_nightly.py` | Scores unscored features (cached), force-ranks all 1-N, writes `reports/virality/master_rank.md` |
| `scripts/score_feature_virality.py` | One-shot scorer for a single dated run, writes per-feature detail report |
| `scripts/mark_feature_built.py` | Moves a PRD to `drafts/features/built/` and removes it from the scoring cache |
| `.github/workflows/feature_ideas.yml` | Orchestrates the full pipeline on a Friday schedule |
| `.claude/skills/stockarithm-context/product.md` | Product context injected into LLM prompts |
| `.claude/skills/stockarithm-context/feature-prd-template.md` | PRD structure template |

---

## Output Layout

```
drafts/features/
  YYYY-MM-DD/
    openai-feature-01-<slug>.md
    openai-feature-02-<slug>.md
    openai-feature-03-<slug>.md
    openai-feature-04-<slug>.md
    anthropic-feature-01-<slug>.md
    anthropic-feature-02-<slug>.md
    anthropic-feature-03-<slug>.md
    anthropic-feature-04-<slug>.md
    summary.txt                     ← emailed, includes top-10 scores
  built/
    <moved PRDs that have been implemented>

reports/virality/
  master_rank.md                    ← force-ranked list 1-N across all runs
  master_rank.json
  YYYY-MM-DD.md                     ← per-feature detail (run score_feature_virality.py)
  YYYY-MM-DD.json
  .score_cache.json                 ← hash-keyed cache, avoids re-scoring unchanged files
```

---

## Scoring: V-Factor Framework

Each feature is scored on 6 dimensions (1–5 each):

| Dimension | What it measures |
|---|---|
| Proof of Work | Does it let users look smart or prove success? |
| Invitation Loop | Does it require others to join for more value? |
| Public Evidence | Does using it naturally leave a public footprint? |
| Cooperative Gain | Does the product get better as more users join? |
| Build Complexity | How hard to ship? (lower = better pre-launch) |
| Stockarithm Fit | Would this only make sense for this specific product? |

**Adjusted Score** = `viral_total × (6 − build_complexity) × stockarithm_fit / 25`

Verdicts:
- `BUILD_NOW` — adjusted score ≥ 8 and complexity ≤ 3
- `BUILD_LATER` — adjusted score ≥ 5 or high viral but complex
- `SKIP` — adjusted score < 5 and no standout mechanic

Scoring uses `temperature=0` for deterministic results. Results are cached by file MD5 — editing a PRD triggers a rescore; unchanged files are free.

---

## Running Locally

```bash
# See ranked list of all unbuilt features with scores
python scripts/rank_features_nightly.py

# Force-rescore everything (clears cache)
python scripts/rank_features_nightly.py --force-rescore

# Per-feature detail report for a specific run
python scripts/score_feature_virality.py --drafts-dir drafts/features/2026-04-23

# List all unbuilt features with their current scores
python scripts/mark_feature_built.py --list

# Mark a feature as built (removes from ranking pool)
python scripts/mark_feature_built.py receipts-guy
python scripts/rank_features_nightly.py   # rebuild without it
```

---

## Workflow Sequence

```
feature_ideas.yml (Friday 22:00 UTC)
  -> feature_idea_generator.py     # 4 OpenAI + 4 Anthropic PRDs
  -> git commit drafts/features/
  -> rank_features_nightly.py      # score new, cache, force-rank
  -> append top-10 to summary.txt
  -> git commit reports/virality/
  -> email summary.txt
```

---

## Required Secrets

| Secret | Used by |
|---|---|
| `OPENAI_API_KEY` | feature_idea_generator.py, rank/score scripts |
| `OPENAI_MODEL` | feature_idea_generator.py (default: `gpt-4.1-mini`) |
| `ANTHROPIC_API_KEY` | feature_idea_generator.py, rank/score scripts |
| `ANTHROPIC_MODEL` | feature_idea_generator.py (default: `claude-haiku-4-5-20251001`) |
| `ALERT_EMAIL_TO` | summary email recipient |
| `ALERT_EMAIL_USER` | Gmail sender |
| `ALERT_EMAIL_PASS` | Gmail app password |

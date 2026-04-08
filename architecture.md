# Architecture

## Overview
This repo runs a paper‑trading research lab with:
- A baseline sector‑rotation system (NRWise) in the root scripts.
- Multiple "normal" algos (academic baselines) in `normal/`.
- Multiple "crazy" algos (alternative data) in `crazy/`.
- Daily idea generation via GitHub Actions (ChatGPT + Claude).
- Dashboards + ledgers published from `docs/`.

## Core Baseline (NRWise)
- Orchestrator: `daily_run.py`
- Seed bootstrap: `seed.py`
- Strategy logic: `scanner.py`, `signals.py`
- Portfolio state: `portfolio.py`
- Dashboard: `dashboard.py`

## Normal Algos (Academic Baselines)
- Algo definitions: `normal/algos.py`
- Runner: `normal/runner.py`
- Seed: `normal/seed.py`
- Consolidated ledger: `normal/ledger.py`
- Entry points: `normal_run.py`, `normal_seed.py`

## Crazy Algos (Alternative Data)
- Algo definitions: `crazy/algos.py`
- Runner: `crazy/runner.py`
- Seed: `crazy/seed.py`
- Combined dashboard: `crazy/combined_dashboard.py`
- Consolidated ledger: `crazy/ledger.py`
- Blocked queue: `crazy/blocked.py` → `data/blocked/algos.jsonl`
- Entry points: `crazy_run.py`, `crazy_seed.py`

## Idea Generation Pipeline
- Prompt: `prompts/crazy_ideas_prompt.txt`
- Generators: `scripts/crazy_generate_chatgpt.sh`, `scripts/crazy_generate_claude.sh`
- Orchestrator: `scripts/crazy_generate_ideas.py`
- Scoring: `scripts/crazy_score_ideas.py`
- Publish markdown: `scripts/crazy_publish_markdown.py`
- Daily stats report: `scripts/daily_stats_email.py`
- GitHub Action: `.github/workflows/crazy_ideas_daily.yml`

## Reporting
- Per‑algo dashboards:
  - Normal: `docs/normal/<algo_id>/index.html`
  - Crazy: `docs/algos/<algo_id>/index.html`
- Combined crazy dashboard: `docs/crazy/index.html`
- Landing page (CTA): `docs/landing.html`
- Honor pages: `docs/biscotti.html`, `docs/bailey.html`
- Rolling 30‑day leaderboard: `docs/leaderboards/rolling_30d.md`, `docs/leaderboards/rolling_30d.json`
- Consolidated ledgers: `docs/ledgers/normal_ledger.json`, `docs/ledgers/crazy_ledger.json`

## State + Data Layout
- Baseline state: `state.json`
- Normal states: `data/normal/state/<algo_id>.json`
- Crazy states: `data/crazy/state/<algo_id>.json`
- Idea runs: `data/ideas/runs/YYYY-MM-DD/`
- Blocked queue: `data/blocked/algos.jsonl`
- Caches: `cache/`

## Execution Flow (Daily)
1. GitHub Action runs idea generation.
2. Normal/crazy runners update states, dashboards, ledgers, leaderboard.
3. Landing/CTA pages read from `docs/` outputs.

## Commands
- Baseline seed: `python seed.py`
- Baseline daily: `python daily_run.py`
- Normal seed: `python normal_seed.py`
- Normal daily: `python normal_run.py`
- Crazy seed: `python crazy_seed.py`
- Crazy daily: `python crazy_run.py`

## Notes
- API‑key‑required algos record missing keys in `data/blocked/algos.jsonl`.
- The idea pipeline does not implement algos yet; it only generates specs.

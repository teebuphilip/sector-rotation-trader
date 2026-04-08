Daily crazy idea generation runs (ChatGPT + Claude) and writes JSONL specs to `data/ideas/runs/`, publishing Markdown to `docs/ideas/` (normal ideas run weekly to `data/normal_ideas/` and `docs/normal_ideas/`).
Baseline, normal, and crazy runners update per‑algo state, dashboards, ledgers, and the rolling 30‑day leaderboard in `docs/`.
Crazy algos live in `crazy/algos/` (one file per algo) and are registered via `crazy/algos/registry.py`.
Each algo has its own state JSON under `data/normal/state/` or `data/crazy/state/`, plus consolidated ledgers in `docs/ledgers/` (new algos auto‑seed on first run).
Public pages and CTAs are served from `docs/`, including landing, honor pages, dashboards, and leaderboards.
Data is segregated per model: each algo has its own state JSON and dashboard, with consolidated ledgers split into normal vs crazy.

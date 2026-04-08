Daily idea generation (ChatGPT + Claude) writes JSONL specs to `data/ideas/runs/` and publishes Markdown to `docs/ideas/`.
Baseline and normal runners update per‑algo state, dashboards, ledgers, and the rolling 30‑day leaderboard in `docs/`.
Crazy algos live in `crazy/algos/` (one file per algo) and are registered via `crazy/algos/registry.py`.
Each algo has its own state JSON under `data/normal/state/` or `data/crazy/state/`, plus consolidated ledgers in `docs/ledgers/`.
Public pages and CTAs are served from `docs/`, including landing, honor pages, dashboards, and leaderboards.

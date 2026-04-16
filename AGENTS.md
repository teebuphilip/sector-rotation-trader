# AGENTS.md

## Project Overview
Sector Rotation Trader is a Python paper-trading simulator for a sector rotation strategy. Daily runs update `state.json` and regenerate the dashboard in `docs/`.

## Key Files
- `config.py`: All tunable parameters.
- `scanner.py`: Sector scan + data download helper.
- `signals.py`: Entry/exit logic.
- `portfolio.py`: Positions, cash, margin, analytics.
- `dashboard.py`: Generates `docs/index.html` + `docs/trades.json`.
- `daily_run.py`: Daily orchestration (`--dry-run` supported).
- `seed.py`: Bootstrap historical state.
- `state.json`: Live portfolio state (committed).

## Common Commands
- Install deps: `pip install -r requirements.txt`
- One-time seed: `python seed.py`
- Daily run: `python daily_run.py`
- Dry run (no state/dashboard writes): `python daily_run.py --dry-run`
- Crazy algos seed (best-effort for no-key strategies): `python crazy_seed.py`
- Crazy algos daily run (per-algo + combined dashboards): `python crazy_run.py`
- Normal algos seed: `python normal_seed.py`
- Normal algos daily run: `python normal_run.py`

## Communication Style
- Always start substantive replies with a short TL;DR first.
- Put the main answer or recommendation before supporting detail.
- Keep the TL;DR concrete and action-oriented, not decorative.

## Conventions
- Prefer small, targeted edits and keep existing behavior unless asked to change strategy rules.
- Avoid modifying `state.json` and `docs/` unless explicitly requested or running the pipeline.
- Use `rg` for searching.
- Default to ASCII in new files.

## Notes
- The strategy rules and system assumptions are documented in `README.md`.

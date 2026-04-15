Sector Rotation Trader is a paper-trading lab with four loops: baseline NRWise, normal/crazy algo execution, LLM idea-to-algo build, and standalone content generation.
Baseline state lives in `state.json`; normal and crazy algo states live under `data/normal/state/` and `data/crazy/state/`.
Normal algos are conventional baselines in `normal/algos/`; crazy algos are alternative-data strategies in `crazy/algos/` and are registered through `data/algos_registry_crazy.txt`.
Crazy idea generation forces every LLM idea through `IDEA -> DATA -> BEHAVIOR -> MARKET IMPACT -> TRADE LOGIC` using `scripts/crazy_schema_gate.py` before it can be published or built.
Published crazy specs are processed by `scripts/run_publish_pipeline.py`: adapter route, structural build, patch/validate, seed, then move to `data/ideas/completed/`, `data/ideas/failed/`, or `data/ideas/intervention/`.
Adapters in `crazy/adapters/` are the approved data access layer; low-confidence or missing adapter matches are parked for manual intervention.
Daily tactical output writes dashboards, ledgers, rank history, rolling 30D leaderboards, and precomputed ticker/sector signals under `docs/`.
Force rank (`data/rank_history.csv`) is full-window/since-seed performance; rolling 30D (`docs/leaderboards/rolling_30d.json`) is recent momentum, so they can disagree without being contradictory.
`precompute_signals.py` writes `docs/signals/` for the ticker lookup product, including sector summaries and per-ticker JSON files.
The standalone content engine is separate from the tactical run: `scripts/run_content_engine.sh` reads rank history, rolling 30D, and signal precompute outputs, writes `reports/deep_validation/`, then renders deterministic text files under `content/`.
Content generation uses the deep validation JSON as truth and does not recompute metrics or use an LLM.
Public pages and CTAs are served from `docs/`, while generated content lives in `content/` and can later be copied to a separate website repo.

Sector Rotation Trader is a paper-trading lab with five loops: core book execution, normal/crazy algo execution, high-action idea generation, post-core experiment activation, and standalone content generation.
The core book is the priority workflow: `daily_run.yml` runs after market close and handles baseline NRWise, normal algos, existing crazy algos, dashboards, ledgers, signal precompute, validation, ranking, and the core email.
Crazy idea generation is separate and silent: `crazy_ideas_daily.yml` runs in the morning, generates high-action ideas, schema-gates them, scores them, publishes markdown specs, commits artifacts, and sends no email.
Experiment activation is downstream: `crazy_daily_builds.yml` triggers only after `Daily Sector Rotation Run` completes successfully.
The experiment workflow runs `final_publish_llm_gate.py`, moves approved specs to `build/`, builds with deterministic templates, seeds accepted algos, runs only the newly seeded algos with `crazy_run.py --algo-id ... --skip-combined`, rebuilds aggregate outputs, and sends the experiment email.
Baseline state lives in `state.json`; normal and crazy algo states live under `data/normal/state/` and `data/crazy/state/`.
Normal algos are conventional baselines in `normal/algos/`; crazy algos are alternative-data strategies in `crazy/algos/` and are registered through `data/algos_registry_crazy.txt`.
Crazy ideas must follow `IDEA -> DATA -> BEHAVIOR -> MARKET IMPACT -> TRADE LOGIC` before they can be published or built.
Adapters in `crazy/adapters/` are the approved data access layer; low-confidence, missing-adapter, unsupported-native-short, or otherwise questionable specs are parked for intervention.
The production build path is template-first: adapter route plus markdown spec type should be enough to produce a runnable algo without asking an LLM to write bespoke strategy code.
Older structural LLM build artifacts are retained under `data/algos_codegen/structural_*` for review until a cleanup/retention script exists.
Failed/intervention generated attempts and specs are retained temporarily because they may be useful for debugging, adapter expansion, or future side projects.
Force rank (`data/rank_history.csv`) is full-window/since-seed performance; rolling 30D (`docs/leaderboards/rolling_30d.json`) is recent momentum, so they can disagree without being contradictory.
`precompute_signals.py` writes `docs/signals/` for the ticker lookup product, including sector summaries and per-ticker JSON files.
The standalone content engine is separate from tactical and experiment workflows: `scripts/run_content_engine.sh` reads rank history, rolling 30D, and signal precompute outputs, writes `reports/deep_validation/`, then renders deterministic text files under `content/`.
Content generation uses the deep validation JSON as truth and does not recompute metrics or use an LLM.
Public pages and CTAs are served from `docs/`, while generated content lives in `content/` and can later be copied to a separate website repo.
Professional Backtest V1 is a reusable engine under `backtest/` plus `scripts/run_professional_backtest.py`; it reviews every algo, runs only honest price-based long/cash sector ETF backtests, executes next trading day open with slippage, compares to SPY, and labels unsupported non-price/live-only strategies instead of faking metrics.

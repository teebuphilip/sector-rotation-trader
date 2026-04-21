# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Sector Rotation Trader is a public paper-trading lab for testing sector rotation, academic baseline strategies, and weird alternative-data trading signals. The repo runs daily simulations, publishes dashboards from `docs/`, generates new signal ideas, builds selected ideas into runnable algos, and produces a standalone content layer from validated system outputs.

This is research infrastructure. It is not investment advice.

The system has five major loops:

1. **Core book loop**: after market close, runs baseline NRWise, normal algos, crazy algos, validation, dashboards, and the core email.
2. **Algo lab loop**: keeps normal academic algos and crazy alternative-data algos running as paper-traded experiments.
3. **Idea generation loop**: silently generates high-action crazy ideas into dated run folders; does not email and does not mutate trading state.
4. **Experiment activation loop**: runs only after the core book succeeds, gates published ideas, builds/seeds accepted experiments, runs only new algos, and sends the experiment email.
5. **Content loop**: independently reads validated reports and turns them into short public-facing content without inventing new facts.

## Commands

Baseline:

```bash
python seed.py
python daily_run.py
python daily_run.py --dry-run
```

Normal algos:

```bash
python normal_seed.py
python normal_run.py
```

Crazy algos:

```bash
python crazy_seed.py
python crazy_run.py
python crazy_seed.py --algo-file crazy/algos/specific_algo.py
python crazy_run.py --algo-id work-from-home-frenzy --skip-combined
```

Build published crazy ideas manually:

```bash
python scripts/final_publish_llm_gate.py --date 2026-04-17
python scripts/autogen_crazy_factory.py \
  --date 2026-04-17 \
  --skip-generate \
  --publish-root data/ideas/runs/2026-04-17/build \
  --template-build \
  --skip-run \
  --verbose
```

Rebuild aggregate outputs after a new algo:

```bash
python scripts/rebuild_crazy_combined_dashboard.py
python precompute_signals.py --min-days 30
```

Standalone content engine:

```bash
scripts/run_content_engine.sh
scripts/run_content_engine.sh --date 2026-04-15
```

No tests, linter, or build step. Pure Python. Dependencies: `yfinance`, `pandas`, `numpy` plus LLM SDKs (`openai`, `anthropic`) for idea generation scripts.

## Architecture

### Baseline NRWise

Files:
- `config.py`: all tunable parameters (capital limits, signal thresholds, lookback periods, file paths). Every module imports from it.
- `scanner.py`: ETF/stock downloads, sector scan, `SECTOR_STOCKS` maps each sector ETF to top 10 holdings (the candidate universe).
- `signals.py`: entry/exit rules.
- `portfolio.py`: cash, positions, margin, taxes, analytics.
- `dashboard.py`: writes `docs/index.html`.
- `daily_run.py`: daily orchestrator.
- `seed.py`: walks day-by-day through 90-day historical window to bootstrap state. Run once.
- `state.json`: live baseline state.

Strategy rules:
- `$100k` base capital, `$10k` max per position, up to `$100k` additional margin.
- `8.5%` annual margin rate with daily accrual; principal repaid first on close.
- Leading sector by 3M-6M performance spread/acceleration.
- Entry: price above 10-day high + volume above 150% of 20-day avg + BB bandwidth expanding (all 3 required simultaneously).
- Exit: 2 consecutive closes below 20-day MA (`consec_below_ma` stored per position) or 8% hard stop-loss.
- Drawdown circuit breaker blocks new entries when equity is >15% below peak.

### Normal Algos

- `normal/algos/`: academic/standard algo implementations.
- `normal/runner.py`, `normal/seed.py`, `normal/ledger.py`.
- `normal_run.py`, `normal_seed.py`: CLI entry points.
- State: `data/normal/state/<algo_id>.json`
- Dashboards: `docs/normal/<algo_id>/index.html`
- Ledger: `docs/ledgers/normal_ledger.json`

### Crazy Algos

- `crazy/algos/`: generated and hand-written algo implementations.
- `data/algos_registry_crazy.txt`: flat-file registry (`module_name:ClassName`), not Python imports.
- `crazy/algos/registry.py`: dynamic registry loader.
- `crazy/runner.py`, `crazy/seed.py`, `crazy/ledger.py`, `crazy/combined_dashboard.py`.
- `crazy_run.py`, `crazy_seed.py`: CLI entry points.
- State: `data/crazy/state/<algo_id>.json`
- Dashboards: `docs/algos/<algo_id>/index.html`
- Ledger: `docs/ledgers/crazy_ledger.json`
- Blocked keys: `data/blocked/algos.jsonl`

Seeding behavior:
- Historical-capable algos simulate history; live-only algos get flat cash history.
- Missing API keys are recorded in `data/blocked/algos.jsonl`, not fatal.
- Registry helper: `scripts/rebuild_registry_crazy.py`

### Idea Generation Pipeline

Morning flow (schema-gated, silent):

```text
LLM high-action idea generation
-> strict schema gate (IDEA -> DATA -> BEHAVIOR -> MARKET IMPACT -> TRADE LOGIC)
-> scoring
-> markdown publishing
-> commit idea artifacts
```

Post-core experiment activation flow:

```text
core book succeeds
-> final publish LLM gate
-> deterministic template build
-> seed accepted experiments
-> run only newly seeded algos
-> rebuild aggregate crazy outputs
-> experiment email
```

Ideas carry an explicit `family` field. Approved families: `consumer_stress`, `travel_mobility`, `labor_jobs`, `freight_logistics`, `attention_sentiment`, `political_insider_filing`, `local_economy_weirdness`, `macro_input_pressure`.

Key scripts:
- `scripts/crazy_generate_high_action_ideas.py`
- `scripts/crazy_schema_gate.py`
- `scripts/crazy_score_ideas.py`
- `scripts/final_publish_llm_gate.py`
- `scripts/autogen_crazy_factory.py` (production orchestrator, template-build preferred)
- `scripts/build_template_algo.py` (production builder)

Idea run layout:

```text
data/ideas/runs/YYYY-MM-DD/raw/
data/ideas/runs/YYYY-MM-DD/filtered/
data/ideas/runs/YYYY-MM-DD/rejected/
data/ideas/runs/YYYY-MM-DD/publish/
data/ideas/runs/YYYY-MM-DD/build/
data/ideas/runs/YYYY-MM-DD/intervention/
data/ideas/runs/YYYY-MM-DD/reject/
data/ideas/runs/YYYY-MM-DD/factory_results/
```

Triage buckets:
- `data/ideas/completed/YYYY-MM-DD/`: built and seeded.
- `data/ideas/failed/YYYY-MM-DD/`: build or seed failed.
- `data/ideas/intervention/YYYY-MM-DD/`: no adapter, low confidence, or needs manual review.

### Adapters

Adapters in `crazy/adapters/` are stable data access functions used by generated algos. They prevent hallucinated fetch logic.

Routing: `scripts/adapter_router.py` — scores all adapters, returns JSON with top adapters and confidence. Exit code `1` = no usable adapter; low-confidence specs go to `data/ideas/intervention/`.

Known families: Reddit, Twitter/social, weather, earthquakes, Google Trends, FRED, TSA tables, Socrata/311, HTML tables, RSS counts, OpenChargeMap, price-only fallback.

### Product Structure Layer

`scripts/build_product_index.py` generates normalized product-facing JSON:

- `data/product/algos_index.json`
- `data/product/families.json`
- `data/product/watchlist.json`
- `data/product/promoted.json`
- `data/product/graveyard.json`
- `data/product/daily_summary.json`

Derived fields: `family`, `status` (promoted / backtest_weak / live_only / sandbox / failed / parked), `evidence_class` (v1_backtested / live_receipts_only / needs_history / short_model_pending / pending_seed).

### Public vs Private Split

Architecture rule:

```text
nightly run computes facts once
-> stripped public JSON is generated
-> static public pages are rendered from that JSON
-> only public-safe artifacts are pushed to the website repo
```

Public nightly contract under `docs/data/public/`:
- `daily.json`, `leaderboard.json`, `families.json`, `watchlist.json`, `promoted.json`, `graveyard.json`
- `benchmarks/spy.json`, `benchmarks/qqq.json`
- `signals/index.json`, `signals/<symbol>.json`

Generator: `scripts/build_public_artifacts.py`

Private/internal artifacts never leave the private repo: raw ideas, factory intervention/failed specs, codegen logs, full state files, full trade logs, full equity curves, private leaderboard payloads, debugging outputs.

Product split:
- **Free**: proves the lab is real — homepage, stripped leaderboard, family summaries, promoted/watchlist/graveyard summaries, blog, lab notes, public daily report, signal summary pages.
- **Paid**: the useful operating layer — full leaderboard, per-algo/per-ticker detail, full trade history, equity curves, premium summaries, downloadable CSVs.

### Ranking

Two separate ranking systems — do not conflate them:

- **Force rank** (`data/rank_history.csv`, `scripts/rank_daily.py`): full-window/since-seed total return and alpha. Long-term trust, promotion/demotion, kill review.
- **Rolling 30D** (`docs/leaderboards/rolling_30d.json`, `scripts/rolling_30d_leaderboard.py`): trailing 30-day return, Sharpe, max drawdown. Recent momentum, signal spotlight, tactical content.

An algo can be weak on force rank but strong on rolling 30D. That is expected, not a contradiction.

### Signal Precompute

`precompute_signals.py` converts algo states into per-ticker and per-sector verdict files for the lookup product.

Outputs: `docs/signals/<TICKER>.json`, `docs/signals/_sectors.json`, `docs/signals/_sectors/<ETF>.json`, `docs/signals/index.json`. Lookup UI: `docs/signals/lookup.html`.

### Professional Backtest V1

Separate from seed/bootstrap. Only honest price-based long/cash sector ETF backtests. Non-price adapters (Reddit, FRED, weather, 311, etc.) are labeled `UNSUPPORTED_DATA`, not faked.

Method: signal after close on day T → execute next open T+1 → 5 bps slippage → SPY benchmark.

Files: `backtest/classifier.py`, `backtest/engine.py`, `backtest/metrics.py`, `backtest/report.py`. CLI: `scripts/run_professional_backtest.py`.

Labels: `BACKTEST_PASS`, `BACKTEST_WEAK`, `BACKTEST_FAIL`, `INSUFFICIENT_ACTIVITY`, `UNSUPPORTED_DATA`, `UNSUPPORTED_SHORT`.

### Standalone Content Engine

Deliberately separate from the tactical run. Does not call an LLM. Does not recompute metrics. Formats already-validated facts only.

Core rule: **If it is not in the deep validation report, it does not exist.**

Flow:

```text
data/rank_history.csv + docs/leaderboards/rolling_30d.json + docs/signals/index.json
-> scripts/write_deep_validation_report.py
-> reports/deep_validation/latest.json + latest.md
-> scripts/generate_content.py
-> content/*.txt
```

Outputs: `content/daily/`, `content/signal_of_day/`, `content/failures/`, `content/call_of_day/`, `content/weekly/`.

Content voice: honest, curious, human, transparent. Named algos like Biscotti and Baileymol. Never: "cutting-edge", "proprietary algorithm", "AI-powered signals", "seamless", or anything that sounds like a LinkedIn post from 2019.

## GitHub Actions

Workflow order:

```text
09:15 UTC: crazy_ideas_daily.yml — morning high-action idea generation (silent, no email)
22:30 UTC: daily_run.yml — core book run (priority workflow)
after core success: crazy_daily_builds.yml — experiment activation (gated on core success)
```

Primary workflows:
- `.github/workflows/daily_run.yml`: baseline + normal + crazy + dashboards + ledgers + signal precompute + validation + core email. Auto-commits `state.json`, `docs/index.html`, `docs/trades.json`.
- `.github/workflows/crazy_ideas_daily.yml`: morning idea generation. Silent.
- `.github/workflows/crazy_daily_builds.yml`: experiment activation. Triggered by core success, not schedule.
- `.github/workflows/normal_ideas_weekly.yml`: weekly normal idea generation.

The content engine is not wired into the daily workflow by design. Run locally or as a separate job.

GitHub Pages served from `docs/`. Dashboard URL: `https://teebuphilip.github.io/sector-rotation-trader/`.

## Required Secrets

LLM: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`
Email: `ALERT_EMAIL_TO`, `ALERT_EMAIL_USER`, `ALERT_EMAIL_PASS` (Gmail app password, not account password)
Optional data: `FRED_API_KEY`, `EIA_API_KEY`, `SOCRATA_APP_TOKEN`, `OPENCHARGEMAP_API_KEY`

## Working With Teebu

**Who he is:** 55yo DevOps/SRE background, VI terminal guy, 2015 MBP on Catalina (Python 3.9 — do not use `X | None` union syntax, it breaks locally). Terse, direct, typo-prone (often on mobile), profanity-comfortable. Motivation: "the girl needs to eat" (3yo daughter). Under financial pressure, needs revenue now.

**What he needs from an AI assistant:**
- Push back hard. He asks for the antagonist view.
- Focus on shipping, not building more infrastructure.
- Keep scope tight. Don't suggest new features before the current thing is launched.
- Remind him of customer acquisition — it's his blind spot.
- Cut his timeline estimates in half.

**Red flags:**
- Talking about building another meta-product → stop him.
- Pivoting because something is "hard" → challenge it.
- "Great new idea" before shipping current thing → red alert.

**Do not:**
- Tell him this will make him a millionaire.
- Encourage complexity or new pipelines.
- Validate every pivot.

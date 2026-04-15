# Architecture

## Executive Summary

Sector Rotation Trader is a paper-trading lab with four independent but related systems:

1. **Trading execution**: baseline NRWise, normal algos, and crazy algos run daily and update state.
2. **Idea generation and build**: LLM-generated ideas are forced through a schema gate, routed to adapters, built into Python algos, seeded, and triaged.
3. **Signal publishing**: dashboards, ledgers, rolling leaderboards, and ticker/sector signal files are written under `docs/`.
4. **Content generation**: a standalone flow reads validated artifacts, writes a deep validation report, and renders short content from that report only.

The core architectural rule is separation of concerns:

```text
trading systems produce facts
validation explains facts
content templates format facts
```

The content layer does not recompute metrics and does not invent narratives.

## System Map

```text
baseline NRWise -+
normal algos ----+--> state files --> dashboards / ledgers / rank history
crazy algos -----+

LLM ideas --> schema gate --> publish specs --> adapter router --> structural build --> seed --> triage

rank history + rolling 30D + signal precompute --> deep validation report --> content files
```

## Baseline NRWise

Purpose:

- Maintain the original sector rotation model and a stable benchmark for the lab.

Files:

- `daily_run.py`: daily orchestrator.
- `seed.py`: historical bootstrap.
- `scanner.py`: data download and sector scan.
- `signals.py`: entry/exit rules.
- `portfolio.py`: positions, cash, margin, taxes, analytics.
- `dashboard.py`: writes `docs/index.html` and dashboard data.
- `state.json`: baseline state.

Outputs:

- `state.json`
- `docs/index.html`
- `docs/trades.json`

## Normal Algos

Purpose:

- Provide more conventional academic or systematic strategy baselines.

Files:

- `normal/algos/`: individual algo files.
- `normal/runner.py`: executes all normal algos.
- `normal/seed.py`: seeds all or one normal algo.
- `normal/ledger.py`: consolidated ledger.
- `normal_run.py`: CLI entry point.
- `normal_seed.py`: CLI seed entry point.

State/output:

- `data/normal/state/<algo_id>.json`
- `docs/normal/<algo_id>/index.html`
- `docs/ledgers/normal_ledger.json`

## Crazy Algos

Purpose:

- Run alternative-data and unconventional strategy ideas at scale.

Files:

- `crazy/algos/`: individual generated or hand-written algo files.
- `data/algos_registry_crazy.txt`: flat-file registry.
- `crazy/algos/registry.py`: dynamic registry loader.
- `crazy/runner.py`: executes all crazy algos.
- `crazy/seed.py`: seeds historical-capable algos or flat-cash states.
- `crazy/ledger.py`: consolidated ledger.
- `crazy/combined_dashboard.py`: combined crazy dashboard.
- `crazy/blocked.py`: missing-key recorder.
- `crazy_run.py`: CLI runner.
- `crazy_seed.py`: CLI seeder.

State/output:

- `data/crazy/state/<algo_id>.json`
- `docs/algos/<algo_id>/index.html`
- `docs/ledgers/crazy_ledger.json`
- `data/blocked/algos.jsonl`

## Crazy Algo Registry

Generated algos are not manually imported into `crazy/algos/registry.py`. Instead, the loader reads:

```text
data/algos_registry_crazy.txt
```

Format:

```text
module_name:ClassName
```

This keeps automation simple and makes generated algos easier to check in.

Helper:

- `scripts/rebuild_registry_crazy.py`

## Adapters

Adapters are stable data access functions used by generated algos. They prevent generated code from hallucinating fetch logic.

Adapter directory:

- `crazy/adapters/`

Routing:

- `scripts/adapter_router.py`

Adapter examples:

- `reddit_activity`
- `twitter_activity`
- `weather_series`
- `earthquake_activity`
- `google_trends`
- `fred_series`
- `tsa_table`
- `socrata_311`
- `html_table`
- `rss_count`
- `openchargemap`
- `price_only`

Routing behavior:

- Scores all adapters.
- Applies tie-breakers.
- Returns top adapters and confidence.
- Exits `1` for no adapter or low confidence.
- Low-confidence specs are parked in `data/ideas/intervention/`.

## Idea Generation Architecture

The crazy idea pipeline is structured to avoid garbage-in/garbage-out.

Required sequence:

```text
IDEA -> DATA -> BEHAVIOR -> MARKET IMPACT -> TRADE LOGIC
```

Files:

- `prompts/crazy_ideas_prompt.txt`: strict generation prompt.
- `scripts/crazy_generate_ideas.py`: ChatGPT + Claude orchestration.
- `scripts/crazy_schema_gate.py`: deterministic schema validation.
- `scripts/crazy_score_ideas.py`: idea scoring.
- `scripts/crazy_publish_markdown.py`: markdown publishing.

Run layout:

```text
data/ideas/runs/YYYY-MM-DD/raw/
data/ideas/runs/YYYY-MM-DD/filtered/
data/ideas/runs/YYYY-MM-DD/rejected/
data/ideas/runs/YYYY-MM-DD/publish/
```

The schema gate rejects ideas before build if they lack real data, clear behavior, sector impact, or deterministic trade logic.

## Build + Seed Architecture

The build pipeline turns published markdown specs into runnable crazy algo files.

Primary orchestrator:

- `scripts/run_publish_pipeline.py`

Single-spec builder:

- `scripts/run_structural_build.sh`

Builder stages:

```text
grill spec
-> route adapter
-> slice spec
-> build structural Python shell
-> LLM patch
-> LLM validation
-> deterministic fallback if needed
-> final compile/sanity validation
```

Builder components:

- `scripts/grill_algo_spec.py`
- `scripts/adapter_router.py`
- `scripts/slice_algo_spec.py`
- `scripts/build_structural_algo.py`
- `scripts/patch_algo.py`
- `scripts/patch_deterministic.py`
- `scripts/validate_structural_algo.py`
- `scripts/validate_algo_llm.py`
- `scripts/validate_final.py`

Triage outputs:

- `data/ideas/completed/YYYY-MM-DD/`
- `data/ideas/failed/YYYY-MM-DD/`
- `data/ideas/intervention/YYYY-MM-DD/`

Failure policy:

- No adapter or low confidence -> intervention.
- Build failure -> failed.
- Seed failure -> failed.
- Successful build + seed -> completed.

## State Layout

Baseline:

- `state.json`

Normal:

- `data/normal/state/<algo_id>.json`

Crazy:

- `data/crazy/state/<algo_id>.json`

Rank history:

- `data/rank_history.csv`

Blocked missing-key queue:

- `data/blocked/algos.jsonl`

Generated idea run artifacts:

- `data/ideas/runs/YYYY-MM-DD/`

Build artifacts:

- `data/algos_codegen/`

Validation cache:

- `data/.validation_cache/`

## Dashboards and Public Outputs

Public-facing files are generated under `docs/`.

Dashboards:

- `docs/index.html`: baseline dashboard.
- `docs/normal/<algo_id>/index.html`: normal algo dashboards.
- `docs/algos/<algo_id>/index.html`: crazy algo dashboards.
- `docs/crazy/index.html`: combined crazy dashboard.

Leaderboards and ledgers:

- `docs/leaderboards/rolling_30d.json`
- `docs/leaderboards/rolling_30d.md`
- `docs/ledgers/normal_ledger.json`
- `docs/ledgers/crazy_ledger.json`

Marketing/site:

- `docs/landing.html`
- `docs/blog/index.html`
- `docs/blog/_posts/`
- `docs/biscotti.html`
- `docs/bailey.html`
- `docs/leaderboard.html`

## Signal Precompute Architecture

Script:

- `precompute_signals.py`

Purpose:

- Convert algo state into ticker and sector verdict files for the lookup product.

Inputs:

- `data/normal/state/`
- `data/crazy/state/`
- optional Wikipedia ticker list, with fallback list if unavailable.

Outputs:

- `docs/signals/<TICKER>.json`
- `docs/signals/_sectors.json`
- `docs/signals/_sectors/<ETF>.json`
- `docs/signals/index.json`

Lookup UI:

- `docs/signals/lookup.html`

SPY benchmark repair:

- `scripts/backfill_spy_equity.py`

## Ranking Architecture

There are two distinct ranking systems.

### Force Rank

Source:

- `data/rank_history.csv`

Script:

- `scripts/rank_daily.py`

Meaning:

- Full-window/since-seed total return and alpha ranking.

Use:

- Long-term trust.
- Promotion/demotion decisions.
- Kill review.
- Tactical email force-rank section.

### Rolling 30D Leaderboard

Source:

- `docs/leaderboards/rolling_30d.json`
- `docs/leaderboards/rolling_30d.md`

Script:

- `scripts/rolling_30d_leaderboard.py`

Meaning:

- Trailing 30-day return, Sharpe, and max drawdown.

Use:

- Recent momentum.
- Signal spotlight.
- Landing page recent winners.
- Tactical content.

These rankings can disagree. That is expected. A signal can be poor since seed but strong over the last 30 days.

## Tactical Email Architecture

Scripts:

- `scripts/evening_email.py`
- `scripts/daily_stats_email.py`

The evening email summarizes:

- baseline state;
- normal/crazy run status;
- force rankings;
- precompute signal state;
- validation status;
- rolling 30D leaderboard;
- blocked algos.

The email is operational. It is not the same as the standalone content engine.

## Standalone Content Generation Architecture

The content engine is outside the tactical run.

Flow:

```text
data/rank_history.csv
+ docs/leaderboards/rolling_30d.json
+ docs/signals/index.json
-> scripts/write_deep_validation_report.py
-> reports/deep_validation/latest.json + latest.md
-> scripts/generate_content.py
-> content/*.txt
```

Scripts:

- `scripts/write_deep_validation_report.py`: writes the authoritative report.
- `scripts/generate_content.py`: renders deterministic content templates.
- `scripts/run_content_engine.sh`: runs both steps.

Outputs:

- `reports/deep_validation/YYYY-MM-DD.md`
- `reports/deep_validation/YYYY-MM-DD.json`
- `reports/deep_validation/latest.md`
- `reports/deep_validation/latest.json`
- `content/daily/YYYY-MM-DD.txt`
- `content/signal_of_day/YYYY-MM-DD.txt`
- `content/failures/YYYY-MM-DD.txt`
- `content/call_of_day/YYYY-MM-DD.txt`
- `content/weekly/YYYY-WW.txt`

Rule:

```text
If it is not in reports/deep_validation/latest.json, the content engine cannot use it.
```

Detailed doc:

- `content-generation.md`

## GitHub Actions

Primary workflows:

- `.github/workflows/daily_run.yml`: runs baseline, normal, crazy, dashboards, ledgers, signal precompute, validation/email steps.
- `.github/workflows/crazy_ideas_daily.yml`: generates and publishes crazy ideas.
- `.github/workflows/normal_ideas_weekly.yml`: generates and publishes normal ideas.

The content engine is not wired into the daily workflow yet by design. It can be run locally or added later as a separate workflow/job.

## Execution Flow: Daily Tactical Run

Current tactical flow:

```text
baseline seed/run as needed
-> daily_run.py
-> normal_run.py
-> crazy_run.py
-> rolling_30d_leaderboard.py
-> precompute_signals.py
-> validate_nightly.py / email scripts
-> docs/ updated
```

## Execution Flow: Standalone Content Run

Manual content flow:

```bash
scripts/run_content_engine.sh
```

Internal steps:

```text
write_deep_validation_report.py
-> generate_content.py
```

This flow consumes existing outputs. It does not trigger trading, seeding, idea generation, or tactical email.

## Operational Principles

- Generated algos should be structurally valid first; strategy polish is secondary.
- Adapters are preferred over generated data-fetching code.
- Low-confidence adapter matches go to intervention.
- Missing-key algos are blocked, not fatal.
- Flat-cash history is acceptable for live-only/no-history crazy algos.
- Force rank and rolling 30D are separate concepts.
- Content generation is deterministic and report-driven.
- Public credibility comes from publishing winners and failures.

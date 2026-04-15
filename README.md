# Sector Rotation Trader

Sector Rotation Trader is a public paper-trading lab for testing sector rotation, academic baseline strategies, and weird alternative-data trading signals. The repo runs daily simulations, publishes dashboards from `docs/`, generates new signal ideas, builds selected ideas into runnable algos, and now produces a separate content layer from validated system outputs.

This is research infrastructure. It is not investment advice.

## What This Repo Does

The system has four major loops:

1. **Baseline trading loop**: runs the original NRWise-style sector rotation model.
2. **Algo lab loop**: runs normal academic algos and crazy alternative-data algos.
3. **Idea-to-algo loop**: generates structured ideas, validates them, routes them to adapters, builds Python algo files, seeds them, and triages the result.
4. **Content loop**: independently reads validated reports and turns them into short public-facing content without inventing new facts.

The daily public output lives under `docs/` and is intended for GitHub Pages.

## Strategy Rules: Baseline NRWise

The root strategy is a realistic paper-trading simulator using SPDR sector ETFs and sector holdings.

Rules:

- `$100k` base capital.
- `$10k` max per position.
- Up to `$100k` additional margin when fully deployed and signal fires.
- `8.5%` annual margin rate with daily accrual and proportional settlement on position close.
- Daily sector scan chooses the leading SPDR ETF by 3M-6M performance spread/acceleration.
- Entry requires price above 10-day high, volume above 150% of 20-day average, and Bollinger Band expansion.
- Exit occurs after 2 consecutive closes below the 20-day moving average or an 8% hard stop-loss.
- Drawdown circuit breaker blocks new entries when equity is more than 15% below peak.
- Sector concentration limits avoid excessive exposure to one sector.

Simulation state is stored in `state.json` and rendered to `docs/index.html`.

## Repo Layout

Core baseline:

- `config.py`: baseline strategy configuration.
- `scanner.py`: ETF/stock downloads and sector scan helpers.
- `signals.py`: baseline entry/exit logic.
- `portfolio.py`: cash, positions, margin, taxes, analytics.
- `dashboard.py`: baseline dashboard generation.
- `daily_run.py`: baseline daily orchestration.
- `seed.py`: baseline historical bootstrap.
- `state.json`: baseline live paper state.

Normal algos:

- `normal/algos/`: academic/standard algo implementations.
- `normal/runner.py`: normal algo runner.
- `normal/seed.py`: normal algo historical seed.
- `normal/ledger.py`: normal consolidated ledger.
- `normal_run.py`: normal run entry point.
- `normal_seed.py`: normal seed entry point.

Crazy algos:

- `crazy/algos/`: alternative-data algo implementations.
- `data/algos_registry_crazy.txt`: flat-file crazy algo registry.
- `crazy/runner.py`: crazy algo runner.
- `crazy/seed.py`: crazy algo historical/best-effort seed.
- `crazy/ledger.py`: crazy consolidated ledger.
- `crazy/combined_dashboard.py`: crazy dashboard/index output.
- `crazy/blocked.py`: missing-key blocked queue writer.
- `crazy_run.py`: crazy run entry point.
- `crazy_seed.py`: crazy seed entry point.

Adapters:

- `crazy/adapters/`: stable adapter functions used by generated crazy algos.
- `scripts/adapter_router.py`: maps an idea/spec to one or more known adapters.
- `docs/taxonomy.md`: taxonomy of known crazy data patterns and valid examples.

Public outputs:

- `docs/index.html`: baseline dashboard.
- `docs/landing.html`: public landing/CTA page.
- `docs/leaderboards/`: rolling 30-day leaderboard outputs.
- `docs/signals/`: precomputed ticker/sector signal lookup data.
- `docs/signals/lookup.html`: ticker lookup UI.
- `docs/algos/<algo_id>/`: crazy algo dashboards.
- `docs/normal/<algo_id>/`: normal algo dashboards.
- `docs/blog/`: blog/build-log scaffold.
- `docs/ledgers/`: consolidated normal/crazy ledger JSON.

Reports and content:

- `reports/deep_validation/`: standalone validation reports for content generation.
- `content/`: generated text content for daily posts, spotlights, failures, calls, and weekly summaries.

## Setup

```bash
git clone https://github.com/teebuphilip/sector-rotation-trader.git
cd sector-rotation-trader
pip install -r requirements.txt
```

Bootstrap baseline state:

```bash
python seed.py
```

Bootstrap normal/crazy algos:

```bash
python normal_seed.py
python crazy_seed.py
```

Run the daily systems locally:

```bash
python daily_run.py
python normal_run.py
python crazy_run.py
```

Dry-run baseline only:

```bash
python daily_run.py --dry-run
```

## Common Commands

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
```

Seed one generated crazy algo:

```bash
python crazy_seed.py --algo-file crazy/algos/reddit_gaming_thread_spike.py
```

Build published crazy ideas:

```bash
python scripts/run_publish_pipeline.py --dry-run
python scripts/run_publish_pipeline.py
```

Run standalone content engine:

```bash
scripts/run_content_engine.sh
scripts/run_content_engine.sh --date 2026-04-15
```

## Idea Generation Pipeline

The crazy idea pipeline is intentionally gated before anything reaches the build harness.

Flow:

```text
LLM idea generation
-> strict schema gate
-> scoring
-> markdown publishing
-> adapter routing
-> structural build
-> seed
-> triage
```

The required crazy idea schema follows:

```text
IDEA -> DATA -> BEHAVIOR -> MARKET IMPACT -> TRADE LOGIC
```

This prevents vague ideas from entering the build stage. The LLM must identify:

- a weird but real-world idea;
- a real, accessible data source;
- the behavior happening in the real world;
- the sector and directional market impact;
- simple deterministic entry and exit logic.

Key files:

- `prompts/crazy_ideas_prompt.txt`: strict schema generation prompt.
- `scripts/crazy_generate_ideas.py`: runs ChatGPT + Claude generators and schema gate.
- `scripts/crazy_schema_gate.py`: deterministic schema validator/normalizer.
- `scripts/crazy_score_ideas.py`: scores accepted ideas.
- `scripts/crazy_publish_markdown.py`: publishes accepted ideas to markdown.
- `data/ideas/runs/YYYY-MM-DD/raw/`: raw LLM JSONL.
- `data/ideas/runs/YYYY-MM-DD/filtered/`: schema-accepted ideas.
- `data/ideas/runs/YYYY-MM-DD/rejected/`: schema-rejected ideas.
- `data/ideas/runs/YYYY-MM-DD/publish/`: markdown specs waiting for build.

GitHub Action:

- `.github/workflows/crazy_ideas_daily.yml`

Normal ideas have a smaller weekly pipeline:

- `prompts/normal_ideas_prompt.txt`
- `scripts/normal_generate_ideas.py`
- `scripts/normal_score_ideas.py`
- `scripts/normal_publish_markdown.py`
- `.github/workflows/normal_ideas_weekly.yml`

## Adapter Routing

Generated crazy algos must be built against stable adapters, not arbitrary hallucinated data fetching code.

Adapter routing:

```bash
python scripts/adapter_router.py --spec-file path/to/spec.md
```

The router scores every known adapter and returns JSON similar to:

```json
{
  "adapters": ["reddit_activity"],
  "scores": {"reddit_activity": 5, "price_only": 3},
  "top_score": 5,
  "confidence": "ok"
}
```

Rules:

- Exit code `0`: usable adapter found.
- Exit code `1`: no adapter or confidence too low.
- Low-confidence ideas are moved to `data/ideas/intervention/` for manual adapter review.

Known adapter families include Reddit, Twitter/social search, weather, earthquakes, Google Trends, FRED, TSA tables, Socrata/311, HTML tables, RSS counts, OpenChargeMap, and price-only fallback.

## Build + Seed Pipeline: Crazy

Main orchestrator:

```bash
python scripts/run_publish_pipeline.py
```

Default input root:

```text
data/ideas/runs
```

The script scans nested `publish/` directories and skips specs already moved into completed, failed, or intervention queues.

Dry run:

```bash
python scripts/run_publish_pipeline.py --dry-run
```

Per-spec build flow:

```text
adapter route
-> structural build
-> final validation
-> seed
-> move spec
```

Structural builder:

```bash
scripts/run_structural_build.sh --spec-file SPEC.md --output-path crazy/algos/new_algo.py
```

Builder components:

- `scripts/grill_algo_spec.py`: turns loose markdown into a tighter JSON spec.
- `scripts/slice_algo_spec.py`: breaks the spec into smaller build slices.
- `scripts/build_structural_algo.py`: writes a structurally valid algo shell.
- `scripts/patch_algo.py`: LLM patch pass for intent-specific logic.
- `scripts/patch_deterministic.py`: deterministic fallback when LLM patching is not reliable.
- `scripts/validate_structural_algo.py`: structural checks.
- `scripts/validate_algo_llm.py`: LLM intent/spec check.
- `scripts/validate_final.py`: compile and final sanity checks.

Triage buckets:

- `data/ideas/completed/YYYY-MM-DD/`: built and seeded.
- `data/ideas/failed/YYYY-MM-DD/`: build or seed failed.
- `data/ideas/intervention/YYYY-MM-DD/`: no adapter, low confidence, or requires manual review.

## Crazy Algo Registry

Crazy algos are registered through a flat text file instead of hand-editing Python imports:

```text
data/algos_registry_crazy.txt
```

Format:

```text
module_name:ClassName
```

Example:

```text
reddit_gaming_thread_spike:RedditGamingThreadSpikeAlgo
```

Registry loader:

- `crazy/algos/registry.py`

Helper:

- `scripts/rebuild_registry_crazy.py`

This makes generated algos friendlier for automation and GitHub workflows.

## Seeding Behavior

The seeders are best-effort and designed not to block the entire lab.

Crazy seeding:

```bash
python crazy_seed.py
python crazy_seed.py --algo-file crazy/algos/specific_algo.py
```

Important behavior:

- Historical-capable algos simulate history.
- Live-only or no-history algos get flat cash history.
- Missing API keys are recorded in `data/blocked/algos.jsonl`.
- Delisted/unavailable tickers are filtered where possible.
- Seed failures in the publish pipeline move the source spec to `data/ideas/failed/`.

Blocked key cleanup:

```bash
python scripts/cleanup_blocked_keys.py --dry-run
python scripts/cleanup_blocked_keys.py
```

The cleanup script removes blocked entries for keys now present in the environment and prints algo id, name, and required keys.

## Signal Precompute: Product 2

`precompute_signals.py` converts seeded/running algo states into per-ticker and per-sector verdict files.

Run locally:

```bash
python precompute_signals.py
python precompute_signals.py --min-days 10
python precompute_signals.py --dry-run
python precompute_signals.py --no-wiki
```

Outputs:

- `docs/signals/<TICKER>.json`
- `docs/signals/_sectors.json`
- `docs/signals/_sectors/<ETF>.json`
- `docs/signals/index.json`

Lookup UI:

- `docs/signals/lookup.html`

SPY benchmark backfill helper:

```bash
python scripts/backfill_spy_equity.py
```

This repairs old state snapshots that lack `spy_equity`, which affects "beating SPY" counts.

## Ranking and Tactical Reporting

There are two separate ranking concepts. They should not be confused.

Force rank:

- Source: `data/rank_history.csv`.
- Script: `scripts/rank_daily.py`.
- Meaning: full-window/since-seed rank.
- Use: long-term trust, promotion/demotion, kill review.

Rolling 30D leaderboard:

- Source: `docs/leaderboards/rolling_30d.json` and `.md`.
- Script: `scripts/rolling_30d_leaderboard.py`.
- Meaning: recent trailing 30-day performance.
- Use: tactical spotlight and recent momentum.

An algo can be weak on force rank but strong over rolling 30D. That is not a contradiction. It means the algo is recently recovering or recently hot but is not yet strong on the full-window record.

Evening/tactical email:

- `scripts/evening_email.py`: post-close tactical email.
- `scripts/daily_stats_email.py`: broader daily stats email.

## Standalone Content Engine

The content engine is deliberately separate from the tactical run.

Flow:

```text
existing artifacts
-> deep validation report
-> deterministic content templates
-> text files under content/
```

Run:

```bash
scripts/run_content_engine.sh
```

Scripts:

- `scripts/write_deep_validation_report.py`
- `scripts/generate_content.py`
- `scripts/run_content_engine.sh`

Inputs:

- `data/rank_history.csv`
- `docs/leaderboards/rolling_30d.json`
- `docs/signals/index.json`

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

Principle:

```text
If it is not in the validation report, it does not exist.
```

The generator does not recompute strategy metrics and does not use an LLM. It formats already-validated facts.

Detailed documentation:

- `content-generation.md`

## Blog and Public Site

The public pages are served from `docs/` via GitHub Pages.

Important pages:

- `docs/landing.html`: main CTA landing page.
- `docs/blog/index.html`: blog/build-log index.
- `docs/blog/_posts/`: individual posts.
- `docs/biscotti.html`: Algo Biscotti page.
- `docs/bailey.html`: Algo Baileymol page.
- `docs/leaderboard.html`: public leaderboard page.
- `docs/signals/lookup.html`: ticker signal lookup.

Future website separation can copy curated `docs/` and `content/` files into another repo without moving the lab internals.

## GitHub Actions

Primary workflows:

- `.github/workflows/daily_run.yml`: after-market daily run.
- `.github/workflows/crazy_ideas_daily.yml`: daily crazy idea generation.
- `.github/workflows/normal_ideas_weekly.yml`: weekly normal idea generation.

The daily run currently handles baseline, normal algos, crazy algos, dashboards, ledgers, rolling leaderboard, signal precompute, and email reporting. The standalone content engine is intentionally not wired into that flow yet.

Manual trigger:

```text
GitHub -> Actions -> Daily Sector Rotation Run -> Run workflow
```

## Required Secrets

LLM access:

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`

Email delivery:

- `ALERT_EMAIL_TO`
- `ALERT_EMAIL_USER`
- `ALERT_EMAIL_PASS`

Optional data/API stability:

- `FRED_API_KEY`
- `SOCRATA_APP_TOKEN`
- provider-specific keys for any blocked algos in `data/blocked/algos.jsonl`

### Gmail App Password

Gmail does not allow your normal password for SMTP. Create an app password:

1. Go to `myaccount.google.com` -> `Security`.
2. Enable `2-Step Verification`.
3. Go to `Security` -> `App passwords`.
4. Select `Mail`.
5. Select device `Other` and name it `sector-rotation-trader`.
6. Generate the app password.
7. Set it as the GitHub secret `ALERT_EMAIL_PASS`.

## GitHub Pages

1. Go to repo `Settings > Pages`.
2. Source: `Deploy from branch`.
3. Branch: `main`, folder: `/docs`.
4. Dashboard URL: `https://teebuphilip.github.io/sector-rotation-trader/`.

## What This Is And Is Not

This is:

- a live, timestamped paper-trading lab;
- a place to test weird alternative-data trading signals;
- a public record of winners, losers, failures, and rebuilds;
- a content source for public posts grounded in validated system outputs.

This is not:

- investment advice;
- a promise of performance;
- a hidden production trading engine;
- an LLM that invents market stories after the fact.

The lab's credibility comes from running many signals, keeping the receipts, and not hiding the failures.

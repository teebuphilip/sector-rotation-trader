# Architecture

## Executive Summary

Sector Rotation Trader is a paper-trading lab with five independent but related systems:

1. **Core book execution**: baseline NRWise, normal algos, and existing crazy algos run after market close and update state.
2. **Idea generation**: high-action LLM ideas are generated silently into dated folders with schema validation.
3. **Experiment activation**: only after the core book succeeds, approved ideas are gated, built, seeded, run narrowly, and reported by email.
4. **Signal publishing**: dashboards, ledgers, rolling leaderboards, and ticker/sector signal files are written under `docs/`.
5. **Content generation**: a standalone flow reads validated artifacts, writes a deep validation report, and renders short content from that report only.

The core architectural rule is separation of concerns:

```text
trading systems produce facts
validation explains facts
content templates format facts
```

The content layer does not recompute metrics and does not invent narratives.

There is now a second architectural rule for product delivery:

```text
nightly runs compute facts once
-> stripped public JSON is generated
-> static public pages are rendered from that JSON
-> only public-safe artifacts are pushed to the website repo
```

This repo remains the private system of record. The public site should be a rendered view, not a browser-side reconstruction of internal state.

## System Map

```text
09:15 UTC high-action ideas --> schema gate --> publish specs

22:30 UTC core book:
baseline NRWise -+
normal algos ----+--> state files --> dashboards / ledgers / rank history / core email
existing crazies -+

after core success:
publish specs --> final gate --> template build --> seed --> run only new experiments --> experiment email

rank history + rolling 30D + signal precompute --> deep validation report --> content files

nightly public artifact generation:
product/state/backtest/signals --> public-safe JSON --> static public pages --> public repo push
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
- `dashboard.py`: writes the baseline dashboard and trade data.
- `state.json`: baseline state.

Outputs:

- `state.json`
- `docs/nrwise.html`
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

The crazy idea pipeline is structured to avoid garbage-in/garbage-out and is separated from trading-state mutation. The morning workflow only produces candidate artifacts. It does not email and does not run any trading simulation.

Required sequence:

```text
IDEA -> DATA -> BEHAVIOR -> MARKET IMPACT -> TRADE LOGIC
```

Files:

- `prompts/crazy_ideas_prompt.txt`: strict generation prompt.
- `prompts/high_action_crazy_ideas_prompt.txt`: daily high-action generation prompt.
- `scripts/crazy_generate_ideas.py`: ChatGPT + Claude orchestration.
- `scripts/crazy_generate_high_action_ideas.py`: high-action wrapper used by the daily idea workflow.
- `scripts/crazy_schema_gate.py`: deterministic schema validation.
- `scripts/crazy_score_ideas.py`: idea scoring.
- `scripts/crazy_publish_markdown.py`: markdown publishing.

Run layout:

```text
data/ideas/runs/YYYY-MM-DD/raw/
data/ideas/runs/YYYY-MM-DD/filtered/
data/ideas/runs/YYYY-MM-DD/deduped/
data/ideas/runs/YYYY-MM-DD/duplicates/
data/ideas/runs/YYYY-MM-DD/rejected/
data/ideas/runs/YYYY-MM-DD/publish/
data/ideas/runs/YYYY-MM-DD/build/
data/ideas/runs/YYYY-MM-DD/intervention/
data/ideas/runs/YYYY-MM-DD/reject/
data/ideas/runs/YYYY-MM-DD/factory_results/
```

The schema gate rejects ideas before build if they lack real data, clear behavior, sector impact, or deterministic trade logic. After that, the pipeline appends anti-duplicate history context to the generator prompts and runs a deterministic dedupe gate before score/publish. The final publish gate performs a second LLM-assisted check before specs are moved into `build/`, `intervention/`, or `reject/`.

High-action crazy ideas now also carry an explicit `family` field so the lab can be grouped and surfaced systematically instead of as a flat list of unrelated experiments.

Approved families:

- `consumer_stress`
- `travel_mobility`
- `labor_jobs`
- `freight_logistics`
- `attention_sentiment`
- `political_insider_filing`
- `local_economy_weirdness`
- `macro_input_pressure`

## Build + Seed Architecture

The build pipeline turns gated markdown specs into runnable crazy algo files. The production path now favors deterministic template builds. The older structural LLM builder remains available for manual/debug work and its artifacts are retained for review.

Primary orchestrator:

- `scripts/autogen_crazy_factory.py`

Production builder:

- `scripts/build_template_algo.py`

Manual/debug structural builder:

- `scripts/run_structural_build.sh`

Production stages:

```text
read specs from data/ideas/runs/YYYY-MM-DD/build
-> adapter route
-> deterministic template build
-> append registry entry
-> seed accepted algo
-> move spec to completed/failed/intervention
-> write factory_results summary
```

Experiment activation stages:

```text
factory_results seeded ids
-> crazy_run.py --algo-id ID --skip-combined
-> rebuild_crazy_combined_dashboard.py
-> precompute_signals.py
-> rolling_30d_leaderboard.py
-> experiment email
```

Structural/debug stages:

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

## Product Structure Layer

The repo now maintains a derived product layer on top of raw pipeline artifacts. This is similar to the AFH model: operational buckets stay noisy, but product-facing outputs are normalized into stable JSON files.

Generator:

- `scripts/build_product_index.py`

Outputs:

- `data/product/algos_index.json`
- `data/product/families.json`
- `data/product/watchlist.json`
- `data/product/promoted.json`
- `data/product/graveyard.json`
- `data/product/daily_summary.json`

Derived fields:

- `family`
- `status`
- `evidence_class`

Current status model:

- `promoted`
- `backtest_weak`
- `live_only`
- `sandbox`
- `failed`
- `parked`

Current evidence model:

- `v1_backtested`
- `live_receipts_only`
- `needs_history`
- `short_model_pending`
- `pending_seed`

This product layer is what future public pages, operator summaries, and premium/private surfaces should read from.

Public contract generator:

- `scripts/build_public_artifacts.py`

## Public vs Private Split

The July ship target assumes a static public site plus a later premium layer. The public site should be generated from a small, stable contract and pushed to a separate public repo.

Public JSON target shape:

- `docs/data/public/daily.json`
- `docs/data/public/leaderboard.json`
- `docs/data/public/families.json`
- `docs/data/public/watchlist.json`
- `docs/data/public/promoted.json`
- `docs/data/public/graveyard.json`
- `docs/data/public/benchmarks/spy.json`
- `docs/data/public/benchmarks/qqq.json`
- `docs/data/public/signals/index.json`
- `docs/data/public/signals/<symbol>.json`

Contract details:

- every top-level public JSON file carries `schema_version`
- current public contract version is `v1`
- canonical field-level schema lives in `docs/data/public/SCHEMA.md`

Static public pages should be rendered from those files every night. The public per-signal payload is intentionally teaser-safe and does not expose the full internal per-algo breakdown.

Comparator outputs:

- `scripts/comparison_nightly.py`: nightly benchmark/comparator suite.
- `docs/comparison/today.json`: latest comparator payload.
- `docs/comparison/history.json`: comparator history.

Generator:

- `scripts/build_public_artifacts.py`

Internal/private artifacts must stay out of the public repo:

- raw ideas
- intervention/failed factory artifacts
- codegen logs
- full state files
- full trade logs
- full equity curves
- private leaderboard payloads
- debugging outputs

See `content-split.md` for the current free vs paid product split.


## Premium Backend Architecture

The premium backend is intentionally small. The core system remains artifact-first: GitHub Actions runs the trading/product pipeline, writes JSON/HTML artifacts, and GitHub Pages serves the free public surface. Railway is only for paid entitlement checks and private artifact delivery.

Current premium backend files:

- `backend/stockarithm_api.py`: FastAPI/Railway API.
- `backend/BACKEND_ARCHITECTURE.md`: detailed backend design.
- `backend/README.md`: environment and endpoint quickstart.
- `docs/app.html`: static premium frontend shell.

Backend responsibility:

- verify Stripe Checkout Sessions in test or live mode
- receive Stripe webhooks
- store paid entitlements
- set signed HTTP-only session cookies
- answer `/api/me/status`
- gate premium JSON/CSV endpoints

The backend does not run the trading engine and should not calculate live performance. It should serve private artifacts generated by the nightly pipeline. During staging, premium endpoints can fall back to public artifacts so the API surface can be tested before `publish_private.py` exists.

Auth0 is not used because launch does not need an identity platform. Stripe is the payment source of truth, and the product only needs email entitlement plus a signed browser session. Passwords, social login, SSO, teams, MFA, account recovery, and RBAC are deferred until there is a real subscriber-driven need.

Target deployment shape:

- `stockarithm.com`: GitHub Pages static public site.
- `api.stockarithm.com`: Railway FastAPI backend.

Stripe flow:

1. User completes Stripe Checkout.
2. Stripe redirects to `/unlock?session_id={CHECKOUT_SESSION_ID}`.
3. Railway verifies the Checkout Session with Stripe.
4. Railway stores entitlement for the email/customer.
5. Railway sets `stockarithm_session` as a signed HTTP-only cookie.
6. Browser redirects to `docs/app.html`.
7. `docs/app.html` calls `/api/me/status` and premium endpoints with credentials included.

Webhook flow:

1. Stripe sends `POST /webhook`.
2. Railway verifies `Stripe-Signature` with `STRIPE_WEBHOOK_SECRET`.
3. Railway records processed event IDs to avoid replay.
4. Railway marks entitlement active or inactive for checkout/subscription events.

Staged endpoints:

- `GET /health`
- `GET /unlock?session_id=...`
- `POST /webhook`
- `POST /logout`
- `GET /api/me/status`
- `GET /api/premium/leaderboard`
- `GET /api/premium/signal/{algo_id}`
- `GET /api/premium/ticker/{symbol}`
- `GET /api/premium/download/{kind}`

Runtime files are gitignored:

- `data/premium/entitlements.json`
- `data/premium/stripe_events.json`
- `private_artifacts/`

Public site publishing:

- `scripts/publish_public_site.py` publishes only an explicit allowlist to `stockarithm-site`.
- The nightly workflow can push the public bundle after the 6:30pm run when `PUBLIC_SITE_PUSH_TOKEN` is configured.
- The public repo receives static pages, blog files, and `docs/data/public/`; it does not receive backend code, trading logic, raw state, ledgers, or private artifacts.

Public site rollback:

- `scripts/rollback_public_site.py` safely rolls back bad `stockarithm-site` publishes with `git revert`.
- It refuses dirty or stale public checkouts and does not force-push.
- Details live in `PUBLIC_SITE_OPERATIONS.md`.

Open before real paid launch:

- deploy Railway service
- create Stripe test product/price
- wire Stripe webhook endpoint
- complete end-to-end test checkout
- build private artifact publisher
- decide whether Railway filesystem is enough or whether entitlement/private artifacts need Postgres/R2

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

- `data/algos_codegen/`: retained LLM/structural build reports for review.
- `data/algos/new_algos.jsonl`: audit log of newly noticed algos; retained pending cleanup/retention decision.

Validation cache:

- `data/.validation_cache/`

## Dashboards and Public Outputs

Public-facing files are generated under `docs/`.

Dashboards:

- `docs/nrwise.html`: baseline dashboard.
- `docs/normal/<algo_id>/index.html`: normal algo dashboards.
- `docs/algos/<algo_id>/index.html`: crazy algo dashboards.
- `docs/crazy/index.html`: combined crazy dashboard.

Leaderboards and ledgers:

- `docs/leaderboards/rolling_30d.json`
- `docs/leaderboards/rolling_30d.md`
- `docs/ledgers/normal_ledger.json`
- `docs/ledgers/crazy_ledger.json`

Marketing/site:

- `docs/index.html`: public homepage.
- `docs/landing.html`: homepage alias generated from the same source.
- `docs/leaderboard.html`: public proof page.
- `docs/families.html`: public family/grouping page.
- `docs/daily.html`: nightly public snapshot page.
- `docs/premium.html`: premium teaser page.
- `docs/legal.html`: public disclaimer/legal page.
- `docs/blog/index.html`
- `docs/blog/_posts/`
- `docs/biscotti.html`
- `docs/bailey.html`

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


## Professional Backtest V1 Architecture

The backtest system is a reusable engine, not one-off code per algo. It loads existing normal/crazy algo plugins, classifies whether each can be honestly tested under V1 rules, then runs only supported algos.

Files:

- `backtest/classifier.py`: decides `BACKTESTABLE`, `UNSUPPORTED_DATA`, or `UNSUPPORTED_SHORT`.
- `backtest/price_data.py`: downloads/caches OHLCV price data and builds the price-only adapter envelope.
- `backtest/engine.py`: no-lookahead simulation loop, next-open execution, slippage, long/cash rebalancing.
- `backtest/metrics.py`: SPY comparison, alpha, drawdown, Sharpe, trade count, win rate, turnover, labels.
- `backtest/report.py`: per-algo and master JSON/Markdown/CSV outputs.
- `scripts/run_professional_backtest.py`: CLI entry point.

V1 method:

```text
signal computed after close on day T
-> target queued
-> trade executes at next trading day open T+1
-> slippage applied
-> daily equity marked at close
-> compared to SPY buy-and-hold
```

V1 intentionally rejects or parks:

- native short exposure;
- non-sector/non-SPY tickers;
- non-price adapters without point-in-time historical data;
- direct live downloads that cannot be proven point-in-time safe.

This is the credibility layer: generated does not mean trusted, seeded does not mean proven, and only backtestable signals get a professional V1 grade.

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

## LLM Post Generator and Morning Content Email

An LLM rewrite pass sits on top of the content engine output.

Flow:

```text
reports/deep_validation/latest.json
-> scripts/post_generator.py (calls Claude API, facts-only)
-> drafts/YYYY-MM-DD.md
-> scripts/morning_content_email.py
-> email to operator at 4:30am EST
```

Scripts:

- `scripts/post_generator.py`: reads locked facts from the deep validation JSON, calls Claude API, writes a 300-400 word Substack draft to `drafts/`. No invention — only facts present in the report can appear in the draft.
- `scripts/morning_content_email.py`: reads `drafts/YYYY-MM-DD.md` and emails it to the operator.

The post generator enforces the same voice rules as the content engine: honest, curious, human, transparent. Forbidden language list applies.

Wired as `.github/workflows/morning_content_email.yml` at 09:30 UTC (4:30am EST) — 1 hour after the ops stats email.

Substack push (cookie-auth via `substack_publisher.py`) is a post-launch task.

### Social Content Generator

`scripts/social_content_generator.py` runs inside the same `morning_content_email.yml` job after `post_generator.py`. It generates 6 channel-specific drafts from the same deep validation facts block:

- `drafts/social/YYYY-MM-DD/reddit_algotrading.md` — methodology-first, self-deprecating, invites critique
- `drafts/social/YYYY-MM-DD/reddit_investing.md` — outcome-focused, accessible
- `drafts/social/YYYY-MM-DD/reddit_stocks.md` — punchy scoreboard, minimal words
- `drafts/social/YYYY-MM-DD/reddit_quant.md` — technical, honest about sample size
- `drafts/social/YYYY-MM-DD/reddit_security_analysis.md` — macro framing, sector rotation rationale
- `drafts/social/YYYY-MM-DD/twitter_x.md` — terse Fintwit, one stat, screenshot prompt

One LLM call per channel. Same facts-only constraint as `post_generator.py`. It now reads the real deep-validation schema keys, uses deterministic temperature, and lints for URL/brand/placeholder errors before writing. Operator decides what to post and when — nothing is auto-published.

### Reddit Launch Post Refresh

`scripts/refresh_reddit_drafts.py` is a deterministic (no LLM) script that fills `{variable}` placeholders in the Reddit launch post templates with live numbers from canonical public/rank artifacts: `docs/data/public/leaderboard.json`, `data/rank_history.csv`, `docs/leaderboards/rolling_30d.json`, and `docs/data/public/daily.json`. It supports optional same-day overrides and fails loudly if unresolved placeholders or stale canned claims remain. Writes dated copies to `drafts/reddit_launch/YYYY-MM-DD/`.

`.github/workflows/reddit_draft_refresh.yml` runs this daily at 14:00 UTC until May 15, keeping fresh number-filled copies committed to the repo. After May 15 the workflow exits cleanly with no action needed.

Detailed doc:

- `content-generation.md`

## GitHub Actions

Primary workflows:

- `.github/workflows/daily_run.yml`: core book run; runs baseline, normal, existing crazy, dashboards, ledgers, signal precompute, nightly comparators, validation, and core email steps.
- `.github/workflows/crazy_ideas_daily.yml`: morning high-action idea generation; silent, no email, no trading-state mutation.
- `.github/workflows/crazy_daily_builds.yml`: experiment activation; triggered by successful completion of the core book workflow.
- `.github/workflows/normal_ideas_weekly.yml`: generates and publishes normal ideas.
- `.github/workflows/morning_stats_email.yml`: ops stats email at 08:30 UTC (3:30am EST).
- `.github/workflows/morning_content_email.yml`: LLM post draft email at 09:30 UTC (4:30am EST). Also runs social content generator.
- `.github/workflows/reddit_draft_refresh.yml`: daily Reddit launch post number refresh at 14:00 UTC; auto-stops after May 15.

## Execution Flow: Daily Tactical Run

Current core tactical flow:

```text
daily_run.py
-> normal_run.py
-> crazy_run.py
-> cleanup_blocked_keys.py
-> precompute_signals.py
-> rolling_30d_leaderboard.py
-> rank_daily.py
-> validate_nightly.py / quality_check.py
-> core email
-> docs/ updated
```

Current experiment activation flow:

```text
core workflow success
-> final_publish_llm_gate.py
-> autogen_crazy_factory.py --template-build --skip-run
-> crazy_run.py --algo-id NEW_ID --skip-combined
-> rebuild_crazy_combined_dashboard.py
-> precompute_signals.py
-> rolling_30d_leaderboard.py
-> experiment email
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

- The core book is the priority workflow; experiments only activate after core success.
- Generated algos should be structurally valid first; strategy polish is secondary.
- Adapters are preferred over generated data-fetching code.
- Low-confidence adapter matches go to intervention.
- Missing-key algos are blocked, not fatal.
- Flat-cash history is acceptable for live-only/no-history crazy algos.
- Force rank and rolling 30D are separate concepts.
- Content generation is deterministic and report-driven.
- Public credibility comes from publishing winners and failures.
- Codegen logs and failed/intervention artifacts are retained temporarily until a cleanup/retention script exists.

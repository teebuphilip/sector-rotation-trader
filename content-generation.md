# Content Generation

## Purpose

The content engine turns validated system output into short public-facing text. It exists so the lab can publish daily posts, signal spotlights, failure reports, calls of the day, and weekly summaries without adding another interpretation layer.

The content engine is intentionally separate from the tactical run.

It does not run algos. It does not seed algos. It does not generate ideas. It does not call an LLM. It only reads already-produced artifacts and formats validated facts.

## Core Rule

```text
If it is not in the deep validation report, it does not exist.
```

The content system must not invent metrics, recompute returns, infer unstated causes, or add market commentary not present in the validation report.

## Current Flow

```text
data/rank_history.csv
+ docs/leaderboards/rolling_30d.json
+ docs/signals/index.json
-> scripts/write_deep_validation_report.py
-> reports/deep_validation/latest.json
-> scripts/generate_content.py
-> content/*.txt
```

Wrapper:

```bash
scripts/run_content_engine.sh
```

Specific report date:

```bash
scripts/run_content_engine.sh --date 2026-04-15
```

## Inputs

### `data/rank_history.csv`

Produced by:

- `scripts/rank_daily.py`

Provides:

- force rank;
- full-window/since-seed return;
- alpha versus SPY;
- days running;
- beat-SPY flag;
- prior rank movement when prior dates exist.

This is the long-term trust source.

### `docs/leaderboards/rolling_30d.json`

Produced by:

- `scripts/rolling_30d_leaderboard.py`

Provides:

- trailing 30-day return;
- trailing 30-day Sharpe;
- trailing 30-day max drawdown;
- SPY 30-day return;
- recent leaderboard rank.

This is the recent-momentum source.

### `docs/signals/index.json`

Produced by:

- `precompute_signals.py`

Provides:

- total signal count;
- ticker count;
- top bullish ETFs;
- top bearish ETFs;
- sector heatmap;
- current ticker/sector lookup metadata.

This is the current sector/ticker consensus source.

## Outputs

Deep validation reports:

- `reports/deep_validation/YYYY-MM-DD.md`
- `reports/deep_validation/YYYY-MM-DD.json`
- `reports/deep_validation/latest.md`
- `reports/deep_validation/latest.json`

Generated content:

- `content/daily/YYYY-MM-DD.txt`
- `content/signal_of_day/YYYY-MM-DD.txt`
- `content/failures/YYYY-MM-DD.txt`
- `content/call_of_day/YYYY-MM-DD.txt`
- `content/weekly/YYYY-WW.txt`

## Scripts

### `scripts/write_deep_validation_report.py`

Builds the authoritative report from existing artifacts.

Responsibilities:

- load latest or requested force-rank date;
- load rolling 30D leaderboard;
- load precomputed signal index;
- define force rank versus rolling 30D explicitly;
- compute only report-level joins such as matching force rank to rolling rank;
- identify notable divergences;
- write Markdown for humans;
- write JSON for machines.

It does not rerun strategies and does not fetch market data.

### `scripts/generate_content.py`

Renders deterministic templates from `reports/deep_validation/latest.json`.

Responsibilities:

- generate a daily leaderboard post;
- generate signal of the day;
- generate failure report;
- generate call of the day;
- generate current weekly snapshot;
- write text files under `content/`.

It does not use an LLM and does not recompute metrics.

### `scripts/run_content_engine.sh`

Runs both report generation and content generation.

```bash
scripts/run_content_engine.sh
```

Optional args are passed to `write_deep_validation_report.py`:

```bash
scripts/run_content_engine.sh --date 2026-04-15
```

## Deep Validation Report Structure

The JSON report contains:

- `report_date`
- `generated_at`
- `definitions`
- `system_state`
- `force_rank`
- `rolling_30d`
- `sector_consensus`
- `events`
- `content_facts`

The Markdown report mirrors the same facts in human-readable form.

## Force Rank vs Rolling 30D

This distinction is critical.

Force rank:

- Source: `data/rank_history.csv`.
- Meaning: full-window/since-seed rank.
- Use: long-term trust, promotion/demotion, kill review.

Rolling 30D:

- Source: `docs/leaderboards/rolling_30d.json`.
- Meaning: trailing 30-day rank.
- Use: tactical spotlight and recent momentum.

A signal can be low on force rank and high on rolling 30D. That is not an error. It means recent performance is stronger than its full-window record.

Example interpretation:

```text
Algo Biscotti is force rank #45 but rolling 30D rank #1.
That means it has strong recent momentum despite weak full-window validation.
```

The content engine surfaces that as a divergence instead of hiding it.

## Content Types

### Daily Post

File:

- `content/daily/YYYY-MM-DD.txt`

Contains:

- top force-ranked signals;
- top rolling 30D signals;
- notable divergences;
- system counts.

Purpose:

- concise public daily status.

### Signal Of The Day

File:

- `content/signal_of_day/YYYY-MM-DD.txt`

Selection source:

- `content_facts.signal_of_day`

Current selection priority:

- top rolling 30D signal if available;
- otherwise top force-ranked signal.

The file includes caveats when rolling rank and force rank diverge.

### Failure Report

File:

- `content/failures/YYYY-MM-DD.txt`

Selection source:

- `content_facts.failure_of_day`

Current behavior:

- selects the lowest full-window force-ranked signal as the failure of the day;
- lists bottom force-ranked signals.

This is intentionally blunt. The lab publishes failures as well as wins.

### Call Of The Day

File:

- `content/call_of_day/YYYY-MM-DD.txt`

Selection source:

- `content_facts.call_of_day`

Current behavior:

- selects the sector with highest bullish percentage from precomputed sector consensus;
- includes composite label and top sector context.

### Weekly Summary

File:

- `content/weekly/YYYY-WW.txt`

Current behavior:

- writes a current snapshot for the ISO week.

Important limitation:

- V1 does not aggregate seven historical reports yet. It says so explicitly in the output. True weekly aggregation should come later from seven deep validation reports.

## Why JSON And Markdown

Markdown exists because humans need to read the validation report.

JSON exists because machines should not parse prose when exact fields are available.

The authoritative content source is:

```text
reports/deep_validation/latest.json
```

The human-readable equivalent is:

```text
reports/deep_validation/latest.md
```

## What The Content Engine Must Not Do

The content engine must not:

- call OpenAI, Anthropic, or any LLM;
- download market data;
- recompute returns;
- decide new rankings;
- invent reasons for performance;
- promote or kill signals independently;
- change algo state;
- write dashboards;
- move ideas between triage buckets.

Those are upstream responsibilities.

## Future Extensions

Safe future additions:

- aggregate seven daily reports into a true weekly summary;
- add a `post_queue/` for manual review before publishing;
- add a website export job that copies selected `content/` and `docs/` files to a public repo;
- add image/screenshot generation from the already-rendered content;
- add an optional LLM rewrite pass that receives only locked JSON facts and is forbidden from adding facts.

Unsafe additions:

- letting an LLM read dashboards and invent narratives;
- letting content generation recompute strategy metrics;
- mixing tactical email logic into the content generator;
- treating rolling 30D and force rank as the same metric.

## Local Validation

Compile the scripts:

```bash
python -m py_compile scripts/write_deep_validation_report.py scripts/generate_content.py
```

Run the content engine:

```bash
scripts/run_content_engine.sh
```

Inspect outputs:

```bash
cat reports/deep_validation/latest.md
cat content/daily/$(date +%F).txt
cat content/signal_of_day/$(date +%F).txt
cat content/failures/$(date +%F).txt
cat content/call_of_day/$(date +%F).txt
```

## Operational Position

The content engine is a reporting layer, not a trading layer.

Its job is to turn system truth into concise text. If the system truth is ugly, the content should be ugly. That is the point of the lab.

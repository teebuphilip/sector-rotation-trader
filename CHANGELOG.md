# Changelog

## 2026-04-21 (session 5 — morning stats email)

### feat: wire up daily_stats_email.py as a morning 8am UTC workflow
- New `.github/workflows/morning_stats_email.yml` runs at 08:00 UTC daily.
- Passes `AFH_RUN_DATE=yesterday` so the email reports on the previous day's completed runs (nightly book closes at 22:30 UTC, so all data is in place by 8am).
- Supports `workflow_dispatch` with optional `run_date` override for replays.
- Uses existing `ALERT_EMAIL_TO`, `ALERT_EMAIL_USER`, `ALERT_EMAIL_PASS` secrets.

### fix: force rank section in daily_stats_email.py used hardcoded utcnow() date
- Line 331 was filtering `rank_history.csv` by `datetime.utcnow()` instead of `run_date`.
- When run at 8am for yesterday's data, force rank always showed "no rows for today".
- Now uses `run_date` (which respects `AFH_RUN_DATE`) consistently.

Files: `scripts/daily_stats_email.py`, `.github/workflows/morning_stats_email.yml`

## 2026-04-21 (session 4 — P2 operational pipeline fixes)

### fix: template-built algo is syntax-checked before being marked as built
- `build_template_algo.py` now runs `compile()` on the generated Python file immediately after writing it.
- If the generated code has syntax errors (e.g., unescaped quotes in idea name or adapter call), the file is removed and the script exits with code 1.
- The factory's existing `build_proc.returncode != 0` check catches this and marks the spec as `failed_build` instead of proceeding to a seed that would fail on import.

Files: `scripts/build_template_algo.py`

### fix: factory crash before summary.json is written now fails the workflow visibly
- Added "Verify factory summary written" step in `crazy_daily_builds.yml` immediately after the autogen step.
- If `summary.json` is missing (autogen crashed before completion), the job fails before the commit and email steps run.
- Previously, the email reported job success even when autogen crashed, because `continue-on-error: true` swallowed the failure and the only check was in a late "Assess" step that ran after the email.

Files: `.github/workflows/crazy_daily_builds.yml`

## 2026-04-21 (session 3 — P1 operational pipeline fixes)

### fix: registry entry now written only after seed succeeds, not after build
- `autogen_crazy_factory.py` was appending to `data/algos_registry_crazy.txt` immediately after a successful build, before `crazy_seed.py` ran.
- If seed failed, the algo was in the registry but unloadable — silently skipped on every future run.
- Registry append now happens only after both build and seed succeed (just before spec is moved to completed/).
- `--seed-only` mode skips the append since the algo was already registered in a prior build run.

Files: `scripts/autogen_crazy_factory.py`

### fix: single LLM generator failure now prints a warning
- `crazy_generate_high_action_ideas.py` previously swallowed ChatGPT or Claude failures silently — error written to file, nothing on stderr.
- Now prints `[warn] <generator> generator failed: <reason>` to stderr on each individual failure.
- Both-fail path already returned exit code 1; this adds visibility for the partial-failure case.

Files: `scripts/crazy_generate_high_action_ideas.py`

## 2026-04-21 (session 2 — P0 operational pipeline fixes)

### fix: state.json corruption no longer crashes the daily run
- `portfolio.py:load_state_from` now wraps `json.load()` in try/except for `JSONDecodeError`/`ValueError`.
- On corruption, prints a CRITICAL warning to stderr and falls back to `_default_state()` instead of raising.
- Previously a truncated state file (e.g. mid-write crash) would hard-fail the entire daily run.

Files: `portfolio.py`

### fix: stock data download failure with open positions now aborts instead of continuing silently
- `daily_run.py` previously continued with empty `prices_all` when yfinance failed on stock data.
- Exit signals would never fire (all tickers skipped), positions held indefinitely with no action.
- Now: if download fails and positions are open, exits with code 1. If no positions, continues with entry-only skip as before.

Files: `daily_run.py`

### fix: zero/negative price guard in open_position
- `portfolio.py:open_position` now rejects prices <= 0 before computing shares.
- Prevents `shares = inf` from corrupting state if yfinance returns a bad close price.

Files: `portfolio.py`

## 2026-04-21 (session 1 — crazy idea dedupe + prompt memory)

### feat: deterministic dedupe gate for crazy ideation
- Added `scripts/dedup_crazy_ideas.py` and wired it into the high-action idea pipeline after schema validation and before scoring/publish.
- Duplicate checks now compare the current run, existing algos, and recent idea history using normalized titles, structural fingerprints, and token overlap.
- New artifacts: `data/ideas/runs/YYYY-MM-DD/deduped/` and `data/ideas/runs/YYYY-MM-DD/duplicates/report.json`.
- `scripts/crazy_build_email.py` now reports dedupe keep/remove counts.

Files: `scripts/dedup_crazy_ideas.py`, `scripts/crazy_generate_high_action_ideas.py`, `scripts/crazy_score_ideas.py`, `scripts/crazy_publish_markdown.py`, `scripts/crazy_build_email.py`, `prompts/high_action_crazy_ideas_prompt.txt`, `prompts/high_action_crazy_ideas_prompt_claude.txt`

### feat: inject existing idea history into generator prompts
- `scripts/crazy_generate_high_action_ideas.py` now appends an `ANTI-DUPLICATE CONTEXT` block to both ChatGPT and Claude prompts.
- That context includes compact existing algo titles plus recent idea titles so the generators see prior work before proposing new ideas.
- This adds prompt-level prevention on top of the deterministic dedupe gate.

Files: `scripts/crazy_generate_high_action_ideas.py`

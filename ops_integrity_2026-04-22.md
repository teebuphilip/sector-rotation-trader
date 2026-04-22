# Ops Integrity Check — 2026-04-22

Scope:

- ideation pipeline
- tactical/core run
- factory/algo generation path
- registry/state/output integrity

## Summary

Current state:

- tactical pipeline is green
- ideation pipeline is green
- state freshness is clean
- crazy registry is syntactically clean
- one factory integrity bug was found and fixed

## Findings

### 1. Factory seed path was broken for newly built algos

Severity: high

What was happening:

- `scripts/autogen_crazy_factory.py` now appends registry lines only after seed succeeds
- that avoids orphaned registry entries
- but `crazy_seed.py --algo-file ...` was still trying to seed by converting the file path to an algo id and then asking the registry loader to find it
- because the new algo was not yet in the registry, seed failed with:
  - `No matching crazy algos found to seed`

Evidence:

- `data/ideas/runs/2026-04-22/factory_results/summary.json`
  - `attempted: 5`
  - `built: 5`
  - `seeded: 0`
  - `failed: 5`
- individual `factory_results/*.json` files showed `failed_seed`

Fix applied:

- `crazy_seed.py` now loads `--algo-file` targets directly from the file path, finds the single `CrazyAlgoBase` subclass in that module, and seeds it without needing a registry entry first

Result:

- preserves the no-orphan registry rule
- restores the build -> seed path for new algos

### 2. Crazy registry integrity is currently clean

Checks:

- `data/algos_registry_crazy.txt`
- corresponding files in `crazy/algos/`
- AST parse of every registered module

Result:

- `99` registry entries
- `0` missing files
- `0` syntax failures

### 3. State freshness is currently clean

Checks:

- `state.json`
- `data/normal/state/*.json`
- `data/crazy/state/*.json`

Result:

- baseline last run: `2026-04-22`
- normal states: `5`, stale: `0`, missing `last_run`: `0`
- crazy states: `99`, stale: `0`, missing `last_run`: `0`

### 4. Ideation run artifacts are consistent again on recent runs

Recent runs checked:

- `2026-04-20`
- `2026-04-22`

Result:

- raw / filtered / rejected / deduped / duplicates report are present where expected
- latest dedupe report for `2026-04-22` shows:
  - `input_count: 25`
  - `kept_count: 25`
  - `duplicate_count: 0`

## Remaining watch items

### Node 20 GitHub Actions deprecation

The latest successful workflows still emit GitHub runner warnings about Node 20 actions.

This is not breaking today, but it is real technical debt for launch operations.

### Factory rerun needed after seed fix

The seed fix is in code now, but the failed `2026-04-22` factory outputs were produced before the fix.

The next factory run should confirm:

- built > 0
- seeded > 0 when eligible specs are present
- completed > 0

## Verdict

Ops integrity is materially better than the prior review.

The main real issue found in this pass was the factory seed regression introduced by the anti-orphan registry change. That is now fixed.

# Quality Check #3 — 2026-04-23 Early Run

Task date: 2026-04-27  
Run date reviewed: 2026-04-22  
Reason run early: pipelines were clean on 2026-04-23 morning and the check was next high-priority work.

## Summary

The lab is operationally clean but product quality is uneven.

Current headline:

- total algos tracked: 112
- normal algos: 5
- crazy algos: 107
- promoted: 5
- watchlist: 35
- graveyard: 7
- crazy algos with any live activity: 33 / 107
- crazy algos still idle: 74 / 107
- algos beating SPY by force-rank: 2 / 104
- algos beating SPY with actual trading activity: 2 / 112

The system is running. The main pattern is not broad alpha yet; it is separation between a small number of working baseline/normal strategies and a large experimental crazy universe that is mostly still collecting evidence.

## What Looks Good

### 1. Core pipelines are green

Start-of-day checks on 2026-04-23:

- Morning Stats Email: success
- Daily Sector Rotation Run: success
- Crazy Idea Daily: success
- Morning Content Email: success

No immediate pipeline triage was needed.

### 2. Factory seed-path fix appears to have unblocked new algo activation

Yesterday's ops integrity scan found that new generated algos could build but not seed because `crazy_seed.py --algo-file` still depended on registry lookup.

After the fix, the latest pulled workflow artifacts show new algos registered and seeded:

- registry count increased to 107 crazy algos
- 8 new generated algo files appeared
- new states/dashboards/backtest artifacts exist for the 2026-04-22 factory run

This is the right behavior.

### 3. Registry and state integrity are clean

Checks:

- crazy registry entries: 107
- missing registered algo files: 0
- syntax failures in registered algo files: 0
- normal state files: 5
- crazy state files: 107

No orphaned registry problem was found after the factory fix.

### 4. Product contract exists and is versioned

The public JSON contract now has `schema_version: "v1"` and `docs/data/public/SCHEMA.md` documents the public payload shape.

This closes the old public-schema architecture gap.

## Performance / Signal Read

### Force-rank leaders

Latest rank date: 2026-04-22  
Ranked algos: 104  
Beating SPY: 2

Top 5:

1. Algo Baileymol (normal): +6.65% YTD, +2.26% alpha
2. Antonacci Dual Momentum Sector Rotation: +4.53% YTD, +0.15% alpha
3. Faber Momentum Rotation: +3.85% YTD, -0.54% alpha
4. Retail Sales Momentum: +0.74% YTD, -3.65% alpha
5. Insider Trading Signals: +0.16% YTD, -4.23% alpha

Bottom 5:

- Algo Biscotti (normal): -1.86% YTD, -6.25% alpha
- Algo Biscotti (crazy): -3.82% YTD, -8.21% alpha
- VIX Term Structure: -5.34% YTD, -9.73% alpha
- Chaos Rotation Lab: -5.35% YTD, -9.74% alpha
- VIX Fear Rotation: -7.14% YTD, -11.53% alpha

Read:

- the strongest current evidence is still in normal/baseline-style rotation, not the broad crazy set
- retail-sales-momentum is the most interesting crazy leader right now, but still badly lagging SPY
- VIX variants are consistently weak and high churn

## Crazy Algo Activity

Active crazy algos: 33 / 107  
Idle crazy algos: 74 / 107

Important interpretation:

- idle is not failure
- the public copy should continue saying idle means the trigger has not had a chance to prove itself
- however, 74 idle algos is high enough that the product should emphasize "lab evidence collection" rather than implying every signal is actively competing every day

## Blocked / Missing Keys

Blocked keys currently visible:

- `EIA_API_KEY`: Electricity Consumption
- `GLASSDOOR_KEY`: Glassdoor Misery Gradient
- `GLASSDOOR_PARTNER_ID`: Glassdoor Misery Gradient
- `YELP_API_KEY`: Yelp Closure Velocity

These are not launch blockers for the free site. They are evidence-depth blockers.

## Warnings

### 1. Comparator suite is running but currently not useful

Comparator artifact exists for 2026-04-22, but both comparators show:

- `momentum_5d`: NEUTRAL 11 / insufficient_data 11
- `momentum_20d`: NEUTRAL 11 / insufficient_data 11

This means the comparator section is structurally wired but not yet producing meaningful baseline context.

This should be fixed before the comparator badges are treated as product proof.

### 2. Deep validation report is stale

`reports/deep_validation/latest.json` is still dated 2026-04-15.

That matters because the morning content generator reads `reports/deep_validation/latest.json`. If this report is stale, the content email may be using stale facts even while the trading/artifact pipeline is current.

This needs a follow-up task or workflow fix.

### 3. Several active strategies hold positions while signal is HOLD

The quality check script flags many `POSITIONS WITH HOLD` warnings. This may be normal depending on strategy semantics, but the warning is currently noisy.

Examples:

- baileymol
- biscotti
- dmsr
- copper-momentum
- electricity-consumption
- finra-dark-pool-signal
- vix-fear-rotation
- vix-term-structure

Action needed:

- decide whether HOLD means "maintain existing position" or "should be flat"
- if HOLD means maintain, update the quality-check warning so it does not create false alarm noise

### 4. Churn warnings are real watch items

Flagged:

- baileymol: 62 trades, -5.35% YTD
- vix-fear-rotation: 118 trades, -7.14% YTD
- vix-term-structure: 106 trades, -5.34% YTD

The VIX family especially looks like overtrading or bad regime fit.

## Decisions / Recommendations

1. Do not promote broad crazy performance yet.
2. Keep public story focused on transparency, evidence collection, and visible failures.
3. Fix comparator insufficient-data before leaning on comparator badges as proof.
4. Fix stale deep-validation report before trusting morning content automation.
5. Review the VIX family as an early failure/overtrading candidate.
6. Clarify HOLD semantics in quality checks.

## Verdict

Go for continued June 15 free-site work.

No launch-blocking operational failure found today, but the system is not yet showing broad signal superiority. The credible story remains: many weird signals are running in public, most are unproven, and the lab is starting to separate evidence from noise.

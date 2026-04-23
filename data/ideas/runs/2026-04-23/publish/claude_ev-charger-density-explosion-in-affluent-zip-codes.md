# Ev Charger Density Explosion In Affluent Zip Codes

**Idea ID:** `ev-charger-density-explosion-in-affluent-zip-codes`
**Family:** `travel_mobility`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Rapid charger deployment in wealthy neighborhoods signals credible EV adoption acceleration and consumer confidence in clean tech. Weekly net new charger installations >50 units in top 5 metros correlate with discretionary spending strength. Charger buildout in affluent areas is a leading indicator of high-income consumer willingness to invest in EV infrastructure; strong EV sales follow deployment surges.

## Universe
- XLY

## Data Sources
- OpenChargeMap API weekly charger count deltas in top 20 affluent metro areas (zip code filtering) vs Yahoo Finance XLY weekly price via price_only adapter

## Signal Logic
If weekly net charger additions in top 5 metros exceed 50 units AND XLY closes > 5-day SMA AND RSI(14) < 70

## Entry / Exit
Entry: If weekly net charger additions in top 5 metros exceed 50 units AND XLY closes > 5-day SMA AND RSI(14) < 70 Exit: After 21 calendar days OR if weekly charger additions fall below 30 units for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API weekly charger count deltas in top 20 affluent metro areas (zip code filtering) vs Yahoo Finance XLY weekly price via price_only adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Infrastructure investment in affluent areas happens in seasonal waves; deployment surges typically occur in spring and fall renewal cycles.

## Required Keys
- None

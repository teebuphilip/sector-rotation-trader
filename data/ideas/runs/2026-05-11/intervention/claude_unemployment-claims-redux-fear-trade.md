# Unemployment Claims Redux Fear Trade

**Idea ID:** `unemployment-claims-redux-fear-trade`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly initial jobless claims spike 15%+ above 4-week moving average, it signals labor market deterioration, triggering defensive rotation into healthcare and staples. Rising claims trigger flight-to-safety rotation; staples outperform as consumer spending shifts to necessities.

## Universe
- XLP

## Data Sources
- FRED series ICSA (Initial Claims, Seasonally Adjusted) via fred_series adapter

## Signal Logic
If weekly initial claims exceed 4-week MA by 15% and close above prior week level

## Entry / Exit
Entry: If weekly initial claims exceed 4-week MA by 15% and close above prior week level Exit: After 10 trading days or if claims revert to <105% of 4-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Claims, Seasonally Adjusted) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Claims volatility is structural; 15%+ spikes occur 4-6x yearly from seasonal shocks, weather layoffs, or economic hiccups.

## Required Keys
- None

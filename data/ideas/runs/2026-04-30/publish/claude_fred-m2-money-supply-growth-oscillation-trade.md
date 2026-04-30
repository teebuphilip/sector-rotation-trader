# Fred M2 Money Supply Growth Oscillation Trade

**Idea ID:** `fred-m2-money-supply-growth-oscillation-trade`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly M2 growth rate crosses from positive to negative or vice versa; reversal signals shift in Fed liquidity stance or unexpected monetary tightening. Technology and growth stocks are most sensitive to liquidity reversals; sudden M2 contraction triggers defensive rebalancing into cash.

## Universe
- XLK

## Data Sources
- FRED M2 Money Supply (weekly) series WIMFSL through fred_series adapter

## Signal Logic
If 4-week M2 growth rate changes sign (pos→neg or neg→pos) and 10-year yield spreads widen by 20+ bps

## Entry / Exit
Entry: If 4-week M2 growth rate changes sign (pos→neg or neg→pos) and 10-year yield spreads widen by 20+ bps Exit: After 8 trading days or once M2 growth rate stabilizes in one direction for 3 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED M2 Money Supply (weekly) series WIMFSL through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: M2 growth oscillates every 4-8 weeks; sign reversals occur 6-8 times per year, especially during Fed policy transitions.

## Required Keys
- None

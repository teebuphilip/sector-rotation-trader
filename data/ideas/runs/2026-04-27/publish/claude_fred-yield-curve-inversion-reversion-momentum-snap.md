# Fred Yield Curve Inversion Reversion Momentum Snap

**Idea ID:** `fred-yield-curve-inversion-reversion-momentum-snap`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When the yield curve inverts (2yr > 10yr) for 3+ weeks then suddenly re-steepens by 15+ bps in one week, it signals a capitulation reversal and flight-to-risk rally. Curve un-inversion after sustained inversion triggers risk-on rotation; consumer discretionary leads the rebound.

## Universe
- XLY

## Data Sources
- FRED 10-year vs 2-year yield spread (T10Y2Y)

## Signal Logic
If curve has been inverted for 20+ days and spreads 20+ bps steeper in one week, long XLY.

## Entry / Exit
Entry: If curve has been inverted for 20+ days and spreads 20+ bps steeper in one week, long XLY. Exit: After 7 trading days or if curve re-inverts.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED 10-year vs 2-year yield spread (T10Y2Y) via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Curve inversions and reversals occur in monetary cycles; steepening bounces fire multiple times per year.

## Required Keys
- None

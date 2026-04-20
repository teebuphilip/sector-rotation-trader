# Housing Market Fever Dream

**Idea ID:** `housing-market-fever-dream`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Rapid changes in mortgage rates can signal heightened volatility and uncertainty in the housing market, with potential spillover effects on related sectors. Rising mortgage rates can negatively impact housing affordability and activity, which has implications for the real estate sector.

## Universe
- XLRE

## Data Sources
- Weekly average mortgage rates from FRED through fred_series adapter

## Signal Logic
If the weekly average mortgage rate increases by more than 0.25 percentage points

## Entry / Exit
Entry: If the weekly average mortgage rate increases by more than 0.25 percentage points Exit: After 2 weeks or once the rate increase is reversed by 0.15 percentage points

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Weekly average mortgage rates from FRED through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Mortgage rates are highly sensitive to economic conditions and monetary policy changes, which can lead to rapid rate movements within a 30-day period.

## Required Keys
- None

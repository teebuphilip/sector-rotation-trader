# Mortgage Rate Shock Yield-curve Steepening Hedge

**Idea ID:** `mortgage-rate-shock-yield-curve-steepening-hedge`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When 2-10 year spread widens >25 bps in a single week after being inverted or flat, bond market is pricing in rate-cut expectations. Utilities and REITs rally on lower discount rates. Steeper curves and falling long rates compress the required return on stable utility cash flows, driving re-rating upward.

## Universe
- XLU

## Data Sources
- FRED series DGS10 (10-year yield) and DGS2 (2-year yield) daily via fred_series adapter, plus XLU (utilities ETF) daily close via price_only adapter

## Signal Logic
If (DGS10 - DGS2) increases by >25 bps over 5 trading days AND XLU closes above 20-day SMA AND 10-year yield drops >10 bps from 5-day high

## Entry / Exit
Entry: If (DGS10 - DGS2) increases by >25 bps over 5 trading days AND XLU closes above 20-day SMA AND 10-year yield drops >10 bps from 5-day high Exit: After 10 trading days OR if spread compresses <15 bps from entry level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series DGS10 (10-year yield) and DGS2 (2-year yield) daily via fred_series adapter, plus XLU (utilities ETF) daily close via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Yield curve reshapes occur monthly in response to Fed messaging, inflation data, and employment reports; steepening events fire reliably.

## Required Keys
- None

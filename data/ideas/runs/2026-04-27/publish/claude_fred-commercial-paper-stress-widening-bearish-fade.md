# Fred Commercial Paper Stress Widening Bearish Fade

**Idea ID:** `fred-commercial-paper-stress-widening-bearish-fade`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Widening spreads between AA-rated and Prime commercial paper signal corporate credit stress and rising default fear, leading to flight-to-safety and sector rotation away from cyclicals. Commercial paper stress is a leading indicator of credit-sensitive equity weakness, especially consumer discretionary.

## Universe
- XLY

## Data Sources
- FRED series AA-rated vs. Prime commercial paper spread (MMNRNJ vs MMNRJD)

## Signal Logic
If CP spread widens by more than 15 bps in one week and remains elevated, short XLY.

## Entry / Exit
Entry: If CP spread widens by more than 15 bps in one week and remains elevated, short XLY. Exit: After 12 trading days or if spread tightens by 10 bps.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series AA-rated vs. Prime commercial paper spread (MMNRNJ vs MMNRJD) via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Credit market volatility is frequent; CP spreads fluctuate weekly and signal genuine stress episodes regularly.

## Required Keys
- None

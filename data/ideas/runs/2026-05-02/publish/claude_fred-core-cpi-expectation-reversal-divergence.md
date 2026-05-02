# Fred Core Cpi Expectation Reversal Divergence

**Idea ID:** `fred-core-cpi-expectation-reversal-divergence`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When 5-year inflation expectations drop >15 basis points in a single week after 4+ weeks of stable/rising expectations, it signals a demand destruction shock or disinflation surprise—bullish for long-duration assets. Collapsing inflation expectations lower discount rates and boost tech/growth valuations.

## Universe
- XLK

## Data Sources
- FRED series MMNRNJ (5-year inflation expectation) weekly aggregation

## Signal Logic
If weekly change in 5-year inflation expectations is <-15bps AND prior 4 weeks showed stable/positive change

## Entry / Exit
Entry: If weekly change in 5-year inflation expectations is <-15bps AND prior 4 weeks showed stable/positive change Exit: After 12 trading days or when expectations stabilize/rebound >10bps

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MMNRNJ (5-year inflation expectation) weekly aggregation via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Inflation expectations shift with Fed policy and CPI surprises; directional reversals occur 3-4 times per quarter during volatile periods.

## Required Keys
- None

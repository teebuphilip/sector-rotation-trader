# Mortgage Rate Shock Consumer Stress Fade

**Idea ID:** `mortgage-rate-shock-consumer-stress-fade`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When mortgage rates spike 25+ basis points in a single week, consumer discretionary spending typically sees a brief relief bounce the following week as expectations reset lower. Rate shock paradoxically stabilizes consumer sentiment after volatility capitulation, unlocking pent-up discretionary demand.

## Universe
- XLY

## Data Sources
- FRED series MORTGAGE30US (30-year mortgage rate) weekly observations through fred_series adapter

## Signal Logic
If weekly change in MORTGAGE30US exceeds +25bp and closes above prior close, enter long XLY at Friday close

## Entry / Exit
Entry: If weekly change in MORTGAGE30US exceeds +25bp and closes above prior close, enter long XLY at Friday close Exit: Exit after 7 trading days or if mortgage rate rises another 15bp

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MORTGAGE30US (30-year mortgage rate) weekly observations through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Mortgage rates oscillate with Fed messaging; 25bp weekly swings occur 2-3 times per quarter, creating recurring entry signals.

## Required Keys
- None

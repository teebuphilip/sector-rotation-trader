# Jobless Claims Momentum Reversal Flash

**Idea ID:** `jobless-claims-momentum-reversal-flash`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Week-over-week drops in jobless claims of 8%+ often signal labor market stabilization and consumer confidence inflection, driving consumer discretionary and financials outperformance. Declining jobless claims reduce economic recession risk and support consumer spending and credit confidence.

## Universe
- XLY

## Data Sources
- FRED series ICSA (initial jobless claims) weekly data

## Signal Logic
If weekly jobless claims drop 8% or more week-over-week AND claims fall below 4-week moving average

## Entry / Exit
Entry: If weekly jobless claims drop 8% or more week-over-week AND claims fall below 4-week moving average Exit: After 8 trading days or if claims spike above prior week's level

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (initial jobless claims) weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly jobless claims data is released every Thursday; momentum reversals occur frequently in normal labor market cycles.

## Required Keys
- None

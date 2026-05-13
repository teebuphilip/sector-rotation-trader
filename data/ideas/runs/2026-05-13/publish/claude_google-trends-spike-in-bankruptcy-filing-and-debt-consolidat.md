# Google Trends Spike In Bankruptcy Filing And Debt Consolidation Signals Consumer Default Risk Surge

**Idea ID:** `google-trends-spike-in-bankruptcy-filing-and-debt-consolidat`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Consumer searches for debt relief spike 4-8 weeks before credit card charge-offs rise and consumer discretionary earnings disappoint. Search surge signals financial desperation. Debt stress searches precede reduced consumer spending and increased defaults, which hurt retail and discretionary companies.

## Universe
- XLY

## Data Sources
- Google Trends weekly search volume for 'bankruptcy filing', 'debt consolidation', 'credit counseling' through google_trends adapter

## Signal Logic
When aggregate weekly Google Trends volume for debt-stress keywords increases 35% or more from prior week's baseline

## Entry / Exit
Entry: When aggregate weekly Google Trends volume for debt-stress keywords increases 35% or more from prior week's baseline Exit: After 10 trading days or when search volume falls back below 15% above 4-week moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search volume for 'bankruptcy filing', 'debt consolidation', 'credit counseling' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Economic cycles drive debt stress searches regularly. Recessions, interest rate shocks, and unemployment spikes all trigger 30-50% spikes multiple times per year.

## Required Keys
- None

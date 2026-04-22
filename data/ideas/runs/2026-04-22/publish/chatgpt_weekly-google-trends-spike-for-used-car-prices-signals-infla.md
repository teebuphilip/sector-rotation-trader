# Weekly Google Trends Spike For Used Car Prices Signals Inflationary Pressure On Consumer Goods

**Idea ID:** `weekly-google-trends-spike-for-used-car-prices-signals-infla`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased search interest in used car prices correlates with inflationary pressures impacting consumer discretionary spending. Higher used car prices reduce discretionary budgets and increase inflation concerns.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'used car prices'

## Signal Logic
Entry when weekly search interest rises by more than 20% week-over-week

## Entry / Exit
Entry: Entry when weekly search interest rises by more than 20% week-over-week Exit: Exit when interest falls below 10% increase or after 4 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'used car prices' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Used car price searches regularly spike with inflation news cycles.

## Required Keys
- None

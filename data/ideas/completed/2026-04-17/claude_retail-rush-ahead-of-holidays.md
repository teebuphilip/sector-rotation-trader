# Retail Rush Ahead Of Holidays

**Idea ID:** `retail-rush-ahead-of-holidays`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** weekly

## Thesis
Increased consumer interest in holiday shopping often precedes stronger retail sales and market activity. Consumer discretionary sector benefits from elevated holiday shopping demand.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for holiday gift ideas through google_trends adapter

## Signal Logic
If Google Trends search interest for holiday gift ideas rises 40% above the prior 4-week average

## Entry / Exit
Entry: If Google Trends search interest for holiday gift ideas rises 40% above the prior 4-week average Exit: After 6 weeks or when search interest falls below 20% above the prior 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for holiday gift ideas through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal consumer interest in holiday shopping tends to ramp up quickly in the final months of the year.

## Required Keys
- None

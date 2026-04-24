# Weekly Rise In Google Trends Searches For Gas Price Protest Signals Bearish Xle

**Idea ID:** `weekly-rise-in-google-trends-searches-for-gas-price-protest-`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing consumer interest in gas price protests often indicates rising fuel costs and consumer dissatisfaction, pressuring energy demand. Energy sector faces demand headwinds when consumer resistance to fuel prices escalates.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly search volume for 'gas price protest' rises 20% above 4-week moving average

## Entry / Exit
Entry: If weekly search volume for 'gas price protest' rises 20% above 4-week moving average Exit: Exit after 4 weeks or when search interest drops below 10% over moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Periodic fuel price increases drive protest interest and Google Trends spikes multiple times yearly.

## Required Keys
- None

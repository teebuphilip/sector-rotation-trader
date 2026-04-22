# Weekly Google Trends Spike For Gas Shortage Correlated With Xle Underperformance

**Idea ID:** `weekly-google-trends-spike-for-gas-shortage-correlated-with-`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Sudden consumer concern about gasoline availability tends to depress energy sector sentiment and pricing. Energy demand fears weigh on sector prices and outlook.

## Universe
- XLE

## Data Sources
- Google Trends weekly for 'gas shortage' and Yahoo Finance weekly XLE prices

## Signal Logic
Short XLE when 'gas shortage' searches rise >25% week-over-week and XLE underperforms SPY weekly

## Entry / Exit
Entry: Short XLE when 'gas shortage' searches rise >25% week-over-week and XLE underperforms SPY weekly Exit: Cover after 3 weeks or when search interest declines by 15%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly for 'gas shortage' and Yahoo Finance weekly XLE prices via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Gas shortage concerns are common and spike during supply disruptions.

## Required Keys
- None

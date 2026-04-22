# Daily Rise In Google Trends Searches For Inflation Hedge Stocks Indicating Rising Inflation Concern

**Idea ID:** `daily-rise-in-google-trends-searches-for-inflation-hedge-sto`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increasing searches for inflation hedges indicate rising market fear of inflation. Materials sector often benefits as an inflation hedge.

## Universe
- XLB

## Data Sources
- Google Trends daily search interest for 'inflation hedge stocks'

## Signal Logic
If daily search interest increases 30% above 5-day average

## Entry / Exit
Entry: If daily search interest increases 30% above 5-day average Exit: After 7 trading days or if interest drops below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'inflation hedge stocks' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Inflation fears and related searches spike frequently with economic data releases.

## Required Keys
- None

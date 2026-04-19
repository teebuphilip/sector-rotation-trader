# Airport Security Surge

**Idea ID:** `airport-security-surge`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Spikes in airport security checkpoint volumes can signal increased travel demand and economic activity. Industrials and transportation sectors benefit from stronger travel and logistics.

## Universe
- XLI

## Data Sources
- TSA throughput data through tsa_table adapter

## Signal Logic
If the daily TSA throughput exceeds the prior 7-day average by 20%

## Entry / Exit
Entry: If the daily TSA throughput exceeds the prior 7-day average by 20% Exit: After 5 trading days or when the daily throughput falls below 10% of the prior 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use TSA throughput data through tsa_table adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Airport security volumes often experience sharp daily and weekly swings, especially during peak travel seasons.

## Required Keys
- None

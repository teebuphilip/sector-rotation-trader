# Weekly Surge In Political Insider Filings Selling In The Energy Sector Signals Near-term Bearish Pressure

**Idea ID:** `weekly-surge-in-political-insider-filings-selling-in-the-ene`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in insider selling activity in energy stocks often precedes sector underperformance. Insiders selling indicates negative outlook or overvaluation concerns.

## Universe
- XLE

## Data Sources
- Political insider trading filings weekly aggregated

## Signal Logic
If weekly insider sell filings volume in energy sector exceeds 20% above 8-week average

## Entry / Exit
Entry: If weekly insider sell filings volume in energy sector exceeds 20% above 8-week average Exit: When filings volume falls below 10% above 8-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Political insider trading filings weekly aggregated via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider selling patterns show medium-frequency periodic spikes ahead of sector moves.

## Required Keys
- None

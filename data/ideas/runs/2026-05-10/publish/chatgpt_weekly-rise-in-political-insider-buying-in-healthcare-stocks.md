# Weekly Rise In Political Insider Buying In Healthcare Stocks Signals Upcoming Sector Strength

**Idea ID:** `weekly-rise-in-political-insider-buying-in-healthcare-stocks`
**Family:** `political_insider_filing`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An uptick in insider purchases suggests confidence in upcoming healthcare sector fundamentals or policy tailwinds. Insiders often buy before positive sector moves driven by innovation or regulation.

## Universe
- XLV

## Data Sources
- Insider filing weekly aggregated data for healthcare sector via political_insider_filing adapter

## Signal Logic
If weekly insider buying volume exceeds 20% above 10-week average

## Entry / Exit
Entry: If weekly insider buying volume exceeds 20% above 10-week average Exit: Once buying volume falls below 5% above 10-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Insider filing weekly aggregated data for healthcare sector via political_insider_filing adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Insider buying activity shows consistent weekly variation with regular buying bursts.

## Required Keys
- None

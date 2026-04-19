# Geopolitical Conflict Escalation

**Idea ID:** `geopolitical-conflict-escalation`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Increased seismic activity in geopolitically sensitive regions can signal rising tensions and military buildup. Industrials and defense sectors are vulnerable to geopolitical instability.

## Universe
- XLI

## Data Sources
- USGS earthquake activity data through earthquake_activity adapter

## Signal Logic
If the daily earthquake count in a conflict-prone region exceeds the prior 7-day average by 50%

## Entry / Exit
Entry: If the daily earthquake count in a conflict-prone region exceeds the prior 7-day average by 50% Exit: After 10 trading days or when the daily earthquake count falls below 20% above the prior 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity data through earthquake_activity adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Geopolitical flashpoints frequently experience sudden escalations in tensions that can be detected through seismic monitoring.

## Required Keys
- None

# Weekly Surge In Labor Union Strike Mentions In Rss Feeds Signals Industrial Sector Caution

**Idea ID:** `weekly-surge-in-labor-union-strike-mentions-in-rss-feeds-sig`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in news mentions about labor strikes often precedes operational disruptions in industrial companies. Rising strike chatter signals potential labor disruptions affecting industrial output.

## Universe
- XLI

## Data Sources
- RSS news feed counts for labor strike keywords

## Signal Logic
Enter short XLI if weekly RSS strike mentions rise by more than 30% vs prior 4-week average

## Entry / Exit
Entry: Enter short XLI if weekly RSS strike mentions rise by more than 30% vs prior 4-week average Exit: Exit after 3 weeks or if mentions drop below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS news feed counts for labor strike keywords via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Labor strike news cycles are frequent and often intensify before resolution or escalation.

## Required Keys
- None

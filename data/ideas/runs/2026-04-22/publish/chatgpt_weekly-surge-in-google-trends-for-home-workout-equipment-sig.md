# Weekly Surge In Google Trends For Home Workout Equipment Signals Discretionary Recovery

**Idea ID:** `weekly-surge-in-google-trends-for-home-workout-equipment-sig`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising interest in home fitness gear often precedes increased discretionary spending on related consumer products. Increased fitness interest drives discretionary retail sales growth.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'home workout equipment'

## Signal Logic
Entry when 2-week moving average of search interest rises by more than 15% week-over-week

## Entry / Exit
Entry: Entry when 2-week moving average of search interest rises by more than 15% week-over-week Exit: Exit when search interest falls below 5% week-over-week or after 4 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'home workout equipment' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Google Trends data for common consumer keywords regularly shows weekly spikes.

## Required Keys
- None

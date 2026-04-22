# Weekly Surge In Google Trends For Car Repair Searches

**Idea ID:** `weekly-surge-in-google-trends-for-car-repair-searches`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A spike in car repair searches suggests rising consumer stress related to unexpected expenses impacting discretionary spending. Consumer discretionary spending may get squeezed when repair-related stress increases.

## Universe
- XLY

## Data Sources
- Google Trends weekly data for 'car repair' keyword

## Signal Logic
Enter short XLY when weekly car repair search interest rises over 20% compared to previous 3-week average

## Entry / Exit
Entry: Enter short XLY when weekly car repair search interest rises over 20% compared to previous 3-week average Exit: Exit after 3 weeks or when interest drops below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'car repair' keyword via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Google Trends weekly keyword interest often shows multiple 20%+ spikes yearly.

## Required Keys
- None

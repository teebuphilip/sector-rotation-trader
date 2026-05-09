# Daily Google Trends Spike For Home Appliance Repair Searches Predicts Consumer Staples Bounce

**Idea ID:** `daily-google-trends-spike-for-home-appliance-repair-searches`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising search interest in home appliance repair reflects consumer stress and willingness to repair rather than replace, signaling defensive consumption. Staples sector benefits from increased spending on repairs and essential goods during consumer stress periods.

## Universe
- XLP

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter long when daily search interest jumps over 20% compared to 5-day average

## Entry / Exit
Entry: Enter long when daily search interest jumps over 20% compared to 5-day average Exit: Exit after 7 days or if search interest drops below 5-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily consumer repair needs fluctuate frequently with weather and economic conditions.

## Required Keys
- None

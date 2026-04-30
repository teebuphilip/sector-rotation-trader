# Daily Jump In Google Trends Searches For Home Water Heater Repair Signals Consumer Stress Lifting Xly

**Idea ID:** `daily-jump-in-google-trends-searches-for-home-water-heater-r`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spikes in home appliance repair interest often reflect deferred maintenance turning urgent as consumer stress eases. Increased home repair activity lifts discretionary spending in consumer sectors.

## Universe
- XLY

## Data Sources
- Google Trends daily searches

## Signal Logic
Enter long XLY if daily search interest for 'home water heater repair' rises >25% vs 7-day average

## Entry / Exit
Entry: Enter long XLY if daily search interest for 'home water heater repair' rises >25% vs 7-day average Exit: Exit after 10 trading days or if searches decline below 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily searches via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily Google search spikes on home repairs occur frequently due to weather or appliance cycles.

## Required Keys
- None

# Local Economy Weirdness Weekly Surge In Municipal Water Consumption Signals Urban Economic Activity Pickup

**Idea ID:** `local-economy-weirdness-weekly-surge-in-municipal-water-cons`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising water consumption often precedes increased local economic activity, benefiting utilities and local real estate. Utility demand grows with urban activity and population movement.

## Universe
- XLU

## Data Sources
- Public municipal water usage data aggregated weekly

## Signal Logic
Enter long XLU if weekly water consumption rises >10% above prior 4-week average

## Entry / Exit
Entry: Enter long XLU if weekly water consumption rises >10% above prior 4-week average Exit: Exit after 6 weeks or if consumption falls below 5% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Public municipal water usage data aggregated weekly via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Water consumption data shows meaningful weekly variation tied to urban economic cycles.

## Required Keys
- None

# Weekly Surge In Google Trends For Diy Car Maintenance Signals Rising Auto Sector Interest

**Idea ID:** `weekly-surge-in-google-trends-for-diy-car-maintenance-signal`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in searches for DIY car maintenance often precedes higher demand for auto parts and services, reflecting consumer stress on vehicle upkeep costs. Auto parts and industrial sectors benefit from increased vehicle maintenance activity.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter long XLI when 3-week moving average of 'DIY car maintenance' Google Trends rises more than 15% week-over-week

## Entry / Exit
Entry: Enter long XLI when 3-week moving average of 'DIY car maintenance' Google Trends rises more than 15% week-over-week Exit: Exit after 4 weeks or if the 2-week moving average declines below 5% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly Google Trends data often shows repeated interest spikes in consumer maintenance topics.

## Required Keys
- None

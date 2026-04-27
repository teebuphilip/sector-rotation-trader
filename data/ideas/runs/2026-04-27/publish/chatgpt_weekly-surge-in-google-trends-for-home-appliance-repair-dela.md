# Weekly Surge In Google Trends For Home Appliance Repair Delay Signals Bearish Xlp

**Idea ID:** `weekly-surge-in-google-trends-for-home-appliance-repair-dela`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing consumer searches for appliance repair delays suggest supply chain issues and rising consumer frustration impacting staples demand. Supply chain delays in staples reduce sales and increase consumer stress.

## Universe
- XLP

## Data Sources
- Google Trends weekly data for 'home appliance repair delay'

## Signal Logic
Enter short if weekly Google Trends interest rises 20%+ week-over-week

## Entry / Exit
Entry: Enter short if weekly Google Trends interest rises 20%+ week-over-week Exit: Exit after 3 weeks or when trends revert below 4-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'home appliance repair delay' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Supply chain and repair delays often spike seasonally or with shocks.

## Required Keys
- None

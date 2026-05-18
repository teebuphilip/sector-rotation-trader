# Daily Spike In Google Trends For Heating Oil Delivery Delay Signals Energy Sector Pressure

**Idea ID:** `daily-spike-in-google-trends-for-heating-oil-delivery-delay-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased searches for heating oil delivery issues indicate rising local energy demand or supply constraints. Energy sector typically benefits from supply tightness and higher local demand.

## Universe
- XLE

## Data Sources
- Google Trends daily search interest for 'heating oil delivery delay'

## Signal Logic
If daily search interest rises by more than 30% compared to prior 7-day average

## Entry / Exit
Entry: If daily search interest rises by more than 30% compared to prior 7-day average Exit: Exit after 10 trading days or when the interest falls below 15% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'heating oil delivery delay' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Heating oil delivery issues spike seasonally in colder months.

## Required Keys
- None

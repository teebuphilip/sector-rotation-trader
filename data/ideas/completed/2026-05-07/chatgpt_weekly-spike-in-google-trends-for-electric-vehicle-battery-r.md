# Weekly Spike In Google Trends For Electric Vehicle Battery Replacement Signals Consumer Stress Lifting Industrial Sector

**Idea ID:** `weekly-spike-in-google-trends-for-electric-vehicle-battery-r`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Higher search interest reflects growing EV maintenance demand and consumer cost concerns. EV battery replacement demand supports industrial manufacturing and repair services.

## Universe
- XLI

## Data Sources
- Google Trends weekly searches for 'electric vehicle battery replacement'

## Signal Logic
Enter long XLI if weekly searches exceed 20% above 10-week average

## Entry / Exit
Entry: Enter long XLI if weekly searches exceed 20% above 10-week average Exit: Exit after 5 weeks or if interest falls below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'electric vehicle battery replacement' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: EV adoption and maintenance concerns grow steadily, generating frequent search interest spikes.

## Required Keys
- None

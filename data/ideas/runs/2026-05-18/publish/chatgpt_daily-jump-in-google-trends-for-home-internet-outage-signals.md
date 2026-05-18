# Daily Jump In Google Trends For Home Internet Outage Signals Consumer Discretionary Tech Stress

**Idea ID:** `daily-jump-in-google-trends-for-home-internet-outage-signals`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
More searches for internet outages indicate consumer tech service disruptions, impacting discretionary tech usage. Discretionary tech goods and services rely on stable internet connectivity.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'home internet outage'

## Signal Logic
If daily search interest spikes by over 25% vs prior 7-day average

## Entry / Exit
Entry: If daily search interest spikes by over 25% vs prior 7-day average Exit: Exit after 5 trading days or when search interest falls below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'home internet outage' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Internet outages are fairly common and prompt immediate consumer attention.

## Required Keys
- None

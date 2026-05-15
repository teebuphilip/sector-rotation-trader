# Daily Surge In Google Trends For Urgent Dental Care Searches Lifting Healthcare Sector

**Idea ID:** `daily-surge-in-google-trends-for-urgent-dental-care-searches`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spikes in urgent dental care searches indicate stress-driven healthcare demand increasing short-term volume. Healthcare utilization tends to rise with consumer stress and urgent health needs.

## Universe
- XLV

## Data Sources
- Google Trends daily search interest for urgent dental care

## Signal Logic
If daily search volume exceeds 20% above 7-day moving average

## Entry / Exit
Entry: If daily search volume exceeds 20% above 7-day moving average Exit: When volume normalizes below 5% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for urgent dental care via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Dental emergencies occur regularly, driving daily search volume fluctuations.

## Required Keys
- None

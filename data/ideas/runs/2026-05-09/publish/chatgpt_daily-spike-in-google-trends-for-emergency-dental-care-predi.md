# Daily Spike In Google Trends For Emergency Dental Care Predicts Healthcare Sector Defensive Demand

**Idea ID:** `daily-spike-in-google-trends-for-emergency-dental-care-predi`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increases in emergency dental care searches indicate urgent health needs, driving short-term demand in healthcare services. Healthcare sector benefits from increased urgent care and elective procedure demand.

## Universe
- XLV

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter long when daily emergency dental care searches spike over 30% compared to 7-day average

## Entry / Exit
Entry: Enter long when daily emergency dental care searches spike over 30% compared to 7-day average Exit: Exit after 10 days or if interest drops below 7-day average

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
- Why It Should Fire Soon: Dental emergencies are common and spike frequently due to accidents or acute illness.

## Required Keys
- None

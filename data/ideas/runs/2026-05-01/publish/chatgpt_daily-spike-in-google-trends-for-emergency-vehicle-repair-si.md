# Daily Spike In Google Trends For Emergency Vehicle Repair Signals Consumer Stress Lifting Industrial Sector

**Idea ID:** `daily-spike-in-google-trends-for-emergency-vehicle-repair-si`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising emergency vehicle repair searches indicate increased urgent spending and maintenance demand in industrial transportation. Higher industrial repair demand supports sector revenue growth.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter long XLI when daily search volume for 'emergency vehicle repair' rises 45% above 7-day average

## Entry / Exit
Entry: Enter long XLI when daily search volume for 'emergency vehicle repair' rises 45% above 7-day average Exit: Exit after 5 trading days or volume falls below 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Emergency vehicle repair needs frequently surge day-to-day, creating daily signals.

## Required Keys
- None

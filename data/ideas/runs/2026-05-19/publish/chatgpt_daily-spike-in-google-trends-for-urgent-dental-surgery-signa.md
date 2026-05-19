# Daily Spike In Google Trends For Urgent Dental Surgery Signals Healthcare Demand Surge

**Idea ID:** `daily-spike-in-google-trends-for-urgent-dental-surgery-signa`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Surges in urgent dental surgery searches often foreshadow increased healthcare service utilization. Healthcare services and providers benefit from heightened urgent care demand.

## Universe
- XLV

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter long XLV when daily searches for 'urgent dental surgery' exceed 2 std deviations above 30-day mean

## Entry / Exit
Entry: Enter long XLV when daily searches for 'urgent dental surgery' exceed 2 std deviations above 30-day mean Exit: Exit after 7 days or if volume declines below 1 std deviation above mean

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
- Why It Should Fire Soon: Healthcare emergencies cause recurring daily search volume spikes.

## Required Keys
- None

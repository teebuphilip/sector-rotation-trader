# Daily Spike In Google Trends For Home Air Purifier Repair Signals Consumer Stress Rebound In Discretionary Sector

**Idea ID:** `daily-spike-in-google-trends-for-home-air-purifier-repair-si`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased repair searches for air purifiers indicate consumers prioritizing indoor air quality and discretionary spending on health-related home goods. Rising consumer spending on home comfort products lifts consumer discretionary stocks.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter long XLY when daily search volume for 'air purifier repair' rises 40% above 7-day average

## Entry / Exit
Entry: Enter long XLY when daily search volume for 'air purifier repair' rises 40% above 7-day average Exit: Exit after 7 trading days or when volume returns below 7-day average

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
- Why It Should Fire Soon: Daily consumer health concerns cause frequent search volume spikes.

## Required Keys
- None

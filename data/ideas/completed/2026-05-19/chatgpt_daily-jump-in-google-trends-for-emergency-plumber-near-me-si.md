# Daily Jump In Google Trends For Emergency Plumber Near Me Signals Consumer Home Repair Stress

**Idea ID:** `daily-jump-in-google-trends-for-emergency-plumber-near-me-si`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increases in emergency plumbing searches indicate acute home repair demand which often benefits consumer discretionary sectors. Consumer discretionary companies supplying home services and repairs gain from heightened demand.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter long XLY when daily search volume for 'emergency plumber near me' exceeds 2 std deviations above 30-day mean

## Entry / Exit
Entry: Enter long XLY when daily search volume for 'emergency plumber near me' exceeds 2 std deviations above 30-day mean Exit: Exit after 5 trading days or once volume falls below 1 std deviation above mean

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
- Why It Should Fire Soon: Daily home emergency repair searches tend to spike frequently due to accidents and weather.

## Required Keys
- None

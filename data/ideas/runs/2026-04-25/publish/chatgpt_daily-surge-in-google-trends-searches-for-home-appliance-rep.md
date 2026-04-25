# Daily Surge In Google Trends Searches For Home Appliance Repair Signals Bullish Xly

**Idea ID:** `daily-surge-in-google-trends-searches-for-home-appliance-rep`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spike in appliance repair searches shows consumers delaying replacement purchases, boosting discretionary repair services. Consumer discretionary firms in repair services and parts see volume increases.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest for 'home appliance repair'

## Signal Logic
Enter long XLY if daily search volume is 30% above 7-day moving average

## Entry / Exit
Entry: Enter long XLY if daily search volume is 30% above 7-day moving average Exit: Exit after 5 trading days or when search volume drops below 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'home appliance repair' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Consumer repair needs fluctuate frequently with appliance failures and weather events.

## Required Keys
- None

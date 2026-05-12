# Weekly Surge In Google Trends For Sudden Appliance Breakdowns Signals Discretionary Sector Rebound

**Idea ID:** `weekly-surge-in-google-trends-for-sudden-appliance-breakdown`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sharp weekly increase in searches related to emergency appliance repairs often precedes increased consumer spending on home services and replacements. Discretionary retailers and home improvement benefit as consumers rush to replace or fix broken appliances.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for appliance repair keywords

## Signal Logic
Enter long XLY when weekly Google Trends for appliance breakdown-related terms rises over 20% from the prior week

## Entry / Exit
Entry: Enter long XLY when weekly Google Trends for appliance breakdown-related terms rises over 20% from the prior week Exit: Exit after 4 weeks or when search volume returns to baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for appliance repair keywords via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly Google Trends data for appliance repair spikes frequently during seasonal appliance wear periods.

## Required Keys
- None

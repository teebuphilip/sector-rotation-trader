# Weekly Surge In Google Trends Searches For Diy Home Repair Signals Consumer Stress Lifting Xly

**Idea ID:** `weekly-surge-in-google-trends-searches-for-diy-home-repair-s`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An uptick in DIY home repair searches often precedes increased discretionary spending on home improvement and related retail sectors. Consumer discretionary spending tends to rise as home repair interest grows.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter long XLY when 3-week moving average of 'DIY home repair' searches rises 15%+ versus prior 3 weeks

## Entry / Exit
Entry: Enter long XLY when 3-week moving average of 'DIY home repair' searches rises 15%+ versus prior 3 weeks Exit: Exit after 4 weeks or when the search interest drops below its 3-week moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly Google Trends data often shows multiple spikes per year in home repair interest.

## Required Keys
- None

# Weekly Increase In Google Trends For Truck Driver Shortage Signals Freight Sector Labor Pressure

**Idea ID:** `weekly-increase-in-google-trends-for-truck-driver-shortage-s`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising searches for truck driver shortages often precede freight capacity constraints and logistic cost rises. Industrial sector performance is impacted by freight labor bottlenecks.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLI when weekly Google Trends for 'truck driver shortage' rises 20%+ week-over-week

## Entry / Exit
Entry: Enter short XLI when weekly Google Trends for 'truck driver shortage' rises 20%+ week-over-week Exit: Exit after 4 weeks or when increases fall below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Truck driver shortage headlines and searches spike regularly with labor market changes.

## Required Keys
- None

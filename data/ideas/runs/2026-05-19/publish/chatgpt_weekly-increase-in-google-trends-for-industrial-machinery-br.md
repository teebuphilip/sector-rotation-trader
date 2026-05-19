# Weekly Increase In Google Trends For Industrial Machinery Breakdown Signals Rising Repair Demand

**Idea ID:** `weekly-increase-in-google-trends-for-industrial-machinery-br`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Growing search interest in machinery breakdowns implies increased industrial maintenance and capital expenditure. Industrial sector firms benefit from repair and replacement demand.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter long XLI when weekly 'industrial machinery breakdown' searches rise over 20% week-over-week

## Entry / Exit
Entry: Enter long XLI when weekly 'industrial machinery breakdown' searches rise over 20% week-over-week Exit: Exit after 4 weeks or if weekly growth drops below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Industrial equipment failures are common and cause measurable weekly search interest spikes.

## Required Keys
- None

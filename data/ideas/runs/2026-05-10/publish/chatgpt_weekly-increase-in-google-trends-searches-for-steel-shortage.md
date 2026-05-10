# Weekly Increase In Google Trends Searches For Steel Shortage Signals Industrial Sector Supply Pressure

**Idea ID:** `weekly-increase-in-google-trends-searches-for-steel-shortage`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Growing concern about steel shortages reflects rising input cost pressures on industrial manufacturing. Steel is a core industrial input; shortages increase costs and reduce margins.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest for 'steel shortage' via google_trends adapter

## Signal Logic
If weekly search interest rises above 15% week-over-week

## Entry / Exit
Entry: If weekly search interest rises above 15% week-over-week Exit: Once weekly change drops below 5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'steel shortage' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Input cost pressures show regular weekly variation based on supply chain news.

## Required Keys
- None

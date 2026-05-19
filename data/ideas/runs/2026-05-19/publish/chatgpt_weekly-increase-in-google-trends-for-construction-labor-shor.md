# Weekly Increase In Google Trends For Construction Labor Shortage Signals Labor Tightness Risk

**Idea ID:** `weekly-increase-in-google-trends-for-construction-labor-shor`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising search interest in construction labor shortage indicates tightening labor market and potential project delays. Labor shortages increase costs and delay industrial and construction sector output.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLI when weekly searches for 'construction labor shortage' rise more than 15% week-over-week

## Entry / Exit
Entry: Enter short XLI when weekly searches for 'construction labor shortage' rise more than 15% week-over-week Exit: Exit after 4 weeks or when weekly growth falls below 5%

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
- Why It Should Fire Soon: Labor market concerns generate recurring weekly search interest spikes.

## Required Keys
- None

# Weekly Increase In Google Trends For Freight Container Backlog Signals Shipping Supply Chain Stress

**Idea ID:** `weekly-increase-in-google-trends-for-freight-container-backl`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising search volume for freight container backlog reflects supply chain bottlenecks impacting industrial sectors. Shipping delays increase costs and reduce industrial output efficiency.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short XLI when weekly 'freight container backlog' searches rise more than 25% week-over-week

## Entry / Exit
Entry: Enter short XLI when weekly 'freight container backlog' searches rise more than 25% week-over-week Exit: Exit after 4 weeks or if weekly increase drops below 10%

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
- Why It Should Fire Soon: Container backlog issues appear regularly in weekly search interest data.

## Required Keys
- None

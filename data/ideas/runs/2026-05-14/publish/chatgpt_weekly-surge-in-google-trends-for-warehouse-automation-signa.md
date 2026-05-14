# Weekly Surge In Google Trends For Warehouse Automation Signals Industrial Sector Demand

**Idea ID:** `weekly-surge-in-google-trends-for-warehouse-automation-signa`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increasing interest in warehouse automation indicates growing investment and activity in industrial logistics and manufacturing automation. Increased searches for warehouse automation typically precede capital expenditure and growth in industrial sector companies.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
If weekly Google Trends interest for 'warehouse automation' rises by more than 15% from previous week

## Entry / Exit
Entry: If weekly Google Trends interest for 'warehouse automation' rises by more than 15% from previous week Exit: After 4 weeks or if interest drops below prior 4-week average

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
- Why It Should Fire Soon: Google Trends data for this term frequently shows weekly fluctuations above 15% due to ongoing supply chain investment news.

## Required Keys
- None

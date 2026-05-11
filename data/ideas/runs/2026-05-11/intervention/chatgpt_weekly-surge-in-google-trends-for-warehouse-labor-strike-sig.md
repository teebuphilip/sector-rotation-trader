# Weekly Surge In Google Trends For Warehouse Labor Strike Signals Freight Disruption

**Idea ID:** `weekly-surge-in-google-trends-for-warehouse-labor-strike-sig`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising search interest in labor strikes at warehouses often precedes slower freight movement and supply chain delays. Industrial sector ETFs are sensitive to freight and logistics disruptions.

## Universe
- XLI

## Data Sources
- Google Trends weekly search interest

## Signal Logic
Enter short on XLI when weekly Google Trends for 'warehouse labor strike' rises 30%+ from prior week

## Entry / Exit
Entry: Enter short on XLI when weekly Google Trends for 'warehouse labor strike' rises 30%+ from prior week Exit: Exit after 3 weeks or when trend falls below 10% weekly increase

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
- Trigger Sensitivity: high
- Why It Should Fire Soon: Labor unrest and strike-related searches spike multiple times yearly, especially seasonally.

## Required Keys
- None

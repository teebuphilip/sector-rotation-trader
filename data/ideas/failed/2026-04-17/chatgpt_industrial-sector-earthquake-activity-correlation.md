# Industrial Sector Earthquake Activity Correlation

**Idea ID:** `industrial-sector-earthquake-activity-correlation`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased moderate earthquake activity near industrial centers correlates with short-term supply chain disruptions, causing volatility. Earthquake shocks can disrupt manufacturing and logistics, pressuring industrial stocks.

## Universe
- XLI

## Data Sources
- USGS earthquake_activity weekly counts near US industrial hubs mapped to XLI

## Signal Logic
If weekly earthquake count near top 5 US industrial metro areas increases 50% week-over-week

## Entry / Exit
Entry: If weekly earthquake count near top 5 US industrial metro areas increases 50% week-over-week Exit: After 3 weeks or price recovers 4%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake_activity weekly counts near US industrial hubs mapped to XLI via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Earthquake activity fluctuates enough to trigger spikes multiple times yearly.

## Required Keys
- None

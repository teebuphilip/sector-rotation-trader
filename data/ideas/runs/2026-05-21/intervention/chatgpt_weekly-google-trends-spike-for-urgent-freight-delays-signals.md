# Weekly Google Trends Spike For Urgent Freight Delays Signals Supply Chain Pressure

**Idea ID:** `weekly-google-trends-spike-for-urgent-freight-delays-signals`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spiking freight delay searches indicate bottlenecks and supply chain stress. Freight delays reduce industrial production efficiency and increase costs.

## Universe
- XLI

## Data Sources
- Google Trends weekly urgent freight delay searches

## Signal Logic
Enter short when weekly search interest rises 25% above 6-week average

## Entry / Exit
Entry: Enter short when weekly search interest rises 25% above 6-week average Exit: Exit when interest falls below 10% above 6-week average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly urgent freight delay searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Freight delays are common due to weather, labor strikes, or port congestion.

## Required Keys
- None

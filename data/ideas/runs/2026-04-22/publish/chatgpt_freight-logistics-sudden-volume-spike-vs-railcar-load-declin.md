# Freight Logistics Sudden Volume Spike Vs Railcar Load Decline

**Idea ID:** `freight-logistics-sudden-volume-spike-vs-railcar-load-declin`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden rise in port container volume combined with falling railcar loads implies modal shift and supply chain stress. Industrial sector exposed to freight disruption and logistic cost inflation.

## Universe
- XLI

## Data Sources
- Port container volume weekly data and freight railcar load weekly data from public APIs

## Signal Logic
Enter short XLI when port container volume rises >10% WoW and railcar load drops >5% WoW simultaneously

## Entry / Exit
Entry: Enter short XLI when port container volume rises >10% WoW and railcar load drops >5% WoW simultaneously Exit: Exit after 3 weeks or when either metric normalizes within 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Port container volume weekly data and freight railcar load weekly data from public APIs via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Weekly freight data regularly shows these cross-modal divergences during supply chain disruptions.

## Required Keys
- None

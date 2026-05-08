# Weekly Rise In Freight Logistics Port Container Volume Delays Signals Supply Chain Disruption

**Idea ID:** `weekly-rise-in-freight-logistics-port-container-volume-delay`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in reported port container volume delays implies congestion that slows goods movement. Commodity and materials supply chains get disrupted, pressuring industrial and materials sectors.

## Universe
- XLB

## Data Sources
- port_container_volume weekly data

## Signal Logic
If weekly port container volume delay index rises 10% above 4-week moving average

## Entry / Exit
Entry: If weekly port container volume delay index rises 10% above 4-week moving average Exit: When delay index falls below 5% above 4-week moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use port_container_volume weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Port congestion regularly fluctuates with shipping cycles, seasonal demand, and labor conditions.

## Required Keys
- None

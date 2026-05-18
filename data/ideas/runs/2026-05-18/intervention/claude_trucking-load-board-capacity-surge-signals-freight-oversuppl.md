# Trucking Load Board Capacity Surge Signals Freight Oversupply

**Idea ID:** `trucking-load-board-capacity-surge-signals-freight-oversuppl`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When available loads vastly outnumber available trucks on public load boards, trucking capacity crashes and freight rates collapse, signaling logistics sector weakness. Trucking oversupply indicates weak shipping demand, depresses carrier margins, and signals industrial slowdown.

## Universe
- XLI

## Data Sources
- Truckstop.com and Uber Freight public load board fill-rate indices through html_table or api adapter

## Signal Logic
If daily load board available-loads-to-trucks ratio rises above 2.0 for 3 consecutive days, short XLI.

## Entry / Exit
Entry: If daily load board available-loads-to-trucks ratio rises above 2.0 for 3 consecutive days, short XLI. Exit: Exit after 7 trading days or when ratio falls below 1.5.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Truckstop.com and Uber Freight public load board fill-rate indices through html_table or api adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Load board ratios spike and crash weekly based on seasonal and cyclical freight demand, firing multiple times per month.

## Required Keys
- None

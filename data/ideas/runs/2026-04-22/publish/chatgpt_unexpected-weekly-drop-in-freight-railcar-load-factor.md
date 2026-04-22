# Unexpected Weekly Drop In Freight Railcar Load Factor

**Idea ID:** `unexpected-weekly-drop-in-freight-railcar-load-factor`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A steep drop in railcar load factor signals weakening industrial demand and potential economic slowdown. Lower freight rail usage correlates to reduced industrial output and economic activity.

## Universe
- XLI

## Data Sources
- Public freight railcar load weekly data

## Signal Logic
Enter short XLI when weekly railcar load factor drops more than 7% WoW

## Entry / Exit
Entry: Enter short XLI when weekly railcar load factor drops more than 7% WoW Exit: Exit after 3 weeks or when load factor recovers by 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Public freight railcar load weekly data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Railcar load fluctuations of this magnitude occur several times annually tied to economic cycles.

## Required Keys
- None

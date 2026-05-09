# Ev Charger Buildout Acceleration Bullish Play

**Idea ID:** `ev-charger-buildout-acceleration-bullish-play`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Public EV charger network expansion correlates with infrastructure investment cycles and consumer EV adoption confidence. Rapid week-over-week growth in charger availability signals macro tailwind for energy transition. Charger installation is industrial capex; growth signals infrastructure spending momentum benefiting industrial equipment and construction.

## Universe
- XLI

## Data Sources
- OpenChargeMap API daily charger counts by region through openchargemap adapter

## Signal Logic
If weekly charger count increase exceeds prior 8-week rolling average by 15% or more

## Entry / Exit
Entry: If weekly charger count increase exceeds prior 8-week rolling average by 15% or more Exit: After 10 trading days or if weekly growth falls below 5% for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API daily charger counts by region through openchargemap adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Charger deployment fluctuates seasonally and by funding cycles; threshold of 15% growth above 8-week MA fires 2–3 times per quarter.

## Required Keys
- None

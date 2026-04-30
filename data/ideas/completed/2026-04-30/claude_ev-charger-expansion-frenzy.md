# Ev Charger Expansion Frenzy

**Idea ID:** `ev-charger-expansion-frenzy`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Weekly net growth in public EV chargers exceeds 2% of prior week's total, signaling acceleration in infrastructure deployment and capital spending. Charger buildout drives industrial equipment orders, electrical infrastructure upgrades, and construction activity.

## Universe
- XLI

## Data Sources
- OpenChargeMap API daily charger count by region through openchargemap adapter

## Signal Logic
If week-over-week net charger additions exceed 2% and 7-day price momentum on XLI is positive

## Entry / Exit
Entry: If week-over-week net charger additions exceed 2% and 7-day price momentum on XLI is positive Exit: After 10 trading days or if weekly charger growth drops below 0.5%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API daily charger count by region through openchargemap adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Charger deployment is steady and accelerates seasonally in spring; 2% weekly growth threshold fires multiple times per quarter.

## Required Keys
- None

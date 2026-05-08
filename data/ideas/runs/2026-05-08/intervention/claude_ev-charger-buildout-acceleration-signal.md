# Ev Charger Buildout Acceleration Signal

**Idea ID:** `ev-charger-buildout-acceleration-signal`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When weekly net new charger additions exceed prior 8-week rolling average by 20%+, it signals infrastructure investment acceleration. Industrial and energy stocks respond bullishly within 3-7 days as construction/manufacturing demand rises. Charger buildout expansion signals sustained capex cycle in industrial manufacturing, electrical equipment, and construction services.

## Universe
- XLI

## Data Sources
- OpenChargeMap total charger count (daily via openchargemap adapter) paired with price_only XLI daily momentum

## Signal Logic
Weekly net charger adds (vs 8-week rolling avg) spike 20%+; XLI volume above 90th percentile; enter long XLI at next day's open

## Entry / Exit
Entry: Weekly net charger adds (vs 8-week rolling avg) spike 20%+; XLI volume above 90th percentile; enter long XLI at next day's open Exit: After 7 trading days OR if weekly charger growth rate drops below 5%, whichever first

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap total charger count (daily via openchargemap adapter) paired with price_only XLI daily momentum via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: OpenChargeMap updates daily; charger deployment accelerations occur monthly; industrial sector responds predictably to capex cycle signals.

## Required Keys
- None

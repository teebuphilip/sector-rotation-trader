# Energy-intensive Manufacturing Pivot Away From Peak-hours Eia Demand Spike Fade

**Idea ID:** `energy-intensive-manufacturing-pivot-away-from-peak-hours-ei`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When peak-hour electricity demand spikes >3% above rolling 20-day average on same day, it signals industrial production surge. Industrials rally, utilities face margin pressure. Fade occurs as demand normalization follows within 2–3 weeks. Peak electricity demand spikes are a real-time read on factory utilization; rallies in industrial output drive equipment/machinery demand.

## Universe
- XLI

## Data Sources
- EIA daily electricity demand (peak hour demand via eia_electricity adapter) plus XLI (industrials) and XLU (utilities) daily closes via price_only adapter

## Signal Logic
If EIA peak-hour demand > 20-day MA × 1.03 AND XLI closes > 5-day SMA AND XLI volume > 10-day MA

## Entry / Exit
Entry: If EIA peak-hour demand > 20-day MA × 1.03 AND XLI closes > 5-day SMA AND XLI volume > 10-day MA Exit: After 10 trading days OR if EIA demand falls below 20-day MA for 3 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA daily electricity demand (peak hour demand via eia_electricity adapter) plus XLI (industrials) and XLU (utilities) daily closes via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Industrial production cycles and seasonal demand spikes trigger electricity surges every 2–3 weeks; signal fires reliably.

## Required Keys
- None

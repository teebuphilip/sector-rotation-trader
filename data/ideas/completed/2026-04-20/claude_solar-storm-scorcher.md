# Solar Storm Scorcher

**Idea ID:** `solar-storm-scorcher`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Spikes in solar activity and geomagnetic storms can disrupt satellite operations, power grids, and other critical infrastructure, signaling potential volatility in energy and technology sectors. Solar storms can impact energy infrastructure and space-based technologies, which are crucial for the energy and technology sectors.

## Universe
- XLE

## Data Sources
- NOAA daily solar activity index through weather_series adapter

## Signal Logic
If the daily solar activity index increases by more than 50% compared to the prior 7-day average

## Entry / Exit
Entry: If the daily solar activity index increases by more than 50% compared to the prior 7-day average Exit: After 3 trading days or once the index retreats by 30%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use NOAA daily solar activity index through weather_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Solar activity can exhibit periodic spikes and storms, which are more likely to occur within a 30-day timeframe, especially during active phases of the solar cycle.

## Required Keys
- None

# Natural Gas Demand Spike From Unseasonable Cold Snap Detection

**Idea ID:** `natural-gas-demand-spike-from-unseasonable-cold-snap-detecti`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Daily minimum temperatures drop >15% below 30-day rolling average in winter months, signaling heating demand surge and natural gas consumption pressure. Utilities and energy infrastructure see immediate margin expansion from peak demand pricing and capacity utilization.

## Universe
- XLU

## Data Sources
- Open-Meteo daily temperature anomaly for US population centers through weather_series adapter

## Signal Logic
When US population-weighted temperature anomaly drops below -2 standard deviations from seasonal norm for 2+ consecutive days

## Entry / Exit
Entry: When US population-weighted temperature anomaly drops below -2 standard deviations from seasonal norm for 2+ consecutive days Exit: When temperature anomaly recovers above -1 standard deviation or after 7 trading days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Open-Meteo daily temperature anomaly for US population centers through weather_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Winter weather volatility is seasonal and repeats reliably; unseasonable cold snaps occur multiple times per winter season.

## Required Keys
- None

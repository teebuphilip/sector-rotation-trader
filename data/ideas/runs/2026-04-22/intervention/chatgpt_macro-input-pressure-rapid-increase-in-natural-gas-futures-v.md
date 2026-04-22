# Macro Input Pressure Rapid Increase In Natural Gas Futures Volatility Signals Energy Sector Rotation

**Idea ID:** `macro-input-pressure-rapid-increase-in-natural-gas-futures-v`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spikes in natural gas volatility often precede energy sector price swings and rotation opportunities. Energy sector volatility can trigger price rallies as markets price supply shocks.

## Universe
- XLE

## Data Sources
- Yahoo Finance daily price and volatility for natural gas futures

## Signal Logic
Enter long XLE if daily volatility rises more than 25% day-over-day and closes above 5-day volatility average

## Entry / Exit
Entry: Enter long XLE if daily volatility rises more than 25% day-over-day and closes above 5-day volatility average Exit: Exit after 7 trading days or if volatility falls below 5-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily price and volatility for natural gas futures via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Energy volatility spikes multiple times per year driven by weather and geopolitical events.

## Required Keys
- None

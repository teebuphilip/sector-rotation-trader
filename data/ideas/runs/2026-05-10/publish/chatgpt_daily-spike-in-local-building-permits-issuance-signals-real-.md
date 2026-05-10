# Daily Spike In Local Building Permits Issuance Signals Real Estate Sector Momentum

**Idea ID:** `daily-spike-in-local-building-permits-issuance-signals-real-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden rise in building permits signals upcoming construction activity and real estate market strength. Higher building permits often lead to increased real estate development and sector growth.

## Universe
- XLRE

## Data Sources
- Local government building permits daily data via html_table adapter

## Signal Logic
If daily permits issued exceed 10% above 30-day average

## Entry / Exit
Entry: If daily permits issued exceed 10% above 30-day average Exit: When daily permits fall below 5% above 30-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Local government building permits daily data via html_table adapter via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily building permit data shows regular bursts due to regulatory and seasonal effects.

## Required Keys
- None

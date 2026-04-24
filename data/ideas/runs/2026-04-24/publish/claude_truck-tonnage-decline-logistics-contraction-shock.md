# Truck Tonnage Decline Logistics Contraction Shock

**Idea ID:** `truck-tonnage-decline-logistics-contraction-shock`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Weekly truck tonnage declines >5% from prior week, indicating sharp pullback in freight demand and supply chain contraction. Trucks move 70% of US freight; sharp tonnage drops precede industrial production weakness.

## Universe
- XLI

## Data Sources
- American Trucking Associations weekly tonnage index via html_table scrape adapter

## Signal Logic
If ATA tonnage index drops >5% week-over-week, short XLI

## Entry / Exit
Entry: If ATA tonnage index drops >5% week-over-week, short XLI Exit: Exit after 7 trading days or if tonnage stabilizes (change <±2% for 2 weeks)

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use American Trucking Associations weekly tonnage index via html_table scrape adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly data with high volatility; tonnage declines trigger 2–3 times per quarter in response to demand shocks.

## Required Keys
- None

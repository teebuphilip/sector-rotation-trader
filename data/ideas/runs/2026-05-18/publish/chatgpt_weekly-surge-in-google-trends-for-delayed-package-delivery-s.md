# Weekly Surge In Google Trends For Delayed Package Delivery Signals Consumer Discretionary Shipping Pressure

**Idea ID:** `weekly-surge-in-google-trends-for-delayed-package-delivery-s`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
An increase in delayed package delivery searches signals shipping bottlenecks affecting retail demand. Retail and discretionary sectors are sensitive to delivery reliability issues.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for 'delayed package delivery'

## Signal Logic
If weekly searches rise by more than 25% vs prior 6-week average

## Entry / Exit
Entry: If weekly searches rise by more than 25% vs prior 6-week average Exit: Exit after 4 weeks or when searches decline below 15% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'delayed package delivery' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 15
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Delivery delays spike seasonally during holidays and peak shopping periods.

## Required Keys
- None

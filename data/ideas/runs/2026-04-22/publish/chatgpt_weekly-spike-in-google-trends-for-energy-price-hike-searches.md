# Weekly Spike In Google Trends For Energy Price Hike Searches

**Idea ID:** `weekly-spike-in-google-trends-for-energy-price-hike-searches`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising consumer search interest in energy price hikes signals growing concern about inflationary pressures. Energy sector may face volatility and sell-offs amid fear of demand destruction or regulation.

## Universe
- XLE

## Data Sources
- Google Trends weekly data for 'energy price hike' keyword

## Signal Logic
Enter short XLE when weekly search interest rises >20% WoW

## Entry / Exit
Entry: Enter short XLE when weekly search interest rises >20% WoW Exit: Exit after 3 weeks or when interest falls below 5% WoW

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly data for 'energy price hike' keyword via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Energy price concern search spikes commonly happen around volatility in crude prices.

## Required Keys
- None

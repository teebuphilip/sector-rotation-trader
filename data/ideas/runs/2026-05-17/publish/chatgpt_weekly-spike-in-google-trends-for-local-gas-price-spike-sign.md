# Weekly Spike In Google Trends For Local Gas Price Spike Signals Energy Sector Volatility

**Idea ID:** `weekly-spike-in-google-trends-for-local-gas-price-spike-sign`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing gas price concern interest signals rising input cost pressures for consumers and industries. Energy sector often rallies on rising fuel price concerns and input cost inflation.

## Universe
- XLE

## Data Sources
- Google Trends weekly search interest for 'gas price spike'

## Signal Logic
Enter long XLE if weekly Google Trends for 'gas price spike' increases 25%+ WoW

## Entry / Exit
Entry: Enter long XLE if weekly Google Trends for 'gas price spike' increases 25%+ WoW Exit: Exit after 6 weeks or if trend drops below 10% WoW increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'gas price spike' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Fuel price concerns show persistent weekly search interest fluctuations.

## Required Keys
- None

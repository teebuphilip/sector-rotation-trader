# Daily Jump In Google Trends For Gas Price Surge Signals Bearish Xle

**Idea ID:** `daily-jump-in-google-trends-for-gas-price-surge-signals-bear`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rapid increases in gas price search interest precede consumer cost pressure and energy sector volatility. Energy price shock fears reduce consumer discretionary spending and increase volatility in energy stocks.

## Universe
- XLE

## Data Sources
- Google Trends daily searches

## Signal Logic
Enter short XLE if daily search interest for 'gas price surge' rises 30%+ above 10-day average

## Entry / Exit
Entry: Enter short XLE if daily search interest for 'gas price surge' rises 30%+ above 10-day average Exit: Exit after 8 trading days or if search interest normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily searches via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Gas price search interest spikes frequently due to fuel price volatility.

## Required Keys
- None

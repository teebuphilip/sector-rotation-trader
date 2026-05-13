# Daily Surge In Google Trends For Car Rental Price Spike Triggers Travel Mobility Sector Pullback

**Idea ID:** `daily-surge-in-google-trends-for-car-rental-price-spike-trig`
**Family:** `travel_mobility`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising interest in rental car price spikes signals travel cost inflation that can reduce travel demand and negatively impact travel-related stocks. Higher travel costs suppress discretionary travel spending.

## Universe
- XLY

## Data Sources
- Google Trends daily queries

## Signal Logic
If daily Google Trends volume for 'car rental price spike' increases by 15% from previous day

## Entry / Exit
Entry: If daily Google Trends volume for 'car rental price spike' increases by 15% from previous day Exit: After 5 trading days or when volume drops 10% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily queries via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Travel cost inflation news and seasonal demand cause frequent search surges.

## Required Keys
- None

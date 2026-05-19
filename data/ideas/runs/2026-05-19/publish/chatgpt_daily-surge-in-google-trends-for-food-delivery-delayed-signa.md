# Daily Surge In Google Trends For Food Delivery Delayed Signals Consumer Frustration And Delivery Stress

**Idea ID:** `daily-surge-in-google-trends-for-food-delivery-delayed-signa`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Daily spikes in food delivery delay complaints indicate logistical stress impacting consumer satisfaction. Consumer discretionary sector faces headwinds from service delays and frustration.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter short XLY when daily 'food delivery delayed' searches exceed 2 std deviations above 30-day mean

## Entry / Exit
Entry: Enter short XLY when daily 'food delivery delayed' searches exceed 2 std deviations above 30-day mean Exit: Exit after 5 days or once volume falls below 1 std deviation

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Food delivery issues cause frequent daily search spikes especially in holidays or bad weather.

## Required Keys
- None

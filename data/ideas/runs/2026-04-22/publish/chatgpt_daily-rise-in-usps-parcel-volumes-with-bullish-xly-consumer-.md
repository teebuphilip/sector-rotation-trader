# Daily Rise In Usps Parcel Volumes With Bullish Xly Consumer Discretionary Impact

**Idea ID:** `daily-rise-in-usps-parcel-volumes-with-bullish-xly-consumer-`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased parcel volume suggests rising e-commerce activity, benefiting consumer discretionary stocks. E-commerce growth drives consumer discretionary sector strength.

## Universe
- XLY

## Data Sources
- USPS daily parcel volume data and Yahoo Finance daily XLY prices

## Signal Logic
Enter long XLY when USPS parcel volume increases >7% day-over-day and XLY outperforms SPY

## Entry / Exit
Entry: Enter long XLY when USPS parcel volume increases >7% day-over-day and XLY outperforms SPY Exit: Exit after 5 trading days or if volume declines

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USPS daily parcel volume data and Yahoo Finance daily XLY prices via scrape (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Parcel volume data is daily with frequent volume bursts.

## Required Keys
- None

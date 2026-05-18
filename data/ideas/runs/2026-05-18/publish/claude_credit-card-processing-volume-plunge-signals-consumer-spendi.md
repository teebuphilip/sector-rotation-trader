# Credit Card Processing Volume Plunge Signals Consumer Spending Halt

**Idea ID:** `credit-card-processing-volume-plunge-signals-consumer-spendi`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Sharp drops in credit card transaction volumes precede broader consumer spending collapses and signal immediate consumer confidence crisis. Spending volume collapse directly compresses revenue for retail, hospitality, and consumer discretionary companies.

## Universe
- XLY

## Data Sources
- Visa and Mastercard weekly transaction volume indices through html_table or rss_count adapter from earnings/investor updates

## Signal Logic
If weekly credit card transaction volume falls 15% or more below 4-week MA, short XLY.

## Entry / Exit
Entry: If weekly credit card transaction volume falls 15% or more below 4-week MA, short XLY. Exit: Exit after 10 trading days or when volume recovers to MA.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Visa and Mastercard weekly transaction volume indices through html_table or rss_count adapter from earnings/investor updates via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Credit card volumes experience 15%+ swings quarterly due to seasonal patterns and economic shocks, creating 2–4 monthly signals.

## Required Keys
- None

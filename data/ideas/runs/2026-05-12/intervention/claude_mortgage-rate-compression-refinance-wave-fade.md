# Mortgage Rate Compression Refinance Wave Fade

**Idea ID:** `mortgage-rate-compression-refinance-wave-fade`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When MORTGAGE30US drops >0.5% over 2 weeks and refinance search interest spikes, consumer discretionary spending rebounds but eventual rate stabilization causes mean reversion. Falling rates unlock household liquidity and home equity; consumers spend on discretionary goods and services.

## Universe
- XLY

## Data Sources
- FRED series MORTGAGE30US (30-year mortgage rate) daily; pair with Google Trends weekly searches for 'mortgage refinance' and 'home equity loan'

## Signal Logic
If MORTGAGE30US drops >0.5% in 2 weeks AND Google Trends 'refinance' searches rise >40% YoY, buy XLY

## Entry / Exit
Entry: If MORTGAGE30US drops >0.5% in 2 weeks AND Google Trends 'refinance' searches rise >40% YoY, buy XLY Exit: After 12 trading days or when rates stabilize for 3+ consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MORTGAGE30US (30-year mortgage rate) daily; pair with Google Trends weekly searches for 'mortgage refinance' and 'home equity loan' via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Fed policy shifts and bond market repricing trigger rate drops several times per year, reliably firing this signal.

## Required Keys
- None

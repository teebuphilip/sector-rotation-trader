# Bank Deposit Outflow Fear Inversion Signal

**Idea ID:** `bank-deposit-outflow-fear-inversion-signal`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly bank deposit flows turn negative (outflows exceed inflows) for 2 consecutive weeks AND high-yield savings rates spike >0.5% above prior month, retail depositors flee traditional banks. Bank funding stress accelerates. Deposit outflows force banks to raise rates, compress NIM, and rely on wholesale funding. Equity valuations contract on net interest margin compression.

## Universe
- XLF

## Data Sources
- FRED series on bank deposits (BMNRNJ) and high-yield savings rate (MMNRNJ) weekly; XLF ETF daily price via price_only adapter

## Signal Logic
Weekly deposit growth <0% for 2 consecutive weeks AND HY savings rate spike >0.5% MoM

## Entry / Exit
Entry: Weekly deposit growth <0% for 2 consecutive weeks AND HY savings rate spike >0.5% MoM Exit: Deposit growth returns >0.5% or 15 trading days elapsed

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series on bank deposits (BMNRNJ) and high-yield savings rate (MMNRNJ) weekly; XLF ETF daily price via price_only adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Deposit volatility and HY rate spreads move 4–6 times per year; signal fires reliably during rate hike cycles.

## Required Keys
- None

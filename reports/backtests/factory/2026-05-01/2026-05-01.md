# Professional Backtest V1

- Run date: 2026-05-01
- Window: 2024-01-01 to 2026-05-01
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- BACKTEST_WEAK: 1
- LIVE_ONLY_NON_PRICE: 8

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Daily Spike In Google Trends For Emergency Plumbing Repair Signals Consumer Stress Rebound Benefiting Discretionary Sector | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Spike In Google Trends For Emergency Vehicle Repair Signals Consumer Stress Lifting Industrial Sector | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Spike In Google Trends For Home Air Purifier Repair Signals Consumer Stress Rebound In Discretionary Sector | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Surge In Google Trends Searches For Home Heating System Failure Signals Consumer Stress Impacting Utilities | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Eia Electricity Demand Shock Rebound Spread | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.eia_electricity |
| Ev Charger Network Expansion Velocity Surge | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Google Trends Surge In Flight Delay Complaints | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Price Momentum Reversion In Defensive Sectors After Tech Crash | crazy | BACKTEST_WEAK | -55.99 | 28 | Backtest completed |
| Weekly Surge In Google Trends For Diy Solar Panel Repair Signals Green Energy Sector Rebound | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |

This is experimental research, not investment advice. Past performance does not predict future results.

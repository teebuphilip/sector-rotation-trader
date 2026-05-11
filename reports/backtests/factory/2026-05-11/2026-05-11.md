# Professional Backtest V1

- Run date: 2026-05-11
- Window: 2024-01-01 to 2026-05-11
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- INSUFFICIENT_ACTIVITY: 1
- LIVE_ONLY_NON_PRICE: 7

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Airline Fuel Cost Volatility Expansion | crazy | INSUFFICIENT_ACTIVITY | -60.36 | 0 | Backtest completed |
| Daily Jump In Google Trends For Emergency Plumber Signals Rising Local Economy Stress Benefiting Staples | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Ev Charger Expansion Velocity Boom | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Freight Rail Congestion Rss Volume Explosion | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Healthcare Cost Inflation Google Trends Acceleration | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Luxury Discretionary Google Trends Collapse Signal | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weather Extremes Utility Demand Spike | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.eia_electricity |
| Weekly Jump In Google Trends For Home Heating Oil Shortage Signals Winter Energy Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |

This is experimental research, not investment advice. Past performance does not predict future results.

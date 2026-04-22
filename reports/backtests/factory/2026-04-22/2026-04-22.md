# Professional Backtest V1

- Run date: 2026-04-22
- Window: 2024-01-01 to 2026-04-22
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- LIVE_ONLY_NON_PRICE: 7
- NEEDS_HISTORY: 1

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Ev Charger Density Saturation Play | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Grocery Store Foot Traffic Collapse Signal | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Healthcare Cost Shock Google Search Spike | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| News Sentiment Rotation Fade Trade | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Rental Car Shortage Volatility Spike | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Seismic Activity Construction Halt Signal | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.earthquake_activity |
| Shipping Container Squeeze Play | crazy | NEEDS_HISTORY |  |  | Historical seed exists, but V1 cannot prove point-in-time price-only behavior |
| Temperature Shock Energy Demand Flip | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.weather_series |

This is experimental research, not investment advice. Past performance does not predict future results.

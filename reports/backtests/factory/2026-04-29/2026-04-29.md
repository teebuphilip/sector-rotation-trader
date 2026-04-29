# Professional Backtest V1

- Run date: 2026-04-29
- Window: 2024-01-01 to 2026-04-29
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- BACKTEST_FAIL: 1
- INSUFFICIENT_ACTIVITY: 1
- LIVE_ONLY_NON_PRICE: 5

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Ev Charger Installation Acceleration Play | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Financial Sector Volatility Crush Trade | crazy | BACKTEST_FAIL | -55.14 | 54 | Backtest completed |
| Gold Volatility Vol-of-vol Spike | crazy | INSUFFICIENT_ACTIVITY | -54.72 | 0 | Backtest completed |
| Mortgage Refinance Wave Google Trends Surge | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Google Trends Surge In Fast Food Job Openings Signals Bullish Consumer Discretionary | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Google Trends Surge In Home Appliance Repair Searches Signals Bullish Consumer Discretionary | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Google Trends Surge In Home Energy Bill Shock Signals Bullish Utilities | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |

This is experimental research, not investment advice. Past performance does not predict future results.

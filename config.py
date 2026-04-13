# ============================================================
# SECTOR ROTATION TRADER — CONFIG
# ============================================================

# Capital
STARTING_CASH        = 100_000.0   # base portfolio cash
MAX_POSITION_SIZE    = 10_000.0    # max $ per trade
MAX_BORROW           = 100_000.0   # max margin borrowing allowed
BORROW_RATE_ANNUAL   = 0.085       # 8.5% annual margin rate (daily accrual)

# Sector ETFs (11 SPDR sectors)
SECTOR_ETFS = ['XLK','XLV','XLF','XLY','XLI','XLC','XLP','XLE','XLB','XLRE','XLU']

# Sector rotation signal
PERF_SHORT_DAYS = 63    # ~3 months
PERF_LONG_DAYS  = 126   # ~6 months

# Entry signals (all 3 must fire)
BREAKOUT_LOOKBACK    = 10    # price closes above N-day high
VOLUME_MULT          = 1.5   # volume must be >= 150% of 20-day avg
VOLUME_AVG_DAYS      = 20
BB_PERIOD            = 20    # Bollinger Band period
BB_STD               = 2.0   # Bollinger Band std devs

# Exit signal
EXIT_MA_PERIOD       = 20    # 20-day MA
EXIT_CONSEC_DAYS     = 2     # N consecutive closes below MA triggers exit

# Risk management
STOP_LOSS_PCT        = 0.08  # 8% hard stop-loss per position
MAX_DRAWDOWN_PCT     = 0.15  # 15% portfolio drawdown — pause new entries
MAX_POSITIONS_PER_SECTOR = 5 # max open positions in the same sector

# Simulation window
SEED_DAYS            = 90    # historical days to seed state on first run
SIM_MONTHS           = 6     # total simulation duration

# Data
DATA_PERIOD          = "1y"  # yfinance download window

# Paths
STATE_FILE           = "state.json"
DASHBOARD_FILE       = "docs/nrwise.html"
LOG_FILE             = "docs/trades.json"

# Fees & Taxes (configurable; conservative/high defaults)
APPLY_FEES           = True
COMMISSION_PER_TRADE = 9.95       # flat commission per buy/sell
SEC_FEE_RATE         = 0.00005    # sell-side fee rate on proceeds (high default)
TAF_FEE_PER_SHARE    = 0.0003     # sell-side fee per share (high default)

APPLY_TAXES          = True
TAX_RATE_SHORT       = 0.37       # short-term cap gains (high default)
TAX_RATE_LONG        = 0.20       # long-term cap gains (high default)
TAX_LONG_TERM_DAYS   = 365

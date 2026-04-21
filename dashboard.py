"""
dashboard.py — Generate docs/index.html from current portfolio state.
Committed to repo → served via GitHub Pages.
"""
import json
import os
from datetime import date
from config import STARTING_CASH, DASHBOARD_FILE


def generate_dashboard(state: dict, current_px: dict, sector: str,
                       analytics: dict = None, spy_prices=None,
                       output_path: str = None,
                       strategy_label: str = None,
                       strategy_value: str = None,
                       title: str = None):
    out_path = output_path or DASHBOARD_FILE
    os.makedirs(os.path.dirname(out_path) or "docs", exist_ok=True)
    legal_href = os.path.relpath(os.path.join("docs", "legal.html"), os.path.dirname(out_path) or ".")

    # ── Compute summary stats ──────────────────────────────────
    pos_value = sum(
        pos["shares"] * current_px.get(ticker, pos["entry_price"])
        for ticker, pos in state["positions"].items()
    )
    equity      = state["cash"] + pos_value - state["borrowed"] - state["accrued_interest"]
    net_pnl     = equity - STARTING_CASH
    net_pnl_pct = (net_pnl / STARTING_CASH) * 100
    realized    = sum(t.get("pnl", 0) for t in state["trade_log"] if t["action"] == "SELL")
    unrealized  = sum(
        (current_px.get(t, p["entry_price"]) - p["entry_price"]) * p["shares"]
        for t, p in state["positions"].items()
    )
    wins  = [t for t in state["trade_log"] if t["action"] == "SELL" and t.get("pnl", 0) > 0]
    total_closed = [t for t in state["trade_log"] if t["action"] == "SELL"]
    win_rate = (len(wins) / len(total_closed) * 100) if total_closed else 0.0

    # ── Analytics ──────────────────────────────────────────────
    if analytics is None:
        analytics = {"sharpe": 0.0, "max_drawdown_pct": 0.0, "avg_win": 0.0, "avg_loss": 0.0, "drawdown_series": []}
    sharpe       = analytics.get("sharpe", 0.0)
    max_dd       = analytics.get("max_drawdown_pct", 0.0)
    avg_win      = analytics.get("avg_win", 0.0)
    avg_loss     = analytics.get("avg_loss", 0.0)
    dd_series    = analytics.get("drawdown_series", [])

    # ── SPY benchmark data ────────────────────────────────────
    spy_returns_js = "[]"
    if spy_prices is not None and not spy_prices.empty:
        import pandas as pd
        sim_start = state.get("sim_start", "")
        if sim_start:
            spy_s = spy_prices.squeeze() if hasattr(spy_prices, 'squeeze') else spy_prices
            spy_s = spy_s.dropna()
            spy_s = spy_s[spy_s.index >= sim_start]
            if len(spy_s) > 0:
                base = float(spy_s.iloc[0])
                spy_norm = [round(float(v) / base * STARTING_CASH, 2) for v in spy_s]
                spy_returns_js = json.dumps(spy_norm)

    # ── Equity curve data ──────────────────────────────────────
    snap_dates  = [s["date"] for s in state["daily_snapshots"]]
    snap_equity = [s["equity"] for s in state["daily_snapshots"]]

    # ── Positions table rows ───────────────────────────────────
    pos_rows = ""
    for ticker, pos in state["positions"].items():
        cur  = current_px.get(ticker, pos["entry_price"])
        pnl  = (cur - pos["entry_price"]) * pos["shares"]
        pct  = ((cur - pos["entry_price"]) / pos["entry_price"]) * 100
        margin_badge = '<span class="badge margin">MARGIN</span>' if pos.get("using_margin") else ''
        color = "#00ff88" if pnl >= 0 else "#ff4d6d"
        pos_rows += f"""
        <tr>
          <td><span class="ticker">{ticker}</span>{margin_badge}</td>
          <td>${pos['entry_price']:.2f}</td>
          <td>${cur:.2f}</td>
          <td style="color:{color}">${pnl:+,.2f} ({pct:+.1f}%)</td>
          <td>{pos['entry_date']}</td>
          <td>{pos.get('consec_below_ma',0)}</td>
        </tr>"""

    # ── Trade log rows (last 30) ───────────────────────────────
    trade_rows = ""
    for t in reversed(state["trade_log"][-30:]):
        if t["action"] == "BUY":
            trade_rows += f"""
            <tr class="buy-row">
              <td>{t['date']}</td>
              <td><span class="action-buy">BUY</span></td>
              <td><span class="ticker">{t['ticker']}</span></td>
              <td>${t['price']:.2f}</td>
              <td>{t['shares']:.4f}</td>
              <td>${t['cost']:,.2f}</td>
              <td>—</td>
              <td>{'MARGIN' if t.get('margin') else 'CASH'}</td>
            </tr>"""
        else:
            pnl_c  = t.get('pnl', 0)
            pnl_pct= t.get('pnl_pct', 0)
            color  = "#00ff88" if pnl_c >= 0 else "#ff4d6d"
            trade_rows += f"""
            <tr class="sell-row">
              <td>{t['date']}</td>
              <td><span class="action-sell">SELL</span></td>
              <td><span class="ticker">{t['ticker']}</span></td>
              <td>${t['price']:.2f}</td>
              <td>{t['shares']:.4f}</td>
              <td>${t.get('proceeds',0):,.2f}</td>
              <td style="color:{color}">${pnl_c:+,.2f} ({pnl_pct:+.1f}%)</td>
              <td>{t.get('reason','—')}</td>
            </tr>"""

    # ── Equity chart JS data ───────────────────────────────────
    dates_js  = json.dumps(snap_dates)
    equity_js = json.dumps(snap_equity)
    dd_js     = json.dumps(dd_series)

    pnl_color  = "#00ff88" if net_pnl >= 0 else "#ff4d6d"
    sector_str = strategy_value or sector or "—"
    label_str = strategy_label or "Leading Sector"
    title_str = title or "Sector<span>/</span>Rotation <span>|</span> Paper Trader"
    lab_start = state.get("sim_start") or (snap_dates[0] if snap_dates else "unknown")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sector Rotation Trader</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;600&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg:        #0a0d12;
    --surface:   #111520;
    --border:    #1e2535;
    --accent:    #00d4ff;
    --green:     #00ff88;
    --red:       #ff4d6d;
    --yellow:    #ffd166;
    --text:      #c8d6e5;
    --muted:     #4a5568;
    --font-mono: 'Space Mono', monospace;
    --font-body: 'DM Sans', sans-serif;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    background: var(--bg);
    color: var(--text);
    font-family: var(--font-body);
    font-size: 14px;
    line-height: 1.6;
  }}

  /* ── Header ── */
  header {{
    border-bottom: 1px solid var(--border);
    padding: 20px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--surface);
  }}
  .logo {{
    font-family: var(--font-mono);
    font-size: 13px;
    color: var(--accent);
    letter-spacing: 0.15em;
    text-transform: uppercase;
  }}
  .logo span {{ color: var(--muted); }}
  .last-update {{
    font-family: var(--font-mono);
    font-size: 11px;
    color: var(--muted);
  }}

  /* ── Layout ── */
  .container {{ max-width: 1400px; margin: 0 auto; padding: 28px 32px; }}

  /* ── KPI bar ── */
  .kpi-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
    margin-bottom: 28px;
  }}
  .kpi {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px 18px;
  }}
  .kpi-label {{
    font-family: var(--font-mono);
    font-size: 10px;
    letter-spacing: 0.1em;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 6px;
  }}
  .kpi-value {{
    font-family: var(--font-mono);
    font-size: 20px;
    font-weight: 700;
    color: var(--text);
  }}
  .kpi-value.green {{ color: var(--green); }}
  .kpi-value.red   {{ color: var(--red); }}
  .kpi-value.accent {{ color: var(--accent); }}

  /* ── Panels ── */
  .panel {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    margin-bottom: 20px;
    overflow: hidden;
  }}
  .panel-header {{
    padding: 14px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .panel-title {{
    font-family: var(--font-mono);
    font-size: 11px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--accent);
  }}
  .panel-body {{ padding: 20px; }}

  /* ── Chart ── */
  .chart-wrap {{
    position: relative;
    height: 280px;
  }}

  /* ── Tables ── */
  .two-col {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}

  table {{ width: 100%; border-collapse: collapse; }}
  thead th {{
    font-family: var(--font-mono);
    font-size: 10px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--muted);
    padding: 8px 12px;
    text-align: left;
    border-bottom: 1px solid var(--border);
  }}
  tbody td {{
    padding: 9px 12px;
    border-bottom: 1px solid rgba(30,37,53,0.6);
    font-size: 13px;
    color: var(--text);
  }}
  tbody tr:last-child td {{ border-bottom: none; }}
  tbody tr:hover td {{ background: rgba(0,212,255,0.03); }}

  .ticker {{
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 700;
    color: var(--accent);
  }}
  .badge {{
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 9px;
    padding: 2px 6px;
    border-radius: 3px;
    margin-left: 6px;
    letter-spacing: 0.05em;
    vertical-align: middle;
  }}
  .badge.margin {{ background: rgba(255,209,102,0.15); color: var(--yellow); border: 1px solid var(--yellow); }}

  .action-buy  {{ font-family: var(--font-mono); font-size: 11px; font-weight:700; color: var(--green); }}
  .action-sell {{ font-family: var(--font-mono); font-size: 11px; font-weight:700; color: var(--red); }}

  .empty-state {{
    text-align: center;
    color: var(--muted);
    font-family: var(--font-mono);
    font-size: 12px;
    padding: 40px;
  }}

  /* ── Dot indicator ── */
  .dot {{ width: 8px; height: 8px; border-radius: 50%; display: inline-block; }}
  .dot.green {{ background: var(--green); box-shadow: 0 0 6px var(--green); }}
  .dot.yellow {{ background: var(--yellow); }}

  .disclaimer {{
    margin-top: 28px;
    padding: 18px 20px;
    border: 1px solid var(--border);
    border-radius: 10px;
    background: rgba(17, 21, 32, 0.72);
    color: var(--muted);
    font-family: var(--font-mono);
    font-size: 11px;
    line-height: 1.7;
  }}

  @media (max-width: 1100px) {{
    .kpi-grid {{ grid-template-columns: repeat(3, 1fr); }}
    .two-col  {{ grid-template-columns: 1fr; }}
  }}
  @media (max-width: 680px) {{
    .kpi-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .container {{ padding: 16px; }}
  }}
</style>
</head>
<body>

<header>
  <div class="logo">{title_str}</div>
  <div class="last-update">Lab started: {lab_start} &nbsp;·&nbsp; Last run: {date.today()} &nbsp;·&nbsp; $100k base · $10k/trade</div>
</header>

<div class="container">

  <!-- KPI Bar -->
  <div class="kpi-grid">
    <div class="kpi">
      <div class="kpi-label">Total Equity</div>
      <div class="kpi-value">${equity:,.0f}</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Net P&L</div>
      <div class="kpi-value {'green' if net_pnl >= 0 else 'red'}">${net_pnl:+,.0f}</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Return</div>
      <div class="kpi-value {'green' if net_pnl_pct >= 0 else 'red'}">{net_pnl_pct:+.2f}%</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Win Rate</div>
      <div class="kpi-value accent">{win_rate:.0f}%</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">{label_str}</div>
      <div class="kpi-value accent">{sector_str}</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Sharpe Ratio</div>
      <div class="kpi-value {'green' if sharpe >= 1.0 else 'red' if sharpe < 0 else 'accent'}">{sharpe:.2f}</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Max Drawdown</div>
      <div class="kpi-value red">{max_dd:.1f}%</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Avg Win</div>
      <div class="kpi-value green">${avg_win:+,.0f}</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Avg Loss</div>
      <div class="kpi-value red">${avg_loss:+,.0f}</div>
    </div>
    <div class="kpi">
      <div class="kpi-label">Realized / Unrealized</div>
      <div class="kpi-value {'green' if realized >= 0 else 'red'}">${realized:+,.0f} / ${unrealized:+,.0f}</div>
    </div>
  </div>

  <!-- Equity Curve -->
  <div class="panel">
    <div class="panel-header">
      <span class="dot green"></span>
      <span class="panel-title">Equity Curve</span>
    </div>
    <div class="panel-body">
      <div class="chart-wrap">
        <canvas id="equityChart"></canvas>
      </div>
    </div>
  </div>

  <!-- Drawdown Chart -->
  <div class="panel">
    <div class="panel-header">
      <span class="dot" style="background:var(--red);box-shadow:0 0 6px var(--red)"></span>
      <span class="panel-title">Drawdown</span>
    </div>
    <div class="panel-body">
      <div class="chart-wrap" style="height:180px">
        <canvas id="drawdownChart"></canvas>
      </div>
    </div>
  </div>

  <!-- Positions + Sector Performance -->
  <div class="two-col">
    <div class="panel">
      <div class="panel-header">
        <span class="dot yellow"></span>
        <span class="panel-title">Open Positions ({len(state['positions'])})</span>
      </div>
      <div class="panel-body" style="padding:0">
        {'<table><thead><tr><th>Ticker</th><th>Entry</th><th>Current</th><th>P&L</th><th>Opened</th><th>Consec↓MA</th></tr></thead><tbody>' + pos_rows + '</tbody></table>' if state['positions'] else '<div class="empty-state">No open positions</div>'}
      </div>
    </div>

    <div class="panel">
      <div class="panel-header">
        <span class="dot yellow"></span>
        <span class="panel-title">Portfolio Stats</span>
      </div>
      <div class="panel-body">
        <table>
          <tbody>
            <tr><td style="color:var(--muted);font-family:var(--font-mono);font-size:11px">CASH</td><td>${state['cash']:,.2f}</td></tr>
            <tr><td style="color:var(--muted);font-family:var(--font-mono);font-size:11px">BORROWED</td><td style="color:{'var(--yellow)' if state['borrowed'] > 0 else 'var(--text)'}">${state['borrowed']:,.2f}</td></tr>
            <tr><td style="color:var(--muted);font-family:var(--font-mono);font-size:11px">ACCRUED INT.</td><td style="color:var(--red)">${state['accrued_interest']:,.2f}</td></tr>
            <tr><td style="color:var(--muted);font-family:var(--font-mono);font-size:11px">OPEN POSITIONS</td><td>{len(state['positions'])}</td></tr>
            <tr><td style="color:var(--muted);font-family:var(--font-mono);font-size:11px">TOTAL TRADES</td><td>{len(total_closed)}</td></tr>
            <tr><td style="color:var(--muted);font-family:var(--font-mono);font-size:11px">WINNERS</td><td>{len(wins)}</td></tr>
            <tr><td style="color:var(--muted);font-family:var(--font-mono);font-size:11px">WIN RATE</td><td>{win_rate:.1f}%</td></tr>
            <tr><td style="color:var(--muted);font-family:var(--font-mono);font-size:11px">SIM START</td><td>{state['sim_start']}</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- Trade Log -->
  <div class="panel">
    <div class="panel-header">
      <span class="dot yellow"></span>
      <span class="panel-title">Trade Log (last 30)</span>
    </div>
    <div class="panel-body" style="padding:0; overflow-x:auto">
      {'<table><thead><tr><th>Date</th><th>Action</th><th>Ticker</th><th>Price</th><th>Shares</th><th>Value</th><th>P&L</th><th>Notes</th></tr></thead><tbody>' + trade_rows + '</tbody></table>' if state['trade_log'] else '<div class="empty-state">No trades yet — this signal is running, but it has never fired in the current state history.</div>'}
    </div>
  </div>

  <div class="disclaimer">
    <strong>Signal Lab Notice:</strong> This is an experimental signal lab. Signals are generated, tracked, and evaluated as research outputs. Many signals will fail, and some may only appear to work because of randomness or limited sample size.<br>
    <strong>Not financial advice:</strong> Nothing here is a recommendation to buy, sell, or hold any asset. Past performance does not guarantee future results.<br>
    <strong>Performance/data disclosure:</strong> Results are model outputs from simulated or simplified conditions and may not reflect slippage, fees, liquidity, execution delays, or market impact. Third-party data may be incomplete, delayed, inaccurate, or revised.<br>
    <strong>Your responsibility:</strong> Do your own research and consult a qualified professional before making investment decisions. Paper-traded only &mdash; no real money at risk. <a href="{legal_href}">Full disclaimer</a>.
  </div>

</div>

<script>
const dates  = {dates_js};
const equity = {equity_js};
const startV = {STARTING_CASH};
const spyData = {spy_returns_js};
const ddData  = {dd_js};

const ctx = document.getElementById('equityChart').getContext('2d');

const grad = ctx.createLinearGradient(0, 0, 0, 280);
grad.addColorStop(0,   'rgba(0,212,255,0.25)');
grad.addColorStop(1,   'rgba(0,212,255,0.00)');

new Chart(ctx, {{
  type: 'line',
  data: {{
    labels: dates,
    datasets: [
      {{
        label: 'Portfolio Equity',
        data: equity,
        borderColor: '#00d4ff',
        borderWidth: 2,
        backgroundColor: grad,
        fill: true,
        tension: 0.3,
        pointRadius: equity.length > 60 ? 0 : 3,
        pointHoverRadius: 5,
        pointBackgroundColor: '#00d4ff',
      }},
      {{
        label: 'SPY Benchmark',
        data: spyData.length ? spyData.slice(0, dates.length) : [],
        borderColor: '#ffd166',
        borderWidth: 1.5,
        borderDash: [6,3],
        fill: false,
        tension: 0.3,
        pointRadius: 0,
      }},
      {{
        label: 'Starting Capital',
        data: Array(dates.length).fill(startV),
        borderColor: 'rgba(255,255,255,0.12)',
        borderWidth: 1,
        borderDash: [4,4],
        fill: false,
        tension: 0,
        pointRadius: 0,
      }}
    ]
  }},
  options: {{
    responsive: true,
    maintainAspectRatio: false,
    interaction: {{ mode: 'index', intersect: false }},
    plugins: {{
      legend: {{
        labels: {{
          color: '#4a5568',
          font: {{ family: 'Space Mono', size: 11 }},
          boxWidth: 12,
        }}
      }},
      tooltip: {{
        backgroundColor: '#111520',
        borderColor: '#1e2535',
        borderWidth: 1,
        titleColor: '#00d4ff',
        bodyColor: '#c8d6e5',
        titleFont: {{ family: 'Space Mono', size: 11 }},
        bodyFont: {{ family: 'DM Sans', size: 12 }},
        callbacks: {{
          label: ctx => ' $' + ctx.parsed.y.toLocaleString(undefined, {{minimumFractionDigits:2, maximumFractionDigits:2}})
        }}
      }}
    }},
    scales: {{
      x: {{
        grid: {{ color: 'rgba(30,37,53,0.8)' }},
        ticks: {{
          color: '#4a5568',
          font: {{ family: 'Space Mono', size: 10 }},
          maxTicksLimit: 12,
        }}
      }},
      y: {{
        grid: {{ color: 'rgba(30,37,53,0.8)' }},
        ticks: {{
          color: '#4a5568',
          font: {{ family: 'Space Mono', size: 10 }},
          callback: v => '$' + (v/1000).toFixed(0) + 'k'
        }}
      }}
    }}
  }}
}});

// ── Drawdown Chart ──
if (ddData.length > 0) {{
  const ddCtx = document.getElementById('drawdownChart').getContext('2d');
  const ddGrad = ddCtx.createLinearGradient(0, 0, 0, 180);
  ddGrad.addColorStop(0, 'rgba(255,77,109,0.00)');
  ddGrad.addColorStop(1, 'rgba(255,77,109,0.30)');

  new Chart(ddCtx, {{
    type: 'line',
    data: {{
      labels: dates,
      datasets: [{{
        label: 'Drawdown %',
        data: ddData,
        borderColor: '#ff4d6d',
        borderWidth: 1.5,
        backgroundColor: ddGrad,
        fill: true,
        tension: 0.3,
        pointRadius: 0,
        pointHoverRadius: 4,
      }}]
    }},
    options: {{
      responsive: true,
      maintainAspectRatio: false,
      plugins: {{
        legend: {{ display: false }},
        tooltip: {{
          backgroundColor: '#111520',
          borderColor: '#1e2535',
          borderWidth: 1,
          titleColor: '#ff4d6d',
          bodyColor: '#c8d6e5',
          titleFont: {{ family: 'Space Mono', size: 11 }},
          bodyFont: {{ family: 'DM Sans', size: 12 }},
          callbacks: {{ label: ctx => ' ' + ctx.parsed.y.toFixed(2) + '%' }}
        }}
      }},
      scales: {{
        x: {{
          grid: {{ color: 'rgba(30,37,53,0.8)' }},
          ticks: {{ color: '#4a5568', font: {{ family: 'Space Mono', size: 10 }}, maxTicksLimit: 12 }}
        }},
        y: {{
          max: 0,
          grid: {{ color: 'rgba(30,37,53,0.8)' }},
          ticks: {{ color: '#4a5568', font: {{ family: 'Space Mono', size: 10 }}, callback: v => v.toFixed(0) + '%' }}
        }}
      }}
    }}
  }});
}}
</script>
</body>
</html>"""

    with open(out_path, "w") as f:
        f.write(html)

    print(f"\n  Dashboard written → {out_path}")

#!/usr/bin/env python3
"""
Generate static public HTML pages from docs/data/public/ contract.

Generates:
  docs/leaderboard.html   — sector heatmap + top-10 leaderboard + ticker lookup
  docs/landing.html       — landing/CTA with pricing section + rolling 30D winners
  docs/premium.html       — premium teaser page for the July paid launch
"""
from __future__ import annotations
import json
import html
import sys
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).parent.parent
PUBLIC = REPO / "docs" / "data" / "public"

SPECIAL = {
    "biscotti":  {"emoji": "\U0001f43e", "row_class": "row-biscotti",  "tip": "Named after Biscotti (2008\u20132026) \u2014 17.75 years of unconditional loyalty"},
    "baileymol": {"emoji": "\u26a1",      "row_class": "row-baileymol", "tip": "The Chaos Monger \u2014 thrives on volatility spikes"},
}

ETF_ORDER = ["XLK", "XLF", "XLV", "XLY", "XLI", "XLC", "XLP", "XLE", "XLB", "XLRE", "XLU"]

FREE_ROWS = 10


def _load(name: str) -> dict:
    p = PUBLIC / name
    if p.exists():
        return json.loads(p.read_text())
    return {}


def _e(s) -> str:
    return html.escape(str(s)) if s is not None else ""


def _fmt(n) -> str:
    if n is None:
        return "n/a"
    try:
        f = float(n)
        return ("+" if f > 0 else "") + f"{f:.2f}%"
    except (TypeError, ValueError):
        return "n/a"


def _ret_class(n) -> str:
    try:
        f = float(n)
        if f > 0:
            return "return-pos"
        if f < 0:
            return "return-neg"
    except (TypeError, ValueError):
        pass
    return "return-zero"


def _get_special(algo_id: str):
    for key, spec in SPECIAL.items():
        if key in str(algo_id):
            return spec
    return None


def _sector_heatmap_html(sector_summary: dict) -> str:
    parts = []
    for etf in ETF_ORDER:
        s = sector_summary.get(etf)
        if not s:
            continue
        label = _e(s.get("composite_label", "MIXED"))
        parts.append(
            f'<div class="sector-tile">'
            f'<div class="sector-tooltip">Composite: {_e(s.get("composite","?"))} '
            f'&bull; {_e(s.get("bullish_pct","?"))}% bullish</div>'
            f'<div class="etf">{_e(etf)}</div>'
            f'<div class="sector-name">{_e(s.get("sector",""))}</div>'
            f'<span class="verdict verdict-{label}">{label}</span>'
            f'</div>'
        )
    return "\n".join(parts) if parts else '<div class="loading">No sector data</div>'


def _leaderboard_rows_html(algos: list) -> str:
    rows = []
    for i, a in enumerate(algos):
        rank = i + 1
        is_free = rank <= FREE_ROWS
        spec = _get_special(str(a.get("algo_id", "")))
        row_cls = spec["row_class"] if spec else ""
        paywall_cls = "" if is_free else " paywall-row"

        emoji = f'<span class="algo-emoji">{spec["emoji"]}</span>' if spec else ""
        if spec:
            name_html = (
                f'<span class="name-tooltip"><span class="algo-name">{emoji}{_e(a.get("name",""))}</span>'
                f'<span class="tip">{_e(spec["tip"])}</span></span>'
            )
        else:
            name_html = f'<span class="algo-name">{_e(a.get("name",""))}</span>'

        ytd = a.get("ytd_pct")
        spy = a.get("spy_pct")
        try:
            diff = float(ytd) - float(spy)
            diff_cls = "vs-spy-pos" if diff >= 0 else "vs-spy-neg"
            diff_str = ("+" if diff >= 0 else "") + f"{diff:.2f}%"
        except (TypeError, ValueError):
            diff_cls = "vs-spy-neg"
            diff_str = "n/a"

        status_html = (
            '<span class="status-beat">BEATING SPY</span>'
            if a.get("beat_spy")
            else '<span class="status-lag">LAGGING</span>'
        )

        rows.append(
            f'<tr class="{row_cls}{paywall_cls}">'
            f'<td class="rank">{rank}</td>'
            f'<td>{name_html}</td>'
            f'<td><span class="algo-type-badge">{_e(a.get("algo_type",""))}</span></td>'
            f'<td class="{_ret_class(ytd)}">{_fmt(ytd)}</td>'
            f'<td class="vs-spy {diff_cls}">{diff_str}</td>'
            f'<td class="days">{_e(a.get("days_running",""))}d</td>'
            f'<td>{status_html}</td>'
            f'</tr>'
        )

    rows.append(
        '<tr class="paywall-cta-row">'
        '<td colspan="7"><a href="landing.html#waitlist">'
        '&rarr; Join our mailing list for launch updates</a></td>'
        '</tr>'
    )
    return "\n".join(rows)


CSS = """
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=IBM+Plex+Mono:wght@400;600&display=swap');
  :root {
    --bg: #0a0a0a;
    --bg2: #111;
    --card: #161616;
    --border: rgba(255,255,255,0.08);
    --accent: #19d38f;
    --accent-dim: #12a06b;
    --red: #ef4444;
    --red-dim: #991b1b;
    --yellow: #eab308;
    --gold: #d4a017;
    --purple: #a855f7;
    --muted: #888;
    --text: #e8e8e8;
    --mono: 'IBM Plex Mono', ui-monospace, monospace;
    --sans: 'Space Grotesk', system-ui, sans-serif;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: var(--sans); color: var(--text); background: var(--bg); line-height: 1.5; -webkit-font-smoothing: antialiased; }
  .hero { text-align: center; padding: 60px 24px 48px; background: radial-gradient(800px 400px at 50% 0%, rgba(25,211,143,0.06), transparent), var(--bg); border-bottom: 1px solid var(--border); }
  .hero-badge { display: inline-block; font-family: var(--mono); font-size: 12px; color: var(--accent); border: 1px solid var(--accent-dim); border-radius: 20px; padding: 4px 14px; margin-bottom: 16px; letter-spacing: 0.5px; }
  .hero h1 { font-size: clamp(28px, 5vw, 48px); font-weight: 700; letter-spacing: -0.5px; margin-bottom: 12px; }
  .hero h1 span { color: var(--accent); }
  .hero-sub { font-family: var(--mono); font-size: 14px; color: var(--muted); margin-bottom: 8px; }
  .hero-stats { display: flex; justify-content: center; gap: 32px; margin: 24px 0; flex-wrap: wrap; }
  .hero-stat { text-align: center; }
  .hero-stat .num { font-size: 32px; font-weight: 700; font-family: var(--mono); color: var(--accent); }
  .hero-stat .label { font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }
  .cta { display: inline-block; margin-top: 20px; padding: 12px 32px; background: var(--accent); color: #000; font-weight: 700; font-size: 15px; border: none; border-radius: 8px; cursor: pointer; text-decoration: none; transition: background 0.2s; }
  .cta:hover { background: #1ee89e; }
  .cta-sub { display: block; font-size: 12px; color: var(--muted); margin-top: 8px; }
  .wrap { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
  section { padding: 48px 0; }
  section + section { border-top: 1px solid var(--border); }
  .section-title { font-size: 22px; font-weight: 700; margin-bottom: 6px; }
  .section-sub { font-size: 13px; color: var(--muted); margin-bottom: 24px; }
  .heatmap { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 10px; }
  .sector-tile { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 14px; text-align: center; cursor: default; transition: transform 0.15s, border-color 0.15s; position: relative; }
  .sector-tile:hover { transform: translateY(-2px); border-color: rgba(255,255,255,0.15); }
  .sector-tile .etf { font-family: var(--mono); font-size: 16px; font-weight: 700; }
  .sector-tile .sector-name { font-size: 11px; color: var(--muted); margin: 4px 0 8px; }
  .sector-tile .verdict { font-family: var(--mono); font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 4px; display: inline-block; letter-spacing: 0.5px; }
  .verdict-BULLISH { background: rgba(25,211,143,0.15); color: var(--accent); }
  .verdict-BEARISH { background: rgba(239,68,68,0.15); color: var(--red); }
  .verdict-MIXED { background: rgba(234,179,8,0.15); color: var(--yellow); }
  .sector-tooltip { display: none; position: absolute; bottom: calc(100% + 8px); left: 50%; transform: translateX(-50%); background: #222; border: 1px solid var(--border); border-radius: 6px; padding: 8px 12px; font-family: var(--mono); font-size: 11px; color: var(--muted); white-space: nowrap; z-index: 10; pointer-events: none; }
  .sector-tile:hover .sector-tooltip { display: block; }
  .table-wrap { overflow-x: auto; border-radius: 10px; border: 1px solid var(--border); background: var(--card); }
  table { width: 100%; border-collapse: collapse; font-size: 14px; }
  thead th { text-align: left; padding: 12px 16px; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: var(--muted); border-bottom: 1px solid var(--border); white-space: nowrap; font-weight: 600; }
  tbody td { padding: 12px 16px; border-bottom: 1px solid rgba(255,255,255,0.04); white-space: nowrap; }
  tbody tr:last-child td { border-bottom: none; }
  tbody tr:hover { background: rgba(255,255,255,0.02); }
  .rank { color: var(--muted); font-family: var(--mono); width: 40px; }
  .algo-name { font-weight: 600; display: flex; align-items: center; gap: 8px; }
  .algo-emoji { font-size: 18px; }
  .algo-type-badge { font-family: var(--mono); font-size: 10px; padding: 2px 6px; border-radius: 3px; background: rgba(255,255,255,0.06); color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; }
  .return-pos { color: var(--accent); font-family: var(--mono); font-weight: 600; }
  .return-neg { color: var(--red); font-family: var(--mono); font-weight: 600; }
  .return-zero { color: var(--muted); font-family: var(--mono); }
  .vs-spy { font-family: var(--mono); font-size: 12px; }
  .vs-spy-pos { color: var(--accent); }
  .vs-spy-neg { color: var(--red); }
  .days { font-family: var(--mono); color: var(--muted); }
  .status-beat { font-family: var(--mono); font-size: 11px; color: var(--accent); background: rgba(25,211,143,0.1); padding: 3px 8px; border-radius: 4px; letter-spacing: 0.3px; }
  .status-lag { font-family: var(--mono); font-size: 11px; color: var(--red); background: rgba(239,68,68,0.1); padding: 3px 8px; border-radius: 4px; letter-spacing: 0.3px; }
  .row-biscotti { border-left: 3px solid var(--gold) !important; }
  .row-baileymol { border-left: 3px solid var(--purple) !important; }
  .name-tooltip { position: relative; cursor: help; }
  .name-tooltip .tip { display: none; position: absolute; bottom: calc(100% + 6px); left: 0; background: #222; border: 1px solid var(--border); border-radius: 6px; padding: 8px 12px; font-size: 12px; font-weight: 400; color: var(--muted); white-space: nowrap; z-index: 20; pointer-events: none; }
  .name-tooltip:hover .tip { display: block; }
  .paywall-row td { color: rgba(255,255,255,0.15) !important; user-select: none; pointer-events: none; }
  .paywall-row .algo-name { filter: blur(4px); }
  .paywall-cta-row td { text-align: center; padding: 16px; border-bottom: none; }
  .paywall-cta-row a { color: var(--accent); font-weight: 600; text-decoration: none; font-size: 14px; }
  .paywall-cta-row a:hover { text-decoration: underline; }
  .ticker-check { max-width: 480px; }
  .ticker-input-wrap { display: flex; gap: 10px; margin-bottom: 16px; }
  .ticker-input { flex: 1; padding: 12px 16px; font-family: var(--mono); font-size: 16px; background: var(--card); border: 1px solid var(--border); border-radius: 8px; color: var(--text); outline: none; text-transform: uppercase; }
  .ticker-input::placeholder { color: rgba(255,255,255,0.2); }
  .ticker-input:focus { border-color: var(--accent-dim); }
  .ticker-btn { padding: 12px 20px; background: var(--accent); color: #000; font-weight: 700; font-size: 14px; border: none; border-radius: 8px; cursor: pointer; font-family: var(--sans); transition: background 0.2s; }
  .ticker-btn:hover { background: #1ee89e; }
  .ticker-result { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 20px; display: none; }
  .ticker-result.show { display: block; }
  .ticker-result .tr-ticker { font-family: var(--mono); font-size: 24px; font-weight: 700; }
  .ticker-result .tr-sector { font-size: 13px; color: var(--muted); margin: 4px 0 12px; }
  .ticker-result .tr-verdict { font-family: var(--mono); font-size: 14px; font-weight: 600; padding: 6px 14px; border-radius: 6px; display: inline-block; }
  .ticker-result .tr-unlock { display: block; margin-top: 16px; font-size: 13px; color: var(--muted); }
  .ticker-result .tr-unlock a { color: var(--accent); text-decoration: none; }
  .ticker-result .tr-unlock a:hover { text-decoration: underline; }
  .ticker-error { color: var(--red); font-family: var(--mono); font-size: 13px; display: none; }
  .ticker-error.show { display: block; }
  footer { border-top: 1px solid var(--border); padding: 32px 20px; text-align: center; font-size: 12px; color: var(--muted); line-height: 1.8; }
  footer a { color: var(--accent-dim); text-decoration: none; }
  footer a:hover { text-decoration: underline; }
  .memorial { margin-top: 16px; padding-top: 16px; border-top: 1px solid var(--border); font-style: italic; color: rgba(255,255,255,0.3); }
  .rank-note { border: 1px solid var(--border); border-radius: 12px; background: rgba(255,255,255,0.035); padding: 14px 16px; margin: 14px 0 18px; color: var(--muted); font-size: 13px; line-height: 1.65; }
  .rank-note strong { color: var(--text); }
  .rank-note code { font-family: var(--mono); color: var(--gold); background: rgba(255,204,102,0.08); padding: 1px 5px; border-radius: 4px; }
  @media (max-width: 600px) {
    .hero { padding: 40px 16px 32px; }
    .hero-stats { gap: 20px; }
    .hero-stat .num { font-size: 24px; }
    table { font-size: 13px; }
    thead th, tbody td { padding: 10px 10px; }
    .heatmap { grid-template-columns: repeat(auto-fill, minmax(110px, 1fr)); gap: 8px; }
    .sector-tile { padding: 10px; }
  }
"""


def build_leaderboard(daily: dict, leaderboard: dict) -> str:
    algos = leaderboard.get("algos", [])
    signal_count = daily.get("signal_count") or len(algos)
    counts = daily.get("counts", {})
    beating = sum(1 for a in algos if a.get("beat_spy"))
    total = counts.get("total") or len(algos)
    generated_at = daily.get("generated_at", "")
    run_date = daily.get("run_date", "")

    sector_html = _sector_heatmap_html(daily.get("sector_summary") or {})
    table_rows = _leaderboard_rows_html(algos)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Crazy Stock Algo \u2014 Live Signal Leaderboard</title>
<meta name="description" content="{_e(signal_count)} experimental trading algorithms running live. Track performance against SPY." />
<style>{CSS}</style>
</head>
<body>

<div class="hero">
  <div class="hero-badge">LIVE EXPERIMENT</div>
  <h1><span>{_e(signal_count)}</span> signals running</h1>
  <p class="hero-sub">Can unconventional data sources beat the S&amp;P 500?</p>
  <div class="hero-stats">
    <div class="hero-stat">
      <div class="num">{_e(total)}</div>
      <div class="label">Total Algos</div>
    </div>
    <div class="hero-stat">
      <div class="num">{_e(beating)}/{_e(total)}</div>
      <div class="label">Beating SPY</div>
    </div>
    <div class="hero-stat">
      <div class="num">11</div>
      <div class="label">Sectors Tracked</div>
    </div>
  </div>
  <a class="cta" href="landing.html#waitlist">Join our mailing list</a>
  <span class="cta-sub">Weekly lab notes, launch updates, and what broke</span>
</div>

<section>
  <div class="wrap">
    <h2 class="section-title">Sector Heatmap</h2>
    <p class="section-sub">Composite signal across all algorithms. Updated nightly.</p>
    <div class="heatmap">
{sector_html}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="section-title">Proven Signals</h2>
    <p class="section-sub">All algorithms ranked by return since seed.</p>
    <div class="rank-note">
      <strong>How to read this:</strong>
      <code>Force rank</code> is the full-window, since-seed paper-traded ranking.
      <code>Rolling 30D</code> is recent momentum. A signal can look great over 30 days
      and still rank poorly over the full window, or the other way around.
      We show both because hiding that split would be dishonest.
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>#</th><th>Algorithm</th><th>Type</th>
            <th>Return</th><th>vs SPY</th><th>Days</th><th>Status</th>
          </tr>
        </thead>
        <tbody>
{table_rows}
        </tbody>
      </table>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="section-title">Ticker Quick Check</h2>
    <p class="section-sub">Look up any tracked stock to see the composite signal. Free preview.</p>
    <div class="ticker-check">
      <div class="ticker-input-wrap">
        <input type="text" class="ticker-input" id="ticker-input" placeholder="NVDA" maxlength="6" autocomplete="off" />
        <button class="ticker-btn" onclick="checkTicker()">Check</button>
      </div>
      <div class="ticker-error" id="ticker-error"></div>
      <div class="ticker-result" id="ticker-result">
        <div class="tr-ticker" id="tr-ticker"></div>
        <div class="tr-sector" id="tr-sector"></div>
        <div class="tr-verdict" id="tr-verdict"></div>
        <span class="tr-unlock">Want the full breakdown later? <a href="landing.html#waitlist">Join our mailing list</a></span>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div><strong>crazystockalgo.com</strong> &mdash; Updated nightly at 6:30 PM ET</div>
    <div>Last updated: {_e(generated_at or run_date)}</div>
    <div style="margin-top:8px;">
      <strong>Signal Lab Notice:</strong> Experimental research only. Signals can and will fail. Do not interpret any signal as a recommendation.<br>
      <strong>Performance Disclosure:</strong> Leaderboards are model/simulation outputs and may not reflect slippage, fees, liquidity, execution delays, or market impact.<br>
      <strong>Data Disclaimer:</strong> Third-party data may be incomplete, delayed, inaccurate, or revised. Use at your own risk.<br>
      <strong>Not financial advice:</strong> Do your own research. You are responsible for your own decisions. Paper-traded only &mdash; no real money at risk.
    </div>
    <div class="memorial">In loving memory of Biscotti (2008&ndash;2026). Good boy. Best algo. &hearts;</div>
  </div>
</footer>

<script>
(function() {{
  var SIGNALS = 'data/public/signals/';
  function escHtml(s) {{ var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }}
  window.checkTicker = function() {{
    var input = document.getElementById('ticker-input');
    var ticker = input.value.trim().toUpperCase();
    var result = document.getElementById('ticker-result');
    var error = document.getElementById('ticker-error');
    result.classList.remove('show');
    error.classList.remove('show');
    if (!ticker) {{ error.textContent = 'Enter a ticker symbol.'; error.classList.add('show'); return; }}
    fetch(SIGNALS + ticker + '.json')
      .then(function(r) {{ if (!r.ok) throw new Error('not found'); return r.json(); }})
      .then(function(d) {{
        document.getElementById('tr-ticker').textContent = d.ticker;
        document.getElementById('tr-sector').textContent = (d.sector || '') + ' \u2022 ' + (d.sector_etf || '');
        var v = document.getElementById('tr-verdict');
        v.textContent = d.composite_label;
        v.className = 'tr-verdict verdict-' + d.composite_label;
        result.classList.add('show');
      }})
      .catch(function() {{
        error.textContent = ticker + ' not found in public signal data.';
        error.classList.add('show');
      }});
  }};
  document.getElementById('ticker-input').addEventListener('keydown', function(e) {{
    if (e.key === 'Enter') window.checkTicker();
  }});
}})();
</script>

</body>
</html>"""


LANDING_CSS = """
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=IBM+Plex+Mono:wght@400;600&display=swap');
  :root {
    --bg: #0d1412;
    --bg-2: #13231f;
    --card: #182b26;
    --accent: #19d38f;
    --muted: #9ab0a7;
    --text: #ecf5f2;
  }
  * { box-sizing: border-box; }
  body { margin: 0; font-family: 'Space Grotesk', system-ui, sans-serif; color: var(--text); background: radial-gradient(1000px 600px at 15% -10%, #1e3f35, transparent), radial-gradient(900px 500px at 90% 0%, #1b352f, transparent), var(--bg); }
  header { padding: 28px; border-bottom: 1px solid rgba(255,255,255,0.08); }
  header h1 { margin: 0; font-size: 30px; letter-spacing: 0.5px; }
  header p { margin: 6px 0 0; color: var(--muted); font-family: 'IBM Plex Mono', ui-monospace, monospace; font-size: 12px; }
  .wrap { padding: 24px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }
  .card { background: var(--card); border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; padding: 16px; box-shadow: 0 14px 30px rgba(0,0,0,0.22); }
  .card h2 { margin: 0 0 8px; font-size: 18px; }
  .card p { margin: 0 0 12px; color: var(--muted); font-size: 14px; line-height: 1.4; }
  .cta { display: inline-block; padding: 10px 12px; border-radius: 8px; border: 1px solid var(--accent); color: var(--accent); text-decoration: none; font-weight: 600; font-size: 13px; }
  .cta:hover { background: rgba(25, 211, 143, 0.1); }
  .winners h3 { margin: 0 0 8px; font-size: 16px; }
  .winners ul { margin: 0; padding: 0; list-style: none; }
  .winners li { padding: 6px 0; border-bottom: 1px solid rgba(255,255,255,0.06); font-size: 14px; }
  .winners li:last-child { border-bottom: none; }
  .muted { color: var(--muted); font-size: 12px; }
  .ret-pos { color: #19d38f; font-family: 'IBM Plex Mono', monospace; }
  .ret-neg { color: #ef4444; font-family: 'IBM Plex Mono', monospace; }
  .waitlist { margin-top: 16px; border: 1px solid rgba(25, 211, 143, 0.28); }
  .waitlist-form { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 8px; margin-top: 12px; }
  .waitlist-form input { min-width: 0; border: 1px solid rgba(255,255,255,0.14); border-radius: 8px; background: #0f1c18; color: var(--text); padding: 10px 12px; font: inherit; font-size: 14px; }
  .waitlist-form button { border: 1px solid var(--accent); border-radius: 8px; background: transparent; color: var(--accent); padding: 10px 12px; font: inherit; font-size: 13px; font-weight: 700; cursor: pointer; }
  .waitlist-form button:hover { background: rgba(25, 211, 143, 0.1); }
  .notice { margin-top: 10px; color: var(--muted); font-size: 12px; line-height: 1.4; }
  @media (max-width: 560px) { .waitlist-form { grid-template-columns: 1fr; } }
"""


def _winners_li(entries: list) -> str:
    if not entries:
        return '<li class="muted">No data yet</li>'
    parts = []
    for i, w in enumerate(entries[:3]):
        ret = w.get("ret_30d_pct")
        try:
            r = float(ret)
            cls = "ret-pos" if r >= 0 else "ret-neg"
            ret_str = f'<span class="{cls}">' + ("+" if r >= 0 else "") + f"{r:.2f}%</span>"
        except (TypeError, ValueError):
            ret_str = "n/a"
        parts.append(
            f'<li>{i + 1}. {_e(w.get("name", ""))} &mdash; {ret_str}</li>'
        )
    return "\n".join(parts)


def build_landing(leaderboard: dict, daily: dict | None = None) -> str:
    entries = leaderboard.get("algos", [])
    winners_html = _winners_li(entries)
    counts = (daily or {}).get("counts", {})
    total = counts.get("total") or len(entries)
    pricing_html = PRICING_SECTION.format(total=total, stripe_url=STRIPE_PAYMENT_URL)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Crazy Models Lab</title>
<style>{LANDING_CSS}</style>
</head>
<body>
  <header>
    <h1>Crazy Models Lab</h1>
    <p>Daily weird models. Public receipts. Failures included.</p>
  </header>

  <div class="wrap">
    <div class="grid">
      <div class="card">
        <h2>Product 1: Daily Crazy Models Feed</h2>
        <p>Every day we run a new, slightly unhinged trading signal. You get the full spec, the timestamps, and the ugly failures along with the wins.</p>
        <a class="cta" href="#waitlist">Join our mailing list</a>
      </div>

      <div class="card">
        <h2>Product 2: Model-Fit Scoring</h2>
        <p>Drop in a stock or sector. We score it against the live model library and show whether the chaos agrees or not.</p>
        <a class="cta" href="#waitlist">Join our mailing list</a>
      </div>

      <div class="card winners">
        <h3>30-Day Rolling Winners</h3>
        <ul>
{winners_html}
        </ul>
        <p class="muted">Source: rolling 30-day leaderboard &mdash; <a href="leaderboard.html">full leaderboard</a></p>
      </div>

      <div class="card">
        <h2>Honor Pages</h2>
        <p>Named algos that mean something to us. We run them forever.</p>
        <a class="cta" href="biscotti.html">Algo Biscotti</a>
        <div style="height:8px"></div>
        <a class="cta" href="bailey.html">Algo Baileymol</a>
      </div>

      <div class="card">
        <h2>Build Log</h2>
        <p>Ship notes, failures, and receipts. This is the public lab notebook.</p>
        <a class="cta" href="blog/index.html">Read the blog</a>
      </div>
    </div>

{pricing_html}

    <div class="card waitlist" id="waitlist">
      <h2>Waitlist</h2>
      <p>Get the weekly lab note: what fired, what broke, what got killed, and what Biscotti was doing.</p>
      <form
        class="waitlist-form"
        id="mailerlite-waitlist-form"
        action="https://assets.mailerlite.com/jsonp/2275606/forms/185025288971748377/subscribe"
        method="post"
        target="mailerlite-waitlist-frame"
      >
        <input type="email" name="fields[email]" placeholder="you@example.com" autocomplete="email" required />
        <input type="hidden" name="fields[source]" value="landing" />
        <input type="hidden" name="ml-submit" value="1" />
        <input type="hidden" name="anticsrf" value="true" />
        <button type="submit">Join waitlist</button>
      </form>
      <iframe name="mailerlite-waitlist-frame" title="Mailing list signup" style="display:none"></iframe>
      <div class="notice">No hype. Weekly notes from the paper-trading lab.</div>
    </div>

    <div class="card waitlist" id="disclaimer">
      <h2>Disclaimer</h2>
      <p>The information provided by this website, its tools, and any associated content is for informational and educational purposes only. Nothing here is financial, investment, legal, or tax advice.</p>
      <p>This service publishes experimental signals, research outputs, and historical observations. These are not recommendations to buy, sell, or hold any asset.</p>
      <p>Trading and investing involve significant risk, including possible loss of principal. Past performance does not guarantee future results. Signals, models, results, and third-party data may be incomplete, incorrect, delayed, or revised.</p>
      <p>You are solely responsible for your own financial decisions. Do your own research and consult a qualified professional before making investment decisions.</p>
      <p>By using this service, you agree that the operators are not liable for losses, damages, or decisions made based on the information provided.</p>
    </div>
  </div>

</body>
</html>"""


PREMIUM_CSS = CSS + """
  .gate-wrap { max-width: 480px; margin: 60px auto; padding: 0 20px; text-align: center; }
  .gate-title { font-size: 24px; font-weight: 700; margin-bottom: 8px; }
  .gate-sub { font-size: 14px; color: var(--muted); margin-bottom: 24px; line-height: 1.6; }
  .gate-form { display: flex; gap: 10px; margin-bottom: 16px; }
  .gate-input { flex: 1; padding: 12px 16px; font-family: var(--mono); font-size: 16px; background: var(--card); border: 1px solid var(--border); border-radius: 8px; color: var(--text); outline: none; letter-spacing: 2px; }
  .gate-input:focus { border-color: var(--accent-dim); }
  .gate-btn { padding: 12px 20px; background: var(--accent); color: #000; font-weight: 700; border: none; border-radius: 8px; cursor: pointer; font-family: var(--sans); transition: background 0.2s; }
  .gate-btn:hover { background: #1ee89e; }
  .gate-error { color: var(--red); font-family: var(--mono); font-size: 13px; margin-top: 8px; display: none; }
  .gate-error.show { display: block; }
  .gate-note { font-size: 12px; color: var(--muted); margin-top: 12px; line-height: 1.6; }
  .gate-note a { color: var(--accent-dim); text-decoration: none; }
  .gate-note a:hover { text-decoration: underline; }
  #premium-content { display: none; }
  #premium-content.unlocked { display: block; }
  .premium-badge { display: inline-block; font-family: var(--mono); font-size: 11px; color: var(--gold); border: 1px solid var(--gold); border-radius: 4px; padding: 2px 8px; margin-left: 8px; letter-spacing: 0.5px; vertical-align: middle; }
  .detail-col { color: var(--muted); font-family: var(--mono); font-size: 12px; }
  .family-badge { font-family: var(--mono); font-size: 10px; padding: 2px 6px; border-radius: 3px; background: rgba(168,85,247,0.1); color: var(--purple); border: 1px solid rgba(168,85,247,0.2); }
  .ev-badge { font-family: var(--mono); font-size: 10px; padding: 2px 6px; border-radius: 3px; background: rgba(25,211,143,0.08); color: var(--accent-dim); border: 1px solid rgba(25,211,143,0.15); }
  .signout-btn { background: none; border: 1px solid var(--border); color: var(--muted); font-size: 12px; padding: 4px 12px; border-radius: 4px; cursor: pointer; font-family: var(--mono); float: right; margin-top: 4px; }
  .signout-btn:hover { border-color: var(--red); color: var(--red); }
"""


def _premium_table_rows(algos: list) -> str:
    rows = []
    for i, a in enumerate(algos):
        rank = i + 1
        spec = _get_special(str(a.get("algo_id", "")))
        row_cls = spec["row_class"] if spec else ""

        emoji = f'<span class="algo-emoji">{spec["emoji"]}</span>' if spec else ""
        if spec:
            name_html = (
                f'<span class="name-tooltip"><span class="algo-name">{emoji}{_e(a.get("name",""))}</span>'
                f'<span class="tip">{_e(spec["tip"])}</span></span>'
            )
        else:
            name_html = f'<span class="algo-name">{_e(a.get("name",""))}</span>'

        ytd = a.get("ytd_pct")
        spy = a.get("spy_pct")
        ret30 = a.get("ret_30d_pct")
        try:
            diff = float(ytd) - float(spy)
            diff_cls = "vs-spy-pos" if diff >= 0 else "vs-spy-neg"
            diff_str = ("+" if diff >= 0 else "") + f"{diff:.2f}%"
        except (TypeError, ValueError):
            diff_cls = "vs-spy-neg"
            diff_str = "n/a"

        status_html = (
            '<span class="status-beat">BEATING SPY</span>'
            if a.get("beat_spy")
            else '<span class="status-lag">LAGGING</span>'
        )
        family = _e(a.get("family") or "")
        ev = _e(a.get("evidence_class") or "")

        rows.append(
            f'<tr class="{row_cls}">'
            f'<td class="rank">{rank}</td>'
            f'<td>{name_html}</td>'
            f'<td><span class="algo-type-badge">{_e(a.get("algo_type",""))}</span></td>'
            f'<td class="{_ret_class(ytd)}">{_fmt(ytd)}</td>'
            f'<td class="vs-spy {diff_cls}">{diff_str}</td>'
            f'<td class="{_ret_class(ret30)}">{_fmt(ret30)}</td>'
            f'<td class="days">{_e(a.get("days_running",""))}d</td>'
            f'<td>{status_html}</td>'
            f'<td><span class="family-badge">{family}</span></td>'
            f'<td><span class="ev-badge">{ev}</span></td>'
            f'</tr>'
        )
    return "\n".join(rows)


def build_premium(daily: dict, leaderboard: dict) -> str:
    algos = leaderboard.get("algos", [])
    total = len(algos)
    beating = sum(1 for a in algos if a.get("beat_spy"))
    generated_at = daily.get("generated_at", "")
    run_date = daily.get("run_date", "")
    sector_html = _sector_heatmap_html(daily.get("sector_summary") or {})
    table_rows = _premium_table_rows(algos[:15])
    counts = daily.get("counts") or {}
    watchlist = counts.get("watchlist", 0)
    promoted = counts.get("promoted", 0)
    graveyard = counts.get("graveyard", 0)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Crazy Stock Algo \u2014 Premium Preview</title>
<style>{PREMIUM_CSS}</style>
</head>
<body>

<div class="hero">
  <div class="hero-badge">PREMIUM PREVIEW</div>
  <h1><span>July 1</span> premium launch</h1>
  <p class="hero-sub">June 15 is free public launch. July 1 adds the paid operating layer.</p>
  <div class="hero-stats">
    <div class="hero-stat">
      <div class="num">{_e(total)}</div>
      <div class="label">Total Algos</div>
    </div>
    <div class="hero-stat">
      <div class="num">{_e(beating)}/{_e(total)}</div>
      <div class="label">Beating SPY</div>
    </div>
    <div class="hero-stat">
      <div class="num">{_e(watchlist)}</div>
      <div class="label">Watchlist</div>
    </div>
  </div>
  <a class="cta" href="landing.html#waitlist">Join the waitlist</a>
  <span class="cta-sub">No checkout yet. Waitlist first, paid launch July 1.</span>
</div>

<section>
  <div class="wrap">
    <h2 class="section-title">What Premium Will Add</h2>
    <p class="section-sub">This page is a teaser, not a gated member area yet.</p>
    <div class="hero-stats" style="justify-content:flex-start; gap:20px; margin:0 0 24px;">
      <div class="hero-stat">
        <div class="num">{_e(promoted)}</div>
        <div class="label">Promoted</div>
      </div>
      <div class="hero-stat">
        <div class="num">{_e(graveyard)}</div>
        <div class="label">Graveyard</div>
      </div>
      <div class="hero-stat">
        <div class="num">11</div>
        <div class="label">Sectors</div>
      </div>
    </div>
    <div class="rank-note">
      <strong>Free on June 15:</strong> blog, stripped leaderboard, families, promoted/watchlist summaries, graveyard, public daily report, and public ticker pages.
      <br>
      <strong>Paid on July 1:</strong> full leaderboard, full per-algo detail, full per-ticker detail, trade history, equity curves, and premium summaries.
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="section-title">Sector Heatmap</h2>
    <p class="section-sub">This stays in the free public site. Premium adds the deeper operating layer around it.</p>
    <div class="heatmap">
{sector_html}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="section-title">Premium Preview <span class="premium-badge">COMING JULY 1</span></h2>
    <p class="section-sub">Preview of the table shape. The live paid layer does not launch until July 1.</p>
    <div class="rank-note">
      <strong>Force rank</strong> = full-window/since-seed return. <strong>Rolling 30D</strong> = trailing 30-day return.
      <code>Family</code> = strategy category. <code>Evidence</code> = validation status.
      Free stays intentionally lighter. Premium is where the full operating detail goes.
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>#</th><th>Algorithm</th><th>Type</th>
            <th>Return</th><th>vs SPY</th><th>30D</th><th>Days</th><th>Status</th>
            <th>Family</th><th>Evidence</th>
          </tr>
        </thead>
        <tbody>
{table_rows}
        </tbody>
      </table>
    </div>
    <div style="margin-top:18px;">
      <a class="cta" href="landing.html#waitlist">Join the waitlist</a>
      <span class="cta-sub">Free launch first. Paid layer starts July 1.</span>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div><strong>crazystockalgo.com</strong> &mdash; Premium Preview &mdash; Updated nightly at 6:30 PM ET</div>
    <div>Last updated: {_e(generated_at or run_date)}</div>
    <div style="margin-top:8px;">
      <strong>Not financial advice.</strong> Experimental research only. Paper-traded signals, not real money.
      Past performance does not guarantee future results.
    </div>
    <div class="memorial">In loving memory of Biscotti (2008&ndash;2026). Good boy. Best algo. &hearts;</div>
  </div>
</footer>

</body>
</html>"""


PRICING_SECTION = """
    <div class="card" id="pricing" style="border-color: rgba(25,211,143,0.3);">
      <h2>Premium &mdash; $19.99/month</h2>
      <p>What free does not show:</p>
      <ul style="margin: 0 0 12px; padding-left: 16px; color: var(--muted); font-size: 14px; line-height: 1.8;">
        <li>Full leaderboard (all {total} algos, not just top 10)</li>
        <li>Rolling 30D column + family + evidence class per algo</li>
        <li>Sector detail per algorithm</li>
        <li>Monthly token emailed on the 1st</li>
      </ul>
      <a class="cta" href="{stripe_url}">Join the mailing list &rarr;</a>
      <div style="margin-top: 8px; font-size: 12px; color: var(--muted);">
        Subscribers get the monthly access token by email on the 1st.
      </div>
    </div>
"""

STRIPE_PAYMENT_URL = "#waitlist"


def build_main():
    daily = _load("daily.json")
    leaderboard = _load("leaderboard.json")

    out_lb = REPO / "docs" / "leaderboard.html"
    out_lb.write_text(build_leaderboard(daily, leaderboard), encoding="utf-8")
    print(f"[pages] wrote {out_lb}")

    out_landing = REPO / "docs" / "landing.html"
    out_landing.write_text(build_landing(leaderboard, daily), encoding="utf-8")
    print(f"[pages] wrote {out_landing}")

    out_premium = REPO / "docs" / "premium.html"
    out_premium.write_text(build_premium(daily, leaderboard), encoding="utf-8")
    print(f"[pages] wrote {out_premium}")


def main():
    build_main()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Build a temporary Vercel preview bundle with both public and premium/internal static content.

This is intentionally NOT the public production publisher. The output is for private
review only and may expose internal dashboards/state-like static artifacts.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = Path("/tmp/stockarithm-vercel-preview")

FILES = [
    "docs/index.html",
    "docs/landing.html",
    "docs/leaderboard.html",
    "docs/families.html",
    "docs/daily.html",
    "docs/how-it-works.html",
    "docs/premium.html",
    "docs/legal.html",
    "docs/biscotti.html",
    "docs/biscotti.jpg",
    "docs/app.html",
    "docs/nrwise.html",
    "docs/trades.json",
    "docs/signals/lookup.html",
]

DIRS = [
    "docs/blog",
    "docs/data/public",
    "docs/signals",
    "docs/leaderboards",
    "docs/quality_checks",
    "docs/algos",
    "docs/normal",
    "docs/ledgers",
    "docs/comparison",
]

IGNORE = shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc")


def copy_file(src_rel: str, out: Path) -> None:
    src = ROOT / src_rel
    if not src.exists():
        print(f"[preview] skip missing file {src_rel}")
        return
    dest = out / Path(src_rel).relative_to("docs")
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def copy_dir(src_rel: str, out: Path) -> None:
    src = ROOT / src_rel
    if not src.exists():
        print(f"[preview] skip missing dir {src_rel}")
        return
    dest = out / Path(src_rel).relative_to("docs")
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest, ignore=IGNORE)


def list_html(out: Path, prefix: str) -> list[str]:
    base = out / prefix if prefix else out
    if not base.exists():
        return []
    return sorted(str(p.relative_to(out)) for p in base.rglob("*.html"))


def write_preview_index(out: Path) -> None:
    links = [
        ("Public Home", "index.html"),
        ("Landing", "landing.html"),
        ("Leaderboard", "leaderboard.html"),
        ("Full Leaderboard (Preview Only)", "leaderboard-full.html"),
        ("Algo Index", "algos/index.html"),
        ("Families", "families.html"),
        ("Daily", "daily.html"),
        ("How It Works", "how-it-works.html"),
        ("Premium Teaser", "premium.html"),
        ("Premium App Shell", "app.html"),
        ("Legal", "legal.html"),
        ("Baseline NRWise Dashboard", "nrwise.html"),
        ("Signal Lookup", "signals/lookup.html"),
        ("Public Leaderboard JSON", "data/public/leaderboard.json"),
        ("Public Daily JSON", "data/public/daily.json"),
        ("Rolling 30D JSON", "leaderboards/rolling_30d.json"),
        ("Comparator Today JSON", "comparison/today.json"),
    ]
    sections = {
        "Algo Dashboards": list_html(out, "algos"),
        "Normal Algo Dashboards": list_html(out, "normal"),
        "Blog": list_html(out, "blog"),
        "Quality Checks": list_html(out, "quality_checks"),
    }
    body_links = "\n".join(f'<li><a href="{href}">{label}</a></li>' for label, href in links if (out / href).exists())
    section_html = []
    for title, paths in sections.items():
        if not paths:
            continue
        rows = "\n".join(f'<li><a href="{p}">{p}</a></li>' for p in paths[:250])
        section_html.append(f"<section><h2>{title}</h2><ul>{rows}</ul></section>")
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Stockarithm Preview Index</title>
<style>
body {{ margin:0; font-family: ui-sans-serif, system-ui, sans-serif; background:#0a0a0a; color:#eee; line-height:1.5; }}
header {{ padding:32px 24px; border-bottom:1px solid #333; background:#111; }}
main {{ max-width:1000px; margin:0 auto; padding:24px; }}
a {{ color:#19d38f; }}
.warning {{ border:1px solid #ef4444; background:rgba(239,68,68,.12); padding:14px; border-radius:10px; margin:18px 0; }}
section {{ border-top:1px solid #333; padding-top:18px; margin-top:24px; }}
li {{ margin:6px 0; }}
code {{ color:#facc15; }}
</style>
</head>
<body>
<header>
  <h1>Stockarithm Preview Index</h1>
  <p>Temporary private Vercel preview bundle: public + premium/internal static content.</p>
</header>
<main>
  <div class="warning"><strong>Not production:</strong> this bundle is for private review only. It may expose internal dashboards and premium-like static artifacts. Do not attach a public domain and delete when finished.</div>
  <section><h2>Main Links</h2><ul>{body_links}</ul></section>
  {''.join(section_html)}
</main>
</body>
</html>"""
    (out / "_preview_index.html").write_text(html, encoding="utf-8")


def write_vercel_config(out: Path) -> None:
    config = {
        "cleanUrls": False,
        "trailingSlash": False,
        "headers": [
            {
                "source": "/(.*)",
                "headers": [
                    {"key": "X-Robots-Tag", "value": "noindex, nofollow, noarchive"},
                    {"key": "Cache-Control", "value": "no-store"},
                ],
            }
        ],
    }
    (out / "vercel.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    (out / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")


def write_full_preview_leaderboard(out: Path) -> None:
    src = out / "leaderboard.html"
    if not src.exists():
        return
    html = src.read_text(encoding="utf-8")
    html = html.replace(" paywall-row", "")
    html = html.replace('class="paywall-row"', 'class=""')
    html = re.sub(r'<tr class="paywall-cta-row">.*?</tr>', "", html, flags=re.S)
    html = html.replace(
        "<title>StockArithm \u2014 Live Signal Leaderboard</title>",
        "<title>StockArithm \u2014 Full Preview Leaderboard</title>",
    )
    marker = '<p class="section-sub">A stripped public view of the lab. The rows below are the names that have actually moved. The zero-trade names are collapsed underneath with reasons.</p>'
    replacement = marker + '\n    <div class="rank-note"><strong>Preview-only note:</strong> This private preview page removes the public blur/paywall treatment so you can inspect the full leaderboard before launch.</div>'
    html = html.replace(marker, replacement)
    (out / "leaderboard-full.html").write_text(html, encoding="utf-8")


def write_algo_index(out: Path) -> None:
    src = ROOT / "docs" / "crazy" / "index.html"
    if not src.exists():
        return
    html = src.read_text(encoding="utf-8")
    replacements = {
        "Crazy Algos Dashboard": "Algo Dashboards",
        "Crazy Algos — Portfolio Overview": "Algo Overview — Portfolio",
        "Crazy Algos": "Algo Dashboards",
        "crazy algos": "algos",
        "active crazy algos": "active algos",
        "Idle crazy algos": "Idle algos",
        "idle crazy algos": "idle algos",
        "Lab started: 2026-01-16 · Last updated: 2026-04-28": "Lab started: 2026-01-16 · Last updated: 2026-04-28",
    }
    for old, new in replacements.items():
        html = html.replace(old, new)
    html = html.replace("/crazy/", "/algos/")
    html = html.replace("crazy/", "algos/")
    html = html.replace("crazy algos", "algos")
    (out / "algos").mkdir(parents=True, exist_ok=True)
    (out / "algos" / "index.html").write_text(html, encoding="utf-8")


def build(out: Path) -> None:
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    for rel in FILES:
        copy_file(rel, out)
    for rel in DIRS:
        copy_dir(rel, out)
    write_algo_index(out)
    write_full_preview_leaderboard(out)
    write_preview_index(out)
    write_vercel_config(out)
    total = sum(1 for p in out.rglob("*") if p.is_file())
    print(f"[preview] wrote {total} files to {out}")
    print(f"[preview] open {out / '_preview_index.html'}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build temporary Vercel preview bundle.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help=f"Output directory. Default: {DEFAULT_OUT}")
    args = parser.parse_args()
    build(Path(args.out).expanduser().resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

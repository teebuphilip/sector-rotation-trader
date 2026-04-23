#!/usr/bin/env python3
"""
Stockarithm premium API.

Small Railway/FastAPI service for Stripe-backed premium access. Designed to
work entirely in Stripe test mode first, then switch to live keys by env vars.
"""
from __future__ import annotations

import base64
import csv
import hashlib
import hmac
import io
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
from fastapi import Cookie, Depends, FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, RedirectResponse, StreamingResponse

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = Path(os.getenv("PUBLIC_ARTIFACT_DIR", ROOT / "docs" / "data" / "public"))
PRIVATE_DIR = Path(os.getenv("PRIVATE_ARTIFACT_DIR", ROOT / "private_artifacts"))
ENTITLEMENTS_PATH = Path(os.getenv("ENTITLEMENTS_PATH", ROOT / "data" / "premium" / "entitlements.json"))
PROCESSED_EVENTS_PATH = Path(os.getenv("PROCESSED_EVENTS_PATH", ROOT / "data" / "premium" / "stripe_events.json"))
SESSION_COOKIE = os.getenv("SESSION_COOKIE", "stockarithm_session")
SESSION_TTL_SECONDS = int(os.getenv("SESSION_TTL_SECONDS", str(31 * 24 * 60 * 60)))
JWT_SECRET = os.getenv("JWT_SECRET") or os.getenv("PREMIUM_JWT_SECRET") or "dev-only-change-me"
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")
APP_URL = os.getenv("APP_URL", "https://stockarithm.com/app.html")
COOKIE_DOMAIN = os.getenv("COOKIE_DOMAIN", "")
COOKIE_SECURE = os.getenv("COOKIE_SECURE", "true").lower() != "false"

app = FastAPI(title="Stockarithm Premium API", version="0.1.0")

allowed_origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "https://stockarithm.com,http://localhost:8000,http://127.0.0.1:8000").split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


def _now() -> int:
    return int(time.time())


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_json(path: Path, default: Any) -> Any:
    try:
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default
    return default


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _b64url_decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode((data + padding).encode("ascii"))


def _sign(payload: dict[str, Any]) -> str:
    header = {"alg": "HS256", "typ": "JWT"}
    head = _b64url(json.dumps(header, separators=(",", ":")).encode("utf-8"))
    body = _b64url(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
    sig = hmac.new(JWT_SECRET.encode("utf-8"), f"{head}.{body}".encode("ascii"), hashlib.sha256).digest()
    return f"{head}.{body}.{_b64url(sig)}"


def _verify(token: str) -> dict[str, Any]:
    try:
        head, body, sig = token.split(".", 2)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail="invalid_session") from exc
    expected = hmac.new(JWT_SECRET.encode("utf-8"), f"{head}.{body}".encode("ascii"), hashlib.sha256).digest()
    if not hmac.compare_digest(_b64url(expected), sig):
        raise HTTPException(status_code=401, detail="invalid_session")
    payload = json.loads(_b64url_decode(body))
    if int(payload.get("exp", 0)) < _now():
        raise HTTPException(status_code=401, detail="session_expired")
    return payload


def _entitlements() -> dict[str, Any]:
    data = _load_json(ENTITLEMENTS_PATH, {"emails": {}, "customers": {}, "updated_at": None})
    data.setdefault("emails", {})
    data.setdefault("customers", {})
    return data


def _save_entitlements(data: dict[str, Any]) -> None:
    data["updated_at"] = _now_iso()
    _write_json(ENTITLEMENTS_PATH, data)


def _set_entitlement(email: str, customer_id: str | None, subscription_id: str | None, active: bool, source: str) -> None:
    if not email:
        return
    key = email.strip().lower()
    data = _entitlements()
    record = {
        "email": key,
        "customer_id": customer_id,
        "subscription_id": subscription_id,
        "active": bool(active),
        "tier": "premium" if active else "free",
        "source": source,
        "updated_at": _now_iso(),
    }
    data["emails"][key] = record
    if customer_id:
        data["customers"][customer_id] = key
    _save_entitlements(data)


def _active_entitlement(email: str) -> dict[str, Any] | None:
    record = _entitlements().get("emails", {}).get(email.strip().lower())
    if isinstance(record, dict) and record.get("active") is True:
        return record
    return None


def _session_payload(email: str, tier: str = "premium") -> dict[str, Any]:
    return {"sub": email.strip().lower(), "email": email.strip().lower(), "tier": tier, "iat": _now(), "exp": _now() + SESSION_TTL_SECONDS}


def _set_cookie(response: Response, token: str) -> None:
    kwargs = {
        "key": SESSION_COOKIE,
        "value": token,
        "max_age": SESSION_TTL_SECONDS,
        "httponly": True,
        "secure": COOKIE_SECURE,
        "samesite": "lax",
        "path": "/",
    }
    if COOKIE_DOMAIN:
        kwargs["domain"] = COOKIE_DOMAIN
    response.set_cookie(**kwargs)


def _current_session(request: Request) -> dict[str, Any]:
    session_token = request.cookies.get(SESSION_COOKIE)
    if not session_token:
        raise HTTPException(status_code=401, detail="not_authenticated")
    payload = _verify(session_token)
    if not _active_entitlement(payload.get("email", "")):
        raise HTTPException(status_code=403, detail="not_entitled")
    return payload


def _stripe_get_session(session_id: str) -> dict[str, Any]:
    if not STRIPE_SECRET_KEY:
        raise HTTPException(status_code=500, detail="stripe_not_configured")
    response = requests.get(
        f"https://api.stripe.com/v1/checkout/sessions/{session_id}",
        auth=(STRIPE_SECRET_KEY, ""),
        timeout=20,
    )
    if response.status_code >= 400:
        raise HTTPException(status_code=400, detail="stripe_session_lookup_failed")
    return response.json()


def _verify_stripe_signature(raw: bytes, sig_header: str) -> None:
    if not STRIPE_WEBHOOK_SECRET:
        raise HTTPException(status_code=500, detail="stripe_webhook_secret_not_configured")
    parts = dict(part.split("=", 1) for part in sig_header.split(",") if "=" in part)
    timestamp = parts.get("t")
    signature = parts.get("v1")
    if not timestamp or not signature:
        raise HTTPException(status_code=400, detail="bad_stripe_signature")
    signed = timestamp.encode("utf-8") + b"." + raw
    expected = hmac.new(STRIPE_WEBHOOK_SECRET.encode("utf-8"), signed, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(expected, signature):
        raise HTTPException(status_code=400, detail="bad_stripe_signature")


def _processed_events() -> set[str]:
    data = _load_json(PROCESSED_EVENTS_PATH, {"events": []})
    return set(data.get("events", [])) if isinstance(data, dict) else set()


def _remember_event(event_id: str) -> None:
    events = sorted(_processed_events() | {event_id})[-2000:]
    _write_json(PROCESSED_EVENTS_PATH, {"updated_at": _now_iso(), "events": events})


def _email_from_checkout(session: dict[str, Any]) -> str:
    details = session.get("customer_details") if isinstance(session.get("customer_details"), dict) else {}
    return (details.get("email") or session.get("customer_email") or "").strip().lower()


def _artifact(name: str) -> Any:
    private_path = PRIVATE_DIR / name
    public_path = PUBLIC_DIR / name
    if private_path.exists():
        return _load_json(private_path, {})
    return _load_json(public_path, {})


@app.get("/health")
def health() -> dict[str, Any]:
    return {"ok": True, "service": "stockarithm-premium-api", "time": _now_iso()}


@app.get("/api/me/status")
def me(session_token: str | None = Cookie(default=None, alias=SESSION_COOKIE)) -> dict[str, Any]:
    if not session_token:
        return {"authenticated": False, "entitled": False, "tier": "free"}
    try:
        payload = _verify(session_token)
    except HTTPException:
        return {"authenticated": False, "entitled": False, "tier": "free"}
    entitled = _active_entitlement(payload.get("email", "")) is not None
    return {"authenticated": True, "entitled": entitled, "tier": "premium" if entitled else "free", "email": payload.get("email")}


@app.get("/unlock")
def unlock(session_id: str) -> Response:
    session = _stripe_get_session(session_id)
    if session.get("payment_status") not in {"paid", "no_payment_required"} and session.get("status") != "complete":
        raise HTTPException(status_code=402, detail="checkout_not_complete")
    email = _email_from_checkout(session)
    if not email:
        raise HTTPException(status_code=400, detail="checkout_email_missing")
    _set_entitlement(email, session.get("customer"), session.get("subscription"), True, "unlock")
    token = _sign(_session_payload(email))
    response = RedirectResponse(APP_URL, status_code=303)
    _set_cookie(response, token)
    return response


@app.post("/webhook")
async def stripe_webhook(request: Request) -> dict[str, Any]:
    raw = await request.body()
    _verify_stripe_signature(raw, request.headers.get("stripe-signature", ""))
    event = json.loads(raw)
    event_id = event.get("id")
    if event_id and event_id in _processed_events():
        return {"ok": True, "duplicate": True}

    event_type = event.get("type")
    obj = ((event.get("data") or {}).get("object") or {}) if isinstance(event, dict) else {}

    if event_type == "checkout.session.completed":
        email = _email_from_checkout(obj)
        _set_entitlement(email, obj.get("customer"), obj.get("subscription"), True, "stripe_checkout")
    elif event_type in {"customer.subscription.deleted", "customer.subscription.paused"}:
        customer = obj.get("customer")
        email = _entitlements().get("customers", {}).get(customer, "")
        _set_entitlement(email, customer, obj.get("id"), False, event_type)
    elif event_type in {"customer.subscription.updated", "invoice.paid"}:
        customer = obj.get("customer")
        email = _entitlements().get("customers", {}).get(customer, "")
        active = obj.get("status") in {"active", "trialing", "paid", None}
        if email:
            _set_entitlement(email, customer, obj.get("id") or obj.get("subscription"), active, event_type)

    if event_id:
        _remember_event(event_id)
    return {"ok": True, "handled": event_type}


@app.post("/logout")
def logout() -> Response:
    response = JSONResponse({"ok": True})
    response.delete_cookie(SESSION_COOKIE, path="/", domain=COOKIE_DOMAIN or None)
    return response


@app.get("/api/premium/leaderboard")
def premium_leaderboard(_: dict[str, Any] = Depends(_current_session)) -> Any:
    return _artifact("leaderboard.json")


@app.get("/api/premium/signal/{algo_id}")
def premium_signal(algo_id: str, _: dict[str, Any] = Depends(_current_session)) -> dict[str, Any]:
    leaderboard = _artifact("leaderboard.json")
    rows = leaderboard.get("algos", []) if isinstance(leaderboard, dict) else []
    row = next((r for r in rows if r.get("algo_id") == algo_id or r.get("key", "").endswith(f":{algo_id}")), None)
    if not row:
        raise HTTPException(status_code=404, detail="signal_not_found")
    algo_type = row.get("algo_type") or "crazy"
    state_dir = ROOT / "data" / str(algo_type) / "state"
    state = _load_json(state_dir / f"{algo_id}.json", {})
    return {"algo": row, "state": state, "detail_level": "premium"}


@app.get("/api/premium/ticker/{symbol}")
def premium_ticker(symbol: str, _: dict[str, Any] = Depends(_current_session)) -> dict[str, Any]:
    ticker = symbol.upper().strip()
    public = _load_json(PUBLIC_DIR / "signals" / f"{ticker}.json", {})
    full = _load_json(ROOT / "docs" / "signals" / f"{ticker}.json", public)
    if not full:
        raise HTTPException(status_code=404, detail="ticker_not_found")
    return {"ticker": ticker, "signal": full, "detail_level": "premium"}


def _csv_response(filename: str, rows: list[dict[str, Any]]) -> StreamingResponse:
    buf = io.StringIO()
    fieldnames = sorted({k for row in rows for k in row.keys()}) or ["empty"]
    writer = csv.DictWriter(buf, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
    payload = io.BytesIO(buf.getvalue().encode("utf-8"))
    return StreamingResponse(payload, media_type="text/csv", headers={"Content-Disposition": f'attachment; filename="{filename}"'})


@app.get("/api/premium/download/{kind}")
def premium_download(kind: str, _: dict[str, Any] = Depends(_current_session)) -> StreamingResponse:
    if kind == "algo_performance":
        rows = (_artifact("leaderboard.json") or {}).get("algos", [])
        return _csv_response("algo_performance.csv", rows)
    if kind == "signals_today":
        index = _load_json(PUBLIC_DIR / "signals" / "index.json", {})
        rows = index.get("signals", []) if isinstance(index, dict) else []
        return _csv_response("signals_today.csv", rows if isinstance(rows, list) else [])
    if kind == "trade_history":
        rows: list[dict[str, Any]] = []
        for algo_type in ("normal", "crazy"):
            for path in (ROOT / "data" / algo_type / "state").glob("*.json"):
                state = _load_json(path, {})
                for trade in state.get("trades", []) or state.get("trade_log", []) or []:
                    if isinstance(trade, dict):
                        rows.append({"algo_type": algo_type, "algo_id": path.stem, **trade})
        return _csv_response("trade_history.csv", rows)
    raise HTTPException(status_code=404, detail="download_not_found")

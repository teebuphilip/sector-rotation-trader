#!/usr/bin/env python3
"""
LangGraph loop:
1) Claude -> spec draft
2) ChatGPT -> spec critique
3) Claude -> spec finalize
4) Claude -> codegen (using prompts/algos_codegen_prompt.txt + scaffold)
5) ChatGPT -> code validation against spec
6) Claude -> finalize code patch

Artifacts are written to data/algos_codegen/<run_id>/.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic


def _now_id() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"[write] {path}")


def _log_cost(provider: str, model: str, usage: dict | None, out_dir: Path, state: dict | None = None) -> None:
    if not usage:
        return
    log_path = Path("logs") / "ai_costs_langgraph.csv"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    # Normalize usage fields
    in_tokens = usage.get("input_tokens") or usage.get("prompt_tokens") or 0
    out_tokens = usage.get("output_tokens") or usage.get("completion_tokens") or 0

    if provider == "openai":
        in_rate = float(os.getenv("OPENAI_INPUT_PER_MTOK", "2.50"))
        out_rate = float(os.getenv("OPENAI_OUTPUT_PER_MTOK", "10.00"))
    else:
        in_rate = float(os.getenv("ANTHROPIC_INPUT_PER_MTOK", "3.00"))
        out_rate = float(os.getenv("ANTHROPIC_OUTPUT_PER_MTOK", "15.00"))

    total = (in_tokens * in_rate + out_tokens * out_rate) / 1_000_000
    ts = datetime.utcnow()

    new_file = not log_path.exists()
    with log_path.open("a", encoding="utf-8") as f:
        if new_file:
            f.write("date,time,provider,model,input_tokens,output_tokens,cost_usd,run_id\n")
        f.write(
            f"{ts.strftime('%Y-%m-%d')},"
            f"{ts.strftime('%H:%M:%S')},"
            f"{provider},{model},{in_tokens},{out_tokens},{total:.6f},{out_dir.name}\n"
        )
    print(
        f"[cost] {provider} {model} in={in_tokens} out={out_tokens} "
        f"cost=${total:.6f} run_id={out_dir.name}"
    )
    if state is not None:
        state.setdefault("costs", {"openai": 0.0, "anthropic": 0.0, "total": 0.0})
        if provider == "openai":
            state["costs"]["openai"] += total
        else:
            state["costs"]["anthropic"] += total
        state["costs"]["total"] += total


def _extract_usage(resp) -> dict | None:
    # LangChain message objects expose usage in response_metadata or usage_metadata
    meta = getattr(resp, "response_metadata", None) or {}
    usage = meta.get("token_usage")
    if usage:
        return usage
    usage = getattr(resp, "usage_metadata", None)
    if isinstance(usage, dict):
        return usage
    return None


def _openai_model() -> str:
    return os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def _anthropic_model() -> str:
    return os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307")


def _llm_openai(max_tokens: int) -> ChatOpenAI:
    return ChatOpenAI(model=_openai_model(), temperature=0.2, max_tokens=max_tokens)


def _llm_anthropic(max_tokens: int) -> ChatAnthropic:
    return ChatAnthropic(model=_anthropic_model(), temperature=0.2, max_tokens=max_tokens)


def _save_artifact(state: Dict[str, Any], name: str, content: str) -> None:
    out_dir = Path(state["out_dir"])
    _write(out_dir / f"{name}.md", content)


def _extract_code(text: str) -> str:
    if text.lstrip().startswith("VALIDATION"):
        return ""
    if "```" not in text:
        return text.strip()
    # Prefer fenced python block, else first fenced block
    blocks = []
    parts = text.split("```")
    for i in range(1, len(parts), 2):
        header_and_body = parts[i]
        lines = header_and_body.splitlines()
        if not lines:
            continue
        lang = lines[0].strip().lower()
        body = "\n".join(lines[1:]).strip()
        blocks.append((lang, body))
    for lang, body in blocks:
        if lang in ("python", "py"):
            return body
    if blocks:
        return blocks[0][1]
    return text.strip()


def _validate_syntax(code: str, out_dir: Path) -> str | None:
    try:
        ast.parse(code)
        print("[validate] syntax OK")
        return None
    except SyntaxError as exc:
        err_path = out_dir / "syntax_error.txt"
        msg = f"{exc.__class__.__name__}: {exc} (line {exc.lineno}, col {exc.offset})"
        _write(err_path, msg)
        print(f"[validate] syntax ERROR -> {err_path}")
        return msg


def _validate_code_quality(code: str, out_dir: Path, category: str) -> list[str]:
    failures = []
    if not code.strip():
        failures.append("empty_code_output")
    if code.lstrip().startswith("VALIDATION"):
        failures.append("invalid_output_contains_validation_text")
    forbidden_snippets = [
        "NotImplementedError",
        "HOLD/{}",
        "BUY/{}",
        "SELL/{}",
        "crazy.utils.data",
        "crazy.utils.signals",
        "normal.utils.data",
        "normal.utils.signals",
        "\"CRAZY_CACHE_DIR\"",
        "'CRAZY_CACHE_DIR'",
        "requests.get(",
        "requests.post(",
        "safe_download(",
    ]

    for snippet in forbidden_snippets:
        if snippet in code:
            failures.append(f"forbidden_snippet: {snippet}")

    if category == "crazy":
        if "CrazyAlgoBase" not in code:
            failures.append("missing_base_class: CrazyAlgoBase")
        required_methods = ["def compute_signal", "def target_allocations", "def universe"]
    else:
        if "NormalAlgoBase" not in code:
            failures.append("missing_base_class: NormalAlgoBase")
        required_methods = ["def compute_target", "def universe"]

    for method in required_methods:
        if method not in code:
            failures.append(f"missing_method: {method}")


    if failures:
        err_path = out_dir / "validation_error.txt"
        _write(err_path, "\n".join(failures))
        print(f"[validate] quality ERROR -> {err_path}")
        return failures
    print("[validate] quality OK")
    return []


def _run_validations(code: str, out_dir: Path, category: str, adapters: list[str]) -> list[str]:
    errors = []
    syntax_err = _validate_syntax(code, out_dir)
    if syntax_err:
        errors.append(f"syntax: {syntax_err}")
        return errors
    quality_errs = _validate_code_quality(code, out_dir, category)
    errors.extend(quality_errs)
    adapter_registry = {
        "reddit_activity": {
            "func": "fetch_reddit_activity",
            "allowed_kwargs": {"subreddits", "days_back", "cache_key"},
        },
        "twitter_activity": {
            "func": "fetch_twitter_activity",
            "allowed_kwargs": {"query", "days_back", "cache_key"},
        },
        "weather_series": {
            "func": "fetch_weather_series",
            "allowed_kwargs": {"latitude", "longitude", "days_back"},
        },
        "earthquake_activity": {
            "func": "fetch_earthquake_activity",
            "allowed_kwargs": {"days_back"},
        },
        "google_trends": {
            "func": "fetch_google_trends",
            "allowed_kwargs": {"keyword", "days_back"},
        },
        "openchargemap": {
            "func": "fetch_openchargemap_counts",
            "allowed_kwargs": {"country_code", "max_results"},
        },
        "fred_series": {
            "func": "fetch_fred_series",
            "allowed_kwargs": {"series_id", "api_key"},
        },
        "tsa_table": {
            "func": "fetch_tsa_table",
            "allowed_kwargs": set(),
        },
        "socrata_311": {
            "func": "fetch_311_counts",
            "allowed_kwargs": {"days_back"},
        },
        "rss_count": {
            "func": "fetch_rss_counts",
            "allowed_kwargs": {"feed_urls", "days_back"},
        },
        "html_table": {
            "func": "fetch_html_table",
            "allowed_kwargs": {"url", "table_index"},
        },
        "price_only": {
            "func": "fetch_prices",
            "allowed_kwargs": {"tickers", "period"},
        },
    }
    # Enforce adapter usage
    # Forbid any cached_fetch usage when adapters are required
    if adapters and "cached_fetch(" in code:
        errors.append("forbidden_cached_fetch_with_adapters")

    # Forbid unknown adapter imports
    for line in code.splitlines():
        line = line.strip()
        if line.startswith("from crazy.adapters."):
            mod = line.split("from crazy.adapters.", 1)[1].split(" import", 1)[0].strip()
            if mod not in adapters:
                errors.append(f"forbidden_adapter_import: {line}")

    for adapter in adapters:
        info = adapter_registry.get(adapter)
        if not info:
            errors.append(f"unknown_adapter: {adapter}")
            continue
        func = info["func"]
        adapter_import = f"from crazy.adapters.{adapter} import {func}"
        adapter_call = f"{func}("
        if adapter_import not in code:
            errors.append(f"missing_adapter_import: {adapter_import}")
        # Require a direct call to the adapter function name
        if adapter_call not in code:
            errors.append(f"missing_adapter_call: {func}")
        # Enforce allowed kwargs (best-effort string scan)
        if adapter_call in code and info["allowed_kwargs"]:
            call_segment = code.split(adapter_call, 1)[1]
            call_args = call_segment.split(")", 1)[0]
            for kw in ["api_key", "data_fields", "data_quality_filters", "headers"]:
                if kw in call_args:
                    errors.append(f"forbidden_adapter_kwarg: {func}.{kw}")
            for token in call_args.split(","):
                token = token.strip()
                if "=" in token:
                    name = token.split("=", 1)[0].strip()
                    if name and name not in info["allowed_kwargs"]:
                        errors.append(f"unknown_adapter_kwarg: {func}.{name}")
        # Disallow wrapping adapter calls inside cached_fetch
        if "cached_fetch(" in code and func in code:
            errors.append(f"adapter_wrapped_in_cached_fetch: {func}")
    # Disallow registry self-registration in generated code
    if "register_algo" in code:
        errors.append("forbidden_symbol: register_algo")
    # record_blocked usage should only be for missing API keys
    for line in code.splitlines():
        if "record_blocked(" in line and "API_KEY" not in line and "api_key" not in line:
            errors.append("record_blocked_without_api_key")
    # If reddit adapter is used, enforce supports_historical_seed = False
    if "reddit_activity" in adapters and "supports_historical_seed = True" in code:
        errors.append("reddit_adapter_requires_no_historical_seed")
    # If moving average is referenced, disallow EWM
    if "moving average" in code.lower() or "ma" in code.lower():
        if ".ewm(" in code:
            errors.append("ewm_not_allowed_for_sma")

    if errors:
        err_path = out_dir / "validation_error.txt"
        _write(err_path, "\n".join(errors))
        print(f"[validate] adapter ERROR -> {err_path}")
    return errors


def _claude_fix_code(
    spec_final: str,
    code: str,
    errors: list[str],
    max_tokens: int,
    iteration: int,
    out_dir: Path,
) -> str:
    prompt = (
        "You are Claude. Fix the code to satisfy the spec and the validation errors. "
        "Output ONLY the corrected python code. No commentary, no markdown.\n\n"
        f"ITERATION: {iteration}\n\n"
        f"SPEC JSON:\n{spec_final}\n\n"
        f"VALIDATION ERRORS:\n" + "\n".join(errors) + "\n\n"
        f"CURRENT CODE:\n{code}\n"
    )
    resp = _llm_anthropic(max_tokens).invoke(prompt)
    _log_cost("anthropic", _anthropic_model(), _extract_usage(resp), out_dir)
    return resp.content


def node_claude_spec(state: Dict[str, Any]) -> Dict[str, Any]:
    print("[step] Claude spec draft")
    spec_input = state["spec_input"]
    prompt = (
        "You are Claude. Draft a complete JSON spec for the algo below. "
        "Return ONLY JSON. Keep fields precise and implementable.\n\n"
        f"SPEC INPUT:\n{spec_input}\n"
    )
    resp = _llm_anthropic(state["anthropic_max_tokens"]).invoke(prompt)
    text = resp.content
    state["spec_draft"] = text
    _save_artifact(state, "1_claude_spec_draft", text)
    _log_cost("anthropic", _anthropic_model(), _extract_usage(resp), Path(state["out_dir"]), state)
    return state


def node_chat_critique(state: Dict[str, Any]) -> Dict[str, Any]:
    print("[step] ChatGPT spec critique")
    prompt = (
        "You are ChatGPT. Critique the following algo spec JSON. "
        "Find missing thresholds, ambiguous data sources, missing edge cases. "
        "Return bullet list of fixes.\n\n"
        f"SPEC JSON:\n{state['spec_draft']}\n"
    )
    resp = _llm_openai(state["openai_max_tokens"]).invoke(prompt)
    text = resp.content
    state["spec_critique"] = text
    _save_artifact(state, "2_chat_spec_critique", text)
    _log_cost("openai", _openai_model(), _extract_usage(resp), Path(state["out_dir"]), state)
    return state


def node_claude_finalize_spec(state: Dict[str, Any]) -> Dict[str, Any]:
    print("[step] Claude spec finalize")
    prompt = (
        "You are Claude. Revise the spec JSON using the critique. "
        "Return ONLY the final JSON.\n\n"
        f"SPEC JSON:\n{state['spec_draft']}\n\n"
        f"CRITIQUE:\n{state['spec_critique']}\n"
    )
    resp = _llm_anthropic(state["anthropic_max_tokens"]).invoke(prompt)
    text = resp.content
    state["spec_final"] = text
    _save_artifact(state, "3_claude_spec_final", text)
    _log_cost("anthropic", _anthropic_model(), _extract_usage(resp), Path(state["out_dir"]), state)
    return state


def node_chat_slice_spec(state: Dict[str, Any]) -> Dict[str, Any]:
    print("[step] ChatGPT spec slice")
    prompt = (
        "You are ChatGPT. Using the taxonomy patterns provided, pick EXACTLY ONE pattern (A/B/C/D) "
        "that best fits the spec. Then produce a minimal, sliced JSON spec that includes ONLY "
        "the fields needed for that pattern and for implementation in this repo. "
        "Return ONLY JSON with keys: pattern, sliced_spec.\n\n"
        f"TAXONOMY:\n{state.get('taxonomy','')}\n\n"
        f"FULL SPEC JSON:\n{state['spec_final']}\n"
    )
    resp = _llm_openai(state["openai_max_tokens"]).invoke(prompt)
    text = resp.content
    state["spec_sliced"] = text
    _save_artifact(state, "3b_chat_spec_sliced", text)
    _log_cost("openai", _openai_model(), _extract_usage(resp), Path(state["out_dir"]), state)
    return state


def node_claude_codegen(state: Dict[str, Any]) -> Dict[str, Any]:
    print("[step] Claude codegen")
    codegen_prompt = state["codegen_prompt"]
    spec_for_codegen = state.get("spec_sliced") or state.get("spec_final") or ""
    prompt = (
        codegen_prompt
        .replace("<PASTE SPEC HERE>", spec_for_codegen)
        .replace("<SPEC_PATH>", state.get("spec_path", "unknown"))
        .replace("<CATEGORY>", state.get("category", "crazy"))
    )
    prompt += f"\n\nADAPTERS (must use all): {state.get('adapters')}\n"
    prompt += "\n\nTAXONOMY (must pick exactly one pattern and follow it):\n"
    prompt += state.get("taxonomy", "")
    prompt += "\n\nIMPORTANT: Output ONLY the final python code for the algo file. No commentary."
    resp = _llm_anthropic(state["anthropic_max_tokens"]).invoke(prompt)
    text = resp.content
    state["code_draft"] = text
    _save_artifact(state, "4_claude_codegen", text)
    _log_cost("anthropic", _anthropic_model(), _extract_usage(resp), Path(state["out_dir"]), state)
    return state


def node_chat_validate_code(state: Dict[str, Any]) -> Dict[str, Any]:
    print("[step] ChatGPT code validation")
    prompt = (
        "You are ChatGPT. Validate that the code matches the spec. "
        "Return a bullet list of mismatches or say 'OK' if none.\n\n"
        f"SPEC JSON:\n{state['spec_final']}\n\n"
        f"CODE:\n{state['code_draft']}\n"
    )
    resp = _llm_openai(state["openai_max_tokens"]).invoke(prompt)
    text = resp.content
    state["code_validation"] = text
    _save_artifact(state, "5_chat_code_validation", text)
    _log_cost("openai", _openai_model(), _extract_usage(resp), Path(state["out_dir"]), state)
    return state


def node_claude_finalize_code(state: Dict[str, Any]) -> Dict[str, Any]:
    print("[step] Claude code finalize")
    prompt = (
        "You are Claude. Apply the validation feedback and output ONLY the final python code. "
        "If validation was OK, return the same code. No commentary, no markdown.\n\n"
        f"VALIDATION:\n{state['code_validation']}\n\n"
        f"CODE:\n{state['code_draft']}\n"
    )
    resp = _llm_anthropic(state["anthropic_max_tokens"]).invoke(prompt)
    text = resp.content
    state["code_final"] = text
    _save_artifact(state, "6_claude_code_final", text)
    _log_cost("anthropic", _anthropic_model(), _extract_usage(resp), Path(state["out_dir"]), state)
    return state


def build_graph() -> StateGraph:
    g = StateGraph(dict)
    g.add_node("claude_spec", node_claude_spec)
    g.add_node("chat_critique", node_chat_critique)
    g.add_node("claude_finalize_spec", node_claude_finalize_spec)
    g.add_node("chat_slice_spec", node_chat_slice_spec)
    g.add_node("claude_codegen", node_claude_codegen)
    g.add_node("chat_validate", node_chat_validate_code)
    g.add_node("claude_finalize_code", node_claude_finalize_code)

    g.set_entry_point("claude_spec")
    g.add_edge("claude_spec", "chat_critique")
    g.add_edge("chat_critique", "claude_finalize_spec")
    g.add_edge("claude_finalize_spec", "chat_slice_spec")
    g.add_edge("chat_slice_spec", "claude_codegen")
    g.add_edge("claude_codegen", "chat_validate")
    g.add_edge("chat_validate", "claude_finalize_code")
    g.add_edge("claude_finalize_code", END)
    return g


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec-file", required=True, help="Path to spec text or JSON")
    parser.add_argument("--out-dir", default=None, help="Output directory")
    parser.add_argument("--output-path", default=None, help="Write final code to this .py file")
    parser.add_argument("--openai-max-tokens", type=int, default=None, help="Override OpenAI max tokens")
    parser.add_argument("--anthropic-max-tokens", type=int, default=None, help="Override Anthropic max tokens")
    parser.add_argument("--max-iters", type=int, default=5, help="Max fix iterations after initial run")
    args = parser.parse_args()

    spec_path = Path(args.spec_file)
    if not spec_path.exists():
        raise SystemExit(f"Spec file not found: {spec_path}")

    out_dir = Path(args.out_dir) if args.out_dir else Path("data/algos_codegen") / _now_id()
    codegen_prompt = _read_text(Path("prompts/algos_codegen_prompt.txt"))
    taxonomy_text = _read_text(Path("docs/taxonomy.md"))

    spec_path_str = str(spec_path)
    spec_path_lower = spec_path_str.lower()
    category = "crazy"
    if "/normal/" in spec_path_lower or "\\normal\\" in spec_path_lower:
        category = "normal"

    default_openai = int(os.getenv("OPENAI_MAX_TOKENS", "2000"))
    default_anthropic = int(os.getenv("ANTHROPIC_MAX_TOKENS", "4000"))
    openai_max = args.openai_max_tokens if args.openai_max_tokens is not None else default_openai
    anthropic_max = (
        args.anthropic_max_tokens if args.anthropic_max_tokens is not None else default_anthropic
    )

    # Grill spec (normalize)
    grilled_spec_path = out_dir / "grilled_spec.json"
    grill_report_path = out_dir / "grill_report.json"
    try:
        subprocess.run(
            [
                "python",
                "scripts/grill_algo_spec.py",
                "--spec-file",
                str(spec_path),
                "--out-spec",
                str(grilled_spec_path),
                "--out-report",
                str(grill_report_path),
            ],
            check=True,
        )
        spec_input_text = grilled_spec_path.read_text(encoding="utf-8")
        print(f"[grill] wrote {grilled_spec_path}")
        print(f"[grill] wrote {grill_report_path}")
        try:
            grill_report = json.loads(grill_report_path.read_text(encoding="utf-8"))
            grill_cost = float(grill_report.get("cost_usd", 0.0))
            if grill_cost:
                state_costs = {"openai": grill_cost, "anthropic": 0.0, "total": grill_cost}
                print(f"[grill][openai] cost=${grill_cost:.6f}")
                # seed costs; will be accumulated later
                initial_costs = state_costs
            else:
                initial_costs = {"openai": 0.0, "anthropic": 0.0, "total": 0.0}
        except Exception:
            initial_costs = {"openai": 0.0, "anthropic": 0.0, "total": 0.0}
    except Exception:
        spec_input_text = _read_text(spec_path)
        initial_costs = {"openai": 0.0, "anthropic": 0.0, "total": 0.0}

    # Deterministic spec completeness check
    try:
        check = subprocess.run(
            ["python", "scripts/check_algo_spec.py", "--spec", str(grilled_spec_path)],
            check=False,
            capture_output=True,
            text=True,
        )
        if check.returncode != 0:
            print("[spec] failed completeness check")
            print(check.stdout.strip())
            raise SystemExit("Spec incomplete")
        print("[spec] completeness PASS")
    except FileNotFoundError:
        pass

    # Deterministic adapter routing
    adapters = []
    try:
        result = subprocess.run(
            ["python", "scripts/adapter_router.py", "--spec-file", str(spec_path)],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.stdout:
            adapters = json.loads(result.stdout.strip()).get("adapters") or []
    except Exception:
        adapters = []

    if not adapters:
        queue_path = Path("data") / "ideas" / "adapter_queue.jsonl"
        queue_path.parent.mkdir(parents=True, exist_ok=True)
        with queue_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps({
                "date": datetime.utcnow().strftime("%Y-%m-%d"),
                "spec_file": str(spec_path),
                "reason": "no_adapter_match",
            }) + "\n")
        print("[route] no adapter match; queued for adapter build")
        raise SystemExit("No adapter match")

    # Deterministic slice
    sliced_path = out_dir / "sliced_spec.json"
    try:
        subprocess.run(
            [
                "python",
                "scripts/slice_algo_spec.py",
                "--spec",
                str(grilled_spec_path),
                "--adapters",
                ",".join(adapters),
                "--out",
                str(sliced_path),
            ],
            check=True,
        )
        spec_input_text = sliced_path.read_text(encoding="utf-8")
        print(f"[slice] wrote {sliced_path}")
    except Exception:
        pass

    state = {
        "spec_input": spec_input_text,
        "codegen_prompt": codegen_prompt,
        "taxonomy": taxonomy_text,
        "out_dir": str(out_dir),
        "openai_max_tokens": openai_max,
        "anthropic_max_tokens": anthropic_max,
        "spec_path": spec_path_str,
        "category": category,
        "costs": initial_costs,
        "adapters": adapters,
    }

    print(f"[run] spec_file={spec_path}")
    print(f"[run] out_dir={out_dir}")
    print(f"[run] openai_model={_openai_model()}")
    print(f"[run] openai_max_tokens={openai_max}")
    print(f"[run] anthropic_model={_anthropic_model()}")
    print(f"[run] anthropic_max_tokens={anthropic_max}")
    graph = build_graph().compile()
    graph.invoke(state)

    code_final = _extract_code(state.get("code_final", ""))
    _write(out_dir / "code_final.py", code_final)

    errors = _run_validations(code_final, out_dir, state.get("category", "crazy"), state.get("adapters", []))
    iteration = 1
    while errors and iteration < args.max_iters:
        print(f"[fix] iteration {iteration} errors: {len(errors)}")
        fixed = _claude_fix_code(
            spec_final=state.get("spec_final", ""),
            code=code_final,
            errors=errors,
            max_tokens=anthropic_max,
            iteration=iteration,
            out_dir=out_dir,
        )
        _write(out_dir / f"fix_{iteration}_code.md", fixed)
        code_final = _extract_code(fixed)
        _write(out_dir / f"fix_{iteration}_code.py", code_final)
        errors = _run_validations(code_final, out_dir, state.get("category", "crazy"), state.get("adapters", []))
        iteration += 1

    if errors:
        print(f"[fail] validation still failing after {args.max_iters} iterations")
        raise SystemExit("Validation failed")

    # Only write output after all validations pass
    if args.output_path:
        output_path = Path(args.output_path)
        _write(output_path, code_final)
        print(f"[output] wrote {output_path}")

    costs = state.get("costs", {})
    if costs:
        import math
        def _ceil2(x: float) -> float:
            return math.ceil(x * 100.0) / 100.0

        openai_cost = _ceil2(costs.get("openai", 0.0))
        anthropic_cost = _ceil2(costs.get("anthropic", 0.0))
        total_cost = _ceil2(costs.get("total", 0.0))
        print(
            f"[costs][openai]=${openai_cost:.2f} "
            f"[costs][anthropic]=${anthropic_cost:.2f} "
            f"[costs][total]=${total_cost:.2f}"
        )

    summary = {
        "out_dir": str(out_dir),
        "spec_file": str(spec_path),
        "openai_model": _openai_model(),
        "anthropic_model": _anthropic_model(),
        "costs": costs,
    }
    _write(out_dir / "run_summary.json", json.dumps(summary, indent=2))
    print(f"[done] LangGraph run complete: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

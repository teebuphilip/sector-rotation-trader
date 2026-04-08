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
import json
import os
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


def _openai_model() -> str:
    return os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def _anthropic_model() -> str:
    return os.getenv("ANTHROPIC_MODEL", "claude-3-haiku-20240307")


def _llm_openai() -> ChatOpenAI:
    return ChatOpenAI(model=_openai_model(), temperature=0.2)


def _llm_anthropic() -> ChatAnthropic:
    return ChatAnthropic(model=_anthropic_model(), temperature=0.2)


def _save_artifact(state: Dict[str, Any], name: str, content: str) -> None:
    out_dir = Path(state["out_dir"])
    _write(out_dir / f"{name}.md", content)


def node_claude_spec(state: Dict[str, Any]) -> Dict[str, Any]:
    spec_input = state["spec_input"]
    prompt = (
        "You are Claude. Draft a complete JSON spec for the algo below. "
        "Return ONLY JSON. Keep fields precise and implementable.\n\n"
        f"SPEC INPUT:\n{spec_input}\n"
    )
    resp = _llm_anthropic().invoke(prompt).content
    state["spec_draft"] = resp
    _save_artifact(state, "1_claude_spec_draft", resp)
    return state


def node_chat_critique(state: Dict[str, Any]) -> Dict[str, Any]:
    prompt = (
        "You are ChatGPT. Critique the following algo spec JSON. "
        "Find missing thresholds, ambiguous data sources, missing edge cases. "
        "Return bullet list of fixes.\n\n"
        f"SPEC JSON:\n{state['spec_draft']}\n"
    )
    resp = _llm_openai().invoke(prompt).content
    state["spec_critique"] = resp
    _save_artifact(state, "2_chat_spec_critique", resp)
    return state


def node_claude_finalize_spec(state: Dict[str, Any]) -> Dict[str, Any]:
    prompt = (
        "You are Claude. Revise the spec JSON using the critique. "
        "Return ONLY the final JSON.\n\n"
        f"SPEC JSON:\n{state['spec_draft']}\n\n"
        f"CRITIQUE:\n{state['spec_critique']}\n"
    )
    resp = _llm_anthropic().invoke(prompt).content
    state["spec_final"] = resp
    _save_artifact(state, "3_claude_spec_final", resp)
    return state


def node_claude_codegen(state: Dict[str, Any]) -> Dict[str, Any]:
    codegen_prompt = state["codegen_prompt"]
    prompt = codegen_prompt.replace("<PASTE SPEC HERE>", state["spec_final"])
    resp = _llm_anthropic().invoke(prompt).content
    state["code_draft"] = resp
    _save_artifact(state, "4_claude_codegen", resp)
    return state


def node_chat_validate_code(state: Dict[str, Any]) -> Dict[str, Any]:
    prompt = (
        "You are ChatGPT. Validate that the code matches the spec. "
        "Return a bullet list of mismatches or say 'OK' if none.\n\n"
        f"SPEC JSON:\n{state['spec_final']}\n\n"
        f"CODE:\n{state['code_draft']}\n"
    )
    resp = _llm_openai().invoke(prompt).content
    state["code_validation"] = resp
    _save_artifact(state, "5_chat_code_validation", resp)
    return state


def node_claude_finalize_code(state: Dict[str, Any]) -> Dict[str, Any]:
    prompt = (
        "You are Claude. Apply the validation feedback and output final code. "
        "If validation was OK, return the same code. Keep outputs minimal.\n\n"
        f"VALIDATION:\n{state['code_validation']}\n\n"
        f"CODE:\n{state['code_draft']}\n"
    )
    resp = _llm_anthropic().invoke(prompt).content
    state["code_final"] = resp
    _save_artifact(state, "6_claude_code_final", resp)
    return state


def build_graph() -> StateGraph:
    g = StateGraph(dict)
    g.add_node("claude_spec", node_claude_spec)
    g.add_node("chat_critique", node_chat_critique)
    g.add_node("claude_finalize_spec", node_claude_finalize_spec)
    g.add_node("claude_codegen", node_claude_codegen)
    g.add_node("chat_validate", node_chat_validate_code)
    g.add_node("claude_finalize_code", node_claude_finalize_code)

    g.set_entry_point("claude_spec")
    g.add_edge("claude_spec", "chat_critique")
    g.add_edge("chat_critique", "claude_finalize_spec")
    g.add_edge("claude_finalize_spec", "claude_codegen")
    g.add_edge("claude_codegen", "chat_validate")
    g.add_edge("chat_validate", "claude_finalize_code")
    g.add_edge("claude_finalize_code", END)
    return g


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec-file", required=True, help="Path to spec text or JSON")
    parser.add_argument("--out-dir", default=None, help="Output directory")
    args = parser.parse_args()

    spec_path = Path(args.spec_file)
    if not spec_path.exists():
        raise SystemExit(f"Spec file not found: {spec_path}")

    out_dir = Path(args.out_dir) if args.out_dir else Path("data/algos_codegen") / _now_id()
    codegen_prompt = _read_text(Path("prompts/algos_codegen_prompt.txt"))

    state = {
        "spec_input": _read_text(spec_path),
        "codegen_prompt": codegen_prompt,
        "out_dir": str(out_dir),
    }

    graph = build_graph().compile()
    graph.invoke(state)

    summary = {
        "out_dir": str(out_dir),
        "spec_file": str(spec_path),
        "openai_model": _openai_model(),
        "anthropic_model": _anthropic_model(),
    }
    _write(out_dir / "run_summary.json", json.dumps(summary, indent=2))
    print(f"✅ LangGraph run complete: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

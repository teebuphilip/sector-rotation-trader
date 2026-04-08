# LangGraph Algo Build Loop

This repo includes a LangGraph pipeline that implements the 6‑step Claude/ChatGPT loop:

1. Claude → spec draft  
2. ChatGPT → spec critique  
3. Claude → spec finalize  
4. Claude → codegen  
5. ChatGPT → code validation  
6. Claude → final code

The runner writes all artifacts to `data/algos_codegen/<run_id>/`.

## Run

```bash
python scripts/algos_langgraph_loop.py --spec-file path/to/spec.txt
```

### Output
Each step writes a markdown file:

- `1_claude_spec_draft.md`
- `2_chat_spec_critique.md`
- `3_claude_spec_final.md`
- `4_claude_codegen.md`
- `5_chat_code_validation.md`
- `6_claude_code_final.md`
- `run_summary.json`

## Requirements

Make sure these are installed (added to `requirements.txt`):

- `langgraph`
- `langchain-openai`
- `langchain-anthropic`

You also need:

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- optional: `OPENAI_MODEL`, `ANTHROPIC_MODEL`

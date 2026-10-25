# MASY1-GC 1800 Common Emerging Technology Agent Scaffold v1.0

## Assignment 2 final package

The completed Creation Agent and its test evidence are in [`agents/creation_agent/`](agents/creation_agent/). Start with its [agent overview](agents/creation_agent/README.md), then read the [Agent Record](agents/creation_agent/records/Assignment_2_Agent_Record_Shuoying_Wang.docx) and [source verification addendum](agents/creation_agent/records/evidence_verification.md). The final package is on `main`; the development branch preserves the testing and revision history. Run `python3 agents/creation_agent/records/verify_submission.py` from the repository root to repeat the local checks.

This is the **frozen course baseline** distributed through Brightspace for Emerging Technologies Assignments 2-8.

## What this scaffold does

It gives every specialist agent the same:
- contextual intake;
- three-level analytical rule: **ET generally -> ET for the application -> ET for that application in the organization**;
- structured output contract;
- prompt-building workflow;
- response-validation workflow.

Students specialize the files under `agents/<agent-name>/`. Files under `core/` are FROZEN CORE.

## Reference course workflow

1. Keep the original Brightspace ZIP unchanged.
2. Unzip a working copy and place it in your own GitHub repository.
3. Use ChatGPT + Codex with the weekly assignment memo to create a specialist from `agents/_template/`.
4. Run `python tools/build_prompt.py ...` to create a ChatGPT-ready prompt packet.
5. Submit that packet to ChatGPT.
6. Save ChatGPT's JSON response and run `python tools/validate_response.py ...`.
7. Test contrasting contexts, revise the specialist logic, and commit the final version.

**No OpenAI API key is required by this scaffold.** It does not call the OpenAI API. ChatGPT is the interactive model runtime; the Python tools are local prompt/validation utilities.

Start with `START_HERE.md` and the Student Operating Guide in `docs/`.

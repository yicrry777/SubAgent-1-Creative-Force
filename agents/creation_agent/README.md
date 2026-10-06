# Assignment 2 Creation Agent

Student: Shuoying Wang. Agent version: `0.2-student`.

This specialist interprets the creation and evolution of LLM-based agentic AI for a mid-sized retailer's shopping assistant, contrasted with procurement assistance in a large hospital network. It preserves the course's three-level analysis and frozen contracts.

## Submission entry points

- [Word Agent Record](records/Assignment_2_Agent_Record_Shuoying_Wang.docx) and [Markdown record](records/agent_record.md): concise A-E record using the course template fields.
- [Evidence verification](records/evidence_verification.md): seven principal sources, audit of other v2 citations, and qualifications that must accompany the archived outputs.
- [Final test review](records/final_test_review.md): observed v1/v2 differences, actual revision history and remaining limitations.
- [Validation report](records/validation_report.txt): executed checks and artifact fingerprints.
- [Submission guide](records/submission_checklist.md): file map, version evidence and final review items.

`responses/*_v2.json` are the original saved test outputs, not silently corrected copies. The source addendum records qualifications without concealing weaknesses. `records/prompts/` contains packets rebuilt at closeout, not historical run transcripts. The unused `cases/contrast_2.json` starter is not a completed test.

From the repository root, reproduce the read-only checks with:

```bash
python agents/creation_agent/records/verify_submission.py
```

The original student-editable instructions and agent metadata remain at the version actually tested. No frozen file, baseline manifest, case input or original response is changed during closeout.

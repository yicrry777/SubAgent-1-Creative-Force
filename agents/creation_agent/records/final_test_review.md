# Final test review

Reviewed 2026-10-06. Agent `0.2-student`; existing run snapshot `ad5040fcca3ec15ad23d210bc2066863180952cc`. This review compares saved outputs; no new ChatGPT model execution is claimed.

## Cases and observed results

| Item | Primary | Contrast 1 |
| --- | --- | --- |
| ET held constant | LLM-based agentic AI systems | LLM-based agentic AI systems |
| Application | Shopping discovery, comparison and cart preparation | Medical-supply procurement assistance and draft orders |
| Organization and posture | Mid-sized U.S. DTC retailer; moderate/fast-follower | Large U.S. hospital network; conservative/risk-averse |
| Decision horizon | Pilot decision within 12 months | Evaluation/limited pilot consideration within 18-24 months |
| Material consequence | Customer trust, incorrect commercial facts, unintended purchase | Supply disruption, inappropriate substitution, unauthorized procurement |
| v2 observation | Bounded shopping pilot, authoritative catalog/commerce data, human purchase authorization | Read-mostly approved-source retrieval, traceable drafts, no independent order submission |

Both cases already require human purchasing approval. The contrast is therefore **not** that one allows autonomous purchasing while the other forbids it. The meaningful changes are approved-source restrictions, narrower state changes, traceability, and a more cautious evaluation posture. Multiple context variables change together, so this is a qualitative sensitivity test, not a causal experiment isolating one variable. `contrast_2.json` is an unused starter and is not counted as a third test.

## Stable and changed conclusions

**Appropriately stable:** each v2 `general_et_finding` describes convergence of Transformer-based models, general task capability, reasoning/action patterns and software tool interfaces. Neither case claims that a hospital's risk posture changes the technical chronology. Coverage differs: contrast explicitly mentions instruction tuning/RLHF; primary emphasizes later tooling. This is an omission to address in the shared synthesis, not a contradictory chronology.

**Appropriately changed:** compare each v2 `organization_specific_finding` and `recommendation_management_implication`. Primary permits reversible cart preparation alongside discovery. Contrast centers approved procurement information, reviewable purchase-order drafts and no autonomous submission. Both reserve consequential authority for humans and decline broad ROI/readiness judgments.

## Weakness, revision and observed improvement

| Criterion | v1 observation | Actual revision | v2 observation and judgment |
| --- | --- | --- | --- |
| Non-technical enabling conditions | Primary `evidence` focuses on technical predecessors and tooling. Contrast notes commercial interfaces but has no developed economic/access condition. | `specialist_instructions.md` requires a supported broader condition or an explicit evidence gap. | Contrast #3/#7 introduces API commercialization and lower prices; primary #10 adds market background. Improvement is visible, but primary's late market statistic is weaker evidence of emergence. **Partial substantive success.** |
| Evidence versus causality | v1 contrast already labels the lineage a synthesis; the weakness was uneven application, not total absence of caution. | Added a rule against inferring economic/social causes solely from chronology. | Primary #10 and contrast #3/#7 distinguish observed facts from causal inference. **Improved explicitness in these samples.** Relative causal importance remains unproved. |
| Reusable citation hygiene | Initial contrast at `b80d5bc` contains an internal file-citation marker in `analytical_question`. | Added a no-internal-markers rule; commit `35a00a2` also removed the marker from the saved v1 contrast. | Current four responses contain no internal markers. **Observed improvement**, but v1 contrast was manually cleaned, so it is not a wholly untouched raw artifact. The original is recoverable in Git. |
| Scope and context sensitivity | v1 already distinguishes shopping from hospital procurement and retains human approval. | Preserved specialist scope and the common schema. | v2 preserves those strengths. **No detected regression**, based on two saved contexts only. |
| Citation truth and freshness | Structural validation cannot establish factual accuracy or temporal suitability. | Closeout audit checks original sources and records qualifications. The tested instructions remain version 0.2. | Census figures need a stale-estimate qualification; API launch was private beta; one NIST date span is too broad. See `evidence_verification.md`. **External review still necessary.** |

The previous short retest statement in `initial_test_review.md` should be read with this more precise assessment. There is no evidence of repeated trials, blinded scoring or isolated revision effects. Changed source selection and model variability could also contribute to differences.

## Actual Git history

Commit contents, rather than their titles alone, establish the sequence:

| Commit | Observed contents |
| --- | --- |
| `1301f07` | Creation Agent baseline. |
| `7c502c8` | Initial primary response. |
| `b80d5bc` | Adds initial contrast response, despite a message mentioning revision. |
| `35a00a2` | Updates metadata to 0.2, revises instructions, adds initial review and primary v2, and cleans the v1 contrast marker. There is no separate instructions-only revision commit. |
| `ad5040f` | Adds contrast v2 and a brief retest conclusion. |

The closeout preserves all files present at `ad5040f` except student-editable documentation. Prompt packets rebuilt during closeout are reproducibility aids, **not recovered historical run transcripts**. The original model identifier, settings, exact execution timestamps and chat transcripts are not present; commit times establish repository history only.

## Verification scope

`validation_report.txt` records the actual frozen-core check, four course-validator runs, field checks, rebuilt prompt checks, and comparison with the initial scaffold commit. Structural checks are separate from this semantic/source review. No package installation or API key is required. The seven manifest-listed files, including the four tools, are protected; the manifest itself is compared with the scaffold commit to avoid accepting a changed baseline.

The repository Student Guide and Word template were inspected. The separate Assignment 2 memo and original Brightspace ZIP are not in this checkout or the referenced chat's accessible attachments; compliance with any additional memo-specific rule or the untouched original ZIP cannot be independently established here.

## Independent judgment for review

The agent is credible enough for team consideration as a bounded creation/evolution specialist when accompanied by the source audit. It relates historical capabilities to two different contexts and explicitly limits its authority. Its most important remaining limitation is evidence discipline: fluent, structurally valid responses can still use weak causal evidence or imprecise recency metadata. The student should review and adopt or amend this drafted judgment before submitting it as their own.

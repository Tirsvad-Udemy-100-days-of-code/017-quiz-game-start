# Review Record: BC-001 Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-001 |
| CrossReference | [BC-001], [QC-BC-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [BC-001]
- Checklist used: [QC-BC-001] (`QC-BC-001`) and, because the type is written in the PO language, [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (S01 reads the language and knows the domain)
- Reviewer: S01. The checklist was applied by an AI assistant at S01's request; S01 gave the verdict in chat on 2026-10-07.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | ROI/Cost-Benefit analysis is quantitative, or where qualitative, is explicitly justified | Pass | Cost-Benefit Assessment states that a monetary return is not meaningful (personal learning project, no budget, no revenue) and gives a qualitative Costs/Benefits table. |
| 2 | Risks are identified with documented impact and mitigation | Pass | Risks table has 7 risks; every row has an Impact and a Mitigation. |
| 3 | Success criteria are measurable, stating explicit targets rather than vague aspirations | Pass | Success Criteria has 9 rows, each with a Target and a Measure (for example 2: `12 Question objects`, measured by a test; 5: `0 findings` from three tools). |
| 4 | Scope explicitly separates In Scope vs Out of Scope | Pass | Scope has the subsections `### In Scope` and `### Out of Scope`. |
| 5 | Stakeholders are cross-referenced to Stakeholder Analysis IDs rather than re-described inline | Pass | The Stakeholders table cites S01, S02 and S03 with a link to SA-001; roles are not re-described. Elsewhere the text names `Product Owner (S01)` only with the ID. |
| 6 | Methodology and quality-standard foundation are stated explicitly (e.g. ISO/IEC 25010, Larman) | Pass | Methodological and Standards Foundation names Larman, ISO/IEC 25010:2023, PEP 8, 257 and 484, Doxygen and the QC checklists. |
| 7 | Assumptions and constraints are explicit and clearly distinguished from one another | Pass | Assumptions and Constraints are separate sections; the constraints (tooling, layout, licence, no commit until asked, plan-first) are requirements, the assumptions are things taken to be true. |
| 8 | Document supports executive decision-making with a clear, unambiguous recommendation | Pass | Recommendation is `Proceed` with a one-sentence rationale. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table has `Language` = `en` and `Domain` = `it`; neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is a value of the registry's domain list (Software and IT). |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Prose and table cells are English. Code identifiers, file names and tool names stay as written, which the criterion allows. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives IT Executive English for this type; the prose is written for that reader. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No domain dictionary (`DICT`) exists for this project (the type is optional), so there are no dictionary terms to contradict. Checked by search instead: the documents use one word per concept (gateway = reviewed checkpoint, lecture part = course unit, player = the person answering the quiz). Uses of `step` in the sense of `gateway` or `lecture part` were replaced in this review; `step by step` remains as an idiom. `user` appears only in the standard terms `user interface` and `user stories`, never for the player. Re-check if a `DICT` is created. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are English; the scripts `find-crossreferences.sh`, `check-languages.sh` and `sync-project.sh` read them without a finding. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | `docs/` holds no `<name>.<language>.md` twin of any document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version of the document; there is no earlier accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 reads English and works in the software and IT domain (S01 is the developer and Product Owner); S01's Go in chat on 2026-10-07 confirms it. No language reviewer is needed. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Spelled out on first use: SQA, QC, PEP, API, CI and AGPL (fixed in this review; before the fix none of them was defined). |

## Overall Verdict

Go — every mandatory criterion of the type's checklist and of QC-LANG-001 passes (7 mandatory criteria of the type; criterion 8 of QC-LANG-001 is not applicable to a first version). Defects found and fixed during the review: (1) the Assumptions said the framework allows S01 to review everything, which is not what the process says; it now states the real situation and points to the open issue in PP-001; (2) abbreviations SQA, QC, PEP, API, CI and AGPL were not spelled out; (3) `step` was used for both gateway and lecture part. S01 gave Go in chat on 2026-10-07; the latest Version History row of BC-001 becomes Accepted.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | n/a | n/a |

---

[BC-001]: ../../business-case.md
[QC-BC-001]: ../../../framework/qc/qc-business-case.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md

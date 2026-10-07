# Traceability Matrix: Quiz Game

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Added the row for the Python code of MIL-002 and RC-011<br>Coverage notes: source code now has rows | [8142317] |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Added the row for the Python code of MIL-003 and RC-012 | [1cda99a] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | it | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | Project Plan | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-003] |
| [MIL-001] | Milestone / Gateway | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-004] |
| [MIL-002] | Milestone / Gateway | en | it | [BC-001], [MIL-001] | [MIL-003] | [RC-005] |
| [MIL-003] | Milestone / Gateway | en | it | [BC-001], [MIL-002] | [MIL-004] | [RC-006] |
| [MIL-004] | Milestone / Gateway | en | it | [BC-001], [MIL-003] | [MIL-005] | [RC-007] |
| [MIL-005] | Milestone / Gateway | en | it | [BC-001], [MIL-004] | [MIL-006] | [RC-008] |
| [MIL-006] | Milestone / Gateway | en | it | [BC-001], [MIL-005] | - | [RC-009] |
| Python code of MIL-001 (`src/constants.py`, `tests/test_data.py`) | Python Source Code (PY) | - | - | [MIL-001] | - | [RC-010] |
| Python code of MIL-002 (`src/question_model.py`, `tests/test_question_model.py`) | Python Source Code (PY) | - | - | [MIL-002] | - | [RC-011] |
| Python code of MIL-003 (`src/main.py`, `src/constants.py`, `tests/test_main.py`) | Python Source Code (PY) | - | - | [MIL-003] | - | [RC-012] |

## Coverage Notes

- In Upstream, `-` means foundational (the Business Case has no prerequisite artifact). In Downstream, `-` means nothing is built on the instance yet; the code rows get a downstream link when a later gateway builds on them. In Last Reviewed, `-` would mean no review record exists; every row above has one.
- Types with no instance in this project yet: KPI, RA, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD, ERD, ADR, DICT, GOV. Use cases and user stories are not planned (Project Plan, open issues). The source-code type PY has one row per gateway, added when the gateway's code is reviewed (MIL-001 to MIL-003 so far).
- Review records RC-001 to RC-012 and this matrix have no QC checklist and are not reviewed.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-foundation.md
[MIL-002]: ../milestones/mil-002-question-class.md
[MIL-003]: ../milestones/mil-003-question-bank.md
[MIL-004]: ../milestones/mil-004-next-question.md
[MIL-005]: ../milestones/mil-005-quiz-loop.md
[MIL-006]: ../milestones/mil-006-answers-and-score.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-mil-004.md
[RC-008]: ./reviews/rc-008-mil-005.md
[RC-009]: ./reviews/rc-009-mil-006.md
[RC-010]: ./reviews/rc-010-python-mil-001.md
[RC-011]: ./reviews/rc-011-python-mil-002.md
[RC-012]: ./reviews/rc-012-python-mil-003.md
[8142317]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/814231725751cc702f911f939b6427268d7a8b85
[1cda99a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/1cda99ac623671380ee5bfae483f3468bd1b1241

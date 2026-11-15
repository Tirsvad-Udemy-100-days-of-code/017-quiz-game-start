# Traceability Matrix: Quiz Game

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Added the row for the Python code of MIL-005 and RC-014 | [831c2be] |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Added the row for the Python code of MIL-006 and RC-015 | [a1b8c74] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Accepted; added MIL-007, the wiki, the concern coverage and the new review records RC-016 to RC-025; set the domain to education; reviewed in autonomous mode, not independent | [cd6c05d] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007] | [RC-016] |
| [SA-001] | Stakeholder Analysis | en | education | [BC-001] | [PP-001] | [RC-017] |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007] | [RC-018] |
| [MIL-001] | Milestone / Gateway | en | education | [BC-001], [PP-001] | [MIL-002] | [RC-019] |
| [MIL-002] | Milestone / Gateway | en | education | [BC-001], [MIL-001] | [MIL-003] | [RC-020] |
| [MIL-003] | Milestone / Gateway | en | education | [BC-001], [MIL-002] | [MIL-004] | [RC-021] |
| [MIL-004] | Milestone / Gateway | en | education | [BC-001], [MIL-003] | [MIL-005] | [RC-022] |
| [MIL-005] | Milestone / Gateway | en | education | [BC-001], [MIL-004] | [MIL-006] | [RC-023] |
| [MIL-006] | Milestone / Gateway | en | education | [BC-001], [MIL-005] | [MIL-007] | [RC-024] |
| [MIL-007] | Milestone / Gateway | en | education | [BC-001], [PP-001], [MIL-006] | - | [RC-025] |
| Wiki | Wiki | en, da, ms | education | [BC-001] | - | [RC-026] |
| Python code of MIL-001 (`src/constants.py`, `tests/test_data.py`) | Python Source Code (PY) | - | - | [MIL-001] | - | [RC-010] |
| Python code of MIL-002 (`src/question_model.py`, `tests/test_question_model.py`) | Python Source Code (PY) | - | - | [MIL-002] | - | [RC-011] |
| Python code of MIL-003 (`src/main.py`, `src/constants.py`, `tests/test_main.py`) | Python Source Code (PY) | - | - | [MIL-003] | - | [RC-012] |
| Python code of MIL-004 (`src/quiz_brain.py`, `src/main.py`, `src/constants.py`, `tests/test_quiz_brain.py`, `tests/test_main.py`, `tests/fakes.py`, `tests/conftest.py`) | Python Source Code (PY) | - | - | [MIL-004] | - | [RC-013] |
| Python code of MIL-005 (`src/quiz_brain.py`, `src/main.py`, `tests/test_quiz_brain.py`, `tests/test_main.py`) | Python Source Code (PY) | - | - | [MIL-005] | - | [RC-014] |
| Python code of MIL-006 (`src/quiz_brain.py`, `src/main.py`, `src/constants.py`, `src/data.py`, `tests/conftest.py`, `tests/test_quiz_brain.py`, `tests/test_main.py`) | Python Source Code (PY) | - | - | [MIL-006] | - | [RC-015] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] to [MIL-006] (the criteria on the classes and the quiz) | - | - | Covered |
| CN-002 | [PP-001] (every gateway ends in a pull request), [MIL-007] (criterion 6) | - | - | Covered |
| CN-003 | [MIL-001] (criteria 2 to 6) | - | - | Covered |
| CN-004 | [MIL-006] (criterion 9), [MIL-007] (criterion 3) | - | - | Covered |
| CN-005 | [MIL-001] (criterion 7), [MIL-006] (criterion 9), [MIL-007] (criterion 3) | - | - | Covered |
| CN-006 | [MIL-001] (criterion 9), [MIL-007] (criterion 3) | - | - | Covered |
| CN-007 | [MIL-001] (criterion 2), [MIL-006] (criterion 10) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

- In Upstream, `-` means foundational (the Business Case has no prerequisite artifact). In Downstream, `-` means nothing is built on the instance yet; the code rows get a downstream link when a later gateway builds on them. In Last Reviewed, `-` would mean no review record exists; every row above has one.
- Types with no instance in this project yet: KPI, RA, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD, ERD, ADR, DICT, GOV. Use cases and user stories are not planned (Project Plan, open issues). The source-code type PY has one row per gateway, added when the gateway's code is reviewed (MIL-001 to MIL-006, one row each).
- Review records RC-001 to RC-015 and this matrix have no QC checklist and are not reviewed. The source code is reviewed in RC-010 to RC-015 and not again in MIL-007.
- The domain of every artifact is `education` since MIL-007; the earlier review records [RC-001] to [RC-009] state the former domain `it` as it was at the time.

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
[RC-013]: ./reviews/rc-013-python-mil-004.md
[RC-014]: ./reviews/rc-014-python-mil-005.md
[RC-015]: ./reviews/rc-015-python-mil-006.md
[831c2be]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/831c2be1f79814229e65f480cfef0b7fed69ba02
[a1b8c74]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/a1b8c7459071a25955e1b4eb27329604bd22968f
[MIL-007]: ../milestones/mil-007-framework-baseline.md
[RC-016]: ./reviews/rc-016-business-case.md
[RC-017]: ./reviews/rc-017-stakeholder-analysis.md
[RC-018]: ./reviews/rc-018-project-plan.md
[RC-019]: ./reviews/rc-019-milestone-001.md
[RC-020]: ./reviews/rc-020-milestone-002.md
[RC-021]: ./reviews/rc-021-milestone-003.md
[RC-022]: ./reviews/rc-022-milestone-004.md
[RC-023]: ./reviews/rc-023-milestone-005.md
[RC-024]: ./reviews/rc-024-milestone-006.md
[RC-025]: ./reviews/rc-025-milestone-007.md
[RC-026]: ./reviews/rc-026-wiki.md
[cd6c05d]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/cd6c05d5cbff83ca2e39e22ee73f4b80d20fc103

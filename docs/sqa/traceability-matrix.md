# Traceability Matrix: Quiz Game

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [ab361ed] |

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

## Coverage Notes

- In Upstream, `-` means foundational (the Business Case has no prerequisite artifact). In Downstream, `-` means nothing is built on the instance yet; the milestones' tasks are not yet code, so G1 to G6 are the first downstream work. In Last Reviewed, `-` would mean no review record exists; every row above has one.
- Types with no instance in this project yet: KPI, RA, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD, ERD, ADR, DICT, GOV, and the source-code type PY. Use cases and user stories are not planned (Project Plan, open issues); `PY` starts with MIL-001.
- Review records RC-001 to RC-009 and this matrix have no QC checklist and are not reviewed.

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
[ab361ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/ab361edf622585f77249d7782a9e2619f7d85cfc

# MIL-002 G2 Question class

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the model of one quiz question, the `Question` class of lecture part 1, is complete, tested and documented, so the question bank can be built from it.

## Deliverable

One branch (`mil-002-question-class`) and one pull request containing the `Question` class in `src/question_model.py`, with a text attribute and an answer attribute set when an object is created, its Doxygen comments and its tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A `Question` created with a text and an answer exposes both as the attributes `text` and `answer` | A test shows this and passes | The attributes are missing, renamed or not tested |
| 2 | `Question` and its initialiser have Doxygen comments and type annotations | `doxygen Doxyfile` exits 0 with 0 warnings; `mypy --strict` has 0 findings | A warning or a finding |
| 3 | `pytest` | Exit code 0, no failures | A failure or error |
| 4 | `ruff check` and `ruff format --check` | 0 findings | Any finding |
| 5 | `pyproject.toml` | Lists no runtime dependency | A runtime dependency is listed |
| 6 | The pull request's code review against the Python quality checklist `QC-PY-001` is recorded | A review record (`RC-*`) with verdict `Go` | No record, `Go-with-conditions` or `No-Go` |
| 7 | Every task of this gateway is a closed issue and the pull request description has one `Closes #N` line per task | All closed and listed | Any open or unlisted |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The starter files, the tooling and the test set-up come from G1 |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 Quiz built from the assignment's classes | [BC-001] |
| O5 One gateway, one branch, one pull request | [BC-001] |
| Success criterion 1 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-12 — inside the 2026-10-21 target in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the Question class | In `src/question_model.py` define the class `Question`. Its initialiser takes the question text and the correct answer and stores them as the attributes `text` and `answer` (lecture part 1). Annotate the signature and add Doxygen comments. | No | |
| 2 | Test the Question class | Add `tests/test_question_model.py`: a `Question` created with a text and an answer returns the same values from `text` and `answer`, and two objects keep their own values. Tests are named `test_<behaviour>_<condition>`. | No | |

---

[BC-001]: ../business-case.md

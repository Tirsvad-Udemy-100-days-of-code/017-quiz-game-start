# MIL-003 G3 Question bank

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [ab361ed] |

---

## Purpose

Decide whether the question bank of lecture part 2 is complete: the raw dictionaries in `question_data` are turned into a list of `Question` objects that the quiz can use.

## Deliverable

One branch (`mil-003-question-bank`) and one pull request containing `src/main.py` with a function that builds the question bank from `question_data` and a `main()` entry point that creates it, plus the tests of the bank.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The question bank built from the course's `question_data` has 12 `Question` objects in the order of the data, each with the text and answer of its dictionary | A test shows this and passes | A different count, order or content |
| 2 | An empty `question_data` gives an empty bank | A test shows this and passes | An error or a non-empty bank |
| 3 | Importing `main` does not start the quiz or ask for input | A test imports it without scripted input and passes | The import blocks or prints |
| 4 | The dictionary keys come from `constants.py`, not from literals in `main.py` | No `"text"` or `"answer"` literal in `main.py` | A literal is found |
| 5 | `pytest` | Exit code 0, no failures | A failure or error |
| 6 | `ruff check`, `ruff format --check` and `mypy --strict src tests` | 0 findings | Any finding |
| 7 | `doxygen Doxyfile` | Exit code 0, 0 warnings | Any warning |
| 8 | `pyproject.toml` | Lists no runtime dependency | A runtime dependency is listed |
| 9 | The pull request's code review against the Python quality checklist `QC-PY-001` is recorded | A review record (`RC-*`) with verdict `Go` | No record, `Go-with-conditions` or `No-Go` |
| 10 | Every task of this gateway is a closed issue and the pull request description has one `Closes #N` line per task | All closed and listed | Any open or unlisted |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | The bank is a list of `Question` objects |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 Quiz built from the assignment's classes and question bank | [BC-001] |
| O5 One gateway, one branch, one pull request | [BC-001] |
| Success criterion 2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — inside the 2026-10-21 target in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add build_question_bank to main.py | In `src/main.py` import `Question` and `question_data`, and add `build_question_bank()`: loop over the dictionaries, read the text and the answer with the keys from `constants.py`, create a `Question` and append it to a list that the function returns (lecture part 2). The lecture does this inline at module level; a function lets tests import `main.py` without running the quiz. | No | |
| 2 | Add the main entry point | Add `main()` that creates `question_bank` from `question_data`, and call it only under `if __name__ == "__main__":`, so `python src/main.py` still works and importing `main` has no side effect. | No | |
| 3 | Test the question bank | Add `tests/test_main.py`: the bank built from the course data has 12 `Question` objects in the data's order with matching text and answer, an empty data list gives an empty bank, and importing `main` has no side effect. | No | |

---

[BC-001]: ../business-case.md
[ab361ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/ab361edf622585f77249d7782a9e2619f7d85cfc

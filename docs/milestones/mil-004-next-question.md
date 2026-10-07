# MIL-004 G4 Next question

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [ab361ed] |

---

## Purpose

Decide whether the `QuizBrain` class of lecture part 3 can show the current question and ask for an answer, while keeping track of where in the quiz the player is.

## Deliverable

One branch (`mil-004-next-question`) and one pull request containing the `QuizBrain` class in `src/quiz_brain.py` (attributes `question_number` and `question_list`, method `next_question`), the prompt text in `constants.py`, `main()` creating the quiz and asking the first question, and the tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A new `QuizBrain` has `question_number` equal to 0 and `question_list` equal to the list it was given | A test shows this and passes | A different start value or list |
| 2 | `next_question` asks for an answer with the question number and the question text, and asks for `True` or `False` | A test with scripted input checks the prompt and passes | A different prompt |
| 3 | After `next_question`, `question_number` has increased by 1 and the prompt used the number of the question being asked (first prompt is question 1) | A test shows this and passes | The number is off by one |
| 4 | The prompt format comes from `constants.py` | No prompt literal in `quiz_brain.py` | A literal is found |
| 5 | `pytest` | Exit code 0, no failures | A failure or error |
| 6 | `ruff check`, `ruff format --check` and `mypy --strict src tests` | 0 findings | Any finding |
| 7 | `doxygen Doxyfile` | Exit code 0, 0 warnings | Any warning |
| 8 | `pyproject.toml` | Lists no runtime dependency | A runtime dependency is listed |
| 9 | The pull request's code review against the Python quality checklist `QC-PY-001` is recorded | A review record (`RC-*`) with verdict `Go` | No record, `Go-with-conditions` or `No-Go` |
| 10 | Every task of this gateway is a closed issue and the pull request description has one `Closes #N` line per task | All closed and listed | Any open or unlisted |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | `QuizBrain` is created from the question bank |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 Quiz built from the assignment's classes and methods | [BC-001] |
| O5 One gateway, one branch, one pull request | [BC-001] |
| Success criterion 3 (first part) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-16 — inside the 2026-10-21 target in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement the QuizBrain initialiser | In `src/quiz_brain.py` define the class `QuizBrain`. Its initialiser takes the list of questions and sets `question_number` to 0 and `question_list` to that list (lecture part 3). Annotate the signature and add Doxygen comments. | No | |
| 2 | Implement next_question | Add `next_question`: take the question at `question_number`, increase the number so that it matches the question being asked, and ask the player with `input`, showing the number and the text and asking for `True` or `False`. The prompt format is a constant in `constants.py`. | No | |
| 3 | Ask the first question from main | In `main()` create `QuizBrain` from the question bank and call `next_question` once, as in the lecture. G5 replaces this single call with the loop. | No | |
| 4 | Test QuizBrain | Add `tests/test_quiz_brain.py`: the start state, the prompt text and the increase of the question number, using pytest's `monkeypatch` to script `input`. | No | |

---

[BC-001]: ../business-case.md
[ab361ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/ab361edf622585f77249d7782a9e2619f7d85cfc

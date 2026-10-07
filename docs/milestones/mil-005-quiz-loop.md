# MIL-005 G5 Quiz loop

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [ab361ed] |

---

## Purpose

Decide whether the quiz of lecture part 4 keeps asking questions until all have been asked, so that the program no longer stops after the first question.

## Deliverable

One branch (`mil-005-quiz-loop`) and one pull request containing `still_has_questions` in `src/quiz_brain.py`, the `while` loop in `main()` that asks every question, and the tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `still_has_questions` is true while `question_number` is below the number of questions and false from then on | Tests for an empty list, the first, the last and the question after the last pass | Any case differs |
| 2 | The method returns the comparison directly, without a separate `if` and `return True` or `return False` | Code review finds none | An `if` branch is found |
| 3 | The loop in `main()` asks exactly as many questions as the bank holds | A test with 12 scripted answers counts 12 prompts and passes | A different count |
| 4 | `pytest` | Exit code 0, no failures | A failure or error |
| 5 | `ruff check`, `ruff format --check` and `mypy --strict src tests` | 0 findings | Any finding |
| 6 | `doxygen Doxyfile` | Exit code 0, 0 warnings | Any warning |
| 7 | `pyproject.toml` | Lists no runtime dependency | A runtime dependency is listed |
| 8 | The pull request's code review against the Python quality checklist `QC-PY-001` is recorded | A review record (`RC-*`) with verdict `Go` | No record, `Go-with-conditions` or `No-Go` |
| 9 | Every task of this gateway is a closed issue and the pull request description has one `Closes #N` line per task | All closed and listed | Any open or unlisted |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-004 | The loop calls `next_question` of `QuizBrain` |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 Quiz built from the assignment's classes and methods | [BC-001] |
| O5 One gateway, one branch, one pull request | [BC-001] |
| Success criterion 3 (second part) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-18 — inside the 2026-10-21 target in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement still_has_questions | Add `still_has_questions` to `QuizBrain`: it answers whether `question_number` is still below the length of `question_list`, returning the comparison directly (lecture part 4). Annotate and add Doxygen comments. | No | |
| 2 | Loop over the questions in main | Replace the single `next_question` call in `main()` with `while quiz.still_has_questions(): quiz.next_question()` so every question is asked. | No | |
| 3 | Test the quiz loop | Extend `tests/test_quiz_brain.py` and `tests/test_main.py`: `still_has_questions` for an empty list, the first, the last and the question after the last; and the loop asks exactly 12 questions when 12 answers are scripted. | No | |

---

[BC-001]: ../business-case.md
[ab361ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/ab361edf622585f77249d7782a9e2619f7d85cfc

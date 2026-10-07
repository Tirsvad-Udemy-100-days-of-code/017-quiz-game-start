# MIL-006 G6 Answers and score

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [ab361ed] |

---

## Purpose

Decide whether the quiz of lecture part 5 is complete: every answer is checked, the player sees whether it was right, the running score and the final score, and the repository is ready to be shared.

## Deliverable

One branch (`mil-006-answers-and-score`) and one pull request containing the `score` attribute and `check_answer` in `src/quiz_brain.py`, the feedback texts in `constants.py`, the final result in `main()`, the tests, and the final check of the README against a clean `.venv`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `check_answer` accepts the player's answer in any letter case and counts it right when it equals the correct answer ignoring case | Tests for `true`, `TRUE`, `False` and a wrong answer pass | A case is handled differently |
| 2 | A right answer adds 1 to `score`; a wrong answer leaves it unchanged; any other text counts as wrong | Tests pass | The score differs |
| 3 | After each answer the player sees whether it was right, the correct answer and the running score as `<score>/<questions answered>`, and a blank line separates questions | A test of the captured output passes | A part is missing |
| 4 | When the quiz ends the player sees a completion message and the final score as `<score>/<number of questions>` | An end-to-end test with 12 scripted answers passes | The message or the score differs |
| 5 | The feedback texts come from `constants.py` | No feedback literal in `quiz_brain.py` or `main.py` | A literal is found |
| 6 | `pytest` | Exit code 0, no failures | A failure or error |
| 7 | `ruff check`, `ruff format --check` and `mypy --strict src tests` | 0 findings | Any finding |
| 8 | `doxygen Doxyfile` | Exit code 0, 0 warnings, and every module, class and function in `src/` has a Doxygen comment | Any warning or an uncommented item |
| 9 | Following the README from a fresh `.venv` (set up, run, tests, documentation) works on the Product Owner's platform, and the README's project layout matches the repository | Every command runs as written | A command fails or the layout differs |
| 10 | `pyproject.toml` | Lists no runtime dependency | A runtime dependency is listed |
| 11 | The pull request's code review against the Python quality checklist `QC-PY-001` is recorded | A review record (`RC-*`) with verdict `Go` | No record, `Go-with-conditions` or `No-Go` |
| 12 | Every task of this gateway is a closed issue and the pull request description has one `Closes #N` line per task | All closed and listed | Any open or unlisted |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-005 | The checks and the score are added to the quiz loop |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 Quiz built from the assignment's classes and methods | [BC-001] |
| O4 Repository usable by others | [BC-001] |
| O5 One gateway, one branch, one pull request | [BC-001] |
| Success criteria 3, 6, 7, 8 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-21 — the target date in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the score and check_answer | Add the attribute `score` (0 at the start) to `QuizBrain` and the method `check_answer(user_answer, correct_answer)`: compare both in lower case, add 1 to `score` on a match, and tell the player whether the answer was right and what the correct answer was (lecture part 5). Texts are constants in `constants.py`. | No | |
| 2 | Pass the player's answer to check_answer | Make `next_question` keep the player's input in `user_answer` and call `check_answer(user_answer, current_question.answer)`, so every question is checked. | No | |
| 3 | Show the running score and separate the questions | After each answer print the current score and the number of questions answered, and a blank line before the next question, so the player can follow their result. | No | |
| 4 | Show the final result | When the loop in `main()` ends, print that the quiz is complete and the final score as `<score>/<number of questions>`. | No | |
| 5 | Test the answers, the score and the final result | Extend `tests/test_quiz_brain.py` and `tests/test_main.py`: right and wrong answers, letter case, other text counting as wrong, score progression, the captured feedback and an end-to-end run with 12 scripted answers. | No | |
| 6 | Final README and documentation check | Run every README command from a fresh `.venv`, add an example session to Run, make Project layout match the repository, and build the source documentation once more with 0 warnings. Completes the repository for S02 and S03 (BC-001 objective O4). | No | |

---

[BC-001]: ../business-case.md
[ab361ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/ab361edf622585f77249d7782a9e2619f7d85cfc

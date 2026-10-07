# Review Record: Python code of MIL-006

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [MIL-006], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: Python code of the pull request for MIL-006: `src/quiz_brain.py` (`score`, `check_answer`, `next_question`), `src/main.py` (the final result), the feedback constants in `src/constants.py`, the header comment in `src/data.py`, and `tests/conftest.py`, `tests/test_quiz_brain.py`, `tests/test_main.py`
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of the code delivered by [MIL-006] (milestone MIL-006, tasks 1 to 5; task 6, the README and documentation check, is not Python code and is covered by the gateway's Go/No-Go criteria 8 and 9)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Reviewer: S01. The checklist was applied by an AI assistant at S01's request; the verdict is S01's to give.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `check_answer`, `score`, `user_answer`, `correct_answer`, the fixture `script_input` and the helpers `right_answers` and `wrong_answers` are `snake_case`; the new constants (`FEEDBACK_RIGHT`, `FEEDBACK_WRONG`, `FEEDBACK_CORRECT_ANSWER`, `FEEDBACK_SCORE`, `MESSAGE_QUIZ_COMPLETE`, `MESSAGE_FINAL_SCORE`) are `UPPER_SNAKE`; `ruff` rule set `N` (pep8-naming) reports nothing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | The assignment's names are kept (`check_answer(user_answer, correct_answer)`, `score`, `user_answer`). The feedback constants are named for what they say. No abbreviation and no single-letter name. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` and `ruff format --check src tests` exit 0 with no inline suppression. The first run found one over-long comment line in `constants.py`, which was shortened. `src/data.py` stays excluded from `ruff` in `pyproject.toml` (configuration, not a suppression): it keeps the course's layout, and S01 decided on 2026-10-07 to keep it that way. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `check_answer(self, user_answer: str, correct_answer: str) -> None`; the new fixture is annotated `-> Callable[[Iterable[str]], ScriptedInput]`; every new test is annotated. `mypy --strict src tests` exits 0. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | The code contains no `try` or `except`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default arguments; no builtin is shadowed (`ruff` rule set `B` reports nothing). |
| 7 | Files, locks and connections are managed with context managers | N-A | The code opens no files, locks or connections. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | `check_answer` and the updated `next_question` and `main` have Doxygen docstrings with `@param` and `@return`; the new attribute `score` and the six constants have `##` comments. `doxygen Doxyfile` exits 0 with 0 warnings. MIL-006 Go/No-Go criterion 8 wants every module, class and function in `src/` documented: a syntax-tree check finds no module, class or function without a docstring in the five modules, and `data.py` is now part of the Doxygen output. S01 chose on 2026-10-07 to add a header comment to `src/data.py`: the lines from `question_data = [` on are byte-identical to the course's starter file, and the loaded objects are equal (both checked). |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | `print` is the program's user interface here (the feedback, the running score and the final result), not logging, as the accepted Project Plan records (open issue on console output). Diagnostics still use `logging` (the line in `main` from G3). No secret or personal data is printed. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | G6 adds no class. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 22 new tests (54 in all): in `tests/test_quiz_brain.py` the start score, 7 right answers in any letter case, 6 wrong or other answers (including an empty answer), the exact output after a right and after a wrong answer, `next_question` checking against the answer of its own question, and the running score over three questions; in `tests/test_main.py` the final result for all-right, all-wrong and all-true answers and the running score over twelve answers. Names follow `test_<behaviour>_<condition>`; the `ScriptedInput` fake and `capsys`, no mocks, no network. Written first: 22 failed and the 32 existing tests passed. The suite passes in reverse order (54 of 54). A mutation check on scratch copies killed all 13 mutants: no `lower()` on either side, score plus two, score never grows, inverted check, no correct answer shown, wrong denominator, no blank line, the question's answer ignored, the player's answer ignored, no completion message, final score zero, final total off by one. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src tests` exits 0; there is no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Optional criterion, open since RC-010: the `dev` group in `pyproject.toml` uses minimum versions, not exact pins, and there is no lock file. S01 decided on 2026-10-07 to keep minimum versions. This gateway adds no dependency. |

## Overall Verdict

Go — the checklist pass found no failing mandatory criterion: 8 criteria pass, 4 are not applicable (5, 7, 9, 10) and the one failing criterion (13) is optional and accepted by S01 (minimum versions kept). The two decisions that were open since G1 are closed by S01: `src/data.py` gets a Doxygen header comment (criterion 8), and the development tools keep minimum versions (criterion 13). S01 gave Go in chat on 2026-10-07. MIL-006 Go/No-Go criterion 11 is met.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | n/a | n/a |

---

[MIL-006]: ../../milestones/mil-006-answers-and-score.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md

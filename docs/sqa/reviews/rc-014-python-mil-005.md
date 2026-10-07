# Review Record: Python code of MIL-005

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [MIL-005], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [831c2be] |

---

## Artifact Under Review

- Instance reviewed: Python code of the pull request for MIL-005: `src/quiz_brain.py` (`still_has_questions`), `src/main.py` (the loop in `main`), `tests/test_quiz_brain.py` and `tests/test_main.py`
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of the code delivered by [MIL-005] (milestone MIL-005, tasks 1 to 3)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Reviewer: S01. The checklist was applied by an AI assistant at S01's request; the verdict is S01's to give.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `still_has_questions` is `snake_case`; the test parameters `questions_asked` and `expected` and the test functions are `snake_case`; `ruff` rule set `N` (pep8-naming) reports nothing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | `still_has_questions` is the assignment's name and reads as a question, as a boolean should. No abbreviation and no single-letter name (the loop variable `_` in one test is the conventional unused name). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` and `ruff format --check src tests` exit 0 on the first run, with no inline suppression. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `still_has_questions(self) -> bool`; the parametrized test is annotated `(questions_asked: int, expected: bool) -> None`; every other new test is `-> None`. `mypy --strict src tests` exits 0. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | The code contains no `try` or `except`. The `IndexError` that `next_question` raises after the last question (noted in RC-013) can no longer happen in `main()`, because the loop only calls it while `still_has_questions()` is true. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No default arguments; no builtin is shadowed (`ruff` rule set `B` reports nothing). |
| 7 | Files, locks and connections are managed with context managers | N-A | The code opens no files, locks or connections. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | `still_has_questions` has a Doxygen docstring with `@return`; the docstring of `main` was updated. `doxygen Doxyfile` exits 0 with 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | This gateway adds no `print` and no logging; the only output is still the prompt passed to `input()`, the program's user interface (open issue in PP-001). |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | G5 adds no class. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | New tests: `test_quiz_brain.py` gained 6 test items (an empty list; a parametrized test for 0, 1 and 2 questions asked, which are true, and 3 asked, which is false; a loop that asks each question once) and `test_main.py` replaced the G4 test that pinned one prompt by two tests (every question in order; exactly twelve prompts when twelve answers are scripted). Names follow `test_<behaviour>_<condition>`; the `ScriptedInput` fake, no mocks, no network. Written first: before the implementation 8 tests failed and the 24 existing ones passed. The suite of 32 passes in reverse order. A mutation check on scratch copies killed all 8 mutants: `<=` (6 failures), `>` (6), always true (6), `==` (8), last one dropped (4), `if` instead of `while` (2), loop skips the last question (2), `while True` (3). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src tests` exits 0; there is no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Unchanged from RC-010: the `dev` group in `pyproject.toml` uses minimum versions, not exact pins, and there is no lock file. This gateway adds no dependency. Optional criterion; the action item of RC-010 stays open. |

## Overall Verdict

Go — the checklist pass found no failing mandatory criterion: 9 criteria pass, 3 are not applicable (5, 7, 10) and the one failing criterion (13) is optional and unchanged from RC-010. MIL-005 Go/No-Go criterion 2 (the comparison is returned directly, without an `if`) was checked on the syntax tree of `still_has_questions`: its body is a docstring and one `return` of the comparison `self.question_number < len(self.question_list)`, and it contains no `if`. S01 gave Go in chat on 2026-10-07. MIL-005 Go/No-Go criterion 8 is met.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether the development tools need exact pins (open since RC-010, criterion 13) | S01 | 2026-10-10 |

---

[MIL-005]: ../../milestones/mil-005-quiz-loop.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[831c2be]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/831c2be1f79814229e65f480cfef0b7fed69ba02

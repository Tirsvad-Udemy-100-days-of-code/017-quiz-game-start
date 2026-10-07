# Review Record: Python code of MIL-004

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [0741def] |

---

## Artifact Under Review

- Instance reviewed: Python code of the pull request for MIL-004: `src/quiz_brain.py` (`QuizBrain`), `src/main.py` (`main` asks the first question), the prompt constant in `src/constants.py`, and `tests/test_quiz_brain.py`, `tests/test_main.py`, `tests/fakes.py`, `tests/conftest.py`
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of the code delivered by [MIL-004] (milestone MIL-004, tasks 1 to 4)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Reviewer: S01. The checklist was applied by an AI assistant at S01's request; the verdict is S01's to give.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `QuizBrain` and `ScriptedInput` are `PascalCase`; `question_number`, `question_list`, `next_question`, the fixture `scripted_input` and the tests are `snake_case`; `PROMPT_QUESTION` is `UPPER_SNAKE`; `ruff` rule set `N` (pep8-naming) reports nothing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | The assignment's names are kept (`QuizBrain`, `question_number`, `question_list`, `next_question`); the initialiser parameter is `question_list`, not the course's `q_list`, because it matches the attribute it sets. No abbreviation and no single-letter name. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` and `ruff format --check src tests` exit 0 with no inline suppression. The first run found 7 findings (3 import-order, 4 over-long lines). The 4 lines were shortened. The import order was fixed in the configuration, not with a suppression: `src = ["src", "tests"]` in `pyproject.toml` tells `ruff` that the test helpers `fakes` and `conftest` are first-party. The G1 exclusion of `src/data.py` is unchanged. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every signature is annotated: `QuizBrain.__init__(self, question_list: list[Question]) -> None`, `next_question(self) -> None`, `ScriptedInput.__call__(self, prompt: str = "") -> str`, the fixture `-> ScriptedInput` and all tests `-> None`. `mypy --strict src tests` exits 0. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | The code contains no `try` or `except`. Calling `next_question` after the last question raises `IndexError` from the list index and nothing hides it; the loop of the next gateway (`still_has_questions`) guards the call. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default argument (`answers: Iterable[str] = ()` is an immutable tuple, `prompt: str = ""`); no builtin is shadowed. `ruff` rule set `B` reports nothing. |
| 7 | Files, locks and connections are managed with context managers | N-A | The code opens no files, locks or connections. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | The module, `QuizBrain`, `__init__` and `next_question` have docstrings in the project's Doxygen style with `@param` and `@return`; both attributes have a `##` comment. `doxygen Doxyfile` exits 0 with 0 warnings. The test helpers have plain PEP 257 docstrings because `tests/` is not Doxygen input. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | This gateway adds no `print` and no logging. The prompt passed to `input()` is the program's user interface, not a diagnostic (open issue in PP-001); the logging added in G3 is unchanged. Nothing secret or personal is written. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | `QuizBrain` is a new class, but no Design Class Diagram exists. As in RC-011, the accepted Project Plan records that none is planned because the lecture part fixes the class (attributes `question_number` and `question_list`, method `next_question`), and MIL-004 tasks 1 and 2 state the same. No deviation from that description. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_quiz_brain.py` has 9 tests (start state, list identity, first prompt as the learner sees it, prompt from the constant, True/False in the prompt, number after one question, second prompt, one answer read per question, list unchanged); `tests/test_main.py` gained a test that `main()` asks the first question. Names follow `test_<behaviour>_<condition>`; the fake `ScriptedInput` in `tests/fakes.py` replaces `input` (a fake, not a mock); no network. Written first and seen failing (`ImportError`). The suite passes in reverse order (25 of 25). A mutation check on scratch copies killed all 9 mutants: start at one (6 failures), list dropped (10), no increment (5), increment twice (5), prompt number off by one (4), wrong question (4), no `input` call (6), prompt without True/False (2), `main` does not ask (1). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src tests` exits 0; there is no `Any` (the fake uses `Iterable[str]`). |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Unchanged from RC-010: the `dev` group in `pyproject.toml` uses minimum versions, not exact pins, and there is no lock file. This gateway adds no dependency. Optional criterion; the action item of RC-010 stays open. |

## Overall Verdict

Go — the checklist pass found no failing mandatory criterion: 9 criteria pass, 3 are not applicable (5, 7, 10) and the one failing criterion (13) is optional and unchanged from RC-010. S01 gave Go in chat on 2026-10-07. MIL-004 Go/No-Go criterion 9 is met.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether the development tools need exact pins (open since RC-010, criterion 13) | S01 | 2026-10-10 |

---

[MIL-004]: ../../milestones/mil-004-next-question.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[0741def]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/0741defd0373768175eec215d95872e6ff92b761

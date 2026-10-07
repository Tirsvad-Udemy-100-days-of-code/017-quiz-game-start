# Review Record: Python code of MIL-003

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [1cda99a] |

---

## Artifact Under Review

- Instance reviewed: Python code of the pull request for MIL-003: `src/main.py` (`build_question_bank`, `main`), the new constant in `src/constants.py` and `tests/test_main.py`
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of the code delivered by [MIL-003] (milestone MIL-003, tasks 1 to 3)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Reviewer: S01. The checklist was applied by an AI assistant at S01's request; the verdict is S01's to give.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `build_question_bank`, `main`, `logger`, `raw_questions` and the test functions are `snake_case`; `LOG_QUESTIONS_LOADED` is `UPPER_SNAKE`; `ruff` rule set `N` (pep8-naming) reports nothing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state the purpose: `raw_questions` are the dictionaries before they become `Question` objects, `question_bank` and `new_question` are the assignment's own names. No abbreviation; the only single-letter name is `q` inside one test comprehension (tiny scope). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` and `ruff format --check src tests` exit 0; there is no inline suppression. `ruff` found three comment lines over 88 characters on the first run; they were shortened. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `build_question_bank(raw_questions: list[dict[str, str]]) -> list[Question]`, `main() -> None`, all test functions (`-> None`) and the local fake `fail_on_input(*args: object, **kwargs: object) -> NoReturn` are annotated; `mypy --strict src tests` exits 0. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | The code contains no `try` or `except`. A dictionary without the `text` or `answer` key raises `KeyError` and nothing catches or hides it. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No default arguments; no builtin is shadowed (`ruff` rule set `B` reports nothing). |
| 7 | Files, locks and connections are managed with context managers | N-A | The code opens no files, locks or connections. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | The module, `build_question_bank` and `main` have docstrings in the project's Doxygen style with `@param` and `@return`; `logger` has a `##` comment. `doxygen Doxyfile` exits 0 with 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | The only diagnostic output uses `logging` (`logger.info` with lazy `%d` arguments, message in `constants.py`); there is no `print` in this gateway and nothing secret or personal is logged. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | G3 adds no class; `Question` was added by MIL-002. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_main.py` has 7 tests: bank size, bank content type, order and values, empty data, other data, `main()` logs the question count, importing `main` neither prints nor asks for input. Names follow `test_<behaviour>_<condition>`; fakes (`monkeypatch`, `caplog`, `capsys`) and no mocks; no network. Written first and seen failing (`ImportError`). The whole suite passes in reverse order (15 of 15), so there is no order dependence. A mutation check on scratch copies killed all 5 mutants: reversed order (2 failures), swapped text and answer (2), last question dropped (4), wrong logged count (1), `print` at import (1). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src tests` exits 0; there is no `Any` (`object` is used for the fake's arguments). |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Unchanged from RC-010: the `dev` group in `pyproject.toml` uses minimum versions, not exact pins, and there is no lock file. This gateway adds no dependency. Optional criterion; the action item of RC-010 stays open. |

## Overall Verdict

Go — the checklist pass found no failing mandatory criterion: 9 criteria pass, 3 are not applicable (5, 7, 10) and the one failing criterion (13) is optional and unchanged from RC-010. S01 gave Go in chat on 2026-10-07. MIL-003 Go/No-Go criterion 9 is met.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether the development tools need exact pins (open since RC-010, criterion 13) | S01 | 2026-10-10 |

---

[MIL-003]: ../../milestones/mil-003-question-bank.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[1cda99a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/1cda99ac623671380ee5bfae483f3468bd1b1241

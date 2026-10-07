# Review Record: Python code of MIL-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-001], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [1c2c852] |

---

## Artifact Under Review

- Instance reviewed: Python code of the pull request for MIL-001: `src/constants.py`, `tests/test_data.py`; `src/data.py`, `src/main.py`, `src/question_model.py` and `src/quiz_brain.py` are the course's starter files, copied unchanged
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of the code delivered by [MIL-001] (milestone MIL-001, tasks 1 to 6); the configuration files, README and workflow are not Python code and are covered by the gateway's own Go/No-Go criteria
- Language and domain: n/a (technical type)
- Language reviewer: none
- Reviewer: S01. The checklist was applied by an AI assistant at S01's request; the verdict is S01's to give.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `QUESTION_KEY_TEXT`, `QUESTION_KEY_ANSWER`, `ANSWER_TRUE`, `ANSWER_FALSE` are `UPPER_SNAKE`; the test module and functions are `snake_case`; ruff rule set `N` (pep8-naming) reports nothing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state the purpose (`QUESTION_KEY_TEXT`, `test_every_answer_is_true_or_false`); the only short names are `entry` and `answers` in tiny scopes. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` and `ruff format --check src tests` exit 0 on a fresh copy; the code has no inline suppression. `src/data.py` is excluded in `pyproject.toml` (`extend-exclude`) because it must stay byte-identical to the course's file; this is a configuration decision, listed in the action items. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every test function is annotated `-> None`; the constants use `Final`; `mypy --strict` exits 0 (`ruff` rule set `ANN` also reports nothing). |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | The code contains no `try` or `except`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No functions with defaults; no builtin is shadowed (`ruff` rule set `B` reports nothing). |
| 7 | Files, locks and connections are managed with context managers | N-A | The code opens no files, locks or connections. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | `src/constants.py` and `tests/test_data.py` have module docstrings; the constants have `##` comments. `doxygen Doxyfile` exits 0 with 0 warnings, and a negative control (an undocumented function, a missing `@param`, a missing `@return`) makes it fail. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | This gateway contains no `print` and no logging. When the quiz arrives, `print` and `input` are the program's user interface, not diagnostics (open issue in PP-001). |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | G1 adds no class. No Design Class Diagram exists; the Project Plan records that none is planned. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_data.py` has 4 tests of the only behaviour G1 adds (the shape of the course data); names follow `test_<behaviour>_<condition>`; no order dependence, no network. `pytest` exits 0 on a fresh copy. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src tests` exits 0; there is no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | The `dev` group in `pyproject.toml` declares `pytest`, `ruff` and `mypy` with minimum versions, not exact pins, and there is no lock file. The program has no runtime dependency (`dependencies = []`) and every listed tool is used. Optional criterion; see the action item. |

## Overall Verdict

Go — the checklist pass found no failing mandatory criterion: 8 criteria pass, 4 are not applicable to this gateway (5, 7, 9, 10) and the one failing criterion (13) is optional. S01 gave Go in chat on 2026-10-07, which accepts minimum versions for the development tools for now. MIL-001 Go/No-Go criterion 10 is met.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether the development tools need exact pins and a lock file (criterion 13); until then minimum versions stand | S01 | 2026-10-10 |
| Confirm that `src/data.py` stays excluded from `ruff` (it must stay byte-identical to the course's file), and decide whether G6 may add a Doxygen header comment to it | S01 | 2026-10-21 |

---

[MIL-001]: ../../milestones/mil-001-project-foundation.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[1c2c852]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/1c2c852b86fb8c330f0cd918eccefd2240b87700

# Review Record: Python code of MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [8142317] |

---

## Artifact Under Review

- Instance reviewed: Python code of the pull request for MIL-002: `src/question_model.py` (the class `Question`) and `tests/test_question_model.py`
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of the code delivered by [MIL-002] (milestone MIL-002, tasks 1 and 2)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Reviewer: S01. The checklist was applied by an AI assistant at S01's request; the verdict is S01's to give.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | The class `Question` is `PascalCase`; the attributes `text` and `answer`, the parameters and the test functions are `snake_case`; `ruff` rule set `N` (pep8-naming) reports nothing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state the purpose (`Question`, `text`, `answer`, `test_each_question_keeps_its_own_values_when_two_exist`); there is no abbreviation and no single-letter name. The course's `q_text` and `q_answer` are not used, because the attribute name is clearer without the prefix. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check src tests` and `ruff format --check src tests` exit 0; there is no inline suppression. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `__init__(self, text: str, answer: str) -> None` and the four test functions (`-> None`) are annotated; `mypy --strict src tests` exits 0. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | The code contains no `try` or `except`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No default arguments; `text` and `answer` are not builtins (`ruff` rule set `B` reports nothing). |
| 7 | Files, locks and connections are managed with context managers | N-A | The code opens no files, locks or connections. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | The module, the class and `__init__` have docstrings in the project's Doxygen style, and both attributes have a `##` comment. `doxygen Doxyfile` exits 0 with 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | This gateway contains no `print` and no logging. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | `Question` is a new class, but no Design Class Diagram exists. The accepted Project Plan records that none is planned because lecture part 1 fixes the class (attributes `text` and `answer`, set by the initialiser), and MIL-002 task 1 states the same. No deviation from that description. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_question_model.py` has 4 tests (text kept, answer kept, two objects independent, attribute types); names follow `test_<behaviour>_<condition>`; no order dependence, no network. Written first and seen failing (`ImportError`) before the implementation. A mutation check on a scratch copy (the two assignments swapped; the answer replaced by an empty string) made 2 tests fail each time. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src tests` exits 0; there is no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Unchanged from RC-010: the `dev` group in `pyproject.toml` uses minimum versions, not exact pins, and there is no lock file. This gateway adds no dependency. Optional criterion; the action item of RC-010 stays open. |

## Overall Verdict

Go — the checklist pass found no failing mandatory criterion: 8 criteria pass, 4 are not applicable (5, 7, 9, 10) and the one failing criterion (13) is optional and unchanged from RC-010. S01 gave Go in chat on 2026-10-07, which also accepts treating criterion 10 as not applicable, as the accepted Project Plan records. MIL-002 Go/No-Go criterion 6 is met.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decide whether the development tools need exact pins (open since RC-010, criterion 13) | S01 | 2026-10-10 |

---

[MIL-002]: ../../milestones/mil-002-question-class.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[8142317]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/814231725751cc702f911f939b6427268d7a8b85

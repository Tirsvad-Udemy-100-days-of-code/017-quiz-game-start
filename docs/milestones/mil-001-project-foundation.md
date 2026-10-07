# MIL-001 G1 Project foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [ab361ed] |

---

## Purpose

Decide whether the project foundation is complete enough for the lecture steps to start: the course's starter files sit in `src/`, the tooling and documentation the Product Owner required are in place, and a clean machine can follow the README to a green test run.

## Deliverable

One branch (`mil-001-project-foundation`) and one pull request containing: the four starter files copied into `src/`, `src/constants.py`, `pyproject.toml`, a Python `.gitignore`, a `Doxyfile`, a first test in `tests/`, a `README.md` that follows the Product Owner's template (with the local `.venv` instructions), a continuous-integration (CI) workflow, and, on the git host, the repository description and topics.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `src/data.py` is identical to `quiz-game-start/data.py`, and `src/main.py`, `src/question_model.py` and `src/quiz_brain.py` exist | `diff` of `data.py` is empty and all four files exist | A difference, or a file is missing |
| 2 | `pyproject.toml` sets `requires-python` to `>=3.13`, lists no runtime dependency and configures pytest | All three are present | Any is missing or a runtime dependency is listed |
| 3 | `.gitignore` covers `.venv/`, `.env`, Python caches, and the Doxygen output folder | `git status --ignored` shows each as ignored | Any is shown as untracked |
| 4 | Following the README on a fresh `.venv` ends with `pytest` passing | Exit code 0 | A non-zero exit code |
| 5 | `ruff check`, `ruff format --check` and `mypy --strict src tests` | 0 findings | Any finding |
| 6 | `doxygen Doxyfile` | Exit code 0, 0 warnings | Any warning or a non-zero exit code |
| 7 | `README.md` has the 11 template sections in order, commands for Windows PowerShell, Linux Debian and MacOS, and `python -m pip install --upgrade pip` | All present | Any missing |
| 8 | The CI workflow runs `ruff`, `mypy` and `pytest` on Python 3.13 | The workflow file shows all three steps | A step is missing |
| 9 | The repository on the git host has a description and at least 5 topics | `GET` of the repository returns both | Either is empty |
| 10 | The pull request's code review against the Python quality checklist `QC-PY-001` is recorded | A review record (`RC-*`) with verdict `Go` | No record, `Go-with-conditions` or `No-Go` |
| 11 | Every task of this gateway is a closed issue and the pull request description has one `Closes #N` line per task | All closed and listed | Any open or unlisted |

## Dependencies

| Depends on | Reason |
| --- | --- |
| BC-001, SA-001 and PP-001, each Accepted | Plan-first gate: no file under `src/` or `tests/` before the planning documents are reviewed |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2 Start from the course's starter files | [BC-001] |
| O3 Project tooling the Product Owner requires | [BC-001] |
| O4 Repository usable by others (README, CI, description, topics) | [BC-001] |
| O6 No runtime dependencies; clean quality tools | [BC-001] |
| Success criteria 4, 5, 6, 7, 9 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-10 — inside the 2026-10-21 target in [BC-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Copy the starter files into src/ | Copy `data.py`, `main.py`, `question_model.py` and `quiz_brain.py` from `quiz-game-start/` into `src/` without changing them, so that every later gateway starts from the course's own starting code (BC-001 objective O2). `data.py` holds the 12 question dictionaries; the other three files are empty. | No | |
| 2 | Add pyproject.toml | Create the project configuration: name and version, `requires-python = ">=3.13"`, an empty runtime dependency list, a development-only group with pytest, ruff and mypy, pytest settings (`testpaths = ["tests"]`, `pythonpath = ["src"]`) and the ruff and mypy settings. Keeps the program free of runtime dependencies (BC-001 objective O6). | No | |
| 3 | Add the Python .gitignore | Add a Python `.gitignore` that also lists `.venv/`, `.env` (it holds personal tokens and must never be committed), the pytest, ruff and mypy caches and the Doxygen output folder. | No | |
| 4 | Add src/constants.py | Create `src/constants.py` as the single place for constants, as the Product Owner requires. Start with the question dictionary keys (`text`, `answer`) and the answer words; later gateways add their prompt and feedback texts here instead of writing literals in the code. | No | |
| 5 | Add the Doxyfile and fix the comment style | Create a `Doxyfile` set up for Python (input `src/`, Python output optimisation, output outside version control) and fix one Doxygen comment style (`@brief`, `@param`, `@return` in docstrings) that every later gateway follows. Check that `doxygen Doxyfile` builds with 0 warnings. | No | |
| 6 | Add a starter-data test | Add `tests/test_data.py`: `question_data` has 12 entries, each with a `text` and an `answer` key, and each answer is `True` or `False`. This gives pytest and the CI workflow a real test from the first gateway. | No | |
| 7 | Write the README from the Product Owner's template | Write `README.md` with the template sections (project name and description, Requirements, Set up for Windows PowerShell, Linux Debian and MacOS, Run, Run the tests, Continuous integration, Build the source documentation, Project layout, License). Set up shows how to create and use a local `.venv` and run `python -m pip install --upgrade pip`, and says the program has no runtime dependencies. | No | |
| 8 | Add the CI workflow | Add `.github/workflows/ci.yml` (read by GitHub Actions and by Gitea Actions) that, on push and pull request, sets up Python 3.13, upgrades pip, installs the development tools and runs `ruff check`, `ruff format --check`, `mypy --strict` and `pytest`. | No | |
| 9 | Set the repository description and topics | On the git host, set a short description and at least 5 topics (for example python, udemy, 100-days-of-code, quiz-game, pytest) for the repository S01 confirms (Project Plan, open issues), using the personal token from the local `.env`. A one-off host action, not project code: the `.env` file is not imported, tested or committed. Verify with a `GET` of the repository. | No | |

---

[BC-001]: ../business-case.md
[ab361ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/ab361edf622585f77249d7782a9e2619f7d85cfc

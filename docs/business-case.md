# Business Case: Quiz Game

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [ab361ed] |

---

## Executive Summary

The project turns the day 17 assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" into a small, runnable and shareable Python repository: a console True/False quiz that asks twelve questions, checks each answer and reports a running and a final score. The course supplies four starter files (`data.py`, `main.py`, `question_model.py`, `quiz_brain.py`); the project copies them into `src/` and completes them in five lecture parts, each delivered as one gateway (a reviewed checkpoint with its own branch and pull request), after one foundation gateway for the project set-up. The result is tested with pytest, documented with Doxygen comments and a README, needs no runtime dependencies and uses the assignment's own class and method names, so fellow course participants can compare solutions. The Product Owner (S01) recommends proceeding.

## Methodological and Standards Foundation

- **Method:** Larman, *Applying UML and Patterns* (the framework's analysis and design method); work is planned as gateways (milestones) with tasks, and every artifact is reviewed before work that depends on it starts (plan-first gate).
- **Quality model:** ISO/IEC 25010:2023 characteristics tag every review criterion.
- **Code standards:** Python Enhancement Proposals (PEP) 8 (style), 257 (docstrings) and 484 (type hints); source comments use the Doxygen form so one tool builds the source documentation.
- **Review:** documents are reviewed against the `QC-*` checklists of the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/`; Python code is reviewed against `QC-PY-001`.

## Problem Statement

The course hands out four starter files, three of them empty, and a series of lecture summaries. Followed as given, the result is a loose set of scripts: no project configuration, no tests, no recorded setup for a clean machine, no history of the individual lecture parts and no documentation. A fellow participant who finds the code cannot run it with confidence, and a visitor cannot tell what it is or whether it needs installing anything.

## Business Opportunity

A small, well-structured repository lets S01 practise professional project habits (tests, branches, pull requests, documentation) on a program that is simple enough to keep the focus on the habits. It also gives S02 a reference solution to compare against and S03 a clear public repository to browse.

## Objectives

| ID | Objective |
| --- | --- |
| O1 | Deliver a console True/False quiz built from the classes `Question` and `QuizBrain`, the methods `next_question`, `still_has_questions` and `check_answer`, and a question bank of twelve questions, using the assignment's own names. |
| O2 | Start from the course's starter files, copied into `src/`, and complete them step by step in the order of lecture parts 1 to 5. |
| O3 | Set up the project tooling the Product Owner requires: Python 3.13 or newer, `venv`, `pytest`, `pyproject.toml`, `constants.py`, a Python `.gitignore`, Doxygen comments and a `Doxyfile`. |
| O4 | Make the repository usable by others: a README that follows the Product Owner's template, setup instructions for Windows PowerShell, Linux Debian and MacOS, a continuous-integration workflow, a repository description and topics. |
| O5 | Keep every gateway traceable: one gateway, one branch, one pull request, and every task an issue that the pull request closes. |
| O6 | Keep the program free of runtime dependencies and keep the source passing the formatter, linter, type checker and tests. |

## Scope

### In Scope

- Copying the starter files from `quiz-game-start/` into `src/` and using them as the starting point.
- The `Question` class (attributes `text` and `answer`), the question bank built from `question_data` in `data.py`, the `QuizBrain` class (`question_number`, `question_list`, `score`, `next_question`, `still_has_questions`, `check_answer`) and the `main.py` loop that runs the quiz, with a running score after each answer and a final score.
- `constants.py` for constants; tests under `tests/` using pytest; documents under `docs/`.
- `pyproject.toml`, `.gitignore`, `Doxyfile`, Doxygen-style comments in `src/`, a README, a continuous-integration workflow.
- Instructions to create and use a local `.venv` and to run `python -m pip install --upgrade pip`.
- Setting the repository description and topics on the git host.

### Out of Scope

- Any user interface other than the console; any question type other than True/False.
- Fetching questions from a service, storing scores, timing, levels or any feature not in lecture parts 1 to 5.
- Re-asking when the player types something other than true or false; such an answer counts as wrong, as in the lecture.
- Publishing the project as an installable package.
- Changing the course data in `data.py` (including its wording).
- Use cases, user stories and a domain model: the behaviour is fixed by the lecture summaries (see the Project Plan, open issues).

## Expected Benefits

### Tangible Benefits

- A working quiz that anyone can run after following the README.
- An automated test suite and a continuous-integration workflow that run it.
- Generated source documentation from the Doxygen comments.
- A history of six pull requests, one per gateway, that shows how the program grew.

### Intangible Benefits

- Practice in object-oriented Python, test-first thinking and a plan-first workflow.
- A repository that other course participants and visitors can read, compare with and learn from.

## Strategic Alignment

The project supports S01's learning path through the 100 Days of Code course. It keeps the layout (`src/`, `tests/`, `docs/`) and the README structure that S01 asked for, so it can sit beside S01's other course projects in the `Tirsvad-Udemy-100-days-of-code` organisation and stay easy to browse.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Tests pass | 0 failures, 0 errors, at least one test per public method | `pytest` exit code 0 |
| 2 | The question bank is complete | 12 `Question` objects built from `question_data` | A test counts the objects |
| 3 | The quiz runs end to end | `python src/main.py` asks 12 questions and ends with a final score line of the form `<score>/12` | A test with scripted input, and one manual run |
| 4 | No runtime dependencies | 0 entries in the project's runtime dependency list | `pyproject.toml` review |
| 5 | Source quality tools are clean | 0 findings from `ruff check`, `ruff format --check` and `mypy --strict` | Tool exit codes |
| 6 | Source documentation builds | `doxygen Doxyfile` exits 0 with 0 warnings; every module, class and function in `src/` has a Doxygen comment | Doxygen output |
| 7 | README is complete | All 11 sections of the Product Owner's template present, in order, with setup commands for three platforms | Heading comparison |
| 8 | Gateways are traceable | 6 pull requests; every task issue closed by a `Closes #N` line | Issue list and pull request descriptions |
| 9 | Repository is described | Non-empty description and at least 5 topics on the git host | A `GET` request to the git host's application programming interface (API) |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The scope grows beyond lecture parts 1 to 5 | Delay, and a solution that no longer matches the assignment other participants compare against | The Out of Scope list is a gateway Go/No-Go check; extra ideas become new gateways |
| The framework's ceremony is large for a program of about sixty lines | Effort spent on documents instead of code | Six small gateways, plain tasks, short documents, one review per document |
| The Python version wording is read two ways ("greater than 3.13") | Participants on 3.13 cannot run the code, or the code needlessly excludes 3.13 | `requires-python` is `>=3.13` (3.13 is installed on S01's machine); S01 confirms at review (Project Plan, open issues) |
| The local `.env` holds personal tokens | A token is published with the repository | `.env` is in `.gitignore` and in the local git exclude list; no project code reads, imports or tests it; it is used only by hand for host calls |
| The git host has no continuous-integration (CI) runner | The CI section cannot be demonstrated on the main host | The workflow is stored under `.github/workflows/`, which GitHub and Gitea both read; the GitHub mirror can run it |
| Doxygen parses Python docstrings differently from what the comments assume | Warnings, or empty documentation | Gateway 1 fixes one comment style and builds the documentation; every later gateway repeats the build |
| The quiz's console output conflicts with the Python rule "use `logging`, not `print`" | A false finding in the code review | `print` and `input` are the program's user interface, not diagnostics; the review records the criterion as not applicable for them |

## Assumptions

- The files in `quiz-game-start/` are the course's starter code and are copied unchanged; the folder stays in the repository.
- "Python greater than 3.13" means 3.13 or newer.
- There is no external deadline; the target of 2026-10-21 for the last gateway is set by S01.
- One person (S01) is Product Owner, developer and reviewer, as S01 defined the role. The documents were drafted by an AI assistant at S01's request, and S01 reviews them. No other stakeholder can review, and the project has no governance document, so the framework rule that a reviewer must not be the author is met only in that sense (Project Plan, open issues).
- The main git host is the Gitea instance behind `origin`; the GitHub remote is a mirror.

## Constraints

- Python 3.13 or newer; a local `venv` (`.venv`); `pytest`; one `pyproject.toml`; constants in `constants.py`.
- Folder structure `src/`, `tests/`, `docs/`.
- Doxygen comments in the source and a `Doxyfile`.
- No runtime dependencies unless needed; development tools are allowed as development-only dependencies.
- The licence is the GNU Affero General Public License (AGPL) version 3 already in the repository.
- Nothing is committed or pushed until S01 asks; changes go through branches and pull requests, and a reviewer, not the author, merges.
- Nothing is written under `src/` or `tests/` until the gateway that contains the task is accepted with a `Go` review (plan-first gate).

## Cost–Benefit Assessment

A monetary return is not meaningful: this is a personal learning project with no budget and no revenue, so the assessment is qualitative.

| Costs | Benefits |
| --- | --- |
| S01's time to plan, write and review six small gateways | A working, tested and documented quiz |
| Time to learn and apply the framework's review habits | A reusable pattern for the next course projects |
| Maintenance of the README and the workflow | A repository that S02 and S03 can use without help |
| No licence, hosting or tooling cost beyond the existing git host | A traceable history of every gateway |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 ([SA-001]) | Completes the assignment step by step with a reviewable history; owns scope, development and review |
| S02 ([SA-001]) | Reads, runs and compares the code; needs the assignment's names and README instructions |
| S03 ([SA-001]) | Browses the repository for ideas; needs a clear description, topics and README, and no runtime dependencies |

## Recommendation

Proceed — the scope is small and fully specified by the lectures, the cost is S01's time only, and the result serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[ab361ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/ab361edf622585f77249d7782a9e2619f7d85cfc

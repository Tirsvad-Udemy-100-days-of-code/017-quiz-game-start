# Stakeholder Analysis: Quiz Game

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [ab361ed] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added concern IDs CN-001 to CN-007 (QC-SA-001 criterion 9), a conflict about author and reviewer being one person, the baseline phase in the communication table and the traceability; set the domain to education; reviewed in autonomous mode, not independent | pending |

---

## Purpose

This analysis names the people who build, use or look at the Quiz Game project and decides how closely each is involved. It uses the power/interest grid: power is the ability to change scope, accept work or block it; interest is how much the stakeholder cares about the result. The stakeholder IDs below are the IDs every other document uses for owners, reviewers and responsibility assignments (RACI: Responsible, Accountable, Consulted, Informed). Concerns are mapped to FURPS+ (Functionality, Usability, Reliability, Performance, Supportability, plus design, implementation, interface and physical constraints). The classification of S01 was given by S01; the classification of S02 and S03 was proposed by the analyst and is accepted by S01 with the review record RC-002.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad-Udemy-100-days-of-code | HIGH | HIGH | Manage Closely | Finish the assignment gateway by gateway, with a history that can be reviewed and traced |
| S02 | Udemy coursists | Fellow participants of the course, who share code and compare solutions | Udemy 100 Days of Code community | LOW | HIGH | Keep Informed | Readable, runnable code that uses the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | GitHub (public) | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies to install |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** S01 sets scope, writes the code and accepts every document and pull request, so both power and interest are high. S01 is the only stakeholder who decides.
- **Keep Informed (S02):** S02 cannot change scope or accept work, but cares strongly about the result because S02 compares it with their own solutions. S02 is kept informed through the README and the repository's public history.
- **Monitor (S03):** S03 has no say and only a passing interest. S03 is served by a repository that explains itself (description, topics, README), without any effort to follow S03 individually.
- **Keep Satisfied:** no stakeholder is in this quadrant.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The quiz does what the five lecture parts describe | Functionality |
| CN-002 | S01 | Every step is a branch and a pull request that can be reviewed and traced to issues | Supportability |
| CN-003 | S01 | The tooling the Product Owner asked for (Python 3.13 or newer, `venv`, pytest, `pyproject.toml`, `constants.py`, Doxygen) is in place | Implementation constraints (+) |
| CN-004 | S02 | The code is readable and keeps the assignment's class and method names | Usability |
| CN-005 | S02 | The README tells how to set up, run and test on their own platform | Usability (documentation) |
| CN-006 | S03 | The repository description, topics and README explain what the project is at a glance | Usability |
| CN-007 | S03 | Nothing has to be installed to run the program | Implementation constraints (+), Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Pull request on the git host, with the review record | Once per gateway | Pull request description with the closed issues, and the `RC-*` record | MIL-001 to MIL-006, MIL-007 |
| S02 | README and public repository history | On every merged pull request | Runnable code and README instructions | MIL-001 (README), MIL-006 (final README check) |
| S03 | Repository description, topics and README | Set once, checked at the end | Description, topics and README | MIL-001 (description and topics), MIL-006 (final check) |
| S02, S03 | Wiki in English, Danish and Malay | Once, updated on change | Wiki pages | MIL-007 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01's tooling (type annotations, constants file, Doxygen comments, a linter) adds ceremony; S02 wants plain, readable code with the assignment's names | S01, S02 | The assignment's names are kept (`Question`, `QuizBrain`, `next_question`, `still_has_questions`, `check_answer`); the extra structure is limited to comments, annotations and a constants file, and the layout stays flat in `src/` |
| S01's development tools (pytest, ruff, mypy) are dependencies; S03 wants nothing to install | S01, S03 | The tools are development-only; the runtime dependency list stays empty and the README says so |
| S01 wants a history of small gateways; S02 and S03 want a finished, clear repository on first look | S01, S02, S03 | The README is complete from the first gateway and is updated at each gateway; the gateway history lives in the pull requests |
| The author and the reviewer of the baseline documents are the same person (S01), so the review is not independent | S01 | The AI assistant acts as stand-in reviewer for S01; every review record says `Mode: autonomous, not independent` and the end-of-run summary lists it for challenge |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | The quiz does what the lecture parts describe (CN-001) | O1, O2 in [BC-001] |
| S01 | Gateway-by-gateway, traceable delivery (CN-002) | O5 in [BC-001] |
| S01 | Required tooling in place (CN-003) | O3 in [BC-001] |
| S02 | Readable, runnable code with the assignment's names (CN-004) | O1, O4 in [BC-001] |
| S02 | README instructions to run and test (CN-005) | O4 in [BC-001] |
| S03 | Clear description, topics and README (CN-006) | O4 in [BC-001] |
| S03 | No runtime dependencies (CN-007) | O6 in [BC-001] |
| S01, S02, S03 | A project that follows the common baseline of the framework, with a wiki in three languages | O7 in [BC-001] |

Stakeholder to actor mapping: the program has one actor, the player, who answers the quiz in a console. The player is S01 while developing and S02 or S03 when they run the code. No use cases are modelled; see the Project Plan, open issues.

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Pending review | |

---

[BC-001]: ./business-case.md
[ab361ed]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start/commit/ab361edf622585f77249d7782a9e2619f7d85cfc

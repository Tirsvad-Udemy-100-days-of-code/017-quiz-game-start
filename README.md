# Quiz Game

A console True/False quiz in plain Python: it asks twelve questions, checks each answer and shows a score. It is the day 17 quiz project of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", built step by step with the assignment's own names (`Question`, `QuizBrain`, `next_question`, `still_has_questions`, `check_answer`). The program has no runtime dependencies, so other course participants can read, run and compare it.

## Requirements

- Python 3.13 or newer. The program itself uses only the standard library.
- `pytest`, `ruff` and `mypy` to run the tests and checks. They are development-only tools, installed in a local `.venv` (see Set up).
- [Doxygen][doxygen] only if you want to build the source documentation.
- Git, to clone the repository.

## Set up

The quiz needs no installation: with Python 3.13 you can run `python src/main.py` straight after cloning. The steps below create a local virtual environment (`.venv`, ignored by Git) and install the development tools used by the tests and checks.

The repository has a `framework/` Git submodule that holds the documentation workflow of the project. You do not need it to run or test the program, so a plain `git clone` is enough.

### Windows powershell

```powershell
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start.git
cd 017-quiz-game-start
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install --group dev
```

If PowerShell refuses to run the activation script, allow scripts for this window only and activate again: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`.

### Linux debian

Debian 13 (trixie) provides Python 3.13. On an older release, install Python 3.13 first (for example with `pyenv`).

```bash
sudo apt install git python3 python3-venv
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start.git
cd 017-quiz-game-start
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --group dev
```

### MacOS

```bash
brew install python@3.13 git
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-quiz-game-start.git
cd 017-quiz-game-start
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --group dev
```

On every platform, `python -m pip install --upgrade pip` comes first because `--group` needs pip 25.1 or newer. Leave the environment with `deactivate`; to use it again, run the activation line of your platform.

## Run

From the repository root:

```bash
python src/main.py
```

The quiz is built in six gateways (see `docs/project-plan.md`). After the first gateway `src/main.py` is still the course's empty starter file, so running it prints nothing yet; each later gateway adds one lecture part, and this section gets an example session when the quiz is complete.

## Run the tests

With the `.venv` active, from the repository root:

```bash
python -m pytest
```

The checks that the continuous integration also runs:

```bash
ruff check src tests
ruff format --check src tests
mypy --strict src tests
```

## Continuous integration

The workflow `.github/workflows/ci.yml` runs on every push and pull request. It sets up Python 3.13, upgrades pip, installs the development tools with `python -m pip install --group dev`, and runs `ruff check`, `ruff format --check`, `mypy --strict` and `pytest`. GitHub Actions and Gitea Actions both read this folder; on Gitea the repository needs an Actions runner.

## Build the source documentation

The source comments are written for [Doxygen][doxygen]; the style is described at the top of the `Doxyfile`. Install Doxygen, then from the repository root:

```bash
doxygen Doxyfile
```

Open `docs/doxygen/html/index.html` in a browser. The folder `docs/doxygen/` is generated and ignored by Git. The build fails on any undocumented module, class, function or parameter, so it also checks that the comments are complete. `src/data.py` is the course's data file and is left out.

## Project layout

```text
.
├── .github/workflows/ci.yml   Continuous integration
├── docs/                      Project documents: business case, stakeholders, plan, milestones, reviews
├── framework/                 SQA and QC framework (Git submodule, not needed to run the program)
├── quiz-game-start/           The course's starter files, unchanged
├── src/
│   ├── constants.py           Constants of the program
│   ├── data.py                The twelve questions (from the course)
│   ├── main.py                Entry point
│   ├── question_model.py      The Question class
│   └── quiz_brain.py          The QuizBrain class
├── tests/                     pytest tests
├── AGENTS.md                  Rules for AI agents working in this repository
├── Doxyfile                   Doxygen configuration
├── LICENSE
├── pyproject.toml             Project configuration and tool settings
└── README.md
```

## License

GNU Affero General Public License version 3. See [LICENSE][license].

---

[doxygen]: https://www.doxygen.nl/
[license]: ./LICENSE

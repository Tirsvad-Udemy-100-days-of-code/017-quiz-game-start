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

The quiz asks twelve True/False questions, one after the other. Type `True` or `False` (in any letter case) and press Enter. After each answer you see whether it was right, the correct answer and your score so far; anything other than the right word counts as wrong. At the end you see your final score.

An example session (the questions between Q.3 and Q.12 are left out):

```text
Q.1: A slug's blood is green. (True/False)?: true
You got it right!
The correct answer was: True.
Your current score is: 1/1

Q.2: The loudest animal is the African Elephant. (True/False)?: True
That's wrong.
The correct answer was: False.
Your current score is: 1/2

Q.3: Approximately one quarter of human bones are in the feet. (True/False)?: false
That's wrong.
The correct answer was: True.
Your current score is: 1/3

[...]

Q.12: A few ounces of chocolate can to kill a small dog. (True/False)?: true
You got it right!
The correct answer was: True.
Your current score is: 9/12

You've completed the quiz
Your final score was: 9/12
```

The program was built in six gateways, one per lecture part after the project set-up; the plan is in `docs/project-plan.md`.

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

Open `docs/doxygen/html/index.html` in a browser. The folder `docs/doxygen/` is generated and ignored by Git. The build fails on any undocumented module, class, function or parameter, so it also checks that the comments are complete.

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
│   ├── main.py                Entry point: builds the question bank and runs the quiz
│   ├── question_model.py      The Question class
│   └── quiz_brain.py          The QuizBrain class
├── tests/
│   ├── conftest.py            pytest fixtures
│   ├── fakes.py               Test double for the built-in input
│   ├── test_data.py           Tests of the course data
│   ├── test_main.py           Tests of the question bank and the entry point
│   ├── test_question_model.py Tests of the Question class
│   └── test_quiz_brain.py     Tests of the QuizBrain class
├── .gitignore
├── .gitmodules                Location of the framework submodule
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

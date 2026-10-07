"""Tests for the QuizBrain class (src/quiz_brain.py)."""

from collections.abc import Callable, Iterable

import pytest

from constants import (
    ANSWER_FALSE,
    ANSWER_TRUE,
    FEEDBACK_CORRECT_ANSWER,
    FEEDBACK_RIGHT,
    FEEDBACK_SCORE,
    FEEDBACK_WRONG,
    PROMPT_QUESTION,
)
from fakes import ScriptedInput
from question_model import Question
from quiz_brain import QuizBrain

FIRST_TEXT = "The sky is blue."
SECOND_TEXT = "Fish can fly."


def make_questions() -> list[Question]:
    return [
        Question(FIRST_TEXT, ANSWER_TRUE),
        Question(SECOND_TEXT, ANSWER_FALSE),
        Question("Water is wet.", ANSWER_TRUE),
    ]


def test_question_number_is_zero_when_the_quiz_is_created() -> None:
    quiz = QuizBrain(make_questions())

    assert quiz.question_number == 0


def test_question_list_is_the_given_list_when_the_quiz_is_created() -> None:
    questions = make_questions()

    quiz = QuizBrain(questions)

    assert quiz.question_list is questions


def test_first_prompt_shows_number_one_and_the_first_text_when_a_question_is_asked(
    scripted_input: ScriptedInput,
) -> None:
    quiz = QuizBrain(make_questions())

    quiz.next_question()

    assert scripted_input.prompts == ["Q.1: The sky is blue. (True/False)?: "]


def test_prompt_comes_from_the_prompt_constant_when_a_question_is_asked(
    scripted_input: ScriptedInput,
) -> None:
    quiz = QuizBrain(make_questions())

    quiz.next_question()

    assert scripted_input.prompts == [PROMPT_QUESTION.format(number=1, text=FIRST_TEXT)]


def test_prompt_asks_for_true_or_false_when_a_question_is_asked(
    scripted_input: ScriptedInput,
) -> None:
    quiz = QuizBrain(make_questions())

    quiz.next_question()

    assert f"({ANSWER_TRUE}/{ANSWER_FALSE})" in scripted_input.prompts[0]


@pytest.mark.usefixtures("scripted_input")
def test_question_number_is_one_after_the_first_question_is_asked() -> None:
    quiz = QuizBrain(make_questions())

    quiz.next_question()

    assert quiz.question_number == 1


def test_second_prompt_shows_number_two_and_second_text_when_two_are_asked(
    scripted_input: ScriptedInput,
) -> None:
    quiz = QuizBrain(make_questions())

    quiz.next_question()
    quiz.next_question()

    assert scripted_input.prompts[1] == PROMPT_QUESTION.format(
        number=2, text=SECOND_TEXT
    )
    assert quiz.question_number == 2


def test_one_answer_is_read_per_question_when_a_question_is_asked(
    scripted_input: ScriptedInput,
) -> None:
    quiz = QuizBrain(make_questions())

    quiz.next_question()

    assert len(scripted_input.prompts) == 1


@pytest.mark.usefixtures("scripted_input")
def test_question_list_is_unchanged_when_questions_are_asked() -> None:
    questions = make_questions()
    quiz = QuizBrain(questions)
    before = list(questions)

    quiz.next_question()
    quiz.next_question()

    assert quiz.question_list == before


def test_quiz_has_no_questions_left_when_the_question_list_is_empty() -> None:
    quiz = QuizBrain([])

    assert quiz.still_has_questions() is False


@pytest.mark.usefixtures("scripted_input")
@pytest.mark.parametrize(
    ("questions_asked", "expected"),
    [
        (0, True),  # the first question is still to be asked
        (1, True),
        (2, True),  # the last question is still to be asked
        (3, False),  # the last question has been asked: the quiz is over
    ],
)
def test_still_has_questions_follows_the_questions_asked_when_there_are_three(
    questions_asked: int, expected: bool
) -> None:
    quiz = QuizBrain(make_questions())

    for _ in range(questions_asked):
        quiz.next_question()

    assert quiz.still_has_questions() is expected


def test_a_loop_on_still_has_questions_asks_each_question_once(
    scripted_input: ScriptedInput,
) -> None:
    questions = make_questions()
    quiz = QuizBrain(questions)

    while quiz.still_has_questions():
        quiz.next_question()

    assert len(scripted_input.prompts) == len(questions)
    assert quiz.question_number == len(questions)


def test_score_is_zero_when_the_quiz_is_created() -> None:
    quiz = QuizBrain(make_questions())

    assert quiz.score == 0


@pytest.mark.parametrize(
    ("user_answer", "correct_answer"),
    [
        ("True", ANSWER_TRUE),
        ("true", ANSWER_TRUE),
        ("TRUE", ANSWER_TRUE),
        ("tRuE", ANSWER_TRUE),
        ("False", ANSWER_FALSE),
        ("false", ANSWER_FALSE),
        ("fAlSe", ANSWER_FALSE),
    ],
)
def test_score_goes_up_by_one_when_the_answer_is_right_in_any_letter_case(
    user_answer: str, correct_answer: str
) -> None:
    quiz = QuizBrain(make_questions())

    quiz.check_answer(user_answer, correct_answer)

    assert quiz.score == 1


@pytest.mark.parametrize(
    ("user_answer", "correct_answer"),
    [
        ("False", ANSWER_TRUE),
        ("true", ANSWER_FALSE),
        ("", ANSWER_TRUE),
        ("yes", ANSWER_TRUE),
        ("t", ANSWER_TRUE),
        ("maybe", ANSWER_FALSE),
    ],
)
def test_score_is_unchanged_when_the_answer_is_wrong_or_other_text(
    user_answer: str, correct_answer: str
) -> None:
    quiz = QuizBrain(make_questions())

    quiz.check_answer(user_answer, correct_answer)

    assert quiz.score == 0


def test_a_right_answer_shows_the_feedback_the_correct_answer_and_the_score(
    script_input: Callable[[Iterable[str]], ScriptedInput],
    capsys: pytest.CaptureFixture[str],
) -> None:
    script_input(["true"])
    quiz = QuizBrain([Question(FIRST_TEXT, ANSWER_TRUE)])

    quiz.next_question()

    assert capsys.readouterr().out == (
        f"{FEEDBACK_RIGHT}\n"
        f"{FEEDBACK_CORRECT_ANSWER.format(answer=ANSWER_TRUE)}\n"
        f"{FEEDBACK_SCORE.format(score=1, answered=1)}\n"
        "\n"
    )


def test_a_wrong_answer_shows_the_feedback_the_correct_answer_and_the_score(
    script_input: Callable[[Iterable[str]], ScriptedInput],
    capsys: pytest.CaptureFixture[str],
) -> None:
    script_input(["true"])
    quiz = QuizBrain([Question(SECOND_TEXT, ANSWER_FALSE)])

    quiz.next_question()

    assert capsys.readouterr().out == (
        f"{FEEDBACK_WRONG}\n"
        f"{FEEDBACK_CORRECT_ANSWER.format(answer=ANSWER_FALSE)}\n"
        f"{FEEDBACK_SCORE.format(score=0, answered=1)}\n"
        "\n"
    )


def test_next_question_checks_the_answer_against_the_answer_of_its_question(
    script_input: Callable[[Iterable[str]], ScriptedInput],
) -> None:
    script_input(["true", "true", "false"])  # right, wrong, wrong for True/False/True
    quiz = QuizBrain(make_questions())

    quiz.next_question()
    quiz.next_question()
    quiz.next_question()

    assert quiz.score == 1


def test_running_score_counts_the_questions_answered_when_three_are_asked(
    script_input: Callable[[Iterable[str]], ScriptedInput],
    capsys: pytest.CaptureFixture[str],
) -> None:
    script_input(["true", "false", "true"])  # all three right
    quiz = QuizBrain(make_questions())

    while quiz.still_has_questions():
        quiz.next_question()

    score_lines = [
        line for line in capsys.readouterr().out.splitlines() if "score" in line
    ]
    assert score_lines == [
        FEEDBACK_SCORE.format(score=1, answered=1),
        FEEDBACK_SCORE.format(score=2, answered=2),
        FEEDBACK_SCORE.format(score=3, answered=3),
    ]

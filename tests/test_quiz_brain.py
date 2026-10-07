"""Tests for the QuizBrain class (src/quiz_brain.py)."""

import pytest

from constants import ANSWER_FALSE, ANSWER_TRUE, PROMPT_QUESTION
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

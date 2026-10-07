"""Tests for the Question class (src/question_model.py)."""

from constants import ANSWER_FALSE, ANSWER_TRUE
from question_model import Question


def test_text_is_kept_when_question_is_created() -> None:
    question = Question("The sky is blue.", ANSWER_TRUE)

    assert question.text == "The sky is blue."


def test_answer_is_kept_when_question_is_created() -> None:
    question = Question("The sky is blue.", ANSWER_TRUE)

    assert question.answer == ANSWER_TRUE


def test_each_question_keeps_its_own_values_when_two_exist() -> None:
    first = Question("The sky is blue.", ANSWER_TRUE)
    second = Question("Fish can fly.", ANSWER_FALSE)

    assert (first.text, first.answer) == ("The sky is blue.", ANSWER_TRUE)
    assert (second.text, second.answer) == ("Fish can fly.", ANSWER_FALSE)


def test_attributes_can_be_read_as_plain_values_when_question_is_created() -> None:
    question = Question("Fish can fly.", ANSWER_FALSE)

    assert isinstance(question.text, str)
    assert isinstance(question.answer, str)

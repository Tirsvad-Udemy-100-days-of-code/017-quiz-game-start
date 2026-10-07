"""Tests for the course's question data (src/data.py)."""

from constants import ANSWER_FALSE, ANSWER_TRUE, QUESTION_KEY_ANSWER, QUESTION_KEY_TEXT
from data import question_data

EXPECTED_QUESTION_COUNT = 12


def test_question_data_has_twelve_entries() -> None:
    assert len(question_data) == EXPECTED_QUESTION_COUNT


def test_every_entry_has_exactly_the_text_and_answer_keys() -> None:
    for entry in question_data:
        assert set(entry) == {QUESTION_KEY_TEXT, QUESTION_KEY_ANSWER}


def test_every_text_is_not_empty() -> None:
    for entry in question_data:
        assert entry[QUESTION_KEY_TEXT].strip()


def test_every_answer_is_true_or_false() -> None:
    answers = {entry[QUESTION_KEY_ANSWER] for entry in question_data}
    assert answers <= {ANSWER_TRUE, ANSWER_FALSE}

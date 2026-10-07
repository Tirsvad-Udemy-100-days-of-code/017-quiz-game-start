"""Tests for the question bank and the entry point (src/main.py)."""

import importlib
import logging
import sys
from typing import NoReturn

import pytest

from constants import (
    ANSWER_FALSE,
    ANSWER_TRUE,
    LOG_QUESTIONS_LOADED,
    QUESTION_KEY_ANSWER,
    QUESTION_KEY_TEXT,
)
from data import question_data
from main import build_question_bank, main
from question_model import Question

EXPECTED_QUESTION_COUNT = 12


def test_bank_has_twelve_questions_when_built_from_the_course_data() -> None:
    question_bank = build_question_bank(question_data)

    assert len(question_bank) == EXPECTED_QUESTION_COUNT


def test_bank_holds_question_objects_when_built_from_the_course_data() -> None:
    question_bank = build_question_bank(question_data)

    assert all(isinstance(question, Question) for question in question_bank)


def test_bank_keeps_the_order_and_values_of_the_data_when_built() -> None:
    question_bank = build_question_bank(question_data)

    for question, entry in zip(question_bank, question_data, strict=True):
        assert question.text == entry[QUESTION_KEY_TEXT]
        assert question.answer == entry[QUESTION_KEY_ANSWER]


def test_bank_is_empty_when_the_data_is_empty() -> None:
    assert build_question_bank([]) == []


def test_bank_follows_the_given_data_when_it_is_not_the_course_data() -> None:
    raw_questions = [
        {QUESTION_KEY_TEXT: "The sky is blue.", QUESTION_KEY_ANSWER: ANSWER_TRUE},
        {QUESTION_KEY_TEXT: "Fish can fly.", QUESTION_KEY_ANSWER: ANSWER_FALSE},
    ]

    question_bank = build_question_bank(raw_questions)

    assert [(q.text, q.answer) for q in question_bank] == [
        ("The sky is blue.", ANSWER_TRUE),
        ("Fish can fly.", ANSWER_FALSE),
    ]


def test_main_logs_the_number_of_questions_when_it_runs(
    caplog: pytest.LogCaptureFixture,
) -> None:
    with caplog.at_level(logging.INFO):
        main()

    assert LOG_QUESTIONS_LOADED % EXPECTED_QUESTION_COUNT in caplog.messages


def test_importing_main_does_not_ask_for_input_or_print_when_imported(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    def fail_on_input(*args: object, **kwargs: object) -> NoReturn:
        raise AssertionError("input() must not be called when main is imported")

    monkeypatch.setattr("builtins.input", fail_on_input)
    monkeypatch.delitem(sys.modules, "main", raising=False)

    importlib.import_module("main")

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""

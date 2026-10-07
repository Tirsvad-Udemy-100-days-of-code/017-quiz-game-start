"""Tests for the question bank and the entry point (src/main.py)."""

import importlib
import logging
import sys
from collections.abc import Callable, Iterable
from typing import NoReturn

import pytest

from constants import (
    ANSWER_FALSE,
    ANSWER_TRUE,
    FEEDBACK_SCORE,
    LOG_QUESTIONS_LOADED,
    MESSAGE_FINAL_SCORE,
    MESSAGE_QUIZ_COMPLETE,
    PROMPT_QUESTION,
    QUESTION_KEY_ANSWER,
    QUESTION_KEY_TEXT,
)
from data import question_data
from fakes import ScriptedInput
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


@pytest.mark.usefixtures("scripted_input")
def test_main_logs_the_number_of_questions_when_it_runs(
    caplog: pytest.LogCaptureFixture,
) -> None:
    with caplog.at_level(logging.INFO):
        main()

    assert LOG_QUESTIONS_LOADED % EXPECTED_QUESTION_COUNT in caplog.messages


def test_main_asks_every_question_in_order_when_it_runs(
    scripted_input: ScriptedInput,
) -> None:
    main()

    expected_prompts = [
        PROMPT_QUESTION.format(number=number, text=entry[QUESTION_KEY_TEXT])
        for number, entry in enumerate(question_data, start=1)
    ]
    assert scripted_input.prompts == expected_prompts


def test_main_asks_exactly_twelve_questions_when_twelve_answers_are_scripted(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fake_input = ScriptedInput([ANSWER_TRUE] * EXPECTED_QUESTION_COUNT)
    monkeypatch.setattr("builtins.input", fake_input)

    main()

    assert len(fake_input.prompts) == EXPECTED_QUESTION_COUNT


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


def right_answers() -> list[str]:
    return [entry[QUESTION_KEY_ANSWER] for entry in question_data]


def wrong_answers() -> list[str]:
    return [
        ANSWER_FALSE if entry[QUESTION_KEY_ANSWER] == ANSWER_TRUE else ANSWER_TRUE
        for entry in question_data
    ]


def test_final_result_shows_a_full_score_when_all_twelve_answers_are_right(
    script_input: Callable[[Iterable[str]], ScriptedInput],
    capsys: pytest.CaptureFixture[str],
) -> None:
    script_input(right_answers())

    main()

    lines = capsys.readouterr().out.splitlines()
    full_score = MESSAGE_FINAL_SCORE.format(
        score=EXPECTED_QUESTION_COUNT, total=EXPECTED_QUESTION_COUNT
    )
    assert lines[-3:] == ["", MESSAGE_QUIZ_COMPLETE, full_score]
    assert lines.count(MESSAGE_QUIZ_COMPLETE) == 1


def test_final_result_shows_a_zero_score_when_all_twelve_answers_are_wrong(
    script_input: Callable[[Iterable[str]], ScriptedInput],
    capsys: pytest.CaptureFixture[str],
) -> None:
    script_input(wrong_answers())

    main()

    lines = capsys.readouterr().out.splitlines()
    zero_score = MESSAGE_FINAL_SCORE.format(score=0, total=EXPECTED_QUESTION_COUNT)
    assert lines[-2:] == [MESSAGE_QUIZ_COMPLETE, zero_score]


def test_final_result_counts_the_right_answers_when_every_answer_is_true(
    script_input: Callable[[Iterable[str]], ScriptedInput],
    capsys: pytest.CaptureFixture[str],
) -> None:
    script_input([ANSWER_TRUE] * EXPECTED_QUESTION_COUNT)
    true_answers = sum(
        1 for entry in question_data if entry[QUESTION_KEY_ANSWER] == ANSWER_TRUE
    )

    main()

    lines = capsys.readouterr().out.splitlines()
    assert lines[-1] == MESSAGE_FINAL_SCORE.format(
        score=true_answers, total=EXPECTED_QUESTION_COUNT
    )


def test_running_score_follows_every_answer_when_all_twelve_answers_are_right(
    script_input: Callable[[Iterable[str]], ScriptedInput],
    capsys: pytest.CaptureFixture[str],
) -> None:
    script_input(right_answers())
    expected = [
        FEEDBACK_SCORE.format(score=number, answered=number)
        for number in range(1, EXPECTED_QUESTION_COUNT + 1)
    ]

    main()

    lines = capsys.readouterr().out.splitlines()
    assert [line for line in lines if line in expected] == expected

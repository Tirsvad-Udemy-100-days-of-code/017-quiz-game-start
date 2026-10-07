"""Test doubles shared by the tests."""

from collections.abc import Iterable

from constants import ANSWER_TRUE


class ScriptedInput:
    """Stands in for the built-in input: records prompts, returns scripted answers.

    When the script runs out it keeps answering with the word for true.
    """

    def __init__(self, answers: Iterable[str] = ()) -> None:
        self._answers = iter(answers)
        self.prompts: list[str] = []

    def __call__(self, prompt: str = "") -> str:
        self.prompts.append(prompt)
        return next(self._answers, ANSWER_TRUE)

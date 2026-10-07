"""Fixtures shared by the tests."""

from collections.abc import Callable, Iterable

import pytest

from fakes import ScriptedInput


@pytest.fixture
def scripted_input(monkeypatch: pytest.MonkeyPatch) -> ScriptedInput:
    """Replace the built-in input with a ScriptedInput and return it."""
    fake = ScriptedInput()
    monkeypatch.setattr("builtins.input", fake)
    return fake


@pytest.fixture
def script_input(
    monkeypatch: pytest.MonkeyPatch,
) -> Callable[[Iterable[str]], ScriptedInput]:
    """Return a function that replaces input with a ScriptedInput of given answers."""

    def install(answers: Iterable[str]) -> ScriptedInput:
        fake = ScriptedInput(answers)
        monkeypatch.setattr("builtins.input", fake)
        return fake

    return install

"""Fixtures shared by the tests."""

import pytest

from fakes import ScriptedInput


@pytest.fixture
def scripted_input(monkeypatch: pytest.MonkeyPatch) -> ScriptedInput:
    """Replace the built-in input with a ScriptedInput and return it."""
    fake = ScriptedInput()
    monkeypatch.setattr("builtins.input", fake)
    return fake

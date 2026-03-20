"""
This Modul contain the configurations for the test
"""

import pytest


@pytest.fixture
def fake_input(monkeypatch):
    """Mock the input()"""
    def _fake_input(value):
        monkeypatch.setattr("builtins.input", lambda _: value)

    return _fake_input

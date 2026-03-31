"""
This Modul contain the configurations for the test
"""

import sqlite3
from collections.abc import Iterable
import builtins
import pytest

from classes.services_manager import ServicesManager


@pytest.fixture
def fake_input(monkeypatch):
    """Mock de input() que funciona con valores simples o iterables."""

    def _fake_input(values):
        if isinstance(values, Iterable) and not isinstance(values, str):
            it = iter(values)
            monkeypatch.setattr(builtins, "input", lambda _: next(it))
        else:
            monkeypatch.setattr(builtins, "input", lambda _: values)

    return _fake_input


@pytest.fixture
def fixture_service_manager():
    """Mock the DB services with a non persisten DB"""
    service_manager = ServicesManager()
    service_manager.conn_db_services = sqlite3.connect(":memory:")
    service_manager.cursor_db_services = service_manager.conn_db_services.cursor()
    service_manager._create_services_db()

    return service_manager

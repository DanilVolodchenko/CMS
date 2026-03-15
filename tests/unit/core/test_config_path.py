import importlib
from pathlib import Path, PosixPath

import pytest

from core import config_path


def test_base_path(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test BASE_PATH variable."""

    monkeypatch.setattr(Path, 'cwd', lambda: Path('/crm'))

    importlib.reload(config_path)  # reload config_path module

    result = config_path.BASE_PATH
    expected_result = PosixPath('/crm')

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_coverage_test_path(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test COVERAGE_TEST_PATH variable."""

    monkeypatch.setattr(Path, 'cwd', lambda: Path('/crm'))

    importlib.reload(config_path)

    result = config_path.COVERAGE_TEST_PATH
    expected_result = PosixPath('/crm') / 'htmlcov'

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

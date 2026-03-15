import dataclasses
from typing import Any

from domain.entities import PageDM


def test_page_db_fields() -> None:
    """Testing PageDM fields."""

    obj = PageDM

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [{'page': str}, {'components': list[Any]}]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

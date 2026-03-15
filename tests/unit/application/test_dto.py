import dataclasses
from typing import Any

from application.dto import ComponentDTO, NewPageComponentDTO


def test_new_page_component_dto_fields() -> None:
    """Testing NewPageComponentDTO fields."""

    obj = NewPageComponentDTO

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [{'page': str}, {'components': list[Any]}]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_component_dto_fields() -> None:
    """Testing ComponentDTO fields."""

    obj = ComponentDTO

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [{'name': str}, {'fields': Any}]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

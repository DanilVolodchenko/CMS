import dataclasses

from infrastructure.schemas.header import HeaderSchema


def test_link_schema() -> None:
    """Testing obj name and type of HeaderSchema."""

    obj = HeaderSchema

    result = [field.name for field in dataclasses.fields(obj)]
    expected_result = ['navigation', 'title']

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

import dataclasses

from infrastructure.schemas.main import MainSchema


def test_main_schema() -> None:
    """Testing obj name and type of MainSchema."""

    obj = MainSchema

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [
        {'description': str},
        {'summary': str},
        {'title': str},
    ]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

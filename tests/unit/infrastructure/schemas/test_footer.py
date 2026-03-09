import dataclasses

from infrastructure.schemas.footer import Column, FooterSchema, Link


def test_footer_schema() -> None:
    """Testing obj name and type of FooterSchema."""

    obj = FooterSchema

    result = [field.name for field in dataclasses.fields(obj)]
    expected_result = ['columns']

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_column_schema() -> None:
    """Testing obj name and type of Column."""

    obj = Column

    result = [field.name for field in dataclasses.fields(obj)]
    expected_result = ['title', 'links']

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_link_schema() -> None:
    """Testing obj name and type of Link."""

    obj = Link

    result = [field.name for field in dataclasses.fields(obj)]
    expected_result = ['url', 'label']

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

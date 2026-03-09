import dataclasses

from infrastructure import fields


def test_title_field() -> None:
    """Testing obj name and type of TitleField."""

    obj = fields.TitleField

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [
        {'title': str},
    ]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_summary_field() -> None:
    """Testing obj name and type of SummaryField."""

    obj = fields.SummaryField

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [
        {'summary': str},
    ]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_description_field() -> None:
    """Testing obj name and type of DescriptionField."""

    obj = fields.DescriptionField

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [
        {'description': str},
    ]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_label_field() -> None:
    """Testing obj name and type of LabelField."""

    obj = fields.LabelField

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [
        {'label': str},
    ]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_url_field() -> None:
    """Testing obj name and type of UrlField."""

    obj = fields.UrlField

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [
        {'url': str},
    ]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_navigation_field() -> None:
    """Testing obj name and type of NavigationField."""

    obj = fields.NavigationField

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [
        {'navigation': list[str]},
    ]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

import dataclasses

from infrastructure import mixins


def test_title_summary_desc_mixin() -> None:
    """Testing obj name and type of TitleSummaryDescMixin."""

    obj = mixins.TitleSummaryDescMixin

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [
        {'description': str},
        {'summary': str},
        {'title': str},
    ]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_link_mixin() -> None:
    """Testing obj name and type of LinkMixin."""

    obj = mixins.LinkMixin

    result = [{field.name: field.type} for field in dataclasses.fields(obj)]
    expected_result = [
        {'url': str},
        {'label': str},
    ]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

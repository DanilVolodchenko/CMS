from unittest import mock

from application import dto
from controllers.http.v1 import admin


def test_get_components_schema() -> None:
    """Test get_components_schema."""

    interactor = mock.Mock()
    interactor.side_effect = lambda: [dto.ComponentDTO(name='test', fields={'test': 'test'})]

    result = admin.get_components_schema(interactor)
    expected_result = [dto.ComponentDTO(name='test', fields={'test': 'test'})]

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_get_component_schema_by_name() -> None:
    """Test get_component_schema_by_name."""

    interactor = mock.Mock()
    interactor.side_effect = lambda name: dto.ComponentDTO(name=name, fields={'test': 'test'})

    result = admin.get_component_schema_by_name('test', interactor)
    expected_result = dto.ComponentDTO(name='test', fields={'test': 'test'})

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

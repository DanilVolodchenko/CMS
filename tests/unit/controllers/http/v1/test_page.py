from unittest import mock

from controllers.http.v1 import page, schemas
from domain.entities import PageDM


def test_get_components() -> None:
    """Test get_components."""

    interactor = mock.Mock()
    interactor.side_effect = lambda page: PageDM(page=page, components=[{'test': 'test'}])

    result = page.get_components('/test', interactor)
    expected_result = schemas.PageSchema(page='/test', components=[{'test': 'test'}])

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_create_components() -> None:
    """Test create_components."""

    page_schema = schemas.PageSchema(page='/test', components=[{'test': 'test'}])
    get_component_interactor = mock.Mock()
    get_component_interactor.side_effect = lambda page: PageDM(page=page, components=[{'test': 'test'}])
    create_component_interactor = mock.Mock()
    create_component_interactor.side_effect = lambda *args: None

    result = page.create_components(page_schema, get_component_interactor, create_component_interactor)
    expected_result = schemas.PageSchema(page='/test', components=[{'test': 'test'}])

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

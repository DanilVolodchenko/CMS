from typing import Any
from unittest import mock

import pytest

from application import interactors
from application.dto import ComponentDTO, NewPageComponentDTO
from domain.entities import PageDM
from infrastructure import errors


@pytest.fixture
def mock_component() -> mock.Mock:
    component = mock.Mock()
    component.name = 'test'
    component.schema = {'test': '[str]'}

    return component


@pytest.fixture
def mock_register_builder(mock_component: mock.Mock) -> mock.Mock:
    builder = mock.Mock()
    builder.get_components.return_value = [mock_component, mock_component]

    return builder


@pytest.fixture
def mock_register_builder_empty_components(mock_component: mock.Mock) -> mock.Mock:
    builder = mock.Mock()
    builder.get_components.return_value = []

    return builder


@pytest.fixture
def mock_dispatcher() -> mock.Mock:
    def generate(schema: Any) -> Any:
        return schema

    dispatcher = mock.Mock()
    dispatcher.generate = generate

    return dispatcher


class TestGetComponentsSchemaInteractor:
    """Test suite for GetComponentsSchemaInteractor."""

    def test_get_components_if_components_exists(
            self, mock_register_builder: mock.Mock, mock_dispatcher: mock.Mock,
    ) -> None:
        """Test interactor if components exists."""

        interactor = interactors.GetComponentsSchemaInteractor(mock_register_builder, mock_dispatcher)

        result = interactor()
        expected_result = [
            ComponentDTO(name='test', fields={'test': '[str]'}),
            ComponentDTO(name='test', fields={'test': '[str]'}),
        ]

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_get_components_if_components_not_exists(
            self, mock_register_builder_empty_components: mock.Mock, mock_dispatcher: mock.Mock,
    ) -> None:
        """Test interactor if components not exists."""

        interactor = interactors.GetComponentsSchemaInteractor(mock_register_builder_empty_components, mock_dispatcher)

        result = interactor()
        expected_result = []

        assert result == expected_result, f'Expected result {expected_result}, result {result}'


class TestGetComponentSchemaByNameInteractor:
    """Test suite for GetComponentSchemaByNameInteractor."""

    def test_get_component_if_component_exists(
            self, mock_register_builder: mock.Mock, mock_dispatcher: mock.Mock,
    ) -> None:
        """Test interactor if component exists."""

        interactor = interactors.GetComponentSchemaByNameInteractor(mock_register_builder, mock_dispatcher)

        result = interactor('test')
        expected_result = ComponentDTO(name='test', fields={'test': '[str]'})

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_get_component_if_component_not_exists(
            self, mock_register_builder_empty_components: mock.Mock, mock_dispatcher: mock.Mock,
    ) -> None:
        """Test interactor if component not exists."""

        interactor = interactors.GetComponentSchemaByNameInteractor(
            mock_register_builder_empty_components, mock_dispatcher,
        )

        with pytest.raises(errors.ComponentNotFoundError):
            interactor('test')


class TestGetComponentsByPathInteractor:
    """Test suite for GetComponentsByPathInteractor."""

    def test_get_component_if_component_exists(self) -> None:
        """Test interactor if component by path exists."""

        component_gateway = mock.Mock()
        component_gateway.get_by_page.return_value = PageDM(page='/page', components=[{'test': 'test'}])
        interactor = interactors.GetComponentsByPageInteractor(component_gateway=component_gateway)

        result = interactor('/page')
        expected_result = PageDM(page='/page', components=[{'test': 'test'}])

        component_gateway.get_by_page.assert_called_with(page='/page')
        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_get_component_if_component_not_exists(self) -> None:
        """Test interactor if component by path not exists."""

        component_gateway = mock.Mock()
        component_gateway.get_by_page.side_effect = KeyError('Component not found')
        interactor = interactors.GetComponentsByPageInteractor(component_gateway=component_gateway)

        with pytest.raises(errors.PageNotFoundError):
            interactor('/path')


class TestCreateComponentInteractor:
    """Test suite for CreateComponentInteractor."""

    def test_create_component_if_component_by_page_not_exists(self) -> None:
        """Test interactor if component by page not exists."""

        component_gateway = mock.Mock()
        component_gateway.save.return_value = None
        interactor = interactors.CreateComponentInteractor(component_gateway=component_gateway)

        result = interactor(NewPageComponentDTO(page='/page', components=[{'test': 'test'}]))
        expected_result = None

        component_gateway.save.assert_called_with(PageDM(page='/page', components=[{'test': 'test'}]))
        assert result == expected_result, f'Expected result {expected_result}, result {result}'

from typing import Any

import pytest
from unittest import mock

from application.dto import ComponentDTO
from application.interactors import GetComponentsSchemaInteractor


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
            self, mock_register_builder: mock.Mock, mock_dispatcher: mock.Mock
    ) -> None:
        """Test interactor if components exists."""

        interactor = GetComponentsSchemaInteractor(mock_register_builder, mock_dispatcher)

        result = interactor()
        expected_result = [
            ComponentDTO(name='test', fields={'test': '[str]'}),
            ComponentDTO(name='test', fields={'test': '[str]'}),
        ]

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_get_components_if_components_not_exists(
            self, mock_register_builder_empty_components: mock.Mock, mock_dispatcher: mock.Mock
    ) -> None:
        """Test interactor if components not exists."""

        interactor = GetComponentsSchemaInteractor(mock_register_builder_empty_components, mock_dispatcher)

        result = interactor()
        expected_result = []

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

from typing import Any

import pytest

from infrastructure.builder import RegisterBuilder
from infrastructure.components.interfaces import IComponent
from infrastructure.dispatcher import IFieldDispatcher
from infrastructure.generators.interfaces import IFieldGenerator


@pytest.fixture
def builder() -> RegisterBuilder:
    return RegisterBuilder()


class MockComponent1(IComponent):
    name = '1'
    schema = 'schema 1'


class MockComponent2(IComponent):
    name = '2'
    schema = 'schema 2'


class MockGenerator1(IFieldGenerator):
    @classmethod
    def supports(cls, schema: Any) -> bool: ...  # type: ignore[empty-body]

    def generate(self, schema: Any, dispatcher: IFieldDispatcher) -> Any: ...


class MockGenerator2(IFieldGenerator):
    @classmethod
    def supports(cls, schema: Any) -> bool: ...  # type: ignore[empty-body]

    def generate(self, schema: Any, dispatcher: IFieldDispatcher) -> Any: ...


class TestRegisterBuilder:
    """Tests suite for RegisterBuilder."""

    def test_get_components_if_array_is_empty(self, builder: RegisterBuilder) -> None:
        """Test get_components method if array is empty."""

        result = builder.get_components()
        expected_result = []

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_get_generators_if_array_is_empty(self, builder: RegisterBuilder) -> None:
        """Test get_generators method if array is empty."""

        result = builder.get_generators()
        expected_result = []

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_add_components(self, builder: RegisterBuilder) -> None:
        """Test add_components method."""

        builder.add_components(MockComponent1, MockComponent2)

        result = builder._components  # noqa: SLF001
        expected_result = [MockComponent1, MockComponent2]

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_add_generators(self, builder: RegisterBuilder) -> None:
        """Test add_generators method."""

        builder.add_generators(MockGenerator1, MockGenerator2)

        result = builder._generators  # noqa: SLF001
        expected_result = [MockGenerator1, MockGenerator2]

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_get_components_if_array_is_not_empty(self, builder: RegisterBuilder) -> None:
        """Test get_components method if array is not empty."""

        builder._components = [MockComponent1, MockComponent2]  # noqa: SLF001

        result = builder.get_components()
        expected_result = [MockComponent1, MockComponent2]

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_get_generators_if_array_is_not_empty(self, builder: RegisterBuilder) -> None:
        """Test get_generators method if array is not empty."""

        builder._generators = [MockGenerator1, MockGenerator2]  # noqa: SLF001

        result = builder.get_generators()
        expected_result = [MockGenerator1, MockGenerator2]

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

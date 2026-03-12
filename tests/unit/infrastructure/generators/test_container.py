from typing import Any

import pytest

from infrastructure.generators.container import ContainerGenerator
from infrastructure.dispatcher import IFieldDispatcher


@pytest.fixture
def container_generator() -> ContainerGenerator:
    return ContainerGenerator()


@pytest.fixture
def dispatcher() -> IFieldDispatcher:
    class MockDispatcher(IFieldDispatcher):
        def generate(self, schema: Any) -> Any:
            return str

        def get_type_name(self, obj: Any) -> str: ...

    return MockDispatcher()


class TestContainerGenerator:
    """Tests suite for ContainerGenerator."""

    @pytest.mark.parametrize('schema', [(list[str]), (dict[str, str]), (set[str])])
    def test_supports_if_schema_is_container(
            self, schema: list | dict | set, container_generator: ContainerGenerator
    ) -> None:
        """Tests supports method if schema is container."""

        result = container_generator.supports(schema)
        expected_result = True

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_supports_if_schema_is_not_container(self, container_generator: ContainerGenerator) -> None:
        """Tests supports method if schema is not container."""

        schema = object

        result = container_generator.supports(schema)
        expected_result = False

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    @pytest.mark.parametrize(
        ('schema', 'expected_result'), [
            (list[str], [str]), (dict[str, str], {'key': str, 'value': str}), (set[str], [str]), (tuple[str], [str])
        ]
    )
    def test_generate_if_schema_is_dataclass(
            self, schema, expected_result, container_generator: ContainerGenerator, dispatcher: IFieldDispatcher
    ) -> None:
        """Tests generate method if schema is dataclass."""

        result = container_generator.generate(schema, dispatcher)

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_generate_if_schema_is_not_dataclass(
            self, container_generator: ContainerGenerator, dispatcher: IFieldDispatcher
    ) -> None:
        """Tests generate method if schema is not container."""

        schema = object

        result = container_generator.generate(schema, dispatcher)
        expected_result = None

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

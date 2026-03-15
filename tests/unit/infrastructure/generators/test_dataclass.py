import dataclasses
from typing import Any

import pytest

from infrastructure.dispatcher import IFieldDispatcher
from infrastructure.generators.dataclass import DataclassGenerator


@pytest.fixture
def dataclass_generator() -> DataclassGenerator:
    return DataclassGenerator()


@pytest.fixture
def dispatcher() -> IFieldDispatcher:
    class MockDispatcher(IFieldDispatcher):
        def generate(self, schema: Any) -> Any:
            return str

        def get_type_name(self, obj: Any) -> str: ...  # type: ignore[empty-body]

    return MockDispatcher()


@dataclasses.dataclass
class MockDataclassSchema:
    field: str


class TestDataclassGenerator:
    """Tests suite for DataclassGenerator."""

    def test_supports_if_schema_is_dataclass(self, dataclass_generator: DataclassGenerator) -> None:
        """Tests supports method if schema is dataclass."""

        schema = MockDataclassSchema

        result = dataclass_generator.supports(schema)
        expected_result = True

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_supports_if_schema_is_not_dataclass(self, dataclass_generator: DataclassGenerator) -> None:
        """Tests supports method if schema is not dataclass."""

        schema = []

        result = dataclass_generator.supports(schema)
        expected_result = False

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_generate_if_schema_is_dataclass(
            self, dataclass_generator: DataclassGenerator, dispatcher: IFieldDispatcher,
    ) -> None:
        """Tests generate method if schema is dataclass."""

        schema = MockDataclassSchema

        result = dataclass_generator.generate(schema, dispatcher)
        expected_result = {'field': str}

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_generate_if_schema_is_not_dataclass(
            self, dataclass_generator: DataclassGenerator, dispatcher: IFieldDispatcher,
    ) -> None:
        """Tests generate method if schema is not dataclass."""

        schema = []

        with pytest.raises(TypeError):
            dataclass_generator.generate(schema, dispatcher)

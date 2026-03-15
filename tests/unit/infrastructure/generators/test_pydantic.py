from typing import Any

import pytest
from pydantic import BaseModel

from infrastructure.dispatcher import IFieldDispatcher
from infrastructure.generators.pydantic import PydanticGenerator


@pytest.fixture
def pydantic_generator() -> PydanticGenerator:
    return PydanticGenerator()


@pytest.fixture
def dispatcher() -> IFieldDispatcher:
    class MockDispatcher(IFieldDispatcher):
        def generate(self, schema: Any) -> Any:
            return str

        def get_type_name(self, obj: Any) -> str: ...  # type: ignore[empty-body]

    return MockDispatcher()


class MockPydanticSchema(BaseModel):
    field: str


class TestDataclassGenerator:
    """Tests suite for DataclassGenerator."""

    def test_supports_if_schema_is_dataclass(self, pydantic_generator: PydanticGenerator) -> None:
        """Tests supports method if schema is pydantic model."""

        schema = MockPydanticSchema

        result = pydantic_generator.supports(schema)
        expected_result = True

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_supports_if_schema_is_not_dataclass(self, pydantic_generator: PydanticGenerator) -> None:
        """Tests supports method if schema is not pydantic model."""

        schema = []

        result = pydantic_generator.supports(schema)
        expected_result = False

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_generate_if_schema_is_dataclass(
            self, pydantic_generator: PydanticGenerator, dispatcher: IFieldDispatcher,
    ) -> None:
        """Tests generate method if schema is pydantic model."""

        schema = MockPydanticSchema

        result = pydantic_generator.generate(schema, dispatcher)
        expected_result = {'field': str}

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_generate_if_schema_is_not_dataclass(
            self, pydantic_generator: PydanticGenerator, dispatcher: IFieldDispatcher,
    ) -> None:
        """Tests generate method if schema is not pydantic model."""

        schema = []

        result = pydantic_generator.generate(schema, dispatcher)
        expected_result = {}

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

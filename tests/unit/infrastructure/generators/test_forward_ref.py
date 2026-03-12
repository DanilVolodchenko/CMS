from annotationlib import ForwardRef
from typing import Any

import pytest

from infrastructure.generators.forward_ref import ForwardRefGenerator
from infrastructure.dispatcher import IFieldDispatcher


@pytest.fixture
def forward_ref_generator() -> ForwardRefGenerator:
    return ForwardRefGenerator()


@pytest.fixture
def dispatcher() -> IFieldDispatcher:
    class MockDispatcher(IFieldDispatcher):
        def generate(self, schema: Any) -> Any:
            return str

        def get_type_name(self, obj: Any) -> str: ...

    return MockDispatcher()


class TestForwardRefGenerator:
    """Tests suite for ForwardRefGenerator."""

    def test_supports_if_schema_is_forward_ref(self, forward_ref_generator: ForwardRefGenerator) -> None:
        """Tests supports method if schema is ForwardRef."""

        schema = ForwardRef('str')

        result = forward_ref_generator.supports(schema)
        expected_result = True

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_supports_if_schema_is_not_forward_ref(self, forward_ref_generator: ForwardRefGenerator) -> None:
        """Tests supports method if schema is not ForwardRef."""

        schema = []

        result = forward_ref_generator.supports(schema)
        expected_result = False

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_generate_if_schema_is_forward_ref(
            self, forward_ref_generator: ForwardRefGenerator, dispatcher: IFieldDispatcher
    ) -> None:
        """Tests generate method if schema is ForwardRef."""

        schema = ForwardRef('str')

        result = forward_ref_generator.generate(schema, dispatcher)
        expected_result = str

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_generate_if_schema_is_not_dataclass(
            self, forward_ref_generator: ForwardRefGenerator, dispatcher: IFieldDispatcher
    ) -> None:
        """Tests generate method if schema is not dataclass."""

        schema = []

        with pytest.raises(AttributeError):
            forward_ref_generator.generate(schema, dispatcher)

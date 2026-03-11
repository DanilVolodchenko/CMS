from typing import Any

import pytest

from infrastructure.builder import IFieldGeneratorBuilder
from infrastructure.dispatcher import FieldDispatcher
from infrastructure.generators.interfaces import IFieldGenerator


class MockRegisterBuilder(IFieldGeneratorBuilder):

    def get_generators(self) -> list[type[IFieldGenerator]]: ...  # type: ignore[empty-body]

    def add_generators(self, *generators: type[IFieldGenerator]) -> None: ...


@pytest.fixture
def dispatcher() -> FieldDispatcher:
    builder = MockRegisterBuilder()

    return FieldDispatcher(builder=builder)


class MockObj: ...


class TestFieldDispatcher:
    """Tests suite for FieldDispatcher."""

    @pytest.mark.parametrize(
        ('obj', 'expected_result'), [(list, 'list'), (dict, 'dict'), (set, 'set'), (str, 'str'), (MockObj, 'MockObj')],
    )
    def test_get_type_name_if_has_attr___name__(
            self, obj: Any, expected_result: str, dispatcher: FieldDispatcher,
    ) -> None:
        """Test method get_type_name if obj has attr __name__."""

        result = dispatcher.get_type_name(obj)

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    @pytest.mark.parametrize(
        ('cls', 'expected_result'), [(list, '[]'), (dict, '{}'), (set, 'set()')],
    )
    def test_get_type_name_if_has_not_attr___name__(
            self, cls: Any, expected_result: str, dispatcher: FieldDispatcher,
    ) -> None:
        """Test method get_type_name if obj has not attr __name__."""

        result = dispatcher.get_type_name(cls())

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

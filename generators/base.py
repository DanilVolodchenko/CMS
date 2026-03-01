import abc
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from dispatcher import FieldDispatcher


class IFieldGenerator(abc.ABC):
    registry: list['IFieldGenerator'] = []

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if not abc.ABC in cls.__bases__:
            IFieldGenerator.registry.append(cls())

    @classmethod
    @abc.abstractmethod
    def supports(cls, schema: Any) -> bool:
        """Can support that type of schema."""

    @abc.abstractmethod
    def generate(self, schema: Any, dispatcher: 'FieldDispatcher') -> Any:
        """Generate data from schema."""

import abc
from typing import TYPE_CHECKING, Any, ClassVar

if TYPE_CHECKING:
    from infrastructure.dispatcher import FieldDispatcher


class IFieldGenerator(abc.ABC):
    registry: ClassVar[list[IFieldGenerator]] = []

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        if abc.ABC not in cls.__bases__:
            IFieldGenerator.registry.append(cls())

    @classmethod
    @abc.abstractmethod
    def supports(cls, schema: Any) -> bool:
        """Can support that type of schema."""

    @abc.abstractmethod
    def generate(self, schema: Any, dispatcher: type[FieldDispatcher]) -> Any:
        """Generate data from schema."""

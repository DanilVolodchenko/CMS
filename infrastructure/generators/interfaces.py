import abc
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from infrastructure.dispatcher import IFieldDispatcher


class IFieldGenerator(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def supports(cls, schema: Any) -> bool:
        """Can support that type of schema."""

    @abc.abstractmethod
    def generate(self, schema: Any, dispatcher: IFieldDispatcher) -> Any:
        """Generate data from schema."""

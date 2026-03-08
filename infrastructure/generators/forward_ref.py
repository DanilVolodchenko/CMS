from annotationlib import ForwardRef
from typing import TYPE_CHECKING, Any

from infrastructure.generators.interfaces import IFieldGenerator

if TYPE_CHECKING:
    from infrastructure.dispatcher import FieldDispatcher


class ForwardRefGenerator(IFieldGenerator):
    @classmethod
    def supports(cls, schema: Any) -> bool:
        return isinstance(schema, ForwardRef)

    def generate(self, schema: Any, dispatcher: type[FieldDispatcher]) -> Any:
        return dispatcher.generate(schema.evaluate())

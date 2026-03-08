from annotationlib import ForwardRef
from typing import TYPE_CHECKING, Any

from generators import IFieldGenerator

if TYPE_CHECKING:
    from dispatcher import FieldDispatcher


class ForwardRefGenerator(IFieldGenerator):

    @classmethod
    def supports(cls, schema: Any) -> bool:
        return isinstance(schema, ForwardRef)

    def generate(self, schema: Any, dispatcher: FieldDispatcher) -> Any:
        return dispatcher.generate(schema.evaluate())

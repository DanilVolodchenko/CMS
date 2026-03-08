from typing import TYPE_CHECKING, Any

from generators.base import IFieldGenerator

if TYPE_CHECKING:
    from dispatcher import FieldDispatcher

try:
    from pydantic import BaseModel
except ImportError:
    BaseModel = None


class PydanticGenerator(IFieldGenerator):

    @classmethod
    def supports(cls, schema: Any) -> bool:
        return BaseModel is not None and isinstance(schema, type) and issubclass(schema, BaseModel)

    def generate(self, schema: Any, dispatcher: FieldDispatcher) -> dict:
        result = {}

        # pydantic v2
        if hasattr(schema, "model_fields"):
            for name, field in schema.model_fields.items():
                result[name] = dispatcher.generate(field.annotation)

        # pydantic v1
        elif hasattr(schema, "__fields__"):
            for name, field in schema.__fields__.items():
                result[name] = dispatcher.generate(field.outer_type_)

        return result

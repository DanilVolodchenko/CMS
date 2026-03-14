from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

from infrastructure.generators.interfaces import IFieldGenerator

if TYPE_CHECKING:
    from infrastructure.dispatcher import IFieldDispatcher


class PydanticGenerator(IFieldGenerator):
    @classmethod
    def supports(cls, schema: Any) -> bool:
        return BaseModel is not None and isinstance(schema, type) and issubclass(schema, BaseModel)

    @classmethod
    def generate(cls, schema: Any, dispatcher: IFieldDispatcher) -> dict:
        result = {}

        if hasattr(schema, 'model_fields'):
            for name, field in schema.model_fields.items():
                result[name] = dispatcher.generate(field.annotation)

        return result

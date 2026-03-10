import dataclasses
from typing import TYPE_CHECKING, Any

from infrastructure.generators.interfaces import IFieldGenerator

if TYPE_CHECKING:
    from infrastructure.dispatcher import IFieldDispatcher


class DataclassGenerator(IFieldGenerator):
    @classmethod
    def supports(cls, schema: Any) -> bool:
        return dataclasses.is_dataclass(schema)

    def generate(self, schema: Any, dispatcher: IFieldDispatcher) -> dict:
        result = {}

        for field in dataclasses.fields(schema):
            result[field.name] = dispatcher.generate(field.type)

        return result

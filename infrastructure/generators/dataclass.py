import dataclasses
from typing import TYPE_CHECKING, Any

from generators.base import IFieldGenerator

if TYPE_CHECKING:
    from dispatcher import FieldDispatcher


class DataclassGenerator(IFieldGenerator):

    @classmethod
    def supports(cls, schema: Any) -> bool:
        return dataclasses.is_dataclass(schema)

    def generate(self, schema: Any, dispatcher: FieldDispatcher) -> dict:
        result = {}

        for field in dataclasses.fields(schema):
            result[field.name] = dispatcher.generate(field.type)

        return result

from typing import Any

from generators import IFieldGenerator


class FieldDispatcher:

    def __init__(self):
        self._generators: list[IFieldGenerator] = IFieldGenerator.registry

    def generate(self, schema: Any) -> Any:
        for generator in self._generators:
            if generator.supports(schema):
                return generator.generate(schema, self)

        return self._get_type_name(schema)

    @staticmethod
    def _get_type_name(obj: Any) -> str:
        return getattr(obj, "__name__", str(obj))

from typing import Any, ClassVar

from infrastructure.generators import IFieldGenerator


class FieldDispatcher:
    _generators: ClassVar[list[IFieldGenerator]] = IFieldGenerator.registry

    @classmethod
    def generate(cls, schema: Any) -> Any:
        for generator in cls._generators:
            if generator.supports(schema):
                return generator.generate(schema, cls)

        return cls.get_type_name(schema)

    @staticmethod
    def get_type_name(obj: Any) -> str:
        return getattr(obj, '__name__', str(obj))

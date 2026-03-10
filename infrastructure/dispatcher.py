import abc
from typing import Any

from infrastructure.builder import RegisterBuilder


class IFieldDispatcher(abc.ABC):

    @abc.abstractmethod
    def generate(self, schema: Any) -> Any:
        """Generates some data from schema."""

    @abc.abstractmethod
    def get_type_name(self, obj: Any) -> str:
        """Returns obj name."""


class FieldDispatcher(IFieldDispatcher):

    def __init__(self, builder: RegisterBuilder) -> None:
        self._builder = builder

    def generate(self, schema: Any) -> Any:
        for generator in self._builder.get_generators():
            if generator.supports(schema):
                return generator().generate(schema, self)

        return self.get_type_name(schema)

    def get_type_name(self, obj: Any) -> str:
        return getattr(obj, '__name__', str(obj))

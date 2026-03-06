import abc
from typing import Any

from dispatcher import FieldDispatcher


class BaseComponent(abc.ABC):
    registry: list[BaseComponent] = []

    name: str
    schema: Any

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if not abc.ABC in cls.__bases__:
            cls.registry.append(cls())

    @classmethod
    def generate_schema(cls) -> dict[str, Any]:
        """Generate schema."""

        dispatcher = FieldDispatcher()

        return {'name': cls.name, 'fields': dispatcher.generate(cls.schema)}

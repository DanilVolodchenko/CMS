import abc
from typing import Any, ClassVar

from infrastructure.dispatcher import FieldDispatcher


class BaseComponent(abc.ABC):
    registry: ClassVar[list[BaseComponent]] = []

    name: str
    schema: Any

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        if abc.ABC not in cls.__bases__:
            cls.registry.append(cls())

    @classmethod
    def generate_schema(cls) -> dict[str, Any]:
        """Generate schema."""

        return {'name': cls.name, 'fields': FieldDispatcher.generate(cls.schema)}

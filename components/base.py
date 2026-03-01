from typing import Any

from dispatcher import FieldDispatcher


class BaseComponent:
    name: str
    schema: Any

    @classmethod
    def generate_schema(cls) -> dict[str, Any]:
        """Generate schema."""

        dispatcher = FieldDispatcher()

        return {'name': cls.name, 'fields': dispatcher.generate(cls.schema)}

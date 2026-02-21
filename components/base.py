import dataclasses
from typing import Any
from annotationlib import ForwardRef

from schemas.base import BaseShema


class BaseComponent:
    name: str
    schema: BaseShema

    @classmethod
    def generate_schema(cls) -> dict[str, Any]:
        """Generate schema."""

        instance = cls()

        return {'name': cls.name, 'fields': instance._get_fields(cls.schema)}

    def _get_fields(self, obj: BaseShema) -> dict[str, Any]:
        fields = {}

        for field in dataclasses.fields(obj):
            if dataclasses.is_dataclass(field.type):
                fields[field.name] = self._get_fields(field.type)  # noqa
            elif isinstance(field.type, ForwardRef):
                fields[field.name] = self._get_fields(field.type.evaluate())
            else:
                fields[field.name] = field.type.__name__

        return fields

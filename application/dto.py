import dataclasses
from typing import Any


@dataclasses.dataclass(frozen=True)
class NewPageComponentDTO:
    page: str
    components: list[Any]


@dataclasses.dataclass(frozen=True)
class ComponentDTO:
    name: str
    fields: Any

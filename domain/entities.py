import dataclasses
from typing import Any


@dataclasses.dataclass(frozen=True, slots=True)
class PageDM:
    page: str
    components: list[Any]

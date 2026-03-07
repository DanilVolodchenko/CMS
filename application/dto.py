from typing import Any

import dataclasses


@dataclasses.dataclass(frozen=True)
class NewPageComponentDTO:
    page: str
    components: list[Any]
from typing import Any

from pydantic import BaseModel


class PageSchema(BaseModel):
    page: str
    components: list[Any]

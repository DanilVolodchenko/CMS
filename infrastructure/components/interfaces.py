import abc
from typing import Any


class IComponent(abc.ABC):
    name: str
    schema: Any

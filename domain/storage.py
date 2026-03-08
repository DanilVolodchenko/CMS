from typing import Any


class ComponentStorage:
    def __init__(self) -> None:
        self._components = {}

    def get_components(self, page: str) -> list[dict[str, Any]]:
        return self._components[page]

    def add_components(self, page: str, components: list[dict[str, Any]]) -> None:
        self._components[page] = components

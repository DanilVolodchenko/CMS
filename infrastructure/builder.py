import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from infrastructure.components.interfaces import IComponent
    from infrastructure.generators.interfaces import IFieldGenerator


class IComponentBuilder(abc.ABC):

    @abc.abstractmethod
    def get_components(self) -> list[type[IComponent]]:
        """Returns components from storage."""

    @abc.abstractmethod
    def add_components(self, *components: type[IComponent]) -> None:
        """Adds components to storage."""


class IFieldGeneratorBuilder(abc.ABC):

    @abc.abstractmethod
    def get_generators(self) -> list[type[IFieldGenerator]]:
        """Returns generators from storage."""

    @abc.abstractmethod
    def add_generators(self, *generators: type[IFieldGenerator]) -> None:
        """Adds generators to storage."""


class RegisterBuilder(IComponentBuilder, IFieldGeneratorBuilder):
    def __init__(self) -> None:
        self._components: list[type[IComponent]] = []
        self._generators: list[type[IFieldGenerator]] = []

    def get_components(self) -> list[type[IComponent]]:
        return self._components

    def get_generators(self) -> list[type[IFieldGenerator]]:
        return self._generators

    def add_components(self, *components: type[IComponent]) -> None:
        for component in components:
            self._components.append(component)

    def add_generators(self, *generators: type[IFieldGenerator]) -> None:
        for generator in generators:
            self._generators.append(generator)

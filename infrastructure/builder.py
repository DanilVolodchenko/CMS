import abc

from infrastructure.components.interfaces import BaseComponent
from infrastructure.generators.interfaces import IFieldGenerator


class IComponentBuilder(abc.ABC):

    @abc.abstractmethod
    def get_components(self) -> list[type[BaseComponent]]:
        """Returns components from storage."""

    @abc.abstractmethod
    def add_components(self, *components: type[BaseComponent]) -> None:
        """Adds components to storage."""


class IFieldGeneratorBuilder(abc.ABC):

    @abc.abstractmethod
    def get_generators(self) -> list[type[IFieldGenerator]]:
        """Returns generators from storage."""

    @abc.abstractmethod
    def add_generators(self, *generators: type[IFieldGenerator]) -> None:
        """Adds generators to storage."""


class Builder(IComponentBuilder, IFieldGeneratorBuilder):
    def __init__(self) -> None:
        self._components: list[type[BaseComponent]] = []
        self._generators: list[type[IFieldGenerator]] = []

    def get_components(self) -> list[type[BaseComponent]]:
        return self._components

    def get_generators(self) -> list[type[IFieldGenerator]]:
        return self._generators

    def add_components(self, *components: type[BaseComponent]) -> None:
        for component in components:
            self._components.append(component)

    def add_generators(self, *generators: type[IFieldGenerator]) -> None:
        for generator in generators:
            self._generators.append(generator)

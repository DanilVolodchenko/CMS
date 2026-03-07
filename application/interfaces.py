import abc

from domain.entities import PageDM


class IGetComponent(abc.ABC):

    @abc.abstractmethod
    def get_by_page(self, page: str) -> PageDM:
        """Returns components by page."""


class ISaveComponent(abc.ABC):

    @abc.abstractmethod
    def save(self, page: PageDM) -> None:
        """Saves component to page."""

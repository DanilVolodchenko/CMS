from application.interfaces import IGetComponent, ISaveComponent
from domain.entities import PageDM
from infrastructure.resources.storage import ComponentStorage


class ComponentStorageGateway(IGetComponent, ISaveComponent):
    def __init__(self, storage: ComponentStorage) -> None:
        self._storage = storage

    def get_by_page(self, page: str) -> PageDM:
        components = self._storage.get_components(page)
        return PageDM(page=page, components=components)

    def save(self, page: PageDM) -> None:
        self._storage.add_components(page.page, page.components)

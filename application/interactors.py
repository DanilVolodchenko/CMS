from typing import Any

from application.dto import NewPageComponentDTO
from application.interfaces import IGetComponent, ISaveComponent
from domain import entities
from errors import ComponentNotFoundError, PageNotFoundError
from infrastructure.components import BaseComponent


class GetComponentsSchemaInteractor:
    def __init__(self, component: BaseComponent) -> None:
        self._component = component

    def __call__(self) -> list[dict[str, Any]]:
        return [component.generate_schema() for component in self._component.registry]


class GetComponentSchemaByNameInteractor:
    def __init__(self, component: BaseComponent) -> None:
        self._component = component

    def __call__(self, name: str) -> dict[str, Any]:
        for component in self._component.registry:
            if component.name == name:
                return component.generate_schema()
        raise ComponentNotFoundError(f'Component `{name}` not found!')


class GetComponentsByPathInteractor:
    def __init__(self, component_gateway: IGetComponent) -> None:
        self._component_gateway = component_gateway

    def __call__(self, page: str) -> entities.PageDM:
        try:
            return self._component_gateway.get_by_page(page=page)
        except KeyError:
            raise PageNotFoundError(f'Page `{page}` not found') from None


class CreateComponentInteractor:
    def __init__(self, component_gateway: ISaveComponent) -> None:
        self._component_gateway = component_gateway

    def __call__(self, page_dto: NewPageComponentDTO) -> None:
        page_dm = entities.PageDM(page=page_dto.page, components=page_dto.components)

        self._component_gateway.save(page_dm)

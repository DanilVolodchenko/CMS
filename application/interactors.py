from application.dto import ComponentDTO, NewPageComponentDTO
from application.interfaces import IGetComponent, ISaveComponent
from domain import entities
from errors import ComponentNotFoundError, PageNotFoundError
from infrastructure.builder import RegisterBuilder
from infrastructure.dispatcher import IFieldDispatcher


class GetComponentsSchemaInteractor:
    def __init__(self, register_builder: RegisterBuilder, dispatcher: IFieldDispatcher) -> None:
        self._builder = register_builder
        self._dispatcher = dispatcher

    def __call__(self) -> list[ComponentDTO]:
        return [
            ComponentDTO(name=component.name, fields=self._dispatcher.generate(component.schema))
            for component in self._builder.get_components()
        ]


class GetComponentSchemaByNameInteractor:
    def __init__(self, register_builder: RegisterBuilder, dispatcher: IFieldDispatcher) -> None:
        self._builder = register_builder
        self._dispatcher = dispatcher

    def __call__(self, name: str) -> ComponentDTO:
        for component in self._builder.get_components():
            if component.name == name:
                return ComponentDTO(name=component.name, fields=self._dispatcher.generate(component.schema))
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

from that_depends import BaseContainer, providers

from application import interactors
from infrastructure.builder import RegisterBuilder
from infrastructure.dispatcher import FieldDispatcher
from infrastructure.gateways import ComponentStorageGateway
from infrastructure.resources.storage import ComponentStorage


class Container(BaseContainer):
    storage = providers.Singleton(ComponentStorage)
    register_builder = providers.Singleton(RegisterBuilder)

    dispatcher = providers.Singleton(FieldDispatcher, builder=register_builder.cast)

    component_storage_gateway = providers.Singleton(
        ComponentStorageGateway,
        storage=storage.cast,
    )

    get_components_schema_interactor = providers.Singleton(
        interactors.GetComponentsSchemaInteractor,
        register_builder=register_builder.cast,
        dispatcher=dispatcher.cast,
    )
    get_component_schema_by_name_interactor = providers.Singleton(
        interactors.GetComponentSchemaByNameInteractor,
        register_builder=register_builder.cast,
        dispatcher=dispatcher.cast,
    )
    create_component_interactor = providers.Singleton(
        interactors.CreateComponentInteractor,
        component_gateway=component_storage_gateway.cast,
    )
    get_component_by_page_interactor = providers.Singleton(
        interactors.GetComponentsByPageInteractor,
        component_gateway=component_storage_gateway.cast,
    )

from that_depends import BaseContainer, providers

from application import interactors
from domain.storage import ComponentStorage
from infrastructure.components import BaseComponent
from infrastructure.dispatcher import FieldDispatcher
from infrastructure.gateways import ComponentStorageGateway


class Container(BaseContainer):
    dispatcher = providers.Singleton(FieldDispatcher)

    component = providers.Singleton(BaseComponent)

    storage = providers.Singleton(ComponentStorage)

    component_storage_gateway = providers.Singleton(
        ComponentStorageGateway,
        storage=storage,  # type: ignore[invalid-argument-type]
    )

    get_components_schema_interactor = providers.Singleton(
        interactors.GetComponentsSchemaInteractor,
        component=component,  # type: ignore[invalid-argument-type]
    )
    get_component_schema_by_name_interactor = providers.Singleton(
        interactors.GetComponentSchemaByNameInteractor,
        component=component,  # type: ignore[invalid-argument-type]
    )
    create_component_interactor = providers.Singleton(
        interactors.CreateComponentInteractor,
        component_gateway=component_storage_gateway,  # type: ignore[invalid-argument-type]
    )
    get_component_by_page_interactor = providers.Singleton(
        interactors.GetComponentsByPathInteractor,
        component_gateway=component_storage_gateway,  # type: ignore[invalid-argument-type]
    )

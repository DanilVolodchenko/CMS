from typing import Annotated, Any

from fastapi import APIRouter, Depends

from application import interactors
from ioc import Container

router = APIRouter(prefix='/admin', tags=['Admin'])


@router.get('/components', name='Get components schema')
def get_components_schema(
    interactor: Annotated[
        interactors.GetComponentsSchemaInteractor, Depends(Container.get_components_schema_interactor),
    ],
) -> list[dict[str, Any]]:
    return interactor()


@router.get('/components/{component_name}')
def get_component_by_name(
    component_name: str,
    interactor: Annotated[
        interactors.GetComponentSchemaByNameInteractor, Depends(Container.get_component_schema_by_name_interactor),
    ],
) -> dict[str, Any]:
    return interactor(name=component_name)

from typing import Any

from fastapi import APIRouter, Depends

from ioc import Container
from application import interactors

router = APIRouter(prefix='/admin', tags=['Admin'])


@router.get('/components', name='Get components schema')
def get_components_schema(
        interactor: interactors.GetComponentsSchemaInteractor = Depends(Container.get_components_schema_interactor)
) -> list[dict[str, Any]]:
    return interactor()


@router.get('/components/{component_name}')
def get_component_by_name(
        component_name: str,
        interactor: interactors.GetComponentSchemaByNameInteractor = Depends(
            Container.get_component_schema_by_name_interactor
        )
) -> dict[str, Any]:
    return interactor(name=component_name)

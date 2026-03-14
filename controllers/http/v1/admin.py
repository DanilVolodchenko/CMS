from typing import Annotated

from fastapi import APIRouter, Depends

from application import dto, interactors
from ioc import Container

router = APIRouter(prefix='/admin', tags=['Admin'])


@router.get('/components', name='Get components schema')
def get_components_schema(
        interactor: Annotated[
            interactors.GetComponentsSchemaInteractor, Depends(Container.get_components_schema_interactor),
        ],
) -> list[dto.ComponentDTO]:
    return interactor()


@router.get('/components/{component_name}')
def get_component_schema_by_name(
        component_name: str,
        interactor: Annotated[
            interactors.GetComponentSchemaByNameInteractor, Depends(Container.get_component_schema_by_name_interactor),
        ],
) -> dto.ComponentDTO:
    return interactor(name=component_name)

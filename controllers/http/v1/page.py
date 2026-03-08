from typing import Annotated

from fastapi import APIRouter, Depends

from application import interactors
from application.dto import NewPageComponentDTO
from controllers.http.v1.schemas import PageSchema
from ioc import Container

router = APIRouter(prefix='/page', tags=['Page'])


@router.get('/{page:path}/components')
def get_components(
    page: str,
    get_interactor: Annotated[
        interactors.GetComponentsByPathInteractor, Depends(Container.get_component_by_page_interactor),
    ],
) -> PageSchema:
    page_dm = get_interactor(page)

    return PageSchema(
        page=page_dm.page,
        components=page_dm.components,
    )


@router.post('/components')
def create_components(
    schema: PageSchema,
    get_interactor: Annotated[
        interactors.GetComponentsByPathInteractor, Depends(Container.get_component_by_page_interactor),
    ],
    create_interactor: Annotated[
        interactors.CreateComponentInteractor, Depends(Container.create_component_interactor),
    ],
) -> PageSchema:
    dto = NewPageComponentDTO(page=schema.page, components=schema.components)
    create_interactor(dto)

    page_dm = get_interactor(schema.page)

    return PageSchema(
        page=page_dm.page,
        components=page_dm.components,
    )

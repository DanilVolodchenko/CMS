from typing import Annotated

from fastapi import APIRouter, Depends, status

from application import interactors
from application.dto import NewPageComponentDTO
from controllers.http.v1.schemas import PageSchema
from ioc import Container

router = APIRouter(prefix='/page', tags=['Page'])


@router.get('/{page:path}/components', status_code=status.HTTP_200_OK, name='Get components for page.')
def get_components(
        page: str,
        get_component_interactor: Annotated[
            interactors.GetComponentsByPageInteractor, Depends(Container.get_component_by_page_interactor),
        ],
) -> PageSchema:
    page_dm = get_component_interactor(page)

    return PageSchema(page=page_dm.page, components=page_dm.components)


@router.post('/components', status_code=status.HTTP_201_CREATED, name='Create components for page.')
def create_components(
        schema: PageSchema,
        get_component_interactor: Annotated[
            interactors.GetComponentsByPageInteractor, Depends(Container.get_component_by_page_interactor),
        ],
        create_component_interactor: Annotated[
            interactors.CreateComponentInteractor, Depends(Container.create_component_interactor),
        ],
) -> PageSchema:
    dto = NewPageComponentDTO(page=schema.page, components=schema.components)
    create_component_interactor(dto)

    page_dm = get_component_interactor(schema.page)

    return PageSchema(
        page=page_dm.page,
        components=page_dm.components,
    )

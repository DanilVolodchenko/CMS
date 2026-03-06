from typing import Any

from fastapi import APIRouter

from components import BaseComponent
from errors import ComponentNotFoundError

router = APIRouter(prefix='/admin', tags=['Admin'])


@router.get('/components')
def get_components() -> list[dict[str, Any]]:
    return [component.generate_schema() for component in BaseComponent.registry]


@router.get('/components/{component_name}')
def get_component_by_name(component_name: str) -> dict[str, Any]:
    for component in BaseComponent.registry:
        if component.name == component_name:
            return component.generate_schema()
    else:
        raise ComponentNotFoundError(f'Component `{component_name}` not found!')


@router.post('/components')
def create_components(components: str):
    ...

from infrastructure.components.base import BaseComponent
from infrastructure.schemas.main import MainSchema


class MainComponent(BaseComponent):
    name = 'main'
    schema = MainSchema

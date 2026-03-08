from infrastructure.components.interfaces import BaseComponent
from infrastructure.schemas.main import MainSchema


class MainComponent(BaseComponent):
    name = 'main'
    schema = MainSchema

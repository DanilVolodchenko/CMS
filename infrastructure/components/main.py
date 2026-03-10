from infrastructure.components.interfaces import IComponent
from infrastructure.schemas.main import MainSchema


class MainComponent(IComponent):
    name = 'main'
    schema = MainSchema

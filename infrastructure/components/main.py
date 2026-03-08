from components.base import BaseComponent
from schemas.main import MainSchema


class MainComponent(BaseComponent):
    name = "main"
    schema = MainSchema

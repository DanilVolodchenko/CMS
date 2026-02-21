import dataclasses

from components.base import BaseComponent, BaseShema


@dataclasses.dataclass
class MainSchema(BaseShema):
    title: str
    summary: str
    description: str


class MainComponent(BaseComponent):
    name = 'main'
    schema = MainSchema

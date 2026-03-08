import dataclasses

from infrastructure.fields import TitleField
from infrastructure.mixins import LinkMixin


@dataclasses.dataclass
class FooterSchema:
    columns: list[Columns]


@dataclasses.dataclass
class Columns(TitleField):
    links: list[Links]


@dataclasses.dataclass
class Links(LinkMixin): ...

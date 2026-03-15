import dataclasses

from infrastructure.fields import TitleField
from infrastructure.mixins import LinkMixin


@dataclasses.dataclass
class FooterSchema:
    columns: list[Column]


@dataclasses.dataclass
class Column(TitleField):
    links: list[Link]


@dataclasses.dataclass
class Link(LinkMixin): ...

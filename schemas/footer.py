import dataclasses

from fields import TitleField
from mixins import LinkMixin


@dataclasses.dataclass
class FooterSchema:
    columns: list[Columns]


@dataclasses.dataclass
class Columns(TitleField):
    links: list[Links]


@dataclasses.dataclass
class Links(LinkMixin):
    ...
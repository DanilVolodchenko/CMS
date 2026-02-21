import dataclasses


@dataclasses.dataclass
class FooterSchema:
    columns: Columns


@dataclasses.dataclass
class Columns:
    title: str
    links: Links


@dataclasses.dataclass
class Links:
    label: str
    url: str

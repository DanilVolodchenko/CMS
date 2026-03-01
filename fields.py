import dataclasses


@dataclasses.dataclass
class TitleField:
    title: str


@dataclasses.dataclass
class SummaryField:
    summary: str


@dataclasses.dataclass
class DescriptionField:
    description: str


@dataclasses.dataclass
class LabelField:
    label: str


@dataclasses.dataclass
class UrlField:
    url: str

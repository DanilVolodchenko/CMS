import dataclasses

from infrastructure.fields import TitleField, NavigationField


@dataclasses.dataclass
class HeaderSchema(TitleField, NavigationField):
    ...

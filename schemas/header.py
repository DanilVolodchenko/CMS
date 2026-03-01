import dataclasses

from fields import TitleField, NavigationField


@dataclasses.dataclass
class HeaderSchema(TitleField, NavigationField):
    ...

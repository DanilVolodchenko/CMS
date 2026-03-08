import dataclasses

from infrastructure.fields import NavigationField, TitleField


@dataclasses.dataclass
class HeaderSchema(TitleField, NavigationField): ...

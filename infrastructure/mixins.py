import dataclasses

from infrastructure import fields


@dataclasses.dataclass
class TitleSummaryDescMixin(fields.TitleField, fields.SummaryField, fields.DescriptionField): ...


@dataclasses.dataclass
class LinkMixin(fields.LabelField, fields.UrlField): ...

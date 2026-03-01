import fields


class TitleSummaryDescMixin(fields.TitleField, fields.SummaryField, fields.DescriptionField):
    ...


class LinkMixin(fields.LabelField, fields.UrlField):
    ...

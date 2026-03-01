import dataclasses

from mixins import TitleSummaryDescMixin


@dataclasses.dataclass
class MainSchema(TitleSummaryDescMixin):
    ...

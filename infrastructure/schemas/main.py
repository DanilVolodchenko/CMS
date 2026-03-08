import dataclasses

from infrastructure.mixins import TitleSummaryDescMixin


@dataclasses.dataclass
class MainSchema(TitleSummaryDescMixin): ...

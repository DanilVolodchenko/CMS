from infrastructure.components.base import BaseComponent
from infrastructure.schemas import HeaderSchema


class HeaderComponent(BaseComponent):
    name = 'header'
    schema = HeaderSchema

from infrastructure.components.interfaces import BaseComponent
from infrastructure.schemas.header import HeaderSchema


class HeaderComponent(BaseComponent):
    name = 'header'
    schema = HeaderSchema

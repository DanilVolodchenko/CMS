from infrastructure.components.interfaces import IComponent
from infrastructure.schemas.header import HeaderSchema


class HeaderComponent(IComponent):
    name = 'header'
    schema = HeaderSchema

from components.base import BaseComponent
from schemas.header import HeaderSchema


class HeaderComponent(BaseComponent):
    name = 'main'
    schema = HeaderSchema

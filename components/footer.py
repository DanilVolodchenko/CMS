from infrastructure.components.base import BaseComponent
from infrastructure.schemas.footer import FooterSchema


class FooterComponent(BaseComponent):
    name = 'footer'
    schema = FooterSchema

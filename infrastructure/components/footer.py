from infrastructure.components.interfaces import BaseComponent
from infrastructure.schemas.footer import FooterSchema


class FooterComponent(BaseComponent):
    name = 'footer'
    schema = FooterSchema

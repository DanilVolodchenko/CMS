from infrastructure.components.interfaces import IComponent
from infrastructure.schemas.footer import FooterSchema


class FooterComponent(IComponent):
    name = 'footer'
    schema = FooterSchema

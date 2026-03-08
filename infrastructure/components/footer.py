from components.base import BaseComponent
from schemas.footer import FooterSchema


class FooterComponent(BaseComponent):
    name = "footer"
    schema = FooterSchema

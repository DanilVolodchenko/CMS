from that_depends import BaseContainer, providers

from core.config import Config


class Container(BaseContainer):
    config: Config = providers.Singleton(Config)
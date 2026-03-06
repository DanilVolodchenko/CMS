class BaseError(Exception):
    """Base exception."""


class ComponentNotFoundError(BaseError):
    """Component not found."""
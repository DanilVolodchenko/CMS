class BaseError(Exception):
    """Base exception."""


class ComponentNotFoundError(BaseError):
    """Component not found."""


class PageNotFoundError(BaseError):
    """Page not found."""

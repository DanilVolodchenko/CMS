from application.interfaces import IGetComponent, ISaveComponent


def test_methods_exists_in_interface_get_component() -> None:
    """Testing methods exists in IGetComponent."""

    result = IGetComponent.__dict__

    assert 'get_by_page' in result, 'Class IGetComponent has not `get_by_page` method'


def test_methods_exists_in_interface_save_component() -> None:
    """Testing methods exists in ISaveComponent."""

    result = ISaveComponent.__dict__

    assert 'save' in result, 'Class ISaveComponent has not `save` method'

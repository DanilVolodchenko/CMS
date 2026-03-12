from unittest import mock

import pytest

from domain.entities import PageDM
from infrastructure.gateways import ComponentStorageGateway


class TestComponentStorageGateway:
    """Tests suite for ComponentStorageGateway."""

    def test_get_by_page_if_storage_is_empty(self) -> None:
        """Tests get_by_page method if storage is empty."""

        storage = mock.Mock()
        storage.get_components_by_page.side_effect = KeyError
        component_storage_gateway = ComponentStorageGateway(storage=storage)

        with pytest.raises(KeyError):
            component_storage_gateway.get_by_page('/test')

    def test_get_by_page_if_storage_is_not_empty(self) -> None:
        """Tests get_by_page method if storage is not empty."""

        storage = mock.Mock()
        storage.get_components_by_page.return_value = [{'test': 'test'}]
        component_storage_gateway = ComponentStorageGateway(storage=storage)

        result = component_storage_gateway.get_by_page('/test')
        expected_result = PageDM(page='/test', components=[{'test': 'test'}])

        assert result == expected_result, f'Expected result {expected_result}, result {result}'
        storage.get_components_by_page.assert_called_once_with('/test')

    def test_save(self) -> None:
        """Tests save method."""

        storage = mock.Mock()
        storage.save.return_value = None
        component_storage_gateway = ComponentStorageGateway(storage=storage)
        page_dm = PageDM(page='/test', components=[{'test': 'test'}])

        component_storage_gateway.save(page=page_dm)

        storage.add_components.assert_called_once_with(page_dm.page, page_dm.components)

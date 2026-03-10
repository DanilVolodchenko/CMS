import pytest

from infrastructure.resources.storage import ComponentStorage


@pytest.fixture
def component_storage() -> ComponentStorage:
    return ComponentStorage()


class TestComponentStorage:
    """Testing ComponentStorage object."""

    def test_get_component_if_storage_empty(self, component_storage: ComponentStorage) -> None:
        """Testing method get_component if it is empty."""

        with pytest.raises(KeyError):
            component_storage.get_components_by_page('/test')

    def test_get_component_if_storage_not_empty(self, component_storage: ComponentStorage) -> None:
        """Testing method get_component if it is not empty."""

        component_storage._components['/test'] = [{'component': '1'}]

        result = component_storage.get_components_by_page('/test')
        expected_result = [{'component': '1'}]

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_add_component(self, component_storage: ComponentStorage) -> None:
        """Testing method add_component."""

        component_storage.add_components('/test', [{'component': '1'}])

        result = component_storage._components
        expected_result = {'/test': [{'component': '1'}]}

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

    def test_add_component_if_add_two_data_with_same_page(self, component_storage: ComponentStorage) -> None:
        """Testing method add_component if add two different data with same page."""

        component_storage.add_components('/test', [{'component': '1'}])
        component_storage.add_components('/test', [{'component': '2'}])

        result = component_storage._components
        expected_result = {'/test': [{'component': '2'}]}

        assert result == expected_result, f'Expected result {expected_result}, result {result}'

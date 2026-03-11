from infrastructure.components.main import MainComponent
from infrastructure.schemas.main import MainSchema


def test_main_component_fields() -> None:
    """Test fields MainComponent."""

    component = MainComponent()

    name = component.name
    schema = component.schema
    expected_name = 'main'
    expected_schema = MainSchema

    assert name == expected_name, f'Expected name {expected_name}, name {name}'
    assert schema == expected_schema, f'Expected result {expected_schema}, result {schema}'

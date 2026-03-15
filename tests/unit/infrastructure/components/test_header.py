from infrastructure.components.header import HeaderComponent
from infrastructure.schemas.header import HeaderSchema


def test_header_component_fields() -> None:
    """Test fields HeaderComponent."""

    component = HeaderComponent()

    name = component.name
    schema = component.schema
    expected_name = 'header'
    expected_schema = HeaderSchema

    assert name == expected_name, f'Expected name {expected_name}, name {name}'
    assert schema == expected_schema, f'Expected result {expected_schema}, result {schema}'

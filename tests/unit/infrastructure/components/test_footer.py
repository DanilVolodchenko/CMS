from infrastructure.components.footer import FooterComponent
from infrastructure.schemas.footer import FooterSchema


def test_footer_component_fields() -> None:
    """Test fields FooterComponent."""

    component = FooterComponent()

    name = component.name
    schema = component.schema
    expected_name = 'footer'
    expected_schema = FooterSchema

    assert name == expected_name, f'Expected name {expected_name}, name {name}'
    assert schema == expected_schema, f'Expected result {expected_schema}, result {schema}'

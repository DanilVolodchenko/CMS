from typing import Any

from infrastructure.components.interfaces import IComponent


def test_main_component_fields() -> None:
    """Test fields of MainComponent."""

    component = IComponent
    attrs = component.__annotations__

    expected_name_attr = 'name'
    expected_schema_attr = 'schema'

    assert expected_name_attr in attrs, f'Class {component} not contain `{expected_name_attr}` attr'
    assert expected_schema_attr in attrs, f'Class {component} not contain `{expected_schema_attr}` attr'


def test_main_component_type_of_fields() -> None:
    """Test type of fields MainComponent."""

    component = IComponent
    attrs = component.__annotations__

    name_attr = 'name'
    schema_attr = 'schema'

    expected_name_type = str
    expected_schema_type = Any

    assert attrs[name_attr] == expected_name_type, f'Type of attr `{name_attr}` not {expected_name_type}'
    assert attrs[schema_attr] == expected_schema_type, f'Type of attr `{schema_attr}` not {expected_schema_type}'

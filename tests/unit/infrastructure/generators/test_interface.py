from infrastructure.generators.interfaces import IFieldGenerator


def test_methods_exists_in_interface_field_generator() -> None:
    """Testing methods exists in IFieldGenerator."""

    result = IFieldGenerator.__dict__

    assert 'supports' in result, 'Class IFieldGeneratorMethod has not `supports` method'
    assert 'generate' in result, 'Class IFieldGeneratorMethod has not `generate` method'

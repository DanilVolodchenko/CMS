from core.config import Config, FastApiConfig


def test_fast_api_config_attrs() -> None:
    """Test FastApiConfig attrs."""

    model_fields = FastApiConfig.model_fields

    result = {field: info.annotation for field, info in model_fields.items()}
    expected_result = {'title': str, 'description': str}

    assert result == expected_result, f'Expected result {expected_result}, result {result}'


def test_config_attrs() -> None:
    """Test Config attrs."""

    model_fields = Config.model_fields

    result = {field: info.annotation for field, info in model_fields.items()}
    expected_result = {'fastapi': FastApiConfig}

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

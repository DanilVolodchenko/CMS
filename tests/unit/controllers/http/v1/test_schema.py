from typing import Any

from controllers.http.v1 import schemas


def test_page_schema_fields() -> None:
    """Test PageSchema fields."""

    model_fields = schemas.PageSchema.model_fields

    result = {field: info.annotation for field, info in model_fields.items()}
    expected_result = {'page': str, 'components': list[Any]}

    assert result == expected_result, f'Expected result {expected_result}, result {result}'

from typing import Any, TYPE_CHECKING, get_args, get_origin

from infrastructure.generators.base import IFieldGenerator

if TYPE_CHECKING:
    from dispatcher import FieldDispatcher


class ContainerGenerator(IFieldGenerator):

    @classmethod
    def supports(cls, schema: Any) -> bool:
        return get_origin(schema) is not None

    def generate(self, schema: Any, dispatcher: 'FieldDispatcher') -> Any:
        origin = get_origin(schema)
        args = get_args(schema)

        if origin in [list, set, frozenset, tuple]:
            inner = args[0] if args else Any
            return [dispatcher.generate(inner)]

        if origin is dict:
            key_type, value_type = args if args else (Any, Any)
            return {
                "key": dispatcher.generate(key_type),
                "value": dispatcher.generate(value_type),
            }

        return dispatcher._get_type_name(schema)

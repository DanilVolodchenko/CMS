from typing import TYPE_CHECKING, Any, get_args, get_origin

from infrastructure.generators.interfaces import IFieldGenerator

if TYPE_CHECKING:
    from infrastructure.dispatcher import IFieldDispatcher


class ContainerGenerator(IFieldGenerator):
    @classmethod
    def supports(cls, schema: Any) -> bool:
        return get_origin(schema) is not None

    def generate(self, schema: Any, dispatcher: IFieldDispatcher) -> Any:
        origin = get_origin(schema)
        args = get_args(schema)

        if origin in [list, set, frozenset, tuple]:
            inner = args[0] if args else Any
            return [dispatcher.generate(inner)]

        if origin is dict:
            key_type, value_type = args or (Any, Any)
            return {
                'key': dispatcher.generate(key_type),
                'value': dispatcher.generate(value_type),
            }

        return dispatcher.get_type_name(schema)

import abc


class ComponentGetter(abc.ABC):

    @abc.abstractmethod
    def get_by_path(self):
        ...


class ComponentSaver(abc.ABC):

    @abc.abstractmethod
    def save(self, obj) -> None:
        ...
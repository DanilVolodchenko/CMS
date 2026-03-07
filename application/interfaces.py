import abc


class IGetRepository[T](abc.ABC):

    @abc.abstractmethod
    def get(self, **kwargs) -> T:
        ...


class ISaveRepository[T](abc.ABC):

    @abc.abstractmethod
    def save(self, obj: T) -> None:
        ...

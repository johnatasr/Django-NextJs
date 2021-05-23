from abc import ABC, abstractmethod
from typing import Any


class ListContactsCase(ABC):
    """ Interface to list contacts iterator"""

    @abstractmethod
    def set_params(self, *args, **kwargs) -> None:
        raise Exception("Iterator should implemets the method: set_params")

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        raise Exception("Iterator should implemets the method: execute")


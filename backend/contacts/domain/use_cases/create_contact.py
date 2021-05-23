from abc import ABC, abstractmethod
from typing import Any


class CreateContactCase(ABC):
    """ Interface to create contact iterator"""

    @abstractmethod
    def set_params(self, *args, **kwargs) -> None:
        raise Exception("Iterator should implemets the method: set_params")

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        raise Exception("Iterator should implemets the method: execute")

    @abstractmethod
    def create_by_payload(self, payload: dict) -> bool:
        raise Exception("Iterator should implemets the method: create_by_payload")


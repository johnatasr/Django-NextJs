from abc import ABC, abstractmethod
from typing import Any


class ShowContactUseCase(ABC):
    """ Interface to show a contact iterator"""

    @abstractmethod
    def set_params(self, *args, **kwargs) -> None:
        raise Exception("Iterator should implemets the method: set_params")

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        raise Exception("Iterator should implemets the method: execute")

    @abstractmethod
    def get_contact_by_id(self, user_id: int) -> bool:
        raise Exception("Iterator should implemets the method: get_by_id")


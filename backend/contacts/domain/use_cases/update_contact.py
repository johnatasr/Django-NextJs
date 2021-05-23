from abc import ABC, abstractmethod
from typing import Any


class UpdateContactCase(ABC):
    """ Interface to update contact iterator"""

    @abstractmethod
    def set_params(self, *args, **kwargs) -> None:
        raise Exception("Iterator should implemets the method: set_params")

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        raise Exception("Iterator should implemets the method: execute")

    @abstractmethod
    def update_contact_by_id(self, payload: dict, user_id: int) -> object:
        raise Exception("Iterator should implemets the method: update_user_by_id")


from typing import Any
from abc import ABC, abstractmethod


class IValidator(ABC):
    """ Interface for Validator"""

    @abstractmethod
    def validate(self, value: bool) -> bool:
        raise Exception("Validator should implemets the method: valid")

    @abstractmethod
    def is_empty_payload(self) -> bool:
        raise Exception("Validator should implemets the method: is_empty_payload")

    @abstractmethod
    def validate_payload(self) -> (bool, dict):
        raise Exception("Validator should implemets the method: validate_payload")


class IIterator(ABC):
    """ Interface for Iterator """

    @abstractmethod
    def set_params(self, *args, **kwargs):
        raise Exception("Iterator should implemets the method: set_params")

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        raise Exception("Iterator should implemets the method: execute")


class ISerializer(ABC):
    """ Interface for Serializer """

    @abstractmethod
    def create_message(self) -> dict:
        raise Exception("Serializer should implemets the method: create_message")

    @abstractmethod
    def mount_payload(self) -> dict:
        raise Exception("Serializer should implemets the method: mount_payload")
from configs.exceptions import InvalidPayloadException
from contacts.infra.interfaces import IValidator
from .helpers import round_floor_number

from typing import Any, Union


class ContactsValidator(IValidator):
    @staticmethod
    def validate(value: bool) -> bool:
        return value

    def is_empty_payload(self, payload) -> Union[bool, Exception]:
        """
          Checks if is a empty payload
        """
        if isinstance(payload, (dict, list, bytes)):
            return True
        else:
            raise InvalidPayloadException(
                source="validator",
                code="empty_payload",
                message="Payload in request is empty",
            )

    def validate_field(self, key: str, field: Any, type_value: object, min_len_field=None, args="") \
            -> Union[bool, Exception]:
        """
            Checks type in field and length
        """
        if not isinstance(field, type_value):
            raise InvalidPayloadException(
                source="validator",
                code="field_wrong_type",
                message=f"Field '{key}' must to be type {type_value.__repr__()}",
            )

        if min_len_field:
            if len(str(field)) < min_len_field:
                raise InvalidPayloadException(
                    source="validator",
                    code="field_wrong_length",
                    message=f"Field '{key}' must to be major than {min_len_field} {args}",
                )
        return True

    def validate_in_payload(self, key: str, payload: dict) -> Union[bool, Exception]:
        """
            Checks field in payload
        """

        if key not in payload:
            raise InvalidPayloadException(
                source="validator",
                code="field_not_exists",
                message=f"Field required: {key}",
            )
        return True

    def validate_id_param(self, id_param: Any) -> Union[int, Exception]:
        """
            Checks id query params
        """
        if isinstance(id_param, str):
            id_param = int(id_param)

        id_param = round_floor_number(id_param)

        if id_param < 0:
            raise InvalidPayloadException(
                source="validator",
                code="field_wrong_value",
                message=f"Param id must be higher than 0",
            )
        return id_param

    def validate_payload(self, payload: dict) -> list:
        """
            Checks all payload, here is the main flow
        """

        self.is_empty_payload(payload)

        self.validate_in_payload(key="name", payload=payload)
        self.validate_field(key="name", field=payload["name"], type_value=str)

        self.validate_in_payload(key="phoneNumber", payload=payload)
        self.validate_field(key="phoneNumber", field=payload["phoneNumber"], type_value=str, min_len_field=8)

        return self.validate(True)
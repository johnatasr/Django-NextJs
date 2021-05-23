from contacts.domain.use_cases.update_contact import UpdateContactCase
from configs.exceptions import IteratorException

from typing import Union


class UpdateContactIterator(UpdateContactCase):
    """
    Interactor responsible for update a contact, called by API
    """
    def __init__(self, validator=None, repo=None, serializer=None, entity=None):
        self.validator: object = validator()
        self.repo: object = repo()
        self.serializer: object = serializer
        self.user_entity = entity

    def set_params(self, contact_payload: dict, contact_id: int):
        self.contact_payload = contact_payload
        self.contact_id = contact_id
        return self

    def execute(self):
        try:
            valided_payload = self.validator.validate_payload(self.contact_payload)

            if valided_payload:
                id_param_validated = self.validator.validate_id_param(self.contact_id)
                self.contact_id: int = id_param_validated

                updated_contact: Union[object, str] = self.update_contact_by_id(
                    payload=self.contact_payload, contact_id=self.contact_id)

                serialized_user = self.serializer(contact=updated_contact, msg="Contact updated").create_message()
                return serialized_user
            else:
                return "Cannot update this contact"

        except IteratorException as error:
            raise IteratorException(error)

    def update_contact_by_id(self, payload: dict, contact_id: int) -> object:
        try:
            contact: object = self.user_entity(
                    name=payload['name'],
                    phone_number=payload['phoneNumber']
                )
            contact.id = contact_id

            return self.repo.update_contact_by_id(contact=contact)
        except IteratorException as error:
            raise IteratorException(error)


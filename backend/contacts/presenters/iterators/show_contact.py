from contacts.domain.use_cases.show_contact import ShowContactUseCase
from configs.exceptions import IteratorException
from typing import Any


class ShowContactIterator(ShowContactUseCase):
    """
    Interactor responsible for brings a specifc contact by ID, called by API
    """
    def __init__(self, validator=None, repo=None, serializer=None):
        self.validator: object = validator
        self.repo: object = repo()
        self.serializer: object = serializer

    def set_params(self, contact_id: int):
        self.contact_id = contact_id
        return self

    def execute(self):
        try:
            valided_user_id = self.validator().validate_id_param(self.contact_id)
            self.contact_id: int = valided_user_id

            contact: Any = self.get_contact_by_id(contact_id=self.contact_id)

            if isinstance(contact, str):
                return contact

            serialized_contact = self.serializer(contact=contact, msg="Contact created")\
                .create_message()
            return serialized_contact
        except IteratorException as error:
            raise IteratorException(error)

    def get_contact_by_id(self, contact_id: int) -> Any:
        try:
            return self.repo.get_contact_by_id(contact_id=contact_id)
        except IteratorException as error:
            raise IteratorException(error)


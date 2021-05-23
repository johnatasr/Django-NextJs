from contacts.domain.use_cases.list_contacts import ListContactsCase
from configs.exceptions import IteratorException

from typing import Union


class ListContactsIterator(ListContactsCase):
    """
    Iteractor responsible for list all contacts, called by API
    """
    def __init__(self, validator=None, repo=None, serializer=None):
        self.validator: object = validator
        self.repo: object = repo()
        self.serializer: object = serializer

    def set_params(self, user_id: int):
        self.user_id = user_id
        return self

    def execute(self):
        try:
            list_contacts: Union[object, str] = self.repo.list_contacts_by_user_id(user_id=self.user_id)

            if isinstance(list_contacts, str):
                return list_contacts

            list_contacts: dict = self.serializer(list_contacts=list_contacts).create_message()
            return list_contacts
        except IteratorException as error:
            raise IteratorException(error)


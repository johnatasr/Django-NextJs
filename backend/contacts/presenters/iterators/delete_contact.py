from contacts.domain.use_cases.delete_contact import DeleteContactCase
from configs.exceptions import IteratorException


class DeleteContactIterator(DeleteContactCase):
    """
    Iterator responsible for delete a contact, called by API
    """
    def __init__(self, validator=None, repo=None):
        self.validator: object = validator
        self.repo: object = repo()

    def set_params(self, contact_id: int):
        self.contact_id = contact_id
        return self

    def execute(self):
        try:
            result: str = self.delete_by_id(contact_id=self.contact_id)
            return result
        except IteratorException as error:
            raise IteratorException(error)

    def delete_by_id(self, contact_id: int) -> bool:
        try:
            return self.repo.delete_contact_by_id(contact_id=contact_id)
        except IteratorException as error:
            raise IteratorException(error)


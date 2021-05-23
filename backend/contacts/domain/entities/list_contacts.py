from contacts.domain.entities.contact import Contact
from dataclasses import dataclass, field
from typing import List


@dataclass()
class ListContacts:
    user_manager_id: int
    contacts: List[Contact]

    def add_user_to_list(self, contact: Contact):
        self.contacts.append(contact)

    def __repr__(self):
        return f"Entity: <{self.__class__.__name__}>"
from contacts.infra.repositories import ContactsRepo
from contacts.infra.serializers import (
    ListContactsSerializer,
    ContactSerializer
)
from contacts.domain.entities.contact import Contact
from .iterators.show_contact import ShowContactIterator
from .iterators.update_contact import UpdateContactIterator
from .iterators.list_contacts import ListContactsIterator
from .iterators.delete_contact import DeleteContactIterator
from .iterators.create_contact import CreateContactIterator
from .validators import ContactsValidator
from typing import Any


class ContactsFactory:

    @staticmethod
    def create_get_iterator(user_id: int, id_params: Any = None) -> dict:
        """
        Create a Iterator to get a list of contacts or a single contact
        :param id_params: Any
        :param user_id: int
        :return: dict
        """
        if id_params:
            return (
                ShowContactIterator(
                    validator=ContactsValidator,
                    repo=ContactsRepo,
                    serializer=ContactSerializer,
                )
                .set_params(contact_id=id_params)
                .execute()
            )
        else:
            return (
                ListContactsIterator(
                    validator=ContactsValidator,
                    repo=ContactsRepo,
                    serializer=ListContactsSerializer,
                )
                .set_params(user_id=user_id)
                .execute()
            )

    @staticmethod
    def create_post_iterator(*, data: Any, user_id: int) -> dict:
        """
        Create a Iterator to post method, used in the most to create a contact
        :param data: Any
        :param user_id: int
        :return: dict
        """
        return (
            CreateContactIterator(
                validator=ContactsValidator,
                repo=ContactsRepo,
                serializer=ContactSerializer,
                entity=Contact
            )
            .set_params(contact_payload=data, user_id=user_id)
            .execute()
        )

    @staticmethod
    def create_update_iterator(*, data: Any, contact_id: Any) -> dict:
        """
        Create a Iterator to update method and update a specifc contact by id
        :param data: Any
        :param contact_id: Any
        :return: dict
        """
        return (
            UpdateContactIterator(
                validator=ContactsValidator,
                repo=ContactsRepo,
                serializer=ContactSerializer,
                entity=Contact
            )
            .set_params(contact_payload=data, contact_id=contact_id)
            .execute()
        )

    @staticmethod
    def create_delete_iterator(*, contact_id: Any) -> dict:
        """
        Create a Iterator to delete method, delete a contact by id
        :param contact_id: Any
        :return: dict
        """
        return (
            DeleteContactIterator(
                validator=ContactsValidator,
                repo=ContactsRepo,
            )
            .set_params(contact_id=contact_id)
            .execute()
        )
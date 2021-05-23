from contacts.domain.models.list_contacts import ListContacts as ListContactsModel
from contacts.domain.models.contact import Contact as ContactModel
from contacts.domain.entities.list_contacts import ListContacts
from contacts.domain.entities.contact import Contact

from configs.exceptions import ConflictException

from django.contrib.auth.models import User
from typing import Type, Union
import datetime


class ContactsRepo:
    """
    This layer is responsible for interacting with models and entities
    """
    def list_contacts_by_user_id(self, user_id: int) -> Union[ListContacts, str]:
        """
        List all contacts by user id
        """
        try:
            list_contacts_model: ListContactsModel = ListContactsModel.objects\
                .filter(user_manager__id=user_id)

            if not list_contacts_model.exists():
                return "Nothing found"

            list_contacts_entity: ListContacts = ListContacts(
                user_manager_id=user_id, contacts=list())

            list_iterator = list_contacts_model.first()\
                .contacts.filter(deleted=False).order_by("-id").iterator()

            for ct in list_iterator:
                contact = Contact(
                    name=ct.name,
                    phone_number=ct.phone_number
                )
                contact.id = ct.id

                list_contacts_entity.add_user_to_list(contact)

            return list_contacts_entity
        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_list",
                message=f"Error to show a list of Contacts: {err}",
            )

    def get_contact_by_id(self, contact_id: int) -> Union[Contact, str]:
        """
        Get Contact by ID
        """
        try:
            contact: ContactModel = ContactModel.objects.filter(id=contact_id)

            if contact.exists():
                contact = contact.first()
                contact_entity = Contact(
                    name=contact.name,
                    phone_number=contact.phone_number
                )
                contact_entity.id = contact.id

                return contact_entity
            else:
                return f"User with id: {contact_id} doesn't exists"

        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_show",
                message=f"Error to show a list of contacts: {err}",
            )

    def create_contact(self, contact: Contact, user_id: int) -> Type[Contact]:
        """
        Create a Contact model
        """
        try:
            contact_model = ContactModel.objects.create(
                name=contact.name,
                phone_number=contact.phone_number
            )

            contact.id = contact_model.id
            contact.created_at = contact_model.created_at

            self.add_contact_to_user_list(contact=contact_model, user_id=user_id)

            return contact
        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_create",
                message=f"Error to create Contact Model object: {err}",
            )

    def add_contact_to_user_list(self, contact: ContactModel, user_id: int):
        """
        Add a contact model to list contacts by user id
        """
        try:
            user: User = User.objects.get(id=user_id)
            list_contacts_model: ListContactsModel = ListContactsModel.objects\
                .get_or_create(user_manager=user)

            if not isinstance(list_contacts_model[0], ListContactsModel):
                return "Nothing found"

            list_contacts_model = list_contacts_model[0]
            list_contacts_model.contacts.add(contact)
            list_contacts_model.save()

        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_add_to_list_contacts",
                message=f"Error to add a contact into list contacts: {err}",
            )

    def update_contact_by_id(self, contact: Contact) -> Union[Contact, str]:
        """
        Update a Contact model
        """
        try:
            contact_model = ContactModel.objects.filter(id=contact.id)

            if not contact_model.exists():
                return f"Contact with ID: {contact.id} does not exists"

            contact_model = contact_model.first()
            contact_model.name = contact.name
            contact_model.phone_number = contact.phone_number
            contact_model.save()

            contact.updated_at = datetime.datetime.now()

            return contact
        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_update",
                message=f"Error to update Contact Model object: {err}",
            )

    def delete_contact_by_id(self, contact_id: int) -> str:
        """
        Delete a Contact Model Object, deactivate a contact
        """
        try:
            contact_model = ContactModel.objects.filter(id=contact_id)

            if not contact_model.exists():
                return f"Contact with ID: {contact_id} does not exists"

            contact_model = contact_model.first()
            contact_model.deleted = True
            contact_model.save()

            return f"User with ID: {contact_id} deleted"
        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_update",
                message=f"Error to delete Contact Model object: {err}",
            )
from contacts.presenters.iterators.create_contact import CreateContactIterator
from contacts.presenters.iterators.delete_contact import DeleteContactIterator
from contacts.presenters.iterators.update_contact import UpdateContactIterator
from contacts.presenters.iterators.list_contacts import ListContactsIterator
from contacts.presenters.iterators.show_contact import ShowContactIterator

from contacts.infra.serializers import ContactSerializer, ListContactsSerializer
from contacts.infra.repositories import ContactsRepo

from contacts.presenters.validators import ContactsValidator

from contacts.domain.models.contact import Contact as ContactModel
from contacts.domain.models.list_contacts import ListContacts
from contacts.domain.entities.contact import Contact

from django.contrib.auth.models import User
from django.test import TestCase


class CreateContactIteratorTestCase(TestCase):
    """
    Tests of CreateContactIterator in contacts.presenters.iterators.create_contact.py
    """

    def setUp(self):
        self.iterator = CreateContactIterator(
            validator=ContactsValidator,
            repo=ContactsRepo,
            serializer=ContactSerializer,
            entity=Contact,
        )

        self.data: dict = {
            "name": "john34",
            "phoneNumber": "8598989899"
        }

        self.user = User.objects.create_user("johnatas", "johnatas@admin.com", "John123*")

    def test_init(self):
        self.assertIsInstance(self.iterator, CreateContactIterator)
        self.assertIsInstance(self.iterator.validator, object)
        self.assertIsInstance(self.iterator.repo, ContactsRepo)
        self.assertIsInstance(self.iterator.serializer, object)

    def test_set_params(self):
        self.iterator.set_params(contact_payload=self.data, user_id=self.user.id)
        self.assertIsInstance(self.iterator.contact_payload, dict)
        self.assertIsInstance(self.iterator.user_id, int)
        self.assertEquals(self.iterator.contact_payload["name"], "john34")
        self.assertEquals(self.iterator.contact_payload["phoneNumber"], "8598989899")

    def test_execute(self):
        result = self.iterator.set_params(contact_payload=self.data, user_id=self.user.id)\
            .execute()
        self.assertIsInstance(result, dict)

    def test_create_by_payload(self):
        result = self.iterator.set_params(contact_payload=self.data, user_id=self.user.id)\
            .create_by_payload()
        self.assertIsInstance(result, Contact)
        self.assertEquals(result.name, "john34")


class DeleteContactIteratorTestCase(TestCase):
    """
    Tests of DeleteContactIterator in contacts.presenters.iterators.delete_contact.py
    """

    def setUp(self):
        self.iterator = DeleteContactIterator(
            validator=ContactsValidator,
            repo=ContactsRepo,
        )

        self.data: dict = {
            "name": "john34",
            "phoneNumber": "8598989899"
        }

    def test_init(self):
        self.assertIsInstance(self.iterator, DeleteContactIterator)
        self.assertIsInstance(self.iterator.validator, object)
        self.assertIsInstance(self.iterator.repo, ContactsRepo)

    def test_set_params(self):
        ContactModel.objects.create(
            name="Joao",
            phone_number="859999999")

        self.iterator.set_params(contact_id=1)
        self.assertEquals(self.iterator.contact_id, 1)

    def test_execute(self):
        ContactModel.objects.create(
            name="Joao",
            phone_number="859999999")

        result = self.iterator.set_params(contact_id=1).execute()
        self.assertIsInstance(result, str)

    def test_delete_by_payload(self):
        ContactModel.objects.create(
            name="Joao",
            phone_number="859999999")

        result = self.iterator.set_params(contact_id=1).delete_by_id(contact_id=1)
        self.assertIsInstance(result, str)


class ListContactsIteratorTestCase(TestCase):
    """
    Tests of ListContactsIterator in contacts.presenters.iterators.list_contacts.py
    """

    def setUp(self):
        self.iterator = ListContactsIterator(
            validator=ContactsValidator,
            repo=ContactsRepo,
            serializer=ListContactsSerializer
        )

        self.data: dict = {
            "name": "john34",
            "phoneNumber": "8598989899"
        }

        self.user = User.objects.create_user("johnatas", "johnatas@admin.com", "John123*")

        self.list_contacts = ListContacts.objects.create(user_manager=self.user)

    def test_init(self):
        self.assertIsInstance(self.iterator, ListContactsIterator)
        self.assertIsInstance(self.iterator.validator, object)
        self.assertIsInstance(self.iterator.repo, ContactsRepo)
        self.assertIsInstance(self.iterator.serializer, object)

    def test_execute(self):
        contact1 = ContactModel.objects.create(
            name="Joao",
            phone_number="859999999")

        contact2 = ContactModel.objects.create(
            name="Pedro",
            phone_number="858888888")

        self.list_contacts.contacts.add(contact1)
        self.list_contacts.contacts.add(contact2)
        self.list_contacts.save()

        result = self.iterator.set_params(user_id=self.user.id).execute()
        self.assertIsInstance(result, dict)


class ShowContactIteratorTestCase(TestCase):
    """
    Tests of ShowContactIterator in contacts.presenters.iterators.show_contact.py
    """

    def setUp(self):
        self.iterator = ShowContactIterator(
            validator=ContactsValidator,
            repo=ContactsRepo,
            serializer=ContactSerializer
        )

        self.data: dict = {
            "name": "john34",
            "phoneNumber": "8598989899"
        }

        self.user = User.objects.create_user("johnatas", "johnatas@admin.com", "John123*")

    def test_init(self):
        self.assertIsInstance(self.iterator, ShowContactIterator)
        self.assertIsInstance(self.iterator.validator, object)
        self.assertIsInstance(self.iterator.repo, ContactsRepo)
        self.assertIsInstance(self.iterator.serializer, object)

    def test_set_params(self):
        self.iterator.set_params(contact_id=1)
        self.assertEquals(self.iterator.contact_id, 1)

    def test_execute(self):
        contac = ContactModel.objects.create(
            name="Joao",
            phone_number="859999999")

        result = self.iterator.set_params(contact_id=contac.id).execute()
        self.assertIsInstance(result, dict)

    def test_get_contact_by_id(self):
        contact = ContactModel.objects.create(
            name="Joao",
            phone_number="859999999")

        result = self.iterator.set_params(contact_id=contact.id).get_contact_by_id(contact.id)
        self.assertIsInstance(result, Contact)


class UpdateContactIteratorTestCase(TestCase):
    """
    Tests of UpdateContactIterator in contacts.presenters.iterators.update_contact.py
    """

    def setUp(self):
        self.iterator = UpdateContactIterator(
            validator=ContactsValidator,
            repo=ContactsRepo,
            serializer=ContactSerializer,
            entity=Contact
        )

        self.data: dict = {
            "name": "john34",
            "phoneNumber": "8598989899"
        }

    def test_init(self):
        self.assertIsInstance(self.iterator, UpdateContactIterator)
        self.assertIsInstance(self.iterator.validator, ContactsValidator)
        self.assertIsInstance(self.iterator.repo, ContactsRepo)
        self.assertIsInstance(self.iterator.serializer, object)

    def test_set_params(self):
        self.iterator.set_params(contact_payload=self.data, contact_id=1)
        self.assertEquals(self.iterator.contact_id, 1)
        self.assertIsInstance(self.iterator.contact_payload, dict)

    def test_execute(self):
        contact = ContactModel.objects.create(
            name="Joao",
            phone_number="859999999")

        result = self.iterator.set_params(contact_payload=self.data, contact_id=contact.id).execute()
        self.assertIsInstance(result, dict)

    def test_update_contact_by_id(self):
        contact = ContactModel.objects.create(
            name="Joao",
            phone_number="859999999")

        result = self.iterator.set_params(contact_payload=self.data, contact_id=contact.id)\
            .update_contact_by_id(payload=self.data, contact_id=contact.id)
        self.assertIsInstance(result, Contact)



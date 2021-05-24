from contacts.domain.models.list_contacts import ListContacts
from contacts.domain.models.contact import Contact
from django.contrib.auth.models import User
from django.test import TestCase


class ContactModelsTest(TestCase):
    """
    Tests of User in contacts.domain.models.contact.py
    """

    def test_create_contact(self):
        Contact.objects.create(
            name="Joao",
            phone_number="859999999")

        contact_filtered = Contact.objects.filter(id=1)
        self.assertEquals(contact_filtered.exists(), True)

    def test_get_contact(self):
        contact = Contact.objects.create(
            name="Joao",
            phone_number="859999999")

        user_filtered = Contact.objects.filter(id=3).first()
        self.assertEquals(contact.name, user_filtered.name)

    def test_update_contact(self):
        Contact.objects.create(
            name="Joao",
            phone_number="859999999")

        contact = Contact.objects.filter(id=4).first()

        contact.name = "Pedro"
        contact.phone_number = "8588888888"
        contact.save()

        contact = Contact.objects.filter(id=4).first()

        self.assertEquals(contact.name, "Pedro")
        self.assertEquals(contact.phone_number, "8588888888")

    def test_delete_contact(self):
        Contact.objects.create(
            name="Joao",
            phone_number="859999999")

        contact = Contact.objects.filter(id=2).first()
        contact.delete()

        contact = Contact.objects.filter(id=2).first()

        self.assertEquals(contact, None)


class ListContactsModelsTest(TestCase):
    """
    Tests of User in contacts.domain.models.list_contacts.py
    """

    def setUp(self) -> None:
        self.username = "test"
        self.email = "testn@test.com"
        self.password = "Test123@"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = ''

    def test_create_list_contacts(self):
        contact1 = Contact.objects.create(
            name="Joao",
            phone_number="859999999")

        contact2 = Contact.objects.create(
            name="Pedro",
            phone_number="858888888")

        list_contacts = ListContacts.objects.create(user_manager=self.user)
        list_contacts.contacts.add(contact1)
        list_contacts.contacts.add(contact2)
        list_contacts.save()

        list_contacts = ListContacts.objects.create(user_manager=self.user)

        self.assertIsInstance(list_contacts, ListContacts)



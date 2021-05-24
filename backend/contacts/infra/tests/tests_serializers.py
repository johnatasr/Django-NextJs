from contacts.infra.serializers import ContactSerializer, ListContactsSerializer
from contacts.domain.entities.list_contacts import ListContacts
from contacts.domain.entities.contact import Contact

from django.test import TestCase


class ContactSerializerTestCase(TestCase):
    """
    Tests of ContactSerializer in contacts.infra.serializer.py
    """

    def setUp(self):
        self.contact = Contact(
            name="Joao",
            phone_number="859999999"
        )
        self.contact.id = 1

        self.serializer = ContactSerializer

    def test_init(self):
        serializer = self.serializer(
            contact=self.contact, msg="testing serializers"
        )
        self.assertIsInstance(serializer, ContactSerializer)
        self.assertIsInstance(serializer.contact, Contact)
        self.assertEquals(serializer.msg, "testing serializers")

    def test_mount_payload(self):
        serializer = self.serializer(
            contact=self.contact, msg="testing serializers"
        )
        result = serializer.mount_payload()

        self.assertIsInstance(result, dict)
        self.assertEquals(result["msg"], "testing serializers")
        self.assertEquals(result["contact"]["id"], 1)
        self.assertEquals(result["contact"]["name"], "Joao")
        self.assertEquals(result["contact"]["phoneNumber"], "859999999")

    def test_create_message(self):
        serializer = self.serializer(
            contact=self.contact, msg="testing serializers"
        )
        result = serializer.create_message()
        self.assertIsInstance(result, dict)


class ListContactsSerializerTestCase(TestCase):
    """
    Tests of ListContactsSerializer in contacts.infra.serializer.py
    """

    def setUp(self):
        self.contact_one = Contact(
            name="Joao",
            phone_number="859999999"
        )
        self.contact_one.id = 1

        self.contact_two = Contact(
            name="Pedro",
            phone_number="858888888"
        )
        self.contact_two.id = 2

        self.list_contacts = ListContacts(contacts=list(), user_manager_id=1)
        self.list_contacts.add_user_to_list(self.contact_one)
        self.list_contacts.add_user_to_list(self.contact_two)

        self.serializer = ListContactsSerializer

    def test_init(self):
        serializer = self.serializer(
            list_contacts=self.list_contacts
        )
        self.assertIsInstance(serializer, ListContactsSerializer)
        self.assertIsInstance(serializer.list_contacts.contacts[0], Contact)
        self.assertIsInstance(serializer.list_contacts.contacts[1], Contact)
        self.assertEquals(len(serializer.list_contacts.contacts), 2)

    def test_mount_list_users(self):
        serializer = self.serializer(
            list_contacts=self.list_contacts
        )
        result = serializer.mount_list_contacts()

        self.assertIsInstance(result, list)
        self.assertEquals(len(result), 2)

    def test_mount_payload(self):
        serializer = self.serializer(
            list_contacts=self.list_contacts
        )
        result = serializer.mount_payload()

        self.assertIsInstance(result, dict)
        self.assertEquals(len(result['contacts']), 2)

    def test_create_message(self):
        serializer = self.serializer(
            list_contacts=self.list_contacts
        )
        result = serializer.create_message()

        self.assertIsInstance(result, dict)

from contacts.domain.entities.contact import Contact
from contacts.domain.entities.list_contacts import ListContacts
from django.test import TestCase


class UserEntityTestCase(TestCase):
    """
    Tests of UserEntity in contacts.domain..entities.contact.py
    """

    def setUp(self):
        self.user_one = Contact(
            name="Joao",
            phone_number="859999999"
        )
        self.user_one.id = 1

        self.user_two = Contact(
            name="Pedro",
            phone_number="858888888"
        )
        self.user_two.id = 2

    def test_isistance_object(self):
        self.assertIsInstance(self.user_one, Contact)
        self.assertIsInstance(self.user_two, Contact)

    def test_atributes_values_user(self):
        user_json1 = {
            "id": 1,
            "name": "Joao",
            "phone_number": "859999999",
        }

        user_json2 = {
            "id": 2,
            "name": "Pedro",
            "phone_number": "858888888",
        }

        self.assertEquals(self.user_one.id, 1)
        self.assertEquals(self.user_one.id, user_json1["id"])
        self.assertEquals(self.user_one.name, "Joao")
        self.assertEquals(self.user_one.name, user_json1["name"])
        self.assertEquals(self.user_one.phone_number, "859999999")
        self.assertEquals(self.user_one.phone_number, user_json1["phone_number"])

        self.assertEquals(self.user_two.id, 2)
        self.assertEquals(self.user_two.id, user_json2["id"])
        self.assertEquals(self.user_two.name, "Pedro")
        self.assertEquals(self.user_two.name, user_json2["name"])
        self.assertEquals(self.user_two.phone_number, "858888888")
        self.assertEquals(self.user_two.phone_number, user_json2["phone_number"])

    def test_atributes_type_user(self):

        self.assertIsInstance(self.user_one.id, int)
        self.assertIsInstance(self.user_one.name, str)
        self.assertIsInstance(self.user_one.phone_number, str)

        self.assertIsInstance(self.user_two.id, int)
        self.assertIsInstance(self.user_two.name, str)
        self.assertIsInstance(self.user_two.phone_number, str)

    def test_repr_class_po(self):

        repr1: str = "Entity: Contact<name: Joao>"
        repr2: str = "Entity: Contact<name: Pedro>"

        self.assertEquals(self.user_one.__str__(), repr1)
        self.assertEquals(self.user_two.__str__(), repr2)


class ListUsersEntityTestCase(TestCase):
    """
    Tests of ListUsersEntity in contacts.domain..entities.list_contacts.py
    """

    def setUp(self):
        self.user_one = Contact(
            name="Joao",
            phone_number="859999999"
        )
        self.user_one.id = 1

        self.user_two = Contact(
            name="Pedro",
            phone_number="858888888"
        )
        self.user_two.id = 2

        self.list_contacts = ListContacts(contacts=list(), user_manager_id=1)
        self.list_contacts.add_user_to_list(self.user_one)
        self.list_contacts.add_user_to_list(self.user_two)

    def test_isistance_object(self):
        self.assertIsInstance(self.list_contacts, ListContacts)
        self.assertIsInstance(self.list_contacts.contacts, list)

    def test_atributes_values_user(self):

        self.assertEquals(len(self.list_contacts.contacts), 2)
        self.assertEquals(self.list_contacts.contacts[0].id, 1)
        self.assertEquals(self.list_contacts.contacts[1].id, 2)

    def test_atributes_type_user(self):
        self.assertIsInstance(self.list_contacts.contacts, list)
        self.assertIsInstance(self.list_contacts.contacts[0], object)
        self.assertIsInstance(self.list_contacts.contacts[1], object)

    def test_repr_class_po(self):
        repr_user: str = "Entity: <ListContacts>"

        self.assertEquals(self.list_contacts.__str__(), repr_user)

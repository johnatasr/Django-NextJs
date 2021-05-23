from contacts.presenters.factory import ContactsFactory
from contacts.domain.models.contact import Contact

from django.contrib.auth.models import User
from django.test import TestCase


class ContactsFactoryTestCase(TestCase):
    """
    Tests of ContactsFactory in contacts.presenters.factories.py
    """

    def setUp(self):
        Contact.objects.create(
            name="Joao",
            phone_number="859999999")

        Contact.objects.create(
            name="Pedro",
            phone_number="858888888")

        self.factory = ContactsFactory()
        self.data: dict = {
            "name": "Johnatas Rabelo",
            "phoneNumber": "8599999999",
        }

        self.user = User.objects.create_user("johnatas", "johnatas@admin.com", "John123*")

    def test_create_get_iterator_with_param(self):
        msg = self.factory.create_get_iterator(user_id=self.user.id, id_params=1)
        self.assertIsInstance(msg, dict)

    def test_create_get_iterator(self):
        msg = self.factory.create_get_iterator(user_id=self.user.id)
        self.assertIsInstance(msg, dict)

    def test_create_post_iterator(self):
        msg = self.factory.create_post_iterator(
            data={
                "name": "john34",
                "phoneNumber": "8598989899"
            }, user_id=self.user.id)
        self.assertIsInstance(msg, dict)

    def test_create_update_iterator(self):
        msg = self.factory.create_update_iterator(
            data={
                "name": "john34",
                "phoneNumber": "8598989899"
            }, contact_id=1)
        self.assertIsInstance(msg, dict)

    def test_create_delete_iterator(self):
        msg = self.factory.create_delete_iterator(contact_id=0)
        self.assertIsInstance(msg, str)


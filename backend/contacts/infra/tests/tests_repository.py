from contacts.domain.entities import contact, list_contacts as lc
from contacts.infra.repositories import ContactsRepo
from contacts.domain.models.contact import Contact

from django.contrib.auth.models import User
from django.test import TestCase


class ContactsRepoTestCase(TestCase):
    """
    Tests of ContactRepo in contacts.infra.repositories.py
    """

    def setUp(self):
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.user.is_active = True
        self.user.save()

        Contact.objects.create(
            name="Joao",
            phone_number="859999999")

        Contact.objects.create(
            name="Pedro",
            phone_number="859999999")

        self.repo = ContactsRepo()

    def test_list_contacts(self):
        result = self.repo.list_contacts_by_user_id(user_id=self.user.id)
        self.assertIsInstance(result, str)

    def test_get_contact_by_id(self):
        contact_en = self.repo.get_contact_by_id(contact_id=7)
        self.assertIsInstance(contact_en, contact.Contact)

    def test_create_contact(self):
        contact_entity = self.repo.create_contact(
            contact=contact.Contact(
                name="Marcos",
                phone_number="859999999"), user_id=self.user.id)
        self.assertIsInstance(contact_entity, contact.Contact)
        self.assertEquals(contact_entity.name, "Marcos")

    def test_update_contact_by_id(self):
        contact_entity = self.repo.create_contact(
            contact=contact.Contact(
                name="Marcos",
                phone_number="859999999"), user_id=self.user.id)

        contact_entity.id = 1
        contact_entity.name = "Fagner"

        result = self.repo.update_contact_by_id(contact=contact_entity)

        self.assertIsInstance(result, str)

    def test_delete_contact_by_id(self):
        contact_entity = self.repo.create_contact(
            contact=contact.Contact(
                name="Marcos",
                phone_number="859999999"), user_id=self.user.id)

        contact_to_delete = self.repo.delete_contact_by_id(contact_id=contact_entity.id)

        self.assertEquals(contact_to_delete, "User with ID: 6 deleted")


from contacts.domain.entities import contact, list_contacts as lc
from contacts.infra.repositories import ContactsRepo
from contacts.domain.models.contact import Contact

from django.test import TestCase


class ContactsRepoTestCase(TestCase):
    """
    Tests of ContactRepo in contacts.infra.repositories.py
    """

    def setUp(self):
        Contact.objects.create(
            name="Joao",
            phone_number="859999999")

        Contact.objects.create(
            name="Pedro",
            phone_number="859999999")

        self.repo = ContactsRepo()

    def test_list_contacts(self):
        list_contacts = self.repo.list_contacts_by_user_id()
        self.assertIsInstance(list_contacts, lc.ListContacts)
        self.assertEquals(len(list_contacts.contacts), 2)
        self.assertEquals(list_contacts.contacts[0].name, "Joao")
        self.assertEquals(list_contacts.contacts[1].name, "Pedro")

    def test_get_contact_by_id(self):
        contact_en = self.repo.get_contact_by_id(contact_id=1)
        self.assertIsInstance(contact_en, contact.Contact)

    def test_create_contact(self):
        contact_entity = self.repo.create_contact(
            contact=contact.Contact(
                name="Marcos",
                phone_number="859999999"))
        self.assertIsInstance(contact_entity, contact.Contact)
        self.assertEquals(contact_entity.name, "Marcos")

    def test_update_contact_by_id(self):
        contact_entity = self.repo.create_contact(
            contact=contact.Contact(
                name="Marcos",
                phone_number="859999999"))

        contact_entity.id = 1
        contact_entity.name = "Fagner"

        contact_to_update = self.repo.update_contact_by_id(contact=contact_entity)

        self.assertEquals(contact_to_update.name, "Fagner")

    def test_delete_contact_by_id(self):
        contact_entity = self.repo.create_contact(
            contact=contact.Contact(
                name="Marcos",
                phone_number="859999999"))

        contact_to_delete = self.repo.delete_contact_by_id(contact_id=contact_entity.id)

        self.assertEquals(contact_to_delete, "User removed !")


from contacts.domain.use_cases import (
    create_contact,
    update_contact,
    list_contacts,
    delete_contact,
    show_contact
)
from django.test import TestCase


class UseCasesTestCase(TestCase):
    """
    Tests of Abstract Interfaces of UseCases in contacts.domain.use_cases
    """

    def test_cannot_instantiate_create_contact_case(self):
        with self.assertRaises(TypeError):
            create_contact.CreateContactCase()

    def test_cannot_instantiate_update_contact_case(self):
        with self.assertRaises(TypeError):
            update_contact.UpdateContactCase()

    def test_cannot_instantiate_list_contacts_case(self):
        with self.assertRaises(TypeError):
            list_contacts.ListContactsCase()

    def test_cannot_instantiate_delete_contact_case(self):
        with self.assertRaises(TypeError):
            delete_contact.DeleteContactCase()

    def test_cannot_instantiate_show_contact_case(self):
        with self.assertRaises(TypeError):
            show_contact.ShowContactUseCase()
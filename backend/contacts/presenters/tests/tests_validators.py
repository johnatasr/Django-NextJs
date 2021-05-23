from contacts.presenters.validators import ContactsValidator

from django.test import TestCase
import unittest


class UsersValidatorTestCase(TestCase):
    """
    Tests of UsersValidator in contacts.presenters.validators.py
    """

    def setUp(self):
        self.validator = ContactsValidator()
        self.data: dict = {
            "name": "john34",
            "phoneNumber": "8598989899"
        }

    def test_validate(self):
        self.assertEquals(self.validator.validate(True), True)
        self.assertEquals(self.validator.validate(False), False)

    def test_is_empty_payload(self):
        result = self.validator.is_empty_payload(self.data)
        self.assertEquals(result, True)

    @unittest.expectedFailure
    def test_is_empty_payload_fail(self):
        self.validator.is_empty_payload(None)

    def test_validate_field(self):
        ob = {"name": "test"}
        result = self.validator.validate_field(key="name", field=ob["name"], type_value=str)
        self.assertEquals(result, True)

    @unittest.expectedFailure
    def test_validate_field_fail(self):
        ob = {"name": "test"}
        self.validator.validate_field(key="name", field=ob["name"], type_value=int)

    def test_validate_field_phoneNumber(self):
        ob = {"phoneNumber": "85455555555"}
        result = self.validator.validate_field(key="name", field=ob["phoneNumber"], type_value=str, min_len_field=8)
        self.assertEquals(result, True)

    @unittest.expectedFailure
    def test_validate_field_fail_phoneNumber(self):
        ob = {"phoneNumber": "8599"}
        result = self.validator.validate_field(key="name", field=ob["phoneNumber"], type_value=str, len_field=8)
        self.assertEquals(result, True)

    def test_validate_id_param(self):
        result1 = self.validator.validate_id_param(id_param=2)
        result2 = self.validator.validate_id_param(id_param=3.5)
        self.assertEquals(result1, 2)
        self.assertEquals(result2, 3)

    @unittest.expectedFailure
    def test_validate_id_param_fail(self):
        self.validator.validate_id_param(id_param=-2)

    def test_validate_payload(self):
        result = self.validator.validate_payload(self.data)
        self.assertEquals(result, True)

    @unittest.expectedFailure
    def test_validate_payload_fail(self):
        self.validator.validate_payload(None)
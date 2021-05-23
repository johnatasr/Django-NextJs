from contacts.presenters.helpers import round_floor_number
from django.test import TestCase


class HelpersTest(TestCase):
    """
    Tests of Helpers in contacts.presenters.helpers.py
    """

    def test_round_floor_number(self):
        number = round_floor_number(2)
        self.assertEquals(number, 2)

    def test_round_floor_number_wrong(self):
        number = round_floor_number(2.5)
        self.assertEquals(number, 2)


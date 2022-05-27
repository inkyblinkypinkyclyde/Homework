import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Boris")

    def test_guest_has_name(self):
        self.assertEqual("Boris", self.guest1.name)
import unittest
from ..utils.util import get_role_object_by_role_name

class TestUtil(unittest.TestCase):
    def test_get_role_object_by_role_name(self):
        expected = "user"

        actual = get_role_object_by_role_name("user")
        self.assertEqual(expected,actual.role)

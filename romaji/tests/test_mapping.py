import unittest

from romaji.mapping import Mapping
from romaji.system import System


class TestMapping(unittest.TestCase):

    def setUp(self):
        pass

    def test_has_STANDARD(self):
        for k, v in Mapping.dump().items():
            self.assertTrue(System.STANDARD in v)

    def test_get(self):
        expected = {
            System.STANDARD: 'xtu',
            System.L: 'ltu',
            System.LONG: 'ltsu',
        }
        self.assertEqual(Mapping.get("っ"), expected)

    def test_not_exits_key(self):
        self.assertIsNone(Mapping.get("五"))

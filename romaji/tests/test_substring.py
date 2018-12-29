import unittest

from romaji.substring import Substring
from romaji.system import System


class TestSubstring(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_systems(self):
        sub = Substring('っ', 0)
        expected = {System.STANDARD, System.L, System.LONG}
        self.assertEqual(sub.get_systems(), expected)

    def test_get_systems_empty(self):
        sub = Substring('五', 0)
        expected = set()
        self.assertEqual(sub.get_systems(), expected)

    def test_get_romaji(self):
        sub = Substring('っ', 0)
        self.assertEqual('xtu', sub.get_romaji(System.STANDARD))

    def test_get_romaji_not_has_romaji(self):
        sub = Substring('五', 0)
        self.assertEqual('五', sub.get_romaji(System.STANDARD))

    def test_lookahead(self):
        sub = Substring.lookahead(1, 'きゃきゃ', 2)
        self.assertEqual('kya', sub.get_romaji(System.STANDARD))

    def test_lookahead_overflow(self):
        sub = Substring.lookahead(0, 'きゃきゃ', 3)
        self.assertEqual('xya', sub.get_romaji(System.STANDARD))
        sub = Substring.lookahead(1, 'きゃきゃ', 3)
        self.assertIsNone(sub)

    def test_lookahead_not_has_romaji(self):
        sub = Substring.lookahead(0, '五十六', 0)
        self.assertIsNone(sub)

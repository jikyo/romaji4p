import unittest

from romaji.substring import Substring
from romaji.system import System
from romaji.transliteration import Transliteration


class TestTransliteration(unittest.TestCase):

    def setUp(self):
        pass

    def test_try_to_append_none(self):
        t = Transliteration()
        t.try_to_append(None)
        self.assertEqual(t.romajis(), set())

    def test_try_to_append_not_match(self):
        t = Transliteration()
        sub = Substring.lookahead(1, "よじょうはん", 3);
        t.try_to_append(sub)
        self.assertEqual(t.romajis(), set())

    def test_find_system(self):
        sub = Substring('っ', 0)
        self.assertEqual(Transliteration.find_system(sub, sub.get_systems()), System.L)

        systems = {System.STANDARD, System.LONG}
        self.assertEqual(Transliteration.find_system(sub, systems), System.LONG)

        systems = {System.X}
        self.assertEqual(Transliteration.find_system(sub, systems), System.STANDARD)

    def test_substring_to_romaji(self):
        sub = Substring('っ', 0)

        systems = {System.STANDARD, System.LONG}
        self.assertEqual(Transliteration.substring_to_romaji(sub, systems), 'ltsu')

        systems = {System.STANDARD, System.L}
        self.assertEqual(Transliteration.substring_to_romaji(sub, systems), 'ltu')

        systems = {System.STANDARD}
        self.assertEqual(Transliteration.substring_to_romaji(sub, systems), 'xtu')

        systems = {System.STANDARD, System.Y}
        self.assertEqual(Transliteration.substring_to_romaji(sub, systems), 'xtu')

    def test_romaji(self):
        src = "あっち"
        subs = [
            Substring(src[0:1], 0),
            Substring(src[1:2], 1),
            Substring(src[2:3], 2),
        ]

        systems = {System.STANDARD, System.LONG}
        self.assertEqual(Transliteration.romaji(subs, systems), 'altsuchi')

        systems = {System.STANDARD, System.Y}
        self.assertEqual(Transliteration.romaji(subs, systems), 'axtuti')

        systems = {System.STANDARD}
        self.assertEqual(Transliteration.romaji(subs, systems), 'axtuti')

    def test_romajis(self):
        src = "アッチ"
        t = Transliteration()
        t.try_to_append(Substring(src[0:1], 0))
        t.try_to_append(Substring(src[1:2], 1))
        t.try_to_append(Substring(src[2:3], 2))

        expected = {
            'axtuti',
            'altuti',
            'altsuchi',
            'altuchi',
            'atti',
            'acchi',
        }
        self.assertEqual(t.romajis(), expected)

import unittest

from romaji.filter import Filter


class TestRule(unittest.TestCase):

    def setUp(self):
        pass

    def test_replace_xtu(self):
        # test for replaced.
        self.assertEqual(Filter.replace_xtu('axtsuchi'), 'acchi')
        self.assertEqual(Filter.replace_xtu('galtutu'), 'gattu')
        self.assertEqual(Filter.replace_xtu('galtsutu'), 'gattu')
        self.assertEqual(Filter.replace_xtu('axtsu'), 'axtsu')

        # test for not replaced.
        self.assertEqual(Filter.replace_xtu('axtsua'), 'axtsua')
        self.assertEqual(Filter.replace_xtu('axtui'), 'axtui')
        self.assertEqual(Filter.replace_xtu('altsuu'), 'altsuu')
        self.assertEqual(Filter.replace_xtu('altue'), 'altue')
        self.assertEqual(Filter.replace_xtu('axtsuo'), 'axtsuo')

        self.assertEqual(Filter.replace_xtu('xtsuxtsu'), 'xtsuxtsu')
        self.assertEqual(Filter.replace_xtu('altultua'), 'altultua')

    def test_replace_ou_to_o(self):
        self.assertEqual(Filter.replace_ou_to_o('ou'), 'o')
        self.assertEqual(Filter.replace_ou_to_o('ouu'), 'ou')
        self.assertEqual(Filter.replace_ou_to_o('ouuu'), 'ouu')
        self.assertEqual(Filter.replace_ou_to_o('ouuuou'), 'ouuo')

    def test_expant_and_reduce(self):
        target = 'axtsuchinohougaku'
        actual = Filter.expand_and_reduce({target})
        expected = {'acchinohogaku', target}
        self.assertEqual(expected, actual)

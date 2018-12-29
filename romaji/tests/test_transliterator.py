import unittest

from romaji.transliterator import transliterate


class TestTransliterator(unittest.TestCase):

    case = {
        'きょうと': [
            'kilyoto',
            'kilyouto',
            'kixyoto',
            'kixyouto',
            'kyoto',
            'kyouto',
        ],
        'トッキョ': [
            'tokkilyo',
            'tokkixyo',
            'tokkyo',
            'toltsukixyo',
            'toltsukyo',
            'toltukilyo',
            'toltukyo',
            'toxtukixyo',
            'toxtukyo',
        ],
        'ドラえもん': [
            'doraemon',
            'doraemon\'',
            'doraemonn',
        ],
        'っっっっっ': [
            'ltsultsultsultsultsu',
            'ltultultultultu',
            'xtuxtuxtuxtuxtu',
        ],
        '僕ドラえもん': [
            '僕doraemon',
            '僕doraemon\'',
            '僕doraemonn',
        ],
        '東京都': [],
        'お茶の水': [
            'o茶no水',
        ]
    }

    def setUp(self):
        pass

    def test_transliterate(self):
        for k, v in self.case.items():
            self.assertEqual(transliterate(k), v)

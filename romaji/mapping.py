""" The mapping from hiragana/katakana to romaji.

Note that each of hiragana/katakana char must have the System.STANDARD as a default system.
 """
from romaji.system import System


class Mapping:

    __map = {
        # 全角ひらがな

        # あ行
        'あ': {
            System.STANDARD: 'a',
        },
        'い': {
            System.STANDARD: 'i',
            # System.Y:		    'yi',
        },
        'う': {
            System.STANDARD: 'u',
            # System.SHORT:   	'wi',
            # System.LONG:    	'whi',
        },
        'え': {
            System.STANDARD: 'e',
        },
        'お': {
            System.STANDARD: 'o',
        },

        'うぁ': {
            System.STANDARD: 'wha',
        },
        'うぃ': {
            System.STANDARD: 'whi',
            System.SHORT: 'wi',
        },
        'うぇ': {
            System.STANDARD: 'whe',
            System.SHORT: 'we',
        },
        'うぉ': {
            System.STANDARD: 'who',
            System.SHORT: 'we',
        },

        'ゐ': {
            System.STANDARD: 'wi',
        },
        'ゑ': {
            System.STANDARD: 'we',
        },

        'ぁ': {
            System.STANDARD: 'xa',
            System.L: 'la',
        },
        'ぃ': {
            System.STANDARD: 'xi',
            System.L: 'li',
            System.XY: 'xyi',
            System.LY: 'lyi',
        },
        'ぅ': {
            System.STANDARD: 'xu',
            System.L: 'lu',
        },
        'ぇ': {
            System.STANDARD: 'xe',
            System.L: 'le',
            System.XY: 'xye',
            System.LY: 'lye',
        },
        'ぉ': {
            System.STANDARD: 'xo',
            System.L: 'lo',
        },

        'いぇ': {
            System.STANDARD: 'ye',
        },

        # か行
        'か': {
            System.STANDARD: 'ka',
            System.SHORT: 'ca',
        },
        'き': {
            System.STANDARD: 'ki',
        },
        'く': {
            System.STANDARD: 'ku',
            System.SHORT: 'cu',
            # System.SHORT:		'qu',
        },
        'け': {
            System.STANDARD: 'ke',
        },
        'こ': {
            System.STANDARD: 'ko',
        },

        'きゃ': {
            System.STANDARD: 'kya',
        },
        'きぃ': {
            System.STANDARD: 'kyi',
        },
        'きゅ': {
            System.STANDARD: 'kyu',
        },
        'きぇ': {
            System.STANDARD: 'kye',
        },
        'きょ': {
            System.STANDARD: 'kyo',
        },

        'くゃ': {
            System.STANDARD: 'qya',
        },
        'くゅ': {
            System.STANDARD: 'qyu',
        },
        'くょ': {
            System.STANDARD: 'quo',
        },

        'くぁ': {
            System.STANDARD: 'qwa',
            System.SHORT: 'qa',
            # System.LONG:		'kwa',
        },
        'くぃ': {
            System.STANDARD: 'qwi',
            System.SHORT: 'qi',
            System.Y: 'qyi',
        },
        'くぅ': {
            System.STANDARD: 'qwu',
        },
        'くぇ': {
            System.STANDARD: 'qwe',
            System.SHORT: 'qe',
            System.Y: 'qye',
        },
        'くぉ': {
            System.STANDARD: 'qwo',
            System.SHORT: 'qo',
        },

        'が': {
            System.STANDARD: 'ga',
        },
        'ぎ': {
            System.STANDARD: 'gi',
        },
        'ぐ': {
            System.STANDARD: 'gu',
        },
        'げ': {
            System.STANDARD: 'ge',
        },
        'ご': {
            System.STANDARD: 'go',
        },

        'ぎゃ': {
            System.STANDARD: 'gya',
        },
        'ぎぃ': {
            System.STANDARD: 'gyi',
        },
        'ぎゅ': {
            System.STANDARD: 'gyu',
        },
        'ぎぇ': {
            System.STANDARD: 'gye',
        },
        'ぎょ': {
            System.STANDARD: 'gyo',
        },

        'ぐぁ': {
            System.STANDARD: 'gwa',
        },
        'ぐぃ': {
            System.STANDARD: 'gwi',
        },
        'ぐぅ': {
            System.STANDARD: 'gwu',
        },
        'ぐぇ': {
            System.STANDARD: 'gwe',
        },
        'ぐぉ': {
            System.STANDARD: 'gwo',
        },

        # さ行
        'さ': {
            System.STANDARD: 'sa',
        },
        'し': {
            System.STANDARD: 'si',
            System.SHORT: 'ci',
            System.LONG: 'shi',
        },
        'す': {
            System.STANDARD: 'su',
        },
        'せ': {
            System.STANDARD: 'se',
            System.SHORT: 'ce',
        },
        'そ': {
            System.STANDARD: 'so',
        },

        'しゃ': {
            System.STANDARD: 'sya',
            System.LONG: 'sha',
        },
        'しぃ': {
            System.STANDARD: 'syi',
        },
        'しゅ': {
            System.STANDARD: 'syu',
            System.LONG: 'shu',
        },
        'しぇ': {
            System.STANDARD: 'sye',
            System.LONG: 'she',
        },
        'しょ': {
            System.STANDARD: 'syo',
            System.LONG: 'sho',
        },

        'すぁ': {
            System.STANDARD: 'swa',
        },
        'すぃ': {
            System.STANDARD: 'swi',
        },
        'すぅ': {
            System.STANDARD: 'swu',
        },
        'すぇ': {
            System.STANDARD: 'swe',
        },
        'すぉ': {
            System.STANDARD: 'swo',
        },

        'ざ': {
            System.STANDARD: 'za',
        },
        'じ': {
            System.STANDARD: 'zi',
            System.SHORT: 'ji',
        },
        'ず': {
            System.STANDARD: 'zu',
        },
        'ぜ': {
            System.STANDARD: 'ze',
        },
        'ぞ': {
            System.STANDARD: 'zo',
        },

        'じゃ': {
            System.STANDARD: 'zya',
            System.SHORT: 'ja',
            System.LONG: 'jya',
        },
        'じぃ': {
            System.STANDARD: 'zyi',
            System.LONG: 'jyi',
        },
        'じゅ': {
            System.STANDARD: 'zyu',
            System.SHORT: 'ju',
            System.LONG: 'jyu',
        },
        'じぇ': {
            System.STANDARD: 'zye',
            System.SHORT: 'je',
            System.LONG: 'zye',
        },
        'じょ': {
            System.STANDARD: 'zyo',
            System.SHORT: 'jo',
            System.LONG: 'jyo',
        },

        # た行
        'た': {
            System.STANDARD: 'ta',
        },
        'ち': {
            System.STANDARD: 'ti',
            System.LONG: 'chi',
        },
        'つ': {
            System.STANDARD: 'tu',
            System.LONG: 'tsu',
        },
        'て': {
            System.STANDARD: 'te',
        },
        'と': {
            System.STANDARD: 'to',
        },

        'ちゃ': {
            System.STANDARD: 'tya',
            System.LONG: 'cha',
            System.Y: 'cya',
        },
        'ちぃ': {
            System.STANDARD: 'tyi',
            System.Y: 'cyi',
        },
        'ちゅ': {
            System.STANDARD: 'tyu',
            System.LONG: 'chu',
            System.Y: 'cyu',
        },
        'ちぇ': {
            System.STANDARD: 'tye',
            System.LONG: 'che',
            System.Y: 'cye',
        },
        'ちょ': {
            System.STANDARD: 'tyo',
            System.LONG: 'cho',
            System.Y: 'cyo',
        },

        'つぁ': {
            System.STANDARD: 'tsa',
        },
        'つぃ': {
            System.STANDARD: 'tsi',
        },
        'つぇ': {
            System.STANDARD: 'tse',
        },
        'つぉ': {
            System.STANDARD: 'tso',
        },

        'てゃ': {
            System.STANDARD: 'tha',
        },
        'てぃ': {
            System.STANDARD: 'thi',
        },
        'てゅ': {
            System.STANDARD: 'thu',
        },
        'てぇ': {
            System.STANDARD: 'the',
        },
        'てょ': {
            System.STANDARD: 'tho',
        },

        'とぁ': {
            System.STANDARD: 'twa',
        },
        'とぃ': {
            System.STANDARD: 'twi',
        },
        'とぅ': {
            System.STANDARD: 'twu',
        },
        'とぇ': {
            System.STANDARD: 'twe',
        },
        'とぉ': {
            System.STANDARD: 'two',
        },

        'だ': {
            System.STANDARD: 'da',
        },
        'ぢ': {
            System.STANDARD: 'di',
        },
        'づ': {
            System.STANDARD: 'du',
        },
        'で': {
            System.STANDARD: 'de',
        },
        'ど': {
            System.STANDARD: 'do',
        },

        'ぢゃ': {
            System.STANDARD: 'dya',
        },
        'ぢぃ': {
            System.STANDARD: 'dyi',
        },
        'ぢゅ': {
            System.STANDARD: 'dyu',
        },
        'ぢぇ': {
            System.STANDARD: 'dye',
        },
        'ぢょ': {
            System.STANDARD: 'dyo',
        },

        'でゃ': {
            System.STANDARD: 'dha',
        },
        'でぃ': {
            System.STANDARD: 'dhi',
        },
        'でゅ': {
            System.STANDARD: 'dhu',
        },
        'でぇ': {
            System.STANDARD: 'dhe',
        },
        'でょ': {
            System.STANDARD: 'dho',
        },

        'どぁ': {
            System.STANDARD: 'dwa',
        },
        'どぃ': {
            System.STANDARD: 'dwi',
        },
        'どぅ': {
            System.STANDARD: 'dwu',
        },
        'どぇ': {
            System.STANDARD: 'dwe',
        },
        'どぉ': {
            System.STANDARD: 'dwo',
        },

        'っ': {
            System.STANDARD: 'xtu',
            System.L: 'ltu',
            System.LONG: 'ltsu',
        },

        # な行
        'な': {
            System.STANDARD: 'na',
        },
        'に': {
            System.STANDARD: 'ni',
        },
        'ぬ': {
            System.STANDARD: 'nu',
        },
        'ね': {
            System.STANDARD: 'ne',
        },
        'の': {
            System.STANDARD: 'no',
        },

        'にゃ': {
            System.STANDARD: 'nya',
        },
        'にぃ': {
            System.STANDARD: 'nyi',
        },
        'にゅ': {
            System.STANDARD: 'nyu',
        },
        'にぇ': {
            System.STANDARD: 'nye',
        },
        'にょ': {
            System.STANDARD: 'nyo',
        },

        # は行
        'は': {
            System.STANDARD: 'ha',
        },
        'ひ': {
            System.STANDARD: 'hi',
        },
        'ふ': {
            System.STANDARD: 'hu',
            System.SHORT: 'fu',
        },
        'へ': {
            System.STANDARD: 'he',
        },
        'ほ': {
            System.STANDARD: 'ho',
        },

        'ひゃ': {
            System.STANDARD: 'hya',
        },
        'ひぃ': {
            System.STANDARD: 'hyi',
        },
        'ひゅ': {
            System.STANDARD: 'hyu',
        },
        'ひぇ': {
            System.STANDARD: 'hye',
        },
        'ひょ': {
            System.STANDARD: 'hyo',
        },

        'ふぁ': {
            System.STANDARD: 'fwa',
            System.SHORT: 'fa',
        },
        'ふぃ': {
            System.STANDARD: 'fwi',
            System.SHORT: 'fi',
            System.Y: 'fyi',
        },
        'ふぅ': {
            System.STANDARD: 'fwu',
        },
        'ふぇ': {
            System.STANDARD: 'fwe',
            System.SHORT: 'fe',
            System.Y: 'fye',
        },
        'ふぉ': {
            System.STANDARD: 'fwo',
            System.SHORT: 'fo',
        },

        'ふゃ': {
            System.STANDARD: 'fya',
        },
        'ふゅ': {
            System.STANDARD: 'fyu',
        },
        'ふょ': {
            System.STANDARD: 'fyo',
        },

        'ば': {
            System.STANDARD: 'ba',
        },
        'び': {
            System.STANDARD: 'bi',
        },
        'ぶ': {
            System.STANDARD: 'bu',
        },
        'べ': {
            System.STANDARD: 'be',
        },
        'ぼ': {
            System.STANDARD: 'bo',
        },

        'びゃ': {
            System.STANDARD: 'bya',
        },
        'びぃ': {
            System.STANDARD: 'byi',
        },
        'びゅ': {
            System.STANDARD: 'byu',
        },
        'びぇ': {
            System.STANDARD: 'bye',
        },
        'びょ': {
            System.STANDARD: 'byo',
        },

        'ぱ': {
            System.STANDARD: 'pa',
        },
        'ぴ': {
            System.STANDARD: 'pi',
        },
        'ぷ': {
            System.STANDARD: 'pu',
        },
        'ぺ': {
            System.STANDARD: 'pe',
        },
        'ぽ': {
            System.STANDARD: 'po',
        },

        'ぴゃ': {
            System.STANDARD: 'pya',
        },
        'ぴぃ': {
            System.STANDARD: 'pyi',
        },
        'ぴゅ': {
            System.STANDARD: 'pyu',
        },
        'ぴぇ': {
            System.STANDARD: 'pye',
        },
        'ぴょ': {
            System.STANDARD: 'pyo',
        },

        # ま行
        'ま': {
            System.STANDARD: 'ma',
        },
        'み': {
            System.STANDARD: 'mi',
        },
        'む': {
            System.STANDARD: 'mu',
        },
        'め': {
            System.STANDARD: 'me',
        },
        'も': {
            System.STANDARD: 'mo',
        },

        'みゃ': {
            System.STANDARD: 'mya',
        },
        'みぃ': {
            System.STANDARD: 'myi',
        },
        'みゅ': {
            System.STANDARD: 'myu',
        },
        'みぇ': {
            System.STANDARD: 'mye',
        },
        'みょ': {
            System.STANDARD: 'myo',
        },

        # や行
        'や': {
            System.STANDARD: 'ya',
        },
        'ゆ': {
            System.STANDARD: 'yu',
        },
        'よ': {
            System.STANDARD: 'yo',
        },

        'ゃ': {
            System.STANDARD: 'xya',
            System.L: 'lya',
        },
        'ゅ': {
            System.STANDARD: 'xyu',
            System.L: 'lyu',
        },
        'ょ': {
            System.STANDARD: 'xyo',
            System.L: 'lyo',
        },

        # ら行
        'ら': {
            System.STANDARD: 'ra',
        },
        'り': {
            System.STANDARD: 'ri',
        },
        'る': {
            System.STANDARD: 'ru',
        },
        'れ': {
            System.STANDARD: 're',
        },
        'ろ': {
            System.STANDARD: 'ro',
        },

        'りゃ': {
            System.STANDARD: 'rya',
        },
        'りぃ': {
            System.STANDARD: 'ryi',
        },
        'りゅ': {
            System.STANDARD: 'ryu',
        },
        'りぇ': {
            System.STANDARD: 'rye',
        },
        'りょ': {
            System.STANDARD: 'ryo',
        },

        # わ行
        'わ': {
            System.STANDARD: 'wa',
        },
        'を': {
            System.STANDARD: 'wo',
        },
        'ん': {
            System.STANDARD: 'n',
            System.LONG: 'nn',
            System.SHORT: 'n\'',
            # System.X:			'xn',
        },

        'ゎ': {
            System.STANDARD: 'xwa',
            System.L: 'lwa',
        },

        # 全角カタカナ

        # ア行
        'ア': {
            System.STANDARD: 'a',
        },
        'イ': {
            System.STANDARD: 'i',
            # System.Y:			'yi',
        },
        'ウ': {
            System.STANDARD: 'u',
            # System.SHORT:		'wi',
            # System.LONG:		'whi',
        },
        'エ': {
            System.STANDARD: 'e',
        },
        'オ': {
            System.STANDARD: 'o',
        },

        'ウァ': {
            System.STANDARD: 'wha',
        },
        'ウィ': {
            System.STANDARD: 'whi',
            System.SHORT: 'wi',
        },
        'ウェ': {
            System.STANDARD: 'whe',
            System.SHORT: 'we',
        },
        'ウォ': {
            System.STANDARD: 'who',
            System.SHORT: 'we',
        },

        'ヰ': {
            System.STANDARD: 'wi',
        },
        'ヱ': {
            System.STANDARD: 'we',
        },

        'ァ': {
            System.STANDARD: 'xa',
            System.L: 'la',
        },
        'ィ': {
            System.STANDARD: 'xi',
            System.L: 'li',
            System.XY: 'xyi',
            System.LY: 'lyi',
        },
        'ゥ': {
            System.STANDARD: 'xu',
            System.L: 'lu',
        },
        'ェ': {
            System.STANDARD: 'xe',
            System.L: 'le',
            System.XY: 'xye',
            System.LY: 'lye',
        },
        'ォ': {
            System.STANDARD: 'xo',
            System.L: 'lo',
        },

        'イェ': {
            System.STANDARD: 'ye',
        },

        # カ行
        'カ': {
            System.STANDARD: 'ka',
            System.SHORT: 'ca',
        },
        'キ': {
            System.STANDARD: 'ki',
        },
        'ク': {
            System.STANDARD: 'ku',
            System.SHORT: 'cu',
            # System.SHORT:		'qu',
        },
        'ケ': {
            System.STANDARD: 'ke',
        },
        'コ': {
            System.STANDARD: 'ko',
        },

        'キャ': {
            System.STANDARD: 'kya',
        },
        'キィ': {
            System.STANDARD: 'kyi',
        },
        'キュ': {
            System.STANDARD: 'kyu',
        },
        'キェ': {
            System.STANDARD: 'kye',
        },
        'キョ': {
            System.STANDARD: 'kyo',
        },

        'クャ': {
            System.STANDARD: 'qya',
        },
        'クュ': {
            System.STANDARD: 'qyu',
        },
        'クョ': {
            System.STANDARD: 'quo',
        },

        'クァ': {
            System.STANDARD: 'qwa',
            System.SHORT: 'qa',
            # System.LONG:		'kwa',
        },
        'クィ': {
            System.STANDARD: 'qwi',
            System.SHORT: 'qi',
            System.Y: 'qyi',
        },
        'クゥ': {
            System.STANDARD: 'qwu',
        },
        'クェ': {
            System.STANDARD: 'qwe',
            System.SHORT: 'qe',
            System.Y: 'qye',
        },
        'クォ': {
            System.STANDARD: 'qwo',
            System.SHORT: 'qo',
        },

        'ガ': {
            System.STANDARD: 'ga',
        },
        'ギ': {
            System.STANDARD: 'gi',
        },
        'グ': {
            System.STANDARD: 'gu',
        },
        'ゲ': {
            System.STANDARD: 'ge',
        },
        'ゴ': {
            System.STANDARD: 'go',
        },

        'ギャ': {
            System.STANDARD: 'gya',
        },
        'ギィ': {
            System.STANDARD: 'gyi',
        },
        'ギュ': {
            System.STANDARD: 'gyu',
        },
        'ギェ': {
            System.STANDARD: 'gye',
        },
        'ギョ': {
            System.STANDARD: 'gyo',
        },

        'グァ': {
            System.STANDARD: 'gwa',
        },
        'グィ': {
            System.STANDARD: 'gwi',
        },
        'グゥ': {
            System.STANDARD: 'gwu',
        },
        'グェ': {
            System.STANDARD: 'gwe',
        },
        'グォ': {
            System.STANDARD: 'gwo',
        },

        'ヵ': {
            System.STANDARD: 'xka',
            System.L: 'lka',
        },
        'ヶ': {
            System.STANDARD: 'xke',
            System.L: 'lke',
        },

        # サ行
        'サ': {
            System.STANDARD: 'sa',
        },
        'シ': {
            System.STANDARD: 'si',
            System.SHORT: 'ci',
            System.LONG: 'shi',
        },
        'ス': {
            System.STANDARD: 'su',
        },
        'セ': {
            System.STANDARD: 'se',
            System.SHORT: 'ce',
        },
        'ソ': {
            System.STANDARD: 'so',
        },

        'シャ': {
            System.STANDARD: 'sya',
            System.LONG: 'sha',
        },
        'シィ': {
            System.STANDARD: 'syi',
        },
        'シュ': {
            System.STANDARD: 'syu',
            System.LONG: 'shu',
        },
        'シェ': {
            System.STANDARD: 'sye',
            System.LONG: 'she',
        },
        'ショ': {
            System.STANDARD: 'syo',
            System.LONG: 'sho',
        },

        'スァ': {
            System.STANDARD: 'swa',
        },
        'スィ': {
            System.STANDARD: 'swi',
        },
        'スゥ': {
            System.STANDARD: 'swu',
        },
        'スェ': {
            System.STANDARD: 'swe',
        },
        'スォ': {
            System.STANDARD: 'swo',
        },

        'ザ': {
            System.STANDARD: 'za',
        },
        'ジ': {
            System.STANDARD: 'zi',
            System.SHORT: 'ji',
        },
        'ズ': {
            System.STANDARD: 'zu',
        },
        'ゼ': {
            System.STANDARD: 'ze',
        },
        'ゾ': {
            System.STANDARD: 'zo',
        },

        'ジャ': {
            System.STANDARD: 'zya',
            System.SHORT: 'ja',
            System.LONG: 'jya',
        },
        'ジィ': {
            System.STANDARD: 'zyi',
            System.LONG: 'jyi',
        },
        'ジュ': {
            System.STANDARD: 'zyu',
            System.SHORT: 'ju',
            System.LONG: 'jyu',
        },
        'ジェ': {
            System.STANDARD: 'zye',
            System.SHORT: 'je',
            System.LONG: 'zye',
        },
        'ジョ': {
            System.STANDARD: 'zyo',
            System.SHORT: 'jo',
            System.LONG: 'jyo',
        },

        # タ行
        'タ': {
            System.STANDARD: 'ta',
        },
        'チ': {
            System.STANDARD: 'ti',
            System.LONG: 'chi',
        },
        'ツ': {
            System.STANDARD: 'tu',
            System.LONG: 'tsu',
        },
        'テ': {
            System.STANDARD: 'te',
        },
        'ト': {
            System.STANDARD: 'to',
        },

        'チャ': {
            System.STANDARD: 'tya',
            System.LONG: 'cha',
            System.Y: 'cya',
        },
        'チィ': {
            System.STANDARD: 'tyi',
            System.Y: 'cyi',
        },
        'チュ': {
            System.STANDARD: 'tyu',
            System.LONG: 'chu',
            System.Y: 'cyu',
        },
        'チェ': {
            System.STANDARD: 'tye',
            System.LONG: 'che',
            System.Y: 'cye',
        },
        'チョ': {
            System.STANDARD: 'tyo',
            System.LONG: 'cho',
            System.Y: 'cyo',
        },

        'ツァ': {
            System.STANDARD: 'tsa',
        },
        'ツィ': {
            System.STANDARD: 'tsi',
        },
        'ツェ': {
            System.STANDARD: 'tse',
        },
        'ツォ': {
            System.STANDARD: 'tso',
        },

        'テャ': {
            System.STANDARD: 'tha',
        },
        'ティ': {
            System.STANDARD: 'thi',
        },
        'テュ': {
            System.STANDARD: 'thu',
        },
        'テェ': {
            System.STANDARD: 'the',
        },
        'テョ': {
            System.STANDARD: 'tho',
        },

        'トァ': {
            System.STANDARD: 'twa',
        },
        'トィ': {
            System.STANDARD: 'twi',
        },
        'トゥ': {
            System.STANDARD: 'twu',
        },
        'トェ': {
            System.STANDARD: 'twe',
        },
        'トォ': {
            System.STANDARD: 'two',
        },

        'ダ': {
            System.STANDARD: 'da',
        },
        'ヂ': {
            System.STANDARD: 'di',
        },
        'ヅ': {
            System.STANDARD: 'du',
        },
        'デ': {
            System.STANDARD: 'de',
        },
        'ド': {
            System.STANDARD: 'do',
        },

        'ヂャ': {
            System.STANDARD: 'dya',
        },
        'ヂィ': {
            System.STANDARD: 'dyi',
        },
        'ヂュ': {
            System.STANDARD: 'dyu',
        },
        'ヂェ': {
            System.STANDARD: 'dye',
        },
        'ヂョ': {
            System.STANDARD: 'dyo',
        },

        'デャ': {
            System.STANDARD: 'dha',
        },
        'ディ': {
            System.STANDARD: 'dhi',
        },
        'デュ': {
            System.STANDARD: 'dhu',
        },
        'デェ': {
            System.STANDARD: 'dhe',
        },
        'デョ': {
            System.STANDARD: 'dho',
        },

        'ドァ': {
            System.STANDARD: 'dwa',
        },
        'ドィ': {
            System.STANDARD: 'dwi',
        },
        'ドゥ': {
            System.STANDARD: 'dwu',
        },
        'ドェ': {
            System.STANDARD: 'dwe',
        },
        'ドォ': {
            System.STANDARD: 'dwo',
        },

        'ッ': {
            System.STANDARD: 'xtu',
            System.L: 'ltu',
            System.LONG: 'ltsu',
        },

        # ナ行
        'ナ': {
            System.STANDARD: 'na',
        },
        'ニ': {
            System.STANDARD: 'ni',
        },
        'ヌ': {
            System.STANDARD: 'nu',
        },
        'ネ': {
            System.STANDARD: 'ne',
        },
        'ノ': {
            System.STANDARD: 'no',
        },

        'ニャ': {
            System.STANDARD: 'nya',
        },
        'ニィ': {
            System.STANDARD: 'nyi',
        },
        'ニュ': {
            System.STANDARD: 'nyu',
        },
        'ニェ': {
            System.STANDARD: 'nye',
        },
        'ニョ': {
            System.STANDARD: 'nyo',
        },

        # ハ行
        'ハ': {
            System.STANDARD: 'ha',
        },
        'ヒ': {
            System.STANDARD: 'hi',
        },
        'フ': {
            System.STANDARD: 'hu',
            System.SHORT: 'fu',
        },
        'ヘ': {
            System.STANDARD: 'he',
        },
        'ホ': {
            System.STANDARD: 'ho',
        },

        'ヒャ': {
            System.STANDARD: 'hya',
        },
        'ヒィ': {
            System.STANDARD: 'hyi',
        },
        'ヒュ': {
            System.STANDARD: 'hyu',
        },
        'ヒェ': {
            System.STANDARD: 'hye',
        },
        'ヒョ': {
            System.STANDARD: 'hyo',
        },

        'ファ': {
            System.STANDARD: 'fwa',
            System.SHORT: 'fa',
        },
        'フィ': {
            System.STANDARD: 'fwi',
            System.SHORT: 'fi',
            System.Y: 'fyi',
        },
        'フゥ': {
            System.STANDARD: 'fwu',
        },
        'フェ': {
            System.STANDARD: 'fwe',
            System.SHORT: 'fe',
            System.Y: 'fye',
        },
        'フォ': {
            System.STANDARD: 'fwo',
            System.SHORT: 'fo',
        },

        'フャ': {
            System.STANDARD: 'fya',
        },
        'フュ': {
            System.STANDARD: 'fyu',
        },
        'フョ': {
            System.STANDARD: 'fyo',
        },

        'バ': {
            System.STANDARD: 'ba',
        },
        'ビ': {
            System.STANDARD: 'bi',
        },
        'ブ': {
            System.STANDARD: 'bu',
        },
        'ベ': {
            System.STANDARD: 'be',
        },
        'ボ': {
            System.STANDARD: 'bo',
        },

        'ビャ': {
            System.STANDARD: 'bya',
        },
        'ビィ': {
            System.STANDARD: 'byi',
        },
        'ビュ': {
            System.STANDARD: 'byu',
        },
        'ビェ': {
            System.STANDARD: 'bye',
        },
        'ビョ': {
            System.STANDARD: 'byo',
        },

        'パ': {
            System.STANDARD: 'pa',
        },
        'ピ': {
            System.STANDARD: 'pi',
        },
        'プ': {
            System.STANDARD: 'pu',
        },
        'ペ': {
            System.STANDARD: 'pe',
        },
        'ポ': {
            System.STANDARD: 'po',
        },

        'ピャ': {
            System.STANDARD: 'pya',
        },
        'ピィ': {
            System.STANDARD: 'pyi',
        },
        'ピュ': {
            System.STANDARD: 'pyu',
        },
        'ピェ': {
            System.STANDARD: 'pye',
        },
        'ピョ': {
            System.STANDARD: 'pyo',
        },

        'ヴァ': {
            System.STANDARD: 'va',
        },
        'ヴィ': {
            System.STANDARD: 'vi',
            System.LONG: 'vyi',
        },
        'ヴ': {
            System.STANDARD: 'vu',
        },
        'ヴェ': {
            System.STANDARD: 've',
            System.LONG: 'vye',
        },
        'ヴォ': {
            System.STANDARD: 'vo',
        },

        'ヴャ': {
            System.STANDARD: 'vya',
        },
        'ヴュ': {
            System.STANDARD: 'vyu',
        },
        'ヴョ': {
            System.STANDARD: 'vyo',
        },

        # マ行
        'マ': {
            System.STANDARD: 'ma',
        },
        'ミ': {
            System.STANDARD: 'mi',
        },
        'ム': {
            System.STANDARD: 'mu',
        },
        'メ': {
            System.STANDARD: 'me',
        },
        'モ': {
            System.STANDARD: 'mo',
        },

        'ミャ': {
            System.STANDARD: 'mya',
        },
        'ミィ': {
            System.STANDARD: 'myi',
        },
        'ミュ': {
            System.STANDARD: 'myu',
        },
        'ミェ': {
            System.STANDARD: 'mye',
        },
        'ミョ': {
            System.STANDARD: 'myo',
        },

        # ヤ行
        'ヤ': {
            System.STANDARD: 'ya',
        },
        'ユ': {
            System.STANDARD: 'yu',
        },
        'ヨ': {
            System.STANDARD: 'yo',
        },

        'ャ': {
            System.STANDARD: 'xya',
            System.L: 'lya',
        },
        'ュ': {
            System.STANDARD: 'xyu',
            System.L: 'lyu',
        },
        'ョ': {
            System.STANDARD: 'xyo',
            System.L: 'lyo',
        },

        # ラ行
        'ラ': {
            System.STANDARD: 'ra',
        },
        'リ': {
            System.STANDARD: 'ri',
        },
        'ル': {
            System.STANDARD: 'ru',
        },
        'レ': {
            System.STANDARD: 're',
        },
        'ロ': {
            System.STANDARD: 'ro',
        },

        'リャ': {
            System.STANDARD: 'rya',
        },
        'リィ': {
            System.STANDARD: 'ryi',
        },
        'リュ': {
            System.STANDARD: 'ryu',
        },
        'リェ': {
            System.STANDARD: 'rye',
        },
        'リョ': {
            System.STANDARD: 'ryo',
        },

        # ワ行
        'ワ': {
            System.STANDARD: 'wa',
        },
        'ヲ': {
            System.STANDARD: 'wo',
        },
        'ン': {
            System.STANDARD: 'n',
            System.LONG: 'nn',
            System.SHORT: 'n\'',
            # System.X:			'xn',
        },

        'ヮ': {
            System.STANDARD: 'xwa',
            System.L: 'lwa',
        },
    }

    @staticmethod
    def dump():
        return Mapping.__map.copy()

    @staticmethod
    def get(key):
        return Mapping.__map.get(key)


__all__ = ['Mapping']

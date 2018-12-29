"""  The entry point to the romanization method.

This provides a method to transliterate hiragana/katakana string to romaji string.
 """
from romaji.substring import Substring
from romaji.transliteration import Transliteration


def transliterate(src):
    """ Transliterate hiragana/katakana string to romaji strings.
    Note that if an input string contained kanji's or ths other characters
    which do not have corresponding romajis,
    the sub-sequence does not be transliterated
    and is as same as the original sub-string.
    For example, an input string "お茶の水" is transliterated to "o茶no水".

    Note for the lookahead.
    "lookahead0" always reduces one character to transliterate to romaji.
    For example, suppose that the input string is "とうきょう".
    Then "lookahead0" always reads "と" at first, then reads "う".
    On the other hand, "lookahead1" peeks on the next one character
    at the current position without shift.
    At first, "lookahead1" tries to transliterate "とう".
    When it failed, then "lookahead1" reads "と".

    In Japanese, the longest length of hiragana/katakana strings
    which correspond to one romaji is 2.
    Therefore, we only need 0 and 1 lookahead's.

    :param src:
    :return:
    """
    if src is None:
        return list()
    if len(src) is 0:
        return list()

    lookahead0 = Transliteration()
    lookahead1 = Transliteration()

    for i in range(0, len(src)):
        lookahead1.try_to_append(Substring.lookahead(1, src, i))
        sub = Substring(src[i:i + 1], i)
        lookahead1.try_to_append(sub)
        lookahead0.try_to_append(sub)

    result = set()
    result.update(lookahead1.romajis())
    result.update(lookahead0.romajis())

    if src in result:
        result.remove(src)

    return sorted(list(result))


__all__ = ['transliterate']

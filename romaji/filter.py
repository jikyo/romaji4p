"""A filter class to expand and reduce romaji strings.
"""
import copy
import re


class Filter:

    """ the pattern for non-vowel following the small "っ", or also "っ" is not continuous."""
    __pattern_xtu = re.compile(r'(xtsu|ltsu|ltu)(?!xtsu|ltsu|ltu)([bcdfghjklmnpqrstvwxyz])', re.IGNORECASE | re.MULTILINE)

    @staticmethod
    def replace_xtu(s):
        return Filter.__pattern_xtu.sub(r'\2\2', s)

    @staticmethod
    def replace_ou_to_o(s):
        return s.replace('ou', 'o')

    @staticmethod
    def expand_and_reduce(input_set):
        """ expand and reduce the input romajis as follows:

        * reduce "ou" to "o".
        * duplicated the char following "っ (xtls, xtu, ...)" and delete the "っ"
          if the following char is not vowel or "っ" is not continuous.

        :param input_set:
        :return:
        """
        result = copy.copy(input_set)
        for item in input_set:
            s = item
            s = Filter.replace_ou_to_o(s)
            s = Filter.replace_xtu(s)
            result.add(s)
        return result


__all__ = ['Filter']

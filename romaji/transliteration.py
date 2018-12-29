""" The transliteration class from the input string to the romaji representation.
"""
import itertools

from romaji.filter import Filter
from romaji.system import System


class Transliteration:

    def __init__(self):
        self.index = 0
        self.substrings = list()
        self.systems = set()

    def try_to_append(self, sub):
        """ try to append the substring to this transliteration.
        Especially note that if the index of the substring was different from this index,
        try_to_append does nothing.
        :param sub:
        :return:
        """
        if sub is None:
            return
        if sub.index is not self.index:
            return
        self.index += sub.window
        self.substrings.append(sub)
        self.systems.update(sub.get_systems())

    @staticmethod
    def find_system(sub, systems):
        """ search the system which the input substring has.
        Note that this method currently returns the first system
        in the systems ordered by the System enum.
        If not to find the system which satisfies the input substring's condition,
        return the the default system, System.STANDARD).

        :param sub:
        :param systems:
        :return: system
        """
        for system in sorted(systems):
            if sub.get_romaji(system) is not None:
                return system
        return System.STANDARD

    @staticmethod
    def substring_to_romaji(sub, systems):
        if sub.has_romaji:
            return sub.get_romaji(Transliteration.find_system(sub, systems))
        return sub.src

    @staticmethod
    def romaji(subs, systems):
        romaji = ""
        for sub in subs:
            romaji += Transliteration.substring_to_romaji(sub, systems)
        return romaji

    @staticmethod
    def power_set(iterable):
        s = list(iterable)
        return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

    def romajis(self):
        result = set()
        if len(self.substrings) is 0:
            return result
        for systems in Transliteration.power_set(self.systems):
            romaji = Transliteration.romaji(self.substrings, systems)
            result.add(romaji)
        return Filter.expand_and_reduce(result)


__all__ = ['Transliteration']

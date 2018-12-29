""" A substring of the input string with attributes including the corresponding romaji.
"""
from romaji.mapping import Mapping


class Substring:

    def __init__(self, src, index):
        self.index = index
        self.window = len(src)
        self.src = src
        self.romaji = Mapping.get(src)
        self.has_romaji = (self.romaji is not None)

    def get_systems(self):
        if self.has_romaji:
            return set(self.romaji.keys())
        return set()

    def get_romaji(self, system):
        if self.has_romaji:
            return self.romaji.get(system)
        return self.src

    @staticmethod
    def lookahead(lookahead, s, begin):
        end = begin + lookahead + 1
        if len(s) < end:
            return None
        sub = Substring(s[begin:end], begin)
        if not sub.has_romaji:
            return None
        return sub


__all__ = ['Substring']

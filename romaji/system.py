""" The romanization systems that can be used in this library.

This system enum is ordered by how popular the system is.
However, the popularity is not based on reasonable basis.
Please notice us if you had found it.
"""
from enum import Enum


class System(Enum):
    STANDARD = 0
    SHORT = 1
    LONG = 2
    L = 3
    X = 4
    LY = 5
    XY = 6
    Y = 7

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return other.value < self.value
        return NotImplemented


__all__ = ['System']

#!/usr/bin/python3
"""Bu modul dogrulanmamis olcusu olan Square klass覺 n獻ueyyen edir."""


class Square:
    """Kvadrat覺temsil eden  klass."""

    def __init__(self, size=0):
        """Klass覺n yei numayyendesini yaradir.

        Args:
            size (int): Kvadrat覺 terefinin olcusu (吳efault 0.

        Raises:
            TypeError: eger size integer deyilse.
            ValueError: eger size 0 dan kicikdirse.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

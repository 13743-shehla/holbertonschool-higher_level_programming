#!/usr/bin/python3
"""Bu modul dogrulanmamis olcusu olan Square klassi mueyyen edir."""


class Square:
    """Kvadrat ±temsil eden  klass."""

    def __init__(self, size=0):
        """klassin yeni numayyendesini yaradir.

        Args:
            size (int): kvadrati± terefinin olcusu(default 0.)

        Raises:
            TypeError: eger size integer deyilse.
            ValueError: eger size 0 dan kicikdirse.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

#!/usr/bin/python3
"""Bu modul olcusu olan bir square klassini mueyyen edir."""


class Square:
    """Kvadratıtemsil eden  klass."""

    def __init__(self, size):
        """Klassın yeninumayendesini yaradir

        Args:
        size (int): kvadratin terefinin olcusu
            """
        self.__size = size

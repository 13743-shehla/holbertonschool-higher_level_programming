#!/usr/bin/python3
"""Bu modul ölçüsü olan bir Squarass teyin edir."""

class Square:
    """Kvadratı emsil eden class."""

    def __init__(self, size):
        """Kvadratı yeni bir ölç�e  yaradır
        
        Args:
        size (int): Kvadratı terefininölçüsü
        """
            self.__size = size  # Private attribute burada teyyin olunur

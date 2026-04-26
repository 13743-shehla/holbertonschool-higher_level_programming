#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that represents a square."""

    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Getter: Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: Sets the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

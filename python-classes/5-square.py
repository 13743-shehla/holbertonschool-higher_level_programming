#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that represents a square."""

    def __init__(self, size=0):
        """Initializes a Square instance."""
        self.size = size

    @property
    def size(self):
        """Getter: Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the # character."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)

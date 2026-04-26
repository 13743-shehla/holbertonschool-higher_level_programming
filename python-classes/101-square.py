#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with # character."""
        print(self.__str__())

    def __str__(self):
        """Defines the string representation of a Square instance."""
        total = ""
        if self.__size == 0:
            return total

        # Vertical offset (yuxarı boşluqlar)
        for _ in range(self.__position[1]):
            total += "\n"

        # Kvadratın sətirlərini yığırıq
        for i in range(self.__size):
            total += (" " * self.__position[0]) + ("#" * self.__size)
            if i != self.__size - 1:
                total += "\n"
        return total

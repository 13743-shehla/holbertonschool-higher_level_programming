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
        """Setter for position with complex validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with position using #."""
        if self.__size == 0:
            print("")
            return

        # Yuxarıdan boşluq (vertical offset)
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print("")

        # Kvadratın çapı
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

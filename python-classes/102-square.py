#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that represents a square."""

    def __init__(self, size=0):
        """Initializes a Square instance."""
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    # Müqayisə metodları
    def __eq__(self, other):
        """Check if areas are equal (==)."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if areas are not equal (!=)."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if current area is less than other (<)."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if current area is less than or equal to other (<=)."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if current area is greater than other (>)."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if current area is greater than or equal to other (>=)."""
        return self.area() >= other.area()

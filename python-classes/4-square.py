#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Square with size validation and area calculation."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return area of square."""
        return self.__size ** 2

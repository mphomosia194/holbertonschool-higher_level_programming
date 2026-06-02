
#!/usr/bin/python3
"""Defines a Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

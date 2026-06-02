#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes are included.
        Otherwise, all attributes are returned.
        """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

        return self.__dict__

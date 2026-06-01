#!/usr/bin/python3
"""Defines MyList class."""


class MyList(list):
    """Inherited list class."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))

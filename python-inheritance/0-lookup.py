#!/usr/bin/python3
"""Returns the list of available attributes and methods of an object."""


def lookup(obj):
    """Return list of attributes and methods."""
    return dir(obj)

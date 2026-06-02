#!/usr/bin/python3
"""Defines a function that reads a UTF-8 text file and prints it."""


def read_file(filename=""):
    """Read a text file and print its contents to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

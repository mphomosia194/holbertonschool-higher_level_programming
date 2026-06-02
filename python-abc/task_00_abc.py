#!/usr/bin/env python3
"""Abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class."""

    def sound(self):
        """Return dog's sound."""
        return "Bark"


class Cat(Animal):
    """Cat class."""

    def sound(self):
        """Return cat's sound."""
        return "Meow"

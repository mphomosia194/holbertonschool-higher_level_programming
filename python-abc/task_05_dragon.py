#!/usr/bin/env python3
"""Mixin example with Dragon."""


class SwimMixin:
    """Provides swimming ability."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying ability."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class with swimming and flying abilities."""

    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")

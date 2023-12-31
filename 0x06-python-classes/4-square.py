#!/usr/bin/python3
"""A class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """A Square"""

    def __init__(self, size=0):
        """Initialization of a new square

    Args:
        size (int): The first parameter.

    Returns:
        None
    """
        self.size = size

    @property
    def size(self):
        """property"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            A public instance method.
        """
        return self.__size * self.__size

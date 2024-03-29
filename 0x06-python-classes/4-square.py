#!/usr/bin/python3
"""Module for calaculating area of square"""


class Square:
    """define area method"""
    def __init__(self, size=0):
        """initilaize size"""
        self.size = size

    def area(self):
        """calculate area"""
        return ((self.__size)**2)

    @property
    def size(self):
        """get size"""
        return (self.__size)

    @size.setter
    def size(self, size):
        """set size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

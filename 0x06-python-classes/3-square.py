#!/usr/bin/python3
"""Module for calaculating area of square"""


class Square:
    """define area method"""
    def __init__(self, size=0):
        """get size"""
        self.set_size(size)

    def set_size(self, size):
        """set size"""
        if size != int(size):
            raise TypeError("{}".format("size must be an integer"))
        elif size < 0:
            raise ValueError("{}".format("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """calculate area"""
        return ((self.__size)**2)

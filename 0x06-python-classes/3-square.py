#!/usr/bin/python3
"""Module for calaculating area of square"""


class Square:
    """define area method"""
    def __init__(self, size):
        """get size"""
        self.set_size(size)

    def set_size(self, size):
        """set size"""
        if size != int(size):
            print("{}".format(""))
        elif size < 0:
            print("{}".format(""))
        else:
            self.__size = size

    def area(self):
        """calculate area"""
        return ((self.__size)**2)

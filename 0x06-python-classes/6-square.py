#!/usr/bin/python3
"""Module for class of a square"""


class Square:
    """define area method"""
    def __init__(self, size=0, position=(0, 0)):
        """initilaize size"""
        self.size = size
        self.position = position

    def area(self):
        """calculate area"""
        return ((self.__size)**2)

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for side in range(self.__size):
                print("{}{}".format(
                    self.__position[0] * " ",
                    self.__size * "#"))

    @property
    def position(self):
        """retrive position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set position"""
        if (value[0] < 0 or value[1] < 0) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

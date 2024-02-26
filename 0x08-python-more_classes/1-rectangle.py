#!/usr/bin/python3
"""Module for a rectangle"""


class Rectangle:
    """define a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set width"""
        if value != int(value):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """return height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """return height"""
        if value != int(value):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

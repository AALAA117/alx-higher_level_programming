#!/usr/bin/python3
"""Module for a rectangle"""


class Rectangle:
    """define a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """return area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return surface area"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rec = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rec += str(self.print_symbol)
                    if j == self.__width - 1:
                        rec += "\n"
        return (rec)

    def __repr__(self):
        return ("Rectangle(2, 4)")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

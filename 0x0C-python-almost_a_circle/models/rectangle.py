#!/usr/bin/python3
"""Rectangle Model"""
from .base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """get area of rectangle"""
        return (self.__width * self.__height)

    @property
    def width(self):
        """get width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        rep = ""
        for h in range(self.__height):
            rep += " " * self.__x + "#" * self.__width + "\n"
        for step in range(self.__y):
            print()
        print((rep[:-1]))

    def __str__(self):
        """return a string represntation when using print"""
        return ('[Rectangle] ({}) {}/{} - {}/{}'.
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    @property
    def x(self):
        """get x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

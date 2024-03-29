#!/usr/bin/python3
"""Rectangle Model"""
from .base import Base
from .rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize"""
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """update arguments of class square"""
        list_t = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, list_t[i], args[i])
        for key, value in kwargs.items():
            setattr(self, str(key), value)

    def area(self):
        """get area of rectangle"""
        return (pow(self.__size, 2))

    @property
    def size(self):
        """get size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value

    def display(self):
        """prints in stdout the Square instance with the character #"""
        rep = ""
        for h in range(self.__size):
            rep += " " * self.__x + "#" * self.__size + "\n"
        for step in range(self.__y):
            print()
        print((rep[:-1]))

    def __str__(self):
        """return a string represntation when using print"""
        return ('[{}] ({}) {}/{} - {}'.
                format(type(self).__name__, self.id, self.__x,
                       self.__y, self.size))

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

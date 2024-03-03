#!/usr/bin/python3
"""Module of BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Child class of BaseGeometry """
    def __init__(self, size):
        """attributes"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)
        super().__str__()

    def area(self):
        """area"""
        return (pow(self.__size, 2))

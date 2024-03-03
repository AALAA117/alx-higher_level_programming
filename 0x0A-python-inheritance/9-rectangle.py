#!/usr/bin/python3
"""Module of BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Child class of BaseGeometry """
    def __init__(self, width, height):
        """attributes"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """area"""
        return (self.__width * self.__height)

    def __str__(self):
        """rectangle description"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

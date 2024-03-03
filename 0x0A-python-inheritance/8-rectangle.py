#!/usr/bin/python3
"""Module of BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Child class of BaseGeometry """
    def __init__(self, width, height):
        """attributes"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

#!/usr/bin/python3
"""BaseModel"""


class Base:
    """manage id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

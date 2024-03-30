#!/usr/bin/python3
"""BaseModel"""
import json


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

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if len(list_dictionaries) == 0 or list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

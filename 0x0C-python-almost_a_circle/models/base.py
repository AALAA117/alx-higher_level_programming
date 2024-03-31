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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding='utf-8') as f:
            if list_objs is not None or len(list_objs) != 0:
                list_t = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_t))
            else:
                f.write(cls.to_json_string(list_objs))

#!/usr/bin/python3
"""class Student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is not None:
            dic = {}
            for key in attrs:
                if hasattr(self, key):
                    dic[key] = getattr(self, key, None)
            return (dic)
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """set attributes in json file"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)

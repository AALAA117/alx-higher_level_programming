#!/usr/bin/python3
""" instance of the specified class """


def is_same_class(obj, a_class):
    """return bool"""
    if isinstance(obj, a_class) and type(obj) is a_class:
        return (True)
    else:
        return (False)

#!/usr/bin/python3
"""inherited (directly or indirectly)"""


def inherits_from(obj, a_class):
    """ object is an instance of a class"""
    if issubclass(obj, a_class):
        if type(obj) is not a_class:
            return (True)
        else:
            return (False)
    else:
        return (False)

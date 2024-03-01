#!/usr/bin/python3
"""
Addition Module
this module give addition of any two numbers

"""


def add_integer(a, b=98):
    """
    Addition of 2 numbers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
    return (a + b)

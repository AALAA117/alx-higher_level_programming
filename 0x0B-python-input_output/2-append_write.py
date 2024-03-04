#!/usr/bin/python3
"""Module for writing"""


def append_write(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "a", encoding="UTF8") as f:
        f.write(text)
        return (len(text))

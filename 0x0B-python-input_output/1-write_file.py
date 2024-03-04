#!/usr/bin/python3
"""Module for writing"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="UTF8") as f:
        f.write(text)
        return (len(text))

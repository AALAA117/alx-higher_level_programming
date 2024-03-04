#!/usr/bin/python3
"""Module to read a file text"""


def read_file(filename=""):
    """read a whole text"""
    with open(filename, encoding="UTF8") as f:
        for line in f:
            print("{}".format(line.rstrip()))

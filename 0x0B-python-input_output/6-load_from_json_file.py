#!/usr/bin/python3
"""creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """Object from a “JSON file"""
    with open(filename) as f:
        data = json.load(f)
        return (data)

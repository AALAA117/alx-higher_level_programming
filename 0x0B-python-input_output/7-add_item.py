#!/usr/bin/python3
"""creates an Object from a “JSON file"""
import json
import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
loaded_data = []
if not os.path.exists(filename):
    loaded_data.extend(sys.argv[1:])
    save_to_json_file(loaded_data, filename)
else:
    loaded_data = load_from_json_file(filename)
    loaded_data.extend(sys.argv[1:])
    save_to_json_file(loaded_data, filename)

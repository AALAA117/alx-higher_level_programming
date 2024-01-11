#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dict = {}
        for key in a_dictionary:
            new_dict[key] = 2 * a_dictionary.get(key)
        return (new_dict)

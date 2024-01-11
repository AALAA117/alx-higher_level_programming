#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is not None:
        result = 0
        for num in set(my_list):
            result = result + num
        return (result)

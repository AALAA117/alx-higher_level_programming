#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        max1 = 0
        if my_list == []:
            return (None)
        else:
            for i in my_list:
                if i > max1:
                    max1 = i
            return (max1)

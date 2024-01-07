#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        new_string = []
        for c in my_string:
            if c != 'c' and c != 'C':
                new_string.append(c)
        return ("".join(new_string))

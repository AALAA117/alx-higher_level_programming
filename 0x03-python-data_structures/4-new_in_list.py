#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is not None:
        listn = my_list[:]
        if idx < 0:
            return (listn)
        elif idx >= len(my_list):
            return (listn)
        else:
            del listn[idx]
            listn.insert(idx, element)
            return (listn)

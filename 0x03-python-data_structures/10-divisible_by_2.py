#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        list1 = []
        if my_list == []:
            return (False)
        else:
            for i in my_list:
                if i % 2 == 0:
                    list1.append(True)
                else:
                    list1.append(False)
            return (list1)

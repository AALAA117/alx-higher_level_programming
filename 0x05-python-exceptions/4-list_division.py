#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 is not None and my_list_2 is not None:
        try:
            result = []
            for i in range(list_length):
                try:
                    div_result = my_list_1[i] / my_list_2[i]
                except ZeroDivisionError:
                    div_result = 0
                    print("division by 0")
                except TypeError:
                    div_result = 0
                    print("wrong type")
                except IndexError:
                    div_result = 0
                    print("out of range")
                result.append(div_result)
        finally:
            return (result)

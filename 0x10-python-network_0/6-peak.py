#!/usr/bin/python3
def find_peak(list_of_integers):
    start = 0
    end = len(list_of_integers) - 1
    mid = (start + end) // 2
    if len(list_of_integers) == 0:
        return (None)
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    else:
        while start < end:
            if list_of_integers[mid] > list_of_integers[mid - 1] and\
                    list_of_integers[mid] > list_of_integers[mid + 1]:
                return (list_of_integers[mid])
            if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
                end = mid
            else:
                start = mid + 1

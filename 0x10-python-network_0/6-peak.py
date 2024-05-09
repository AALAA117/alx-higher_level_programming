#!/usr/bin/python3
"""Module to find peak number using binary search"""


def find_peak(list_of_integers):
    """
    function that finds a peak in a
    list of unsorted integers.
    """
    start = 0
    end = len(list_of_integers) - 1
    mid = (start + end) // 2
    if len(list_of_integers) == 0:
        return (None)
    if list_of_integers[mid] == list_of_integers[mid - 1] ==\
            list_of_integers[mid + 1]:
        return (list_of_integers[mid])
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    else:
        if list_of_integers[mid] > list_of_integers[mid - 1] and\
                list_of_integers[mid] > list_of_integers[mid + 1]:
            return (list_of_integers[mid])
        if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            end = mid
            list_a = list_of_integers[:end]
        else:
            start = mid
            list_a = list_of_integers[start:]
        return (find_peak(list_a))

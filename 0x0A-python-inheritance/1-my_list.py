#!/usr/bin/python3
"""
Module for My_list
"""


class MyList(list):
    """
    sort My list
    """
    def print_sorted(self):
        """
        sorting
        """
        My_list = super().copy()
        print(sorted(My_list))

#!/usr/bin/python3
def safe_print_integer(value):
    if value is not None:
        try:
            print("{:d}".format(value))
            return (True)
        except Exception as err:
            return (False)

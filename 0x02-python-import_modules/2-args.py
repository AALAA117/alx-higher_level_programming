#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 1
    if (len(argv) == 1):
        print("{:d} arguments.".format(0))
    else:
        if (len(argv) == 2):
            print("{:d} argument:".format(1))
            print("{:d}: {}".format(i, argv[i]))
        else:
            print("{:d} arguments:".format(len(argv) - 1))
    if (len(argv) > 2):
        for i in range(len(argv)):
            print("{:d}: {}".format(i, argv[i]))

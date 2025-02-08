#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = argv[1:]
    if len(args) == 0:
        print("0 arguments.")

    else:
        if len(args) == 1:
            print("1 argument:")
        else:
            print("{:d} arguments:".format(len(args)))
        for i in range(len(args)):
            print("{:d}: {}".format(i+1, args[i]))

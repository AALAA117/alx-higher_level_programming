#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = argv[1:]
    result = 0
    if len(args) >= 1:
        for i in range(len(args)):
            result += int(args[i])
    print(result)

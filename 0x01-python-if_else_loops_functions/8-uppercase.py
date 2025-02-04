#!/usr/bin/python3
def uppercase(str):
    string = []
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            string.append(chr(ord(str[i]) - 32))
        else:
            string.append(str[i])
    print("{}".format(''.join(string)))

#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 and i % 15 != 0):
            print("{}".format("Fizz"), end=' ')
            continue
        if (i % 5 == 0 and i % 15 != 0):
            print("{}".format("Buzz"), end=' ')
            continue
        if (i % 15 == 0):
            print("{}".format("FizzBuzz"), end=' ')
            continue
        else:
            print("{:d}".format(i), end=' ')
            continue

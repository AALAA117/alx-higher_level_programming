#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is not None and tuple_b is not None:
        for i in tuple_a:
            for j in tuple_b:
                tuple_a[i] = tuple_a[i] + tuple_b[j]
                break
        return (tuple_a)

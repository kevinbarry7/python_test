"""
Module to show off tuple methods.

Neither this module nor the function should import the introcs module.  In addition,
the function should not use a loop or recursion.

Author: Kevin Barry
Date: May 31, 2020
"""


def replace_first(tup, a, b):
    """
    Returns a copy of tup with the first value of a replaced by b

    Examples:
        replace_first((1,2,1),1,3) returns (3,2,1)
        replace_first((1,2,1),4,3) returns (1,2,1)

    Parameter tup: The tuple to copy
    Precondition: tup is a tuple of integers

    Parameter a: The value to replace
    Precondition: a is an int

    Parameter b: The value to replace with
    Precondition: b is an int
    """
    assert type(a) == int
    assert type(b) == int
    new_tup = ()
    if tup.count(a) < 1:
        return tup
    elif tup.count(a) > 0:
        y = tup.index(a)
        print(y)
        if y == 0:
            new_tup = new_tup + (b,)
            new_tup = new_tup + tup[1:]
        else:
            print(y)
            new_tup = tup[:y]
            new_tup = new_tup + (b,)
            new_tup = new_tup + tup[y+1:]
    return new_tup


result = replace_first((1, 2, 3), 1, 4)
print(result)
result = replace_first((2, 3), 1, 4)
print(result)
result = replace_first((2, 1, 3), 1, 4)
print(result)
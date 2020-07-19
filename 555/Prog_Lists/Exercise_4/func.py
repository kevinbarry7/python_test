"""
Module to demonstrate tuple expansion.

Author: Kevin Barry
Date: June 6, 2020
"""


def avg(*args):  # The parameter is MISSING.  Add it back.
    """
    Returns average of all of arguments (passed via tuple expansion)

    Remember that the average of a list of arguments is the sum of all of the elements
    divided by the number of elements.

    Examples:
        avg(1.0, 2.0, 3.0) returns 2.0
        avg(1.0, 1.0, 3.0, 5.0) returns 2.5

    Parameter args: the function arguments
    Precondition: args are all numbers (int or float)
    """
    average = 0
    total = 0
    count = len(args)
    if count > 0:
        for i in args:
            total = total + i
    else:
        return 0
    average = total/count
    return average


result = avg(1.0, 2.0, 3.0)
print(result)
result = avg(1.0, 1.0, 3.0, 5.0)
print(result)


print(tuple(range(10, 20)))
tup = (tuple(range(10, 20)))
print(tup)
result = avg(*tup)
print(result)